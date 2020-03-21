import csv
from trade import *

def is_bullish_candlestick(candle):
    return candle['Close'] > candle['Open']

def is_bearish_candlestick(candle):
        return candle['Close'] < candle['Open']

def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and  float(current_day['Close']) > float(previous_day['Open']) \
        and  float(current_day['Open']) < float(previous_day['Close']):
        return True
    return False

def is_bearish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

    if is_bearish_candlestick(previous_day) \
        and  float(current_day['Open']) > float(previous_day['Close']) \
        and  float(current_day['Close'])< float(previous_day['Open']):
        return True
    return False


snp500 = open('snp500.csv')
snp500_compaines = csv.reader(snp500)

for company in snp500_compaines:
    ticker, name = company
    history_file = open('directory/{}.csv'.format(ticker))
    reader = csv.DictReader(history_file)
    candles = list(reader)

    candles = candles[-2:]

    if len(candles) > 1:
        if is_bullish_engulfing(candles,1):
            #print("{} - {} is bullish engulfing".format(ticker, candles[1]['Date']));
            create_order("{}".format(ticker), 100, "sell", "market", "gtc" )

        #if is_bearish_engulfing(candles,1):
            #print("{} - {} is bearish engulfing".format(ticker, candles[1]['Date'])) \
            #and create_order("{}".format(ticker), 100, "sell", "market", "gtc" )
