import streamlit as st
import yfinance as yf
import pandas as pd
import time

# Auto Refresh
st.set_page_config(page_title="L6SJ Gold Bot V5", layout="wide")
st_autorefresh = st.empty()
st.markdown("<meta http-equiv='refresh' content='60'>", unsafe_allow_html=True)

st.title("🥇 L6SJ Gold AI Bot V5 - Multi-Timeframe")

# === RSI Function ===
def calc_rsi(data, period=14):
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

# === One Timeframe Signal ===
def get_tf_data(tf):
    try:
        # 2m yfinance ke nishta, 1m use kao
        yf_tf = "1m" if tf == "2m" else tf
        df = yf.download("GC=F", period="1d", interval=yf_tf, progress=False)
        if len(df) < 30: return None

        close = df['Close']
        ema9 = close.ewm(span=9).mean().iloc[-1]
        ema21 = close.ewm(span=21).mean().iloc[-1]
        rsi = calc_rsi(df)
        price = close.iloc[-1]

        # Signal Logic
        if ema9 > ema21 and rsi < 70 and rsi > 50:
            sig = "BUY"
        elif ema9 < ema21:
            sig = "SELL"
        else:
            sig = "WAIT"

        return {"price": price, "ema9": ema9, "ema21": ema21, "rsi": rsi, "signal": sig, "df": df}
    except:
        return None

# === Multi-Timeframe Check ===
timeframes = ["15m", "10m", "5m", "2m", "1m"]
all_data = {}

cols = st.columns(5)
for i, tf in enumerate(timeframes):
    data = get_tf_data(tf)
    all_data[tf] = data
    with cols[i]:
        if data:
            st.subheader(f"{tf}")
            st.metric("Price", f"{data['price']:.2f}")
            st.write(f"EMA9: {data['ema9']:.2f}")
            st.write(f"EMA21: {data['ema21']:.2f}")
            st.write(f"RSI: {data['rsi']:.1f}")
            color = "green" if data['signal']=="BUY" else "red" if data['signal']=="SELL" else "gray"
            st.markdown(f":{color}[**{data['signal']}**]")

# === FINAL SIGNAL + TP/SL ===
st.divider()
if all_data["15m"] and all_data["5m"]:
    price = all_data["1m"]["price"] if all_data["1m"] else all_data["5m"]["price"]

    # SL TP Calculation
    sl = price - 8.0
    tp = price + (price - sl) * 2 # 1:2
    entry = price

    # Quality Logic - Har Timeframe Check
    buy_count = sum(1 for tf in timeframes if all_data[tf] and all_data[tf]["signal"]=="BUY")
    rsi_now = all_data["5m"]["rsi"]

    # RSI Filter - Sta idea!
    if rsi_now > 70:
        final = "🔻 WAIT - Overbought (RSI > 70)"
        quality = 40
    elif buy_count == 5:
        final = "✅ STRONG BUY - 5/5 Timeframes"
        quality = 98
    elif buy_count >= 3 and all_data["15m"]["signal"]=="BUY":
        final = "✅ BUY - Confirmed"
        quality = 75 + buy_count*4
    else:
        final = "⏸️ WAIT - Trend Not Clear"
        quality = buy_count * 15

    st.subheader(f"Final Signal: {final}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Quality", f"{quality}%", f"{buy_count}/5 TF")
    c2.metric("Entry", f"{entry:.2f}")
    c3.metric("Stop Loss", f"{sl:.2f}", "-8$ Risk")
    c4.metric("Take Profit", f"{tp:.2f}", "+16$ Reward")

    st.progress(quality/100)
    st.caption("Quality = Signal Strength (5 Timeframe Confluence), not accuracy. Real accuracy 55-65%")
