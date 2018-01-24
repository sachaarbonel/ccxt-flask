import ccxt
import pandas as pd

def poloniex_ethbtc_ohlc():
    poloniex = ccxt.poloniex()
    return poloniex.fetch_ohlcv('ETH/BTC')

def poloniex_historical_to_DF():
    ohlc= poloniex_ethbtc_ohlc()
    ohlc_tup = tuple(map(tuple, ohlc))
    historical_DF = pd.DataFrame(list(ohlc_tup), columns=["Date","Open","High","Low","Close","Volume"])
    historical_DF["Date"] = historical_DF["Date"].apply(pd.to_datetime,unit='ms')
    historical_DF.index= historical_DF["Date"].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S.%f')
    clean_DF = historical_DF.drop('Date', axis=1)
    return clean_DF