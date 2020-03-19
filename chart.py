import plotly.graph_objects as go
import pandas

df = pandas.read_csv('stock.csv')

candleStick = go.Candlestick(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])
fig = go.Figure(data=[candleStick])
fig.show()
