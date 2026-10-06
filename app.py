import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="L6SJ Gold V6 PRO", layout="wide")
st.title("🏅 L6SJ Gold AI V6 PRO - High Quality")
st.caption("GC=F | 15m + 5m + 1m | EMA + RSI + MACD + ATR")

# --- INDICATORS ---
def calc_rsi(close, p=14):
    try:
        d = close.diff()
        g = d.where(d>0,0).rolling(p).mean()
        l = -d.where(d<0,0).rolling(p).mean()
        rs = g / l
        return float((100 - (100/(1+rs))).iloc[-1])
    except: return 50

def calc_macd(close):
    try:
        e12 = close.ewm(span=12).mean()
        e26 = close.ewm(span=26).mean()
        macd = e12 - e26
        sig = macd.ewm(span=9).mean()
        return float(macd.iloc[-1]), float(sig.iloc[-1])
    except: return 0,0

def get_data(tf):
    try:
        df = yf.download("GC=F", period="5d", interval=tf, progress=False, auto_adjust=True)
        if df is None or len(df) < 50: return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        c = df['Close']
        h = df['High']
        l = df['Low']
        price = float(c.iloc[-1])
        e9 = float(c.ewm(span=9).mean().iloc[-1])
        e21 = float(c.ewm(span=21).mean().iloc[-1])
        e50 = float(c.ewm(span=50).mean().iloc[-1])
        rsi = calc_rsi(c)
        macd, macd_sig = calc_macd(c)
        # ATR for SL/TP
        tr = pd.concat([h-l, (h-c.shift()).abs(), (l-c.shift()).abs()], axis=1).max(axis=1)
        atr = float(tr.rolling(14).mean().iloc[-1])

        # SIGNAL LOGIC
        score = 0
        if e9 > e21: score += 1
        if e21 > e50: score += 1
        if 40 < rsi < 68: score += 1
        if macd > macd_sig: score += 1
        if price > e9: score += 1

        if score >= 4:
            sig = "BUY"
        elif score <= 1:
            sig = "SELL"
        else:
            sig = "WAIT"

        return {"price":price, "e9":e9, "e21":e21, "e50":e50, "rsi":rsi, "macd":macd, "macd_sig":macd_sig, "atr":atr, "score":score, "signal":sig}
    except:
        return None

# --- FETCH ---
tfs = ["15m", "5m", "1m"]
cols = st.columns(3)
all_data = {}

for i, tf in enumerate(tfs):
    with cols[i]:
        st.subheader(f"⏰ {tf}")
        d = get_data(tf)
        all_data[tf] = d
        if d:
            st.metric("Price", f"{d['price']:.2f}", f"RSI {d['rsi']:.0f}")
            st.write(f"EMA 9/21/50: {d['e9']:.1f} / {d['e21']:.1f} / {d['e50']:.1f}")
            st.write(f"MACD: {d['macd']:.2f} vs {d['macd_sig']:.2f} | ATR: {d['atr']:.2f}")
            st.write(f"Score: {d['score']}/5")
            if d['signal']=="BUY":
                st.success(f"✅ {d['signal']} - {d['score']}/5")
            elif d['signal']=="SELL":
                st.error(f"🔻 {d['signal']} - {d['score']}/5")
            else:
                st.warning(f"⏸️ {d['signal']} - {d['score']}/5")
        else:
            st.warning("Loading...")

st.divider()
st.subheader("🎯 FINAL DECISION")

if all_data.get("15m") and all_data.get("5m") and all_data.get("1m"):
    p = all_data["5m"]["price"]
    atr = all_data["5m"]["atr"]
    buy_count = sum(1 for v in all_data.values() if v and v["signal"]=="BUY")
    sell_count = sum(1 for v in all_data.values() if v and v["signal"]=="SELL")
    avg_score = sum(v["score"] for v in all_data.values() if v) / 3
    avg_rsi = sum(v["rsi"] for v in all_data.values() if v) / 3

    # QUALITY CALCULATION
    quality = 0
    quality += buy_count * 25 # 75% max
    quality += (avg_score / 5) * 15 # 15% max
    if 45 < avg_rsi < 65: quality += 10 # perfect RSI

    quality = min(95, int(quality))

    # SL / TP with ATR (Professional)
    sl = p - (atr * 1.5)
    tp1 = p + (atr * 2)
    tp2 = p + (atr * 3.5)

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Avg RSI", f"{avg_rsi:.0f}")
    c2.metric("Avg Score", f"{avg_score:.1f}/5")
    c3.metric("BUY TFs", f"{buy_count}/3")
    c4.metric("Quality", f"{quality}%")

    st.progress(quality/100)

    if all_data["15m"]["rsi"] > 72:
        st.error("🔴 HIGH RISK - 15m RSI >72 Overbought! WAIT")
    elif all_data["15m"]["rsi"] < 28:
        st.error("🔴 HIGH RISK - 15m RSI <28 Oversold! WAIT")
    elif buy_count == 3 and quality >= 80:
        st.success(f"✅✅ STRONG BUY CONFIRMED - {buy_count}/3 TF | Quality {quality}%")
        st.balloons()
        st.write(f"**Entry:** {p:.2f} | **SL:** {sl:.2f} (-{p-sl:.2f}) | **TP1:** {tp1:.2f} (+{tp1-p:.2f}) | **TP2:** {tp2:.2f}")
    elif buy_count >= 2 and quality >= 65:
        st.success(f"✅ BUY CONFIRMED - {buy_count}/3 TF | Quality {quality}%")
        st.write(f"**Entry:** {p:.2f} | **SL:** {sl:.2f} | **TP1:** {tp1:.2f} | **TP2:** {tp2:.2f}")
    elif sell_count >= 2:
        st.error(f"🔻 SELL SIGNAL - {sell_count}/3 TF | Quality {quality}%")
        st.write(f"**Entry:** {p:.2f} | **SL:** {p + atr*1.5:.2f} | **TP:** {p - atr*2:.2f}")
    else:
        st.warning(f"⏸️ WAIT - No Confirmation | {buy_count} BUY / {sell_count} SELL | Quality {quality}%")
        st.info("Rule: Need 2/3 BUY + RSI 45-65 + MACD Bullish for High Quality")

    with st.expander("📊 Details Analysis"):
        st.write(all_data)

else:
    st.info("⏳ Loading multi-timeframe data... Auto refresh in 60s")

time.sleep(60)
st.rerun()
