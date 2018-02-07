import ccxt
import pandas as pd
#import jsonpickle
from collections import defaultdict
from time import sleep
import feather

#path = 'dataframes/poloniex.feather'

class Exchange:
    def __init__(self,name,pairs=None):
        self.name = name
        self.pairs = pairs
        self.result = self.instanceof(name)
        self.hasOHLCV = self.hasOHLCV(self.result)
        self.result.load_markets()
        self.symbols = list(self.result.markets.keys())

    def instanceof(self,name):
        exchange_instance = getattr(ccxt, self.name )
        result = exchange_instance()
        return result

    def hasOHLCV(self,res):
        return 'fetch_ohlcv' in dir(res)

    def fetch_ohlcv(self):
        return self.result.fetch_ohlcv(self.pairs)

    def historical_to_DF(self):
        ohlc= self.fetch_ohlcv()
        ohlc_tup = tuple(map(tuple, ohlc))
        historical_DF = pd.DataFrame(list(ohlc_tup), columns=["Date","Open","High","Low","Close","Volume"])
        historical_DF["Date"] = historical_DF["Date"].apply(pd.to_datetime,unit='ms')
        historical_DF.index= historical_DF["Date"].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S.%f')
        clean_DF = historical_DF.drop('Date', axis=1)
        return clean_DF

# poloniex = Exchange('poloniex')
# print(list(poloniex.symbols))


#{'bittrex': ['1ST/BTC', '2GIVE/BTC', 'ABY/BTC', 'ADA/BTC', 'ADT/BTC', 'ADX/BTC', 'AEON/BTC', 'AGRS/BTC', 'AMP/BTC', 'ANT/BTC', 'ARDR/BTC', 'ARK/BTC', 'AUR/BTC', 'BAT/BTC', 'BAY/BTC', 'BCH/BTC', 'BCY/BTC', 'BITB/BTC', 'BLITZ/BTC', 'BLK/BTC', 'BLOCK/BTC', 'BNT/BTC', 'BRK/BTC', 'BRX/BTC', 'BSD/BTC', 'BTG/BTC', 'BURST/BTC', 'BYC/BTC','CANN/BTC', 'CFI/BTC', 'CLAM/BTC', 'CLOAK/BTC', 'CLUB/BTC', 'COVAL/BTC', 'CPC/BTC', 'CRB/BTC', 'CRW/BTC', 'CURE/BTC', 'CVC/BTC', 'DASH/BTC', 'DCR/BTC', 'DCT/BTC', 'DGB/BTC', 'DMD/BTC', 'DNT/BTC', 'DOGE/BTC', 'DOPE/BTC', 'DTB/BTC', 'DYN/BTC', 'EBST/BTC', 'EDG/BTC', 'EFL/BTC', 'EGC/BTC', 'EMC/BTC', 'EMC2/BTC', 'ENG/BTC', 'ENRG/BTC','ERC/BTC', 'ETC/BTC', 'ETH/BTC', 'EXCL/BTC', 'EXP/BTC', 'FAIR/BTC', 'FCT/BTC', 'FLDC/BTC', 'FLO/BTC', 'FTC/BTC', 'FUN/BTC', 'GAM/BTC', 'GAME/BTC', 'GBG/BTC', 'GBYTE/BTC', 'GCR/BTC', 'GEO/BTC', 'GLD/BTC', 'GNO/BTC', 'GNT/BTC', 'GOLOS/BTC', 'GRC/BTC', 'GRS/BTC', 'GUP/BTC', 'HMQ/BTC', 'IGNIS/BTC', 'INCNT/BTC', 'INFX/BTC', 'IOC/BTC', 'ION/BTC', 'IOP/BTC', 'KMD/BTC', 'KORE/BTC', 'LBC/BTC', 'LGD/BTC', 'LMC/BTC', 'LSK/BTC', 'LTC/BTC', 'LUN/BTC', 'MAID/BTC', 'MANA/BTC', 'MCO/BTC', 'MEME/BTC', 'MER/BTC', 'MLN/BTC', 'MONA/BTC', 'MUE/BTC', 'MUSIC/BTC', 'NAV/BTC', 'NBT/BTC', 'NEO/BTC', 'NEOS/BTC', 'NLG/BTC', 'NMR/BTC', 'NXC/BTC', 'NXS/BTC', 'NXT/BTC', 'OK/BTC', 'OMG/BTC', 'OMNI/BTC', 'PART/BTC', 'PAY/BTC', 'PDC/BTC', 'PINK/BTC', 'PIVX/BTC', 'PKB/BTC', 'POT/BTC', 'POWR/BTC', 'PPC/BTC', 'PTC/BTC', 'PTOY/BTC', 'QRL/BTC', 'QTUM/BTC', 'QWARK/BTC', 'RADS/BTC', 'RBY/BTC', 'RCN/BTC', 'RDD/BTC','REP/BTC', 'RISE/BTC', 'RLC/BTC', 'SALT/BTC', 'SBD/BTC', 'SC/BTC', 'SEQ/BTC', 'SHIFT/BTC', 'SIB/BTC', 'SLR/BTC', 'SLS/BTC', 'SNRG/BTC', 'SNT/BTC', 'SPHR/BTC', 'SPR/BTC', 'START/BTC', 'STEEM/BTC', 'STORJ/BTC', 'STRAT/BTC','SWIFT/BTC', 'SWT/BTC', 'SYNX/BTC', 'SYS/BTC', 'THC/BTC', 'TIX/BTC', 'TKS/BTC', 'TRST/BTC', 'TRUST/BTC', 'TX/BTC', 'UBQ/BTC', 'UKG/BTC', 'UNB/BTC', 'VIA/BTC', 'VIB/BTC', 'VOX/BTC', 'VRC/BTC', 'VRM/BTC', 'VTC/BTC', 'VTR/BTC', 'WAVES/BTC', 'WINGS/BTC', 'XCP/BTC', 'XDN/BTC', 'XEL/BTC', 'XEM/BTC', 'XLM/BTC', 'XMG/BTC', 'XMR/BTC', 'XMY/BTC', 'XRP/BTC', 'XST/BTC', 'XVC/BTC', 'XVG/BTC', 'XWC/BTC', 'XZC/BTC', 'ZCL/BTC', 'ZEC/BTC', 'ZEN/BTC', '1ST/ETH', 'ADA/ETH', 'ADT/ETH', 'ADX/ETH', 'ANT/ETH', 'BAT/ETH', 'BCH/ETH', 'BNT/ETH', 'BTG/ETH', 'CFI/ETH', 'CRB/ETH', 'CVC/ETH', 'DASH/ETH', 'DGB/ETH', 'DNT/ETH', 'ENG/ETH', 'ETC/ETH', 'FCT/ETH', 'FUN/ETH', 'GNO/ETH', 'GNT/ETH', 'GUP/ETH', 'HMQ/ETH', 'LGD/ETH', 'LTC/ETH', 'LUN/ETH', 'MANA/ETH', 'MCO/ETH', 'NEO/ETH', 'NMR/ETH', 'OMG/ETH', 'PAY/ETH', 'POWR/ETH', 'PTOY/ETH', 'QRL/ETH', 'QTUM/ETH', 'RCN/ETH', 'REP/ETH', 'RLC/ETH', 'SALT/ETH', 'SC/ETH', 'SNT/ETH', 'STORJ/ETH', 'STRAT/ETH', 'TIX/ETH', 'TRST/ETH', 'UKG/ETH', 'VIB/ETH', 'WAVES/ETH', 'WINGS/ETH', 'XEM/ETH', 'XLM/ETH', 'XMR/ETH', 'XRP/ETH', 'ZEC/ETH', 'ADA/USDT', 'BCH/USDT', 'BTC/USDT', 'BTG/USDT', 'DASH/USDT', 'ETC/USDT', 'ETH/USDT', 'LTC/USDT', 'NEO/USDT', 'NXT/USDT', 'OMG/USDT', 'XMR/USDT', 'XRP/USDT', 'XVG/USDT', 'ZEC/USDT']}

# def poloniex_historical_to_feather():
#     df = poloniex_historical_to_DF()
#     historical_DF["Date"] = historical_DF["Date"].apply(pd.to_datetime,unit='ms')
#     historical_DF.index= historical_DF["Date"].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S.%f')
#     clean_DF = historical_DF.drop('Date', axis=1)
#     feather.write_dataframe(df, path)

# #poloniex_historical_to_feather()
# df = feather.read_dataframe(path)
# df.index= df["Date"].apply(pd.to_datetime,format='%Y-%m-%d %H:%M:%S.%f')
# #df = poloniex_historical_to_DF()
# print(df)