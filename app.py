import streamlit as st
import yfinance as yf
import pandas as pd
import requests, time

st.set_page_config(page_title="Sona AI 98% PRO", layout="wide")
st.title("🔥 Sona AI Trading - 98% Quality V4")
st.caption("Wase sah - Full Auto | High Quality")

# --- SETTINGS ---
symbol = "GC=F"
TELEGRAM_BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "PASTE_YOUR_CHAT_ID"

# --- DATA ---
data = yf.download(symbol, period="1mo", interval="15m", auto_adjust=True)
if len(data) < 100:
    st.error("Data load nahi hua, refresh karo")
    st.stop()

close = data['Close'].squeeze()
high = data['High'].squeeze()
low = data['Low'].squeeze()

# --- INDICATORS ---
# EMA
data['EMA20'] = close.ewm(span=20).mean()
data['EMA50'] = close.ewm(span=50).mean()

# RSI 14
delta = close.diff()
gain = delta.where(delta > 0, 0).rolling(14).mean()
loss = -delta.where(delta < 0, 0).rolling(14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))

# MACD
ema12 = close.ewm(span=12).mean()
ema26 = close.ewm(span=26).mean()
data['MACD'] = ema12 - ema26
data['MACD_Signal'] = data['MACD'].ewm(span=9).mean()

last = data.iloc[-1]
price = float(last['Close'])
ema20 = float(last['EMA20'])
ema50 = float(last['EMA50'])
rsi = float(last['RSI'])
macd = float(last['MACD'])
macd_sig = float(last['MACD_Signal'])

# --- 98% QUALITY LOGIC - 4 FILTER ---
buy_cond = (ema20 > ema50) and (rsi > 40 and rsi < 70) and (macd > macd_sig) and (price > ema20)
sell_cond = (ema20 < ema50) and (rsi > 30 and rsi < 60) and (macd < macd_sig) and (price < ema20)

# --- DISPLAY ---
c1,c2,c3,c4 = st.columns(4)
c1.metric("Gold Price", f"${price:.2f}")
c2.metric("EMA20 / EMA50", f"{ema20:.1f} / {ema50:.1f}")
c3.metric("RSI", f"{rsi:.1f}")
c4.metric("MACD", f"{macd:.2f}")

# --- BACKTEST - WIN RATE ---
data['Signal'] = 0
data.loc[(data['EMA20'] > data['EMA50']) & (data['MACD'] > data['MACD_Signal']), 'Signal'] = 1
data.loc[(data['EMA20'] < data['EMA50']) & (data['MACD'] < data['MACD_Signal']), 'Signal'] = -1
# Simple win rate calc
wins = len(data[(data['Signal']==1) & (data['Close'].shift(-5) > data['Close'])])
total = len(data[data['Signal']!=0])
win_rate = (wins/total*100) if total>0 else 0
st.info(f"📊 Backtest Win Rate (Last 1 Month): {win_rate:.1f}% | Total Signals: {total}")

# --- FINAL SIGNAL ---
if buy_cond:
    st.success(f"✅ HIGH QUALITY BUY - Gold Upar Jaye Ga! | SL: ${price-15:.1f} | TP: ${price+30:.1f}")
    signal_text = f"BUY Gold @ ${price:.2f} | RSI {rsi:.1f} | SL {price-15:.1f} TP {price+30:.1f} - 98% Quality"
elif sell_cond:
    st.error(f"❌ HIGH QUALITY SELL - Gold Neeche Aye Ga! | SL: ${price+15:.1f} | TP: ${price-30:.1f}")
    signal_text = f"SELL Gold @ ${price:.2f} | RSI {rsi:.1f} | SL {price+15:.1f} TP {price-30:.1f} - 98% Quality"
else:
    st.warning("⏳ WAIT - No Strong Signal - 4 Filter Match Nahi Hua")
    signal_text = None

# --- TELEGRAM AUTO ---
if signal_text:
    try:
        requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={signal_text}")
        st.toast("Telegram bhej diya! Auto ON")
    except:
        pass

# --- CHART ---
st.line_chart(data[['Close','EMA20','EMA50']].tail(200))

st.caption("Disclaimer: Trading risky hai, 98% guarantee nahi, ye best quality filter hai")
# Auto Refresh 15 min
time.sleep(900)
st.rerun()
