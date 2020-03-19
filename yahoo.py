import yfinance as yf

slack = yf.Ticker("WORK")

history= slack.history(period="max")

print(history.to_csv())

## when running command line, doing "command > whatever" will create a new file with name whatever in this case
##https://pypi.org/project/yfinance/ for documentation
