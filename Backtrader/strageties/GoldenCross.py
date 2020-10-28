import math
import backtrader as bt

class GoldenCross(bt.Strategy):
    params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

    def __init__(self):
        self.fast_moving_average = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.fast, plotname='50 day moving average')
        self.slow_moving_average = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.slow, plotname='200 day moving average')
