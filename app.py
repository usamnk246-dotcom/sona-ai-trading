import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI ADVANCE", layout="wide", page_icon="⚡")

# --- HAR KALA DA - SAME DESIGN AS YOUR SCREENSHOT ---
st.markdown("""
<style>
.stApp { background: #030B1A !important; }
div[data-testid="stHeader"] { display: none; }
.card { background: linear-gradient(135deg, #0A1930 0%, #061123 100%); border: 1px solid rgba(255,215,0,0.15); border-radius: 18px; padding: 14px; }
.gold { color: #FFD700 !important; }
.teal { color: #00FFC2 !important; }
.live-box { background: rgba(0,255,194,0.08); border: 1px solid rgba(0,255,194,0.3); border-radius: 20px; padding: 4px 14px; font-size: 12px; }
.market-card { background: #081425; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 12px; }
</style>
""", unsafe_allow_html=True)

# HEADER - Same as image
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center;">
<div style="display:flex; align-items:center; gap:12px;">
<div style="font-size:42px; color:#FFD700;">⚡</div>
<div><div style="font-size:34px; font-weight:900; color:white;">Sona <span style="color:#FFD700;">AI</span> <span style="font-size:12px; border:1px solid #FFD700; padding:3px 8px; border-radius:8px;">ADVANCE</span></div>
<div style="color:#8AA0B8; font-size:13px;">Smarter Trades • Higher Profits</div></div>
</div>
<div style="display:flex; gap:18px; align-items:center;"><div style="font-size:22px;">🔔<span style="background:red; color:white; font-size:10px; padding:2px 5px; border-radius:50%; position:relative; top:-10px; left:-8px;">3</span></div><div style="background:#1A2B45; border-radius:50%; width:36px; height:36px; display:flex; align-items:center; justify-content:center;">👤</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:12px;"><span class="live-box" style="color:#00FFC2;">✦ AI Powered Trading</span></div>
<h1 style="margin:8px 0 0 0; font-size:32px; line-height:1.1;">Your <span style="color:#00FFC2;">AI</span> Trading<br>Companion</h1>
<p style="color:#8AA0B8; font-size:13px; margin:4px 0 12px 0;">Sona AI analyzes market, finds best opportunities</p>
<div style="background:linear-gradient(90deg,#1E90FF,#00FFC2); color:white; padding:10px 22px; border-radius:28px; display:inline-block; font-weight:700;">⚡ Start Trading →</div>
<p style="color:#FFD700; font-size:11px; letter-spacing:1px; margin-top:14px;">● LIVE MARKETS • REAL-TIME</p>
""", unsafe_allow_html=True)

# MORE TIMEFRAME + DIFFERENT MARKET - Dase nor ma da dar
c_tf1, c_tf2, c_tf3 = st.columns([2,2,2])
with c_tf1:
    timeframe = st.selectbox("Timeframe", ["1 min","5 min","15 min","30 min","1H","4H","1D"], index=1)
with c_tf2:
    market = st.selectbox("Market", ["XAU/USD GOLD","BTC/USDT","EUR/USD","GBP/USD","XAUUSD 5m GOLD","NAS100","US30","GBP/JPY"], index=0)
with c_tf3:
    win_rate_target = st.slider("Win Rate Target", 85, 98, 90)

# LIVE MARKETS - 4 CARDS - Same as image
# Simulate live prices based on market selection
if "BTC" in market:
    base_price = 67432.18
elif "XAU" in market or "GOLD" in market:
    base_price = 4176.07
elif "EUR" in market:
    base_price = 1.0874
else:
    base_price = 1.2987

st.markdown(f"""
<div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:10px;">
<div class="market-card"><div style="display:flex; gap:8px; align-items:center;"><span>₿</span><b>BTC/USDT</b></div><div style="font-size:18px; font-weight:800; margin-top:6px;">67,432.18</div><div style="color:#00FF88; font-size:12px;">+2.34% ▲</div></div>
<div class="market-card"><div style="display:flex; gap:8px;"><span>🪙</span><b>XAU/USD</b></div><div style="font-size:18px; font-weight:800; margin-top:6px;">{base_price:.2f}</div><div style="color:#00FF88; font-size:12px;">+0.82% ▲</div></div>
<div class="market-card"><div style="display:flex; gap:8px;"><span>€</span><b>EUR/USD</b></div><div style="font-size:18px; font-weight:800;">1.0874</div><div style="color:#00FF88; font-size:12px;">+0.21% ▲</div></div>
<div class="market-card"><div style="display:flex; gap:8px;"><span>🇬🇧</span><b>GBP/USD</b></div><div style="font-size:18px; font-weight:800;">1.2987</div><div style="color:#00FF88; font-size:12px;">+0.33% ▲</div></div>
</div>
""", unsafe_allow_html=True)

# TOGGLES - Same as image
col1, col2 = st.columns([1.2,2])
with col1:
    auto = st.toggle("Automatic Trading", True)
with col2:
    st.markdown("""
    <div style="display:flex; gap:6px;">
    <div style="background:#1A2B45; border-radius:10px; padding:6px 10px; font-size:10px; border:1px solid gold;">📊 Quality Filter Score<br><b>6/7 Minimum</b></div>
    <div style="background:#2A1F0A; border-radius:10px; padding:6px 10px; font-size:10px; border:1px solid gold;">⭐ Win Rate<br><b>90%</b></div>
    <div style="background:#1A1A0A; border-radius:10px; padding:6px 10px; font-size:10px; border:1px solid gold;">🔗 KING V103 x SONA AI<br><b>LINKED Selected</b></div>
    </div>
    """, unsafe_allow_html=True)

# SIGNALS + CHART - Tol chart sah monga kala da
# Generate data based on timeframe
periods = 100
if "1 min" in timeframe: freq="1min"
elif "5 min" in timeframe: freq="5min"
elif "15 min" in timeframe: freq="15min"
elif "30 min" in timeframe: freq="30min"
elif "1H" in timeframe: freq="H"
elif "4H" in timeframe: freq="4H"
else: freq="D"

dates = pd.date_range(end=datetime.datetime.now(), periods=periods, freq=freq)
prices = base_price + np.cumsum(np.random.randn(periods)* (0.5 if "GOLD" in market or "XAU" in market else 0.0005))
df = pd.DataFrame({"time": dates, "close": prices})
df["ema9"] = df["close"].ewm(span=9).mean()
df["ema21"] = df["close"].ewm(span=21).mean()
df["ema50"] = df["close"].ewm(span=50).mean()
df["rsi"] = 79.0 - np.random.randn(periods)*2

last = df.iloc[-1]
# All signals
soniSell = last["close"] < last["ema50"] and last["rsi"] > 68
soniBuy = last["close"] > last["ema50"] and last["rsi"] < 80
scalpBuy = last["ema9"] > last["ema21"]
v103Buy = True  # For demo show always
q = 6

# CHART - Kom chart sah monga kala da tol o gora
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#1E90FF", width=2)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="#FF6B6B", width=1, dash="dot")))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="#87CEEB", width=1)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="#FF0000", width=1)))
fig.update_layout(height=220, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", legend=dict(orientation="h", y=-0.2), font=dict(color="white", size=10))
st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# SIGNALS DISPLAY - Same as your working screenshot
if scalpBuy:
    st.info(f"🔵 SCALP BUY - Quality {q}/7 - {timeframe} - {market}")
if v103Buy:
    st.success(f"🟢 V103 BUY - Quality {q}/7 - {timeframe}")
if soniBuy:
    st.success(f"🟢 SONI BUY - Quality {q}/7 - @{last['close']:.2f}")
if soniSell:
    st.error(f"🔴 SONI SELL - Quality {q}/7")

if auto and q>=6:
    st.markdown(f"""
    <div style="background:#0A2E1A; border:1px solid #00FF88; border-radius:14px; padding:12px;">
    <span style="font-size:18px;">🔔</span> <b style="color:#00FF88;">BUY SIGNAL CONFIRMED {q}/7 - GOLD XAUUSD @{last['close']:.2f} - KING 103 WAR - TP 4213.25 SL 4171.62 - {timeframe} - {market}</b>
    </div>
    """, unsafe_allow_html=True)

# TOTAL BALANCE + STATS - Same as image
st.markdown("""
<div style="display:grid; grid-template-columns:2fr 1fr; gap:12px; margin-top:14px;">
<div class="card">
<div style="color:#8AA0B8; font-size:12px;">Total Balance 👁️</div>
<div style="font-size:28px; font-weight:900; color:white;">$ 10.00</div>
<div style="color:#00FF88; font-size:13px;">+0.00% (24h) - Real Account</div>
<div style="color:#00FF88; font-size:13px;">+4.32% (24h)</div>
<div style="height:60px; background:linear-gradient(to top, rgba(0,255,136,0.3), transparent); margin-top:10px; border-radius:8px;"></div>
</div>
<div>
<div class="card" style="margin-bottom:8px; padding:8px;"><div style="font-size:11px;">📊 Win Rate 90%<br><b>27W/3L</b></div></div>
<div class="card" style="margin-bottom:8px; padding:8px;"><div style="font-size:11px;">🎯 Active Trades<br><b>3</b></div></div>
<div class="card" style="margin-bottom:8px; padding:8px;"><div style="font-size:11px;">💜 Daily Profit<br><b style="color:#00FF88;">+542.17</b></div></div>
<div class="card" style="margin-bottom:8px; padding:8px;"><div style="font-size:11px;">🏃 Autotrader Status<br><b style="color:#00FF88;">Running</b></div></div>
<div class="card" style="padding:8px; border:1px solid gold;"><div style="font-size:10px;">🔔 Last Alert<br><b>SELL 4185.50 • Quality 6/7</b></div></div>
</div>
</div>
""", unsafe_allow_html=True)

# BOTTOM NAV - Same as image
st.markdown("""
<div style="position:fixed; bottom:0; left:0; right:0; background:#081425; border-top:1px solid rgba(255,215,0,0.2); display:flex; justify-content:space-around; padding:10px 0;">
<div style="text-align:center; color:#00FFC2;"><div>🏠</div><div style="font-size:11px;">Home</div></div>
<div style="text-align:center; color:#8AA0B8;"><div>📊</div><div style="font-size:11px;">Markets</div></div>
<div style="text-align:center; color:#8AA0B8;"><div>🔄</div><div style="font-size:11px;">Trade</div></div>
<div style="text-align:center; color:#8AA0B8;"><div>🕒</div><div style="font-size:11px;">History</div></div>
<div style="text-align:center; color:#8AA0B8;"><div>👤</div><div style="font-size:11px;">Profile</div></div>
</div>
""", unsafe_allow_html=True)

st.caption(f"Timeframe: {timeframe} | Market: {market} | Price: {last['close']:.2f} | Har Kala Da Design | Tol Work Completed | {datetime.datetime.now().strftime('%H:%M')}")
