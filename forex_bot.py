import MetaTrader5 as mt5
import pandas as pd
import time

# --- SETTINGS ---
SYMBOL = "XAUUSD"  # GOLD
TIMEFRAME = mt5.TIMEFRAME_M15
LOT = 0.01

def check_sweep(df):
    # Simple Sweep Logic - last candle ne pichla low toda phir wapas upar
    last_low = df['low'].iloc[-10:-1].min()
    curr_low = df['low'].iloc[-1]
    curr_close = df['close'].iloc[-1]
    
    # SSL Sweep = neeche liquidity leke wapas upar
    if curr_low < last_low and curr_close > last_low:
        return "BUY_SWEEP"
    
    last_high = df['high'].iloc[-10:-1].max()
    curr_high = df['high'].iloc[-1]
    
    # BSL Sweep = upar liquidity leke wapas neeche
    if curr_high > last_high and curr_close < last_high:
        return "SELL_SWEEP"
    
    return None

# --- MAIN ---
mt5.initialize()
print(f"{SYMBOL} Bot Started... No Theta Decay tension!")

while True:
    rates = mt5.copy_rates(SYMBOL, TIMEFRAME, 0, 100)
    df = pd.DataFrame(rates)
    
    signal = check_sweep(df)
    
    if signal:
        print(f"Signal Mila: {signal} at {df['close'].iloc[-1]}")
        # Yaha pe Order bhejne ka code ayega demo ke liye
        # Abhi sirf print karega taaki tu check kar sake
    
    time.sleep(60) # Har 1 min check
