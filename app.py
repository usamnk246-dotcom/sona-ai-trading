import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="L6SJ Gold Bot V5", layout="wide")
st.title("🏅 L6SJ Gold AI Bot V5 - Multi-Timeframe")

# Requirements check
st.write("Loading gold data...")

def calc_rsi(close, period=14):
    try:
        delta = close.diff()
        gain = delta.where(delta > 0, 0).rolling(window=period).mean()
        loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return float(rsi.iloc[-1])
    except:
        return 50.0

def get_data(tf):
    try:
        # GC=F kabhi kabhi block hota, XAUUSD try
        df = yf.download("GC=F", period="2d", interval=tf, progress=False, auto_adjust=True)
        if df is None or len(df) < 20:
            return None
        # Fix MultiIndex issue
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        close = df['Close']
        price = float(close.iloc[-1])
        ema9 = float(close.ewm(span=9).mean().iloc[-1])
        ema21 = float(close.ewm(span=21).mean().iloc[-1])
        rsi = calc_rsi(close)

        if ema9 > ema21 and rsi < 68:
            sig = "BUY"
        elif ema9 < ema21:
            sig = "SELL"
        else:
            sig = "WAIT"
        return {"price":price, "ema9":ema9, "ema21":ema21, "rsi":rsi, "signal":sig}
    except Exception as e:
        st.error(f"{tf} error: {e}")
        return None

# ONLY 4 TF - 2m hatao, yfinance ke nahi
timeframes = ["15m", "5m", "1m"]
cols = st.columns(3)

all_data = {}
for i, tf in enumerate(timeframes):
    with cols[i]:
        st.subheader(tf)
        d = get_data(tf)
        all_data[tf] = d
        if d:
            st.metric("Price", f"{d['price']:.2f}")
            st.write(f"EMA9: {d['ema9']:.2f} | EMA21: {d['ema21']:.2f}")
            st.write(f"RSI: {d['rsi']:.1f}")
                        if d['signal']=="BUY":
                st.success(f"✅ {d['signal']}")
            elif d['signal']=="SELL":
                st.error(f"🔻 {d['signal']}")
            else:
                st.warning(f"⏸️ {d['signal']}")
                else:
        st.warning("Loading...")

st.divider()

# Final Signal
if all_data.get("15m") and all_data.get("5m"):
    price = all_data["5m"]["price"]
    buy_count = sum(1 for v in all_data.values() if v and v["signal"]=="BUY")

    sl = price - 8
    tp = price + 16
    quality = 40 + buy_count*20

    if all_data["15m"]["rsi"] > 70:
        st.error("🔻 WAIT - Overbought RSI > 70")
    elif buy_count >= 2:
        st.success(f"✅ BUY CONFIRMED - {buy_count}/3 TF")
        st.progress(quality/100)
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Quality", f"{quality}%")
        c2.metric("Entry", f"{price:.2f}")
        c3.metric("SL", f"{sl:.2f}")
        c4.metric("TP", f"{tp:.2f}")
    else:
        st.warning(f"⏸️ WAIT - {buy_count}/3 BUY")
else:
    st.info("Market closed or data loading, 1 min wait then refresh")

# Auto refresh
time.sleep(60)
st.rerun()
