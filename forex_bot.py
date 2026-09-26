import MetaTrader5 as mt5
import pandas as pd
import time

LOGIN = 169440229
SERVER = "XMGlobal-MT5 2"
# PASSWORD yaha apna wala daal de - GitHub pe push mat karna!
PASSWORD = "TeraPasswordYahaDaal"

SYMBOL = "XAUUSD"
TIMEFRAME = mt5.TIMEFRAME_M15

mt5.initialize(login=LOGIN, password=PASSWORD, server=SERVER)
print("XM Connected!")
print("Balance:", mt5.account_info().balance)

# ... baaki wahi sweep wala logic
