import streamlit as st
import yfinance as yf
import pandas as pd
import requests

def send_telegram(msg):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        r = requests.get(url, timeout=10).json()
        if r.get("result"):
            chat_id = r["result"][-1]["message"]["chat"]["id"]
            send_url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(send_url, data={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})
            st.success(f"Telegram OK: {chat_id}")
        else:
            st.warning("Pehle Telegram bot ko /start bhejo!")
    except Exception as e:
        st.error(f"Telegram Error: {e}")

st.set_page_config(page_title="Sona AI PRO MAX V3", page_icon="💰")
st.title("💰 Sona AI - GOLD PRO MAX V3")
st.write("Wase sah ka Sona AI - Live!")

symbol = "GC=F"
data = yf.download(symbol, period="5d", interval="15m", auto_adjust=True)

if data.empty:
    st.error("Data nahi aa raha")
    st.stop()

# --- IMPORTANT FIX for ValueError & TypeError ---
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

data = data.dropna()
if len(data) < 30:
    st.warning("Data kam hai")
    st.stop()

data['EMA20'] = data['Close'].ewm(span=20).mean()
data['EMA50'] = data['Close'].ewm(span=50).mean()

# Safe price extract
close_col = data['Close']
if isinstance(close_col, pd.DataFrame):
    close_col = close_col.iloc[:,0]
last_price = float(close_col.iloc[-1])
ema20 = float(data['EMA20'].iloc[-1])
ema50 = float(data['EMA50'].iloc[-1])

st.metric("Gold Price (XAUUSD)", f"${last_price:.2f}")

col1, col2 = st.columns(2)
with col1:
    st.write(f"EMA20: {ema20:.2f}")
with col2:
    st.write(f"EMA50: {ema50:.2f}")

if ema20 > ema50:
    st.success(f"🚀 BUY SIGNAL @ ${last_price:.2f}")
    if st.button("Telegram pe Bhejo 📲"):
        send_telegram(f"🚀 *GOLD BUY* @ ${last_price:.2f}\nEMA20 {ema20:.2f} > EMA50 {ema50:.2f}")
else:
    st.error(f"🔻 SELL SIGNAL @ ${last_price:.2f}")
    if st.button("Telegram pe Bhejo 📲"):
        send_telegram(f"🔻 *GOLD SELL* @ ${last_price:.2f}\nEMA20 {ema20:.2f} < EMA50 {ema50:.2f}")

st.line_chart(data[['Close','EMA20','EMA50']].tail(100))
st.caption("Sona AI V3 | Wase sah")
