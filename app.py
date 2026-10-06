import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

st.set_page_config(page_title="L6SJ Gold AI V6 PRO", layout="wide")
st.title("🏅 L6SJ Gold AI V6 PRO - High Quality")
st.caption("GC=F | 15m + 5m + 1m | EMA + RSI + MACD + ATR")

@st.cache_data(ttl=60)
def get_data(tf):
    try:
        period_map = {"15m": "5d", "5m": "2d", "1m": "1d"}
        data = yf.download("GC=F", period=period_map[tf], interval=tf, progress=False)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        data['EMA9'] = data['Close'].ewm(span=9).mean()
        data['EMA21'] = data['Close'].ewm(span=21).mean()
        data['EMA50'] = data['Close'].ewm(span=50).mean()
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).ewm(alpha=1/14).mean()
        loss = (-delta.where(delta < 0, 0)).ewm(alpha=1/14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        exp1 = data['Close'].ewm(span=12).mean()
        exp2 = data['Close'].ewm(span=26).mean()
        data['MACD'] = exp1 - exp2
        data['MACD_SIGNAL'] = data['MACD'].ewm(span=9).mean()
        data['ATR'] = (data['High'] - data['Low']).ewm(span=14).mean()
        return data.dropna().tail(100)
    except:
        return None

# FETCH ALL TIMEFRAMES
tf_list = ["15m", "5m", "1m"]
all_data = {}
cols = st.columns(3)

for i, tf in enumerate(tf_list):
    df = get_data(tf)
    if df is not None and len(df) > 20:
        last = df.iloc[-1]
        price = float(last['Close'])
        rsi = float(last['RSI'])
        ema9 = float(last['EMA9'])
        ema21 = float(last['EMA21'])
        ema50 = float(last['EMA50'])
        macd = float(last['MACD'])
        macd_sig = float(last['MACD_SIGNAL'])
        atr = float(last['ATR'])

        score = 0
        if price > ema9: score += 1
        if ema9 > ema21: score += 1
        if ema21 > ema50: score += 1
        if rsi > 50: score += 1
        if macd > macd_sig: score += 1

        signal = "BUY" if score >= 3 else "SELL"
        if score == 3: signal = "NEUTRAL"

        all_data[tf] = {"price": price, "rsi": rsi, "score": score, "signal": signal, "ema9": ema9, "ema21": ema21, "ema50": ema50, "macd": macd, "macd_sig": macd_sig, "atr": atr}

        with cols[i]:
            st.subheader(f"⏰ {tf}")
            st.metric("Price", f"{price:.2f}", delta=f"RSI {rsi:.0f}")
            st.write(f"EMA 9/21/50: {ema9:.1f} / {ema21:.1f} / {ema50:.1f}")
            st.write(f"MACD: {macd:.2f} vs {macd_sig:.2f} | ATR: {atr:.2f}")
            st.write(f"Score: {score}/5")
            if "BUY" in signal:
                st.success(f"▲ {signal} - {score}/5")
            elif "SELL" in signal:
                st.error(f"▼ {signal} - {score}/5")
            else:
                st.warning(f"{signal} - {score}/5")

if len(all_data) == 3:
    buy_count = sum(1 for v in all_data.values() if "BUY" in v["signal"])
    sell_count = sum(1 for v in all_data.values() if "SELL" in v["signal"])
    avg_rsi = np.mean([v["rsi"] for v in all_data.values()])
    avg_score = np.mean([v["score"] for v in all_data.values()])
    curr_price = all_data["5m"]["price"]
    curr_atr = all_data["5m"]["atr"]

    # QUALITY CALCULATION - FOR BOTH BUY & SELL - FIXED
    quality = 0
    strong_count = max(buy_count, sell_count)
    quality += strong_count * 25
    quality += 10
    quality += 15 if (avg_score >= 3 or avg_score <= 2) else 0
    quality = min(quality, 95)

    st.divider()
    st.header("🎯 FINAL DECISION")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg RSI", f"{avg_rsi:.0f}")
    c2.metric("Avg Score", f"{avg_score:.1f}/5")
    c3.metric("BUY TFs", f"{buy_count}/3")
    c4.metric("Quality", f"{quality:.0f}%")

    st.progress(quality/100)

    sl = curr_price - curr_atr*1.2 if buy_count > sell_count else curr_price + curr_atr*1.2
    tp = curr_price + curr_atr*1.5 if buy_count > sell_count else curr_price - curr_atr*1.5

    if all_data["15m"]["rsi"] > 72:
        st.warning("⚠️ 15m RSI Overbought (>72) - WAIT for BUY")
    elif buy_count == 3 and quality >= 80:
        st.success(f"✅ STRONG BUY CONFIRMED - 3/3 TF | Quality {quality:.0f}%")
        st.balloons()
    elif buy_count >= 2 and quality >= 65:
        st.success(f"✅ BUY SIGNAL - {buy_count}/3 TF | Quality {quality:.0f}%")
    elif sell_count == 3 and quality >= 80:
        st.error(f"🔻 STRONG SELL CONFIRMED - 3/3 TF | Quality {quality:.0f}%")
    elif sell_count >= 2:
        st.error(f"🔻 SELL SIGNAL - {sell_count}/3 TF | Quality {quality:.0f}%")
    else:
        st.info(f"⏸️ NO CLEAR SIGNAL - Wait | Quality {quality:.0f}%")

    st.write(f"**Entry:** {curr_price:.2f} | **SL:** {sl:.2f} | **TP:** {tp:.2f}")

    with st.expander("📊 Details Analysis"):
        st.json(all_data)

st.button("🔄 Refresh")
