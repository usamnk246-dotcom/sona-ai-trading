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
            st.success(f"Telegram bheja! Chat ID: {chat_id}")
        else:
            st.warning("Telegram me /start bhejo pehle!")
    except Exception as e:
        st.error(f"Error: {e}")

st.set_page_config(page_title="Sona AI PRO MAX V3", page_icon="💰")
st.title("💰 Sona AI - GOLD PRO MAX V3")
st.write("Wase sah ka Sona AI - Live!")

symbol = "GC=F"
data = yf.download(symbol, period="5d", interval="15m", auto_adjust=True)

if data.empty:
    st.error("Data nahi aa raha")
    st.stop()

data = data.dropna()
if len(data) < 30:
    st.warning("Data kam hai, wait karo")
    st.stop()

data['EMA20'] = data['Close'].ewm(span=20).mean()
data['EMA50'] = data['Close'].ewm(span=50).mean()

last_price = float(data['Close'].iloc[-1])
ema20 = float(data['EMA20'].iloc[-1])
ema50 = float(data['EMA50'].iloc[-1])

st.metric("Gold Price", f"${last_price:.2f}")

if ema20 > ema50:
    st.success(f"🚀 BUY SIGNAL @ ${last_price:.2f}")
    if st.button("Telegram pe Bhejo 📲"):
        send_telegram(f"🚀 *GOLD BUY* @ ${last_price:.2f}\nEMA20 {ema20:.2f} > EMA50 {ema50:.2f}\nSona AI V3")
else:
    st.error(f"🔻 SELL SIGNAL @ ${last_price:.2f}")
    if st.button("Telegram pe Bhejo 📲"):
        send_telegram(f"🔻 *GOLD SELL* @ ${last_price:.2f}\nEMA20 {ema20:.2f} < EMA50 {ema50:.2f}\nSona AI V3")

st.line_chart(data[['Close','EMA20','EMA50']].tail(100))
