# app.py - FINAL FIX - Sona AI Advance Dark Premium - USMAN
import streamlit as st
st.set_page_config(page_title="ADVANCE - KING V103 x SONA LINKED", layout="centered")

st.markdown("""
<style>
.stApp { background: #020A14 !important; }
[data-testid="stHeader"] { background: #020A14 !important; }
h1,h2,h3,p,span,label { color: white !important; }
.stSelectbox div[data-baseweb="select"] > div { background: #0F1F35 !important; color: white !important; border: 1px solid #1E3A5F !important; }
.stNumberInput input, .stTextInput input { background: #0F1F35 !important; color: white !important; }
section[data-testid="stSlider"] { background: #0F1F35 !important; border-radius: 12px; padding: 10px; }
div[data-testid="stMetric"] { background: linear-gradient(135deg, #0B1E35, #081425); border: 1px solid rgba(255,215,0,0.2); border-radius: 16px; padding: 12px; }
</style>

<div style="background: linear-gradient(135deg, #081425, #0B1E35); border:1px solid rgba(255,215,0,0.25); box-shadow:0 0 25px rgba(255,215,0,0.12); border-radius:20px; padding:18px; margin-bottom:20px;">
  <span style="background: rgba(0,255,194,0.1); border:1px solid #00FFC2; color:#00FFC2; border-radius:20px; padding:5px 12px; font-size:12px;">⭐ AI Powered Trading</span>
  <h2 style="font-size:28px; font-weight:800; margin-top:12px; line-height:1.1; color:white;">Your <span style="color:#00FFC2;">AI</span> Trading<br>Companion</h2>
  <p style="color:#9CA3AF; font-size:13px;">Sona AI analyzes market, finds best opportunities</p>
  <div style="margin-top:14px; display:inline-block; background: linear-gradient(90deg, #00D4FF, #00FF9D); color:black; font-weight:800; padding:10px 20px; border-radius:30px;">📈 Start Trading →</div>
  <div style="margin-top:14px; color:#FFD700; font-size:11px;">• LIVE MARKETS • REAL-TIME</div>
  <div style="display:grid; grid-template-columns: 1fr 1fr; gap:8px; margin-top:14px;">
    <div style="background:#0F2A4A; border-radius:12px; padding:10px;"><div style="font-size:11px; color:#aaa;">₿ BTC/USDT</div><div style="font-weight:800; color:white;">67,432.18</div><div style="color:#00FF88; font-size:12px;">+2.34% ▲</div></div>
    <div style="background:#0F2A4A; border-radius:12px; padding:10px;"><div style="font-size:11px; color:#aaa;">🪙 XAU/USD</div><div style="font-weight:800; color:white;">2,658.42</div><div style="color:#00FF88; font-size:12px;">+0.82% ▲</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### USMAN Strategy - All IN ONE - KING + SONI + KING V103")
ema_fast = st.selectbox("EMA Fast", ["EMA 9", "EMA 50"])
ema_slow = st.selectbox("EMA Slow", ["EMA 21", "EMA 200"])
rsi = st.slider("RSI 14", 0, 100, 63)
macd = st.number_input("MACD", value=0.44)
vwap = st.number_input("VWAP", value=4175.17)
atr = st.number_input("ATR (14)", value=9.25)

vol = st.checkbox("Volume Confirm", True)
liq = st.checkbox("Liquidity Sweep Detected", True)
bos = st.checkbox("BOS Confirmed", True)
pull = st.checkbox("Pullback + OB + FVG", True)

tf = st.selectbox("Timeframe", ["5m", "15m", "30m", "1H", "4H"], index=2)
market = st.selectbox("Market", ["XAU/USD GOLD", "BTC/USDT", "EUR/USD"])

auto = st.toggle("Automatic Trading", True)
self_alert = st.toggle("Self Alert - Yesterday wala link", True)
win = st.slider("Win Rate Target", 85, 99, 95)

score = 7 if (vol and liq and bos and pull) else 5

st.markdown(f"""
<div style="background:#081425; border:1px solid rgba(255,215,0,0.2); border-radius:16px; padding:14px; display:flex; gap:16px; margin:16px 0;">
  <div><div style="color:#aaa; font-size:12px;">Quality Filter Score</div><div style="font-size:26px; font-weight:800; color:white;">{score}/7 Minimum 6/7</div></div>
  <div><div style="color:#aaa; font-size:12px;">Win Rate</div><div style="font-size:26px; font-weight:800; color:#00FF88;">{win}%</div></div>
  <div><div style="color:#aaa; font-size:12px;">Automatic Trading</div><div style="color:#00FF88; font-weight:700;">Running ✅</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("#### KING V103 4/HR BOTH • KING V103 x SONA AI LINKED • XAUUSD 5m")
st.line_chart({"Price": [4172, 4179, 4182]})

if auto and score >= 6:
    st.success(f"🔔 BUY SIGNAL CONFIRMED HIGH QUALITY {score}/7 - GOLD XAUUSD @ 4185.50 - KING 103 WAR - TP 4213.25 SL 4171.62 RR 1:2.5 - AUTOTRADER EXECUTED | Timeframe: {tf} • Market: {market} • EMA 9/21/200 Aligned • VWAP {vwap} • ATR {atr}")
    if self_alert:
        st.info("Self Alert Triggered: https://har-kala-alert... - BUY XAUUSD - Yesterday wala link")
else:
    st.warning(f"Skipped - Score {score}/7 - Need 6/7")

c1,c2,c3 = st.columns(3)
c1.metric("Total Balance", "$12,452", "+$824.50")
c2.metric("Win Rate", "90%", "27W/3L")
c3.metric("Open Trades", "3", "Running")
st.metric("Daily Profit", "+$542.17", "+4.32% (24h)")
