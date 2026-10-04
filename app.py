import streamlit as st
import yfinance as yf
import pandas as pd
import requests
import time

# --- AUTO TELEGRAM ---
def send_telegram_auto(msg):
    try:
        token = st.secrets["TELEGRAM_TOKEN"]
        url = f"https://api.telegram.org/bot{token}/getUpdates"
        r = requests.get(url, timeout=10).json()
        if r.get("result"):
            chat_id = r["result"][-1]["message"]["chat"]["id"]
            send_url = f"https://api.telegram.org/bot{token}/sendMessage"
            requests.post(send_url, data={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"})
    except:
        pass

st.set_page_config(page_title="Sona AI PRO MAX V3", page_icon="💰", layout="wide")

# Yesterday wala design
st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
div[data-testid="metric"] { background: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid gold; }
</style>
""", unsafe_allow_html=True)

st.title("💰 Sona AI - GOLD PRO MAX V3")
st.caption("Wase sah | Auto Telegram ON")

symbol = "GC=F"
data = yf.download(symbol, period="5d", interval="15m", auto_adjust=True)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)
data = data.dropna()

if len(data) < 30:
    st.warning("Data loading...")
    st.stop()

data['EMA20'] = data['Close'].ewm(span=20).mean()
data['EMA50'] = data['Close'].ewm(span=50).mean()

close_col = data['Close']
if isinstance(close_col, pd.DataFrame):
    close_col = close_col.iloc[:,0]

last_price = float(close_col.iloc[-1])
ema20 = float(data['EMA20'].iloc[-1])
ema50 = float(data['EMA50'].iloc[-1])

c1, c2, c3 = st.columns(3)
c1.metric("Gold Price", f"${last_price:.2f}")
c2.metric("EMA20", f"{ema20:.2f}")
c3.metric("EMA50", f"{ema50:.2f}")

if ema20 > ema50:
    st.success(f"🚀 BUY SIGNAL @ ${last_price:.2f} - Auto Telegram bhej diya!")
    # AUTOMATIC SEND
    send_telegram_auto(f"🚀 *GOLD BUY AUTO* @ ${last_price:.2f}\nEMA20 {ema20:.2f} > EMA50 {ema50:.2f}\nTime: {pd.Timestamp.now()}\nSona AI V3")
else:
    st.error(f"🔻 SELL SIGNAL @ ${last_price:.2f} - Auto Telegram bhej diya!")
    send_telegram_auto(f"🔻 *GOLD SELL AUTO* @ ${last_price:.2f}\nEMA20 {ema20:.2f} < EMA50 {ema50:.2f}\nTime: {pd.Timestamp.now()}\nSona AI V3")

st.line_chart(data[['Close','EMA20','EMA50']].tail(100))

# Auto refresh every 15 min
st.caption("Auto refresh: 15 min | Telegram Auto ON")
time.sleep(5)
st.rerun()
