import csv

def is_bullish_engulfing(candles, index):
    current_day = candles[index]
    previous_day = candles[index-1]

with open('schrodinger.csv') as f:
    reader = csv.DictReader(f)
    #print(reader)
    candles = list(reader)
    print(candles)
#this is a csv package that reads line into a dictonary that makes it easy to reference the values
for i in range(1, len(candles)):
    print(candles[i])
