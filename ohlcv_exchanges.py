import ccxt 
from time import sleep
from dynamically import Exchange

def load_markets(result):
    loading = result.load_markets()
    sleep(1)
    return loading

def keys(result):
    keys = result.markets.keys()
    sleep(1)
    return keys

def load_symbols(exchange):
    exchange_instance = getattr(ccxt, exchange)
    result = exchange_instance()
    load_markets(result)
    sleep(1)
    symbols = keys(result)
    sleep(1)
    return tuple(symbols)

def load_ohlcv_exchanges():
    exchanges = ccxt.exchanges
    exchanges_ohlcv = []
    for e in exchanges:
        try:
            if Exchange(e).hasOHLCV:
                exchanges_ohlcv.append(e)
        except:
            pass
    return exchanges_ohlcv
    

#d = defaultdict(list)
#l = ()
# for e in exchanges:
#     try:
#         s = load_symbols(e)
#         sleep(5)
#         l += (e,s,)
#     except:
#         pass 
# print(l)
# exchanges = load_ohlcv_exchanges()
# for e in exchanges:
#     ins = Exchange(e)
#     sleep(1)
#     s = list(ins.symbols)
#     l += (e,s,)

# data = [l]
# dic = {i[0] : list(i[1])  for i in data}
# print(dic)

# ['_1btcxe', 'acx', 'allcoin', 'anxpro', 'binance', 'bit2c', 'bitbay', 'bitcoincoid', 'bitfinex', 'bitfinex2', 'bitflyer', 'bithumb', 'bitlish', 'bitmarket', 'bitmex', 'bitso', 'bitstamp', 'bitstamp1', 'bittrex', 'bl3p', 'bleutrade', 'btcbox', 'btcchina', 'btcexchange', 'btcmarkets', 'btctradeua', 'btcturk', 'btcx', 'bxinth', 'ccex', 'cex', 'chbtc', 'chilebit', 'coincheck', 'coinexchange', 'coinfloor', 'coingi', 'coinmarketcap', 'coinmate','coinsecure', 'coinspot', 'dsx', 'exmo', 'foxbit', 'fybse', 'fybsg', 'gatecoin', 'gateio', 'gdax', 'gemini', 'getbtc', 'hitbtc', 'hitbtc2', 'huobi', 'huobicny', 'huobipro', 'independentreserve', 'itbit', 'jubi', 'kraken','kucoin', 'kuna', 'lakebtc', 'liqui', 'livecoin', 'luno', 'lykke', 'mercado', 'mixcoins', 'nova', 'okcoincny','okcoinusd', 'okex', 'paymium', 'poloniex', 'qryptos', 'quadrigacx', 'quoinex', 'southxchange', 'surbitcoin', 'therock', 'tidex', 'urdubit', 'vaultoro', 'vbtc', 'virwox', 'wex', 'zaif', 'zb']