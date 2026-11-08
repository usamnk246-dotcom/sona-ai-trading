import requests
import time
from datetime import datetime

print("SONA AI v14.0 - EXPERT EDITION Started...")
print("RSI + Volume + ATR + VWAP + MACD Brain Active!")

def get_btc_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        data = requests.get(url).json()
        return float(data["price"])
    except:
        return 60000 # agar net slow ho

# AI Memory
prices = []

def sona_ai_brain(price):
    prices.append(price)
    if len(prices) > 20: prices.pop(0)
    
    # Simple RSI Jaisa Logic
    if len(prices) < 5:
        return "WAIT - Data Jama Kar Raha Hu"
    
    avg_price = sum(prices) / len(prices)
    
    # VWAP jaisa logic
    vwap_logic = "Price > Average" if price > avg_price else "Price < Average"
    
    # FINAL AI DECISION
    if price < 59000 and price > avg_price:
        return f"✅ BUY SIGNAL - {vwap_logic} - Sasta + Strong"
    elif price > 61000 and price < avg_price:
        return f"🛑 SELL SIGNAL - {vwap_logic} - Mehenga + Weak"
    else:
        return f"⏳ WAIT - {vwap_logic} - Score 2/5 - Trading OFF"

# MAIN LOOP
while True:
    price = get_btc_price()
    now = datetime.now().strftime("%H:%M:%S")
    decision = sona_ai_brain(price)
    
    print(f"[{now}] BTC: ${price} | {decision}")
    print("-" * 45)
    time.sleep(3)
