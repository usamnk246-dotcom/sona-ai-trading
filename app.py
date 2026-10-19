import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="L6SJ Gold AI V6 PRO - KING 103 WAR", page_icon="👑", layout="wide")

st.markdown("""<div style="background: linear-gradient(90deg, #000, #FFD700); padding:12px; border-radius:12px; text-align:center; color:white;">
<h2>👑 SONA AI - KING 103 WAR MODE 👑</h2></div>""", unsafe_allow_html=True)

st.title("🏆 L6SJ Gold AI V6 PRO - High Quality Signals")
st.caption("GC=F | 15m + 5m + 1m | EMA 9/21/50 | RSI14 | MACD | ATR | King 103 War + Alert")

@st.cache_data(ttl=60)
def get_data(tf):
    try:
        period_map = {"15m": "5d", "5m": "2d", "1m": "1d"}
        data = yf.download("GC=F", period=period_map.get(tf, "5d"), interval=tf, progress=False)
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)
        data = data.dropna()
        data['EMA9'] = data['Close'].ewm(span=9).mean()
        data['EMA21'] = data['Close'].ewm(span=21).mean()
        data['EMA50'] = data['Close'].ewm(span=50).mean()
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        exp1 = data['Close'].ewm(span=12).mean()
        exp2 = data['Close'].ewm(span=26).mean()
        data['MACD'] = exp1 - exp2
        data['MACD_SIGNAL'] = data['MACD'].ewm(span=9).mean()
        data['ATR'] = (data['High'] - data['Low']).rolling(14).mean()
        return data.dropna().tail(100)
    except: return None

tf_list = ["15m", "5m", "1m"]
all_data = {}
cols = st.columns(3)
for i, tf in enumerate(tf_list):
    df = get_data(tf)
    if df is not None and len(df) > 20:
        last = df.iloc[-1]
        price = float(last['Close']); rsi = float(last['RSI']); ema9 = float(last['EMA9'])
        ema21 = float(last['EMA21']); ema50 = float(last['EMA50']); macd = float(last['MACD'])
        macd_sig = float(last['MACD_SIGNAL']); atr = float(last['ATR'])
        score = 0
        if price > ema9: score += 1
        if ema9 > ema21: score += 1
        if ema21 > ema50: score += 1
        if rsi > 50: score += 1
        if macd > macd_sig: score += 1
        signal = "BUY" if score >= 3 else "SELL"
        if score == 3: signal = "NEUTRAL"
        all_data[tf] = {"price": price, "rsi": rsi, "score": score, "signal": signal, "atr": atr}
        with cols[i]:
            st.subheader(f"⏰ {tf}"); st.metric("Price", f"{price:.2f}")
            st.write(f"EMA 9/21/50: {ema9:.1f}/{ema21:.1f}/{ema50:.1f}"); st.write(f"Score: {score}/5")
            if "BUY" in signal and signal != "NEUTRAL": st.success(f"▲ {signal}")
            elif "SELL" in signal: st.error(f"▼ {signal}")
            else: st.warning(f"{signal}")

if len(all_data) == 3:
    buy_count = sum(1 for v in all_data.values() if "BUY" in v["signal"])
    sell_count = sum(1 for v in all_data.values() if "SELL" in v["signal"])
    avg_rsi = np.mean([v["rsi"] for v in all_data.values()]); avg_score = np.mean([v["score"] for v in all_data.values()])
    curr_price = all_data["5m"]["price"]; curr_atr = all_data["5m"]["atr"]
    quality = 0; strong_count = max(buy_count, sell_count); quality += strong_count * 25; quality += 10
    quality += 15 if (avg_score >= 3 or avg_rsi > 55) else 0; quality = min(quality, 95)
    st.divider(); st.header("🎯 FINAL DECISION - KING 103 WAR")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Avg RSI", f"{avg_rsi:.0f}"); c2.metric("Avg Score", f"{avg_score:.1f}/5")
    c3.metric("BUY TFs", f"{buy_count}/3"); c4.metric("Quality", f"{quality:.0f}%")
    st.progress(quality/100)
    sl = curr_price - curr_atr*1.2 if buy_count >=2 else curr_price + curr_atr*1.2
    tp = curr_price + curr_atr*1.5 if buy_count >=2 else curr_price - curr_atr*1.5
    st.subheader("🔔 KHAPEL ALERT - King 103 War Mode")
    alert_on = st.toggle("🔔 Alert ON Karo - Morning War Active", value=False)
    alert_quality = st.slider("Min Quality", 50, 90, 65)
    alert_triggered = False
    if all_data["15m"]["rsi"] > 72: st.warning("⚠️ 15m RSI Overbought")
    elif buy_count == 3 and quality >= 80:
        st.success(f"✅ STRONG BUY CONFIRMED - {curr_price:.2f} | Quality {quality:.0f}% - KING 103 WAR"); st.balloons(); alert_triggered = True
    elif buy_count >= 2 and quality >= 65:
        st.success(f"✅ BUY SIGNAL - {buy_count}/3 TFs - Quality {quality:.0f}%"); alert_triggered = True
    elif sell_count == 3 and quality >= 80:
        st.error(f"▼ STRONG SELL CONFIRMED - {curr_price:.2f}"); alert_triggered = True
    elif sell_count >= 2:
        st.error(f"▼ SELL SIGNAL - {sell_count}/3 TFs"); alert_triggered = True
    else: st.info(f"⏸️ NO CLEAR SIGNAL - Buy {buy_count} Sell {sell_count}")
    if alert_on and alert_triggered and quality >= alert_quality:
        st.components.v1.html(f"""<script>if (Notification.permission !== 'granted') {{ Notification.requestPermission(); }} else {{ new Notification('👑 KING 103 WAR!', {{body: 'GOLD {curr_price:.2f} Quality {quality:.0f}%'}}); }}</script><audio autoplay><source src="https://www.soundjay.com/buttons/beep-07a.wav"></audio>""", height=100)
        st.toast(f"🔔 KING 103 ALERT! {curr_price:.2f}", icon="👑")
    elif alert_on:
        st.info("🔄 60 sec me auto reload..."); time.sleep(60); st.rerun()
    st.write(f"**Entry:** {curr_price:.2f} | **SL:** {sl:.2f} | **TP:** {tp:.2f}")
    with st.expander("📊 Details Analysis"): st.json(all_data)
st.button("🔄 Refresh - War Mode")
