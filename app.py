from binance.client import Client
from config import client
from functions import store_ticker_prices_backtest
import backtrader as bt
from teststrategies import SmaCross, SupplyAndDemand, TestStrategy

df = store_ticker_prices_backtest("BTCUSDT", "1h", 10)
print(df)
cerebro = bt.Cerebro()

feed = bt.feeds.PandasData(dataname=df)
cerebro.adddata(feed)

cerebro.addstrategy(SupplyAndDemand)
cerebro.broker.setcommission(commission=0.005)
cerebro.addsizer(bt.sizers.PercentSizer, percents=50)

cerebro.run()
cerebro.plot(style="candlestick")
