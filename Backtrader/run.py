import os, sys, argparse
import pandas as pd
import backtrader as bt
from backtrader import Cerebro
#from strageties.buyHold import BuyHold
from strageties.GoldenCross import GoldenCross
cerebro = bt.Cerebro()
cerebro = Cerebro()
cerebro.broker.setcash(1000000)

spy_prices = pd.read_csv('oracle.csv', index_col='Date', parse_dates= True)
feed = bt.feeds.PandasData(dataname=spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)
cerebro.run()
cerebro.plot()
