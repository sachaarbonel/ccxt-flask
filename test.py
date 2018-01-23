import ccxt
import pandas as pd
import time


def poloniex_ethbtc_ohlc():
    poloniex = ccxt.poloniex()
    return poloniex.fetch_ohlcv('ETH/BTC')

s = poloniex_ethbtc_ohlc()
tup = tuple(map(tuple, s))
print(pd.DataFrame(list(tup), columns=["Timestamp","Open","High","Low","Close","Volume"]))