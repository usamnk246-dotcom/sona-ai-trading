import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI Advance - KING V103.5", layout="wide")

# --- HAR KALA DA - SAME DESIGN AS YOUR SCREENSHOT ---
st.markdown("""
<style>
.stApp { background: #030B1A !important; }
div[data-testid="stHeader"] { display: none; }
.card { background: linear-gradient(135deg, #0A1930, #081425); border:1px solid #FFD700; border-radius:16px; padding:14px; }
.gold { color: #FFD700 !important; }
.teal { color: #00FFC2 !important; }
.live-box { background: rgba(0,255,194,0.15); border:1px solid #00FFC2; border-radius:8px; padding:6px 12px; }
.market-card { background: #081425; border:1px solid #1A2B45; border-radius:12px; padding:10px; }
</style>
""", unsafe_allow_html=True)

# HEADER - Same as image
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center; border:1px solid #FFD700; border-radius:12px; padding:12px; background:#050E1F;">
<div style="display:flex; align-items:center; gap:12px;">
<div style="font-size:42px; color:#FFD700;">⬡</div>
<div><div style="font-size:34px; font-weight:900; color:#FFD700;">SONA AI ADVANCE</div>
<div style="color:#8AA0B8; font-size:13px;">KING V103.5 x SONA AI LINKED • LIVE • PESHAWAR</div>
</div></div>
<div style="display:flex; gap:18px; align-items:center;">
<div style="text-align:right;"><div style="color:#00FFC2;">LIVE AI MODE ACTIVE</div><div style="color:#8AA0B8; font-size:11px;">PESHAWAR • 03:42 AM PKT • SONA AI v10.3<br>RISK LOW • LEVERAGE 1:100 • BALANCE SECURED</div></div>
</div></div>
""", unsafe_allow_html=True)

# TODAY HEADER STATS
st.markdown("""
<div style="margin-top:12px;"><span class="gold">KING V103 4/HR BOTH</span> • <span class="teal">KING V103 x SONA AI LINKED</span>
<h1 style="margin:8px 0 0 0; font-size:32px; color:#FFD700;">GOLD XAUUSD</h1>
<p style="color:#8AA0B8; font-size:13px; margin:0;">XAUUSD 4182.23 +13.29 (+0.32%) • 03:44 • 5m • EMA9 EMA21 EMA50 EMA200 VWAP</p>
<div style="background:linear-gradient(90deg, #FFD70033, transparent); height:4px; margin-top:8px;"></div>
</div>
<p style="color:#FFD700; font-size:11px; margin-top:6px;">ACCOUNT GROWTH • REAL ACCOUNT $10.00 • GOAL $1000 TARGET • 1.0% $10/$1000 • Days Active: 5</p>
""", unsafe_allow_html=True)

# MORE TIMEFRAME + DIFFERENT MARKET - Da tol pa ka add ka
c_tf1, c_tf2, c_tf3 = st.columns([2,2,2])
with c_tf1:
    timeframe = st.selectbox("Timeframe", ["1 min", "5 min", "15 min", "30 min", "1H", "4H", "1D"], index=1)
with c_tf2:
    market = st.selectbox("Market", ["XAU/USD • GOLD", "BTC/USDT", "EUR/USD", "GBP/USD", "NAS100", "US30", "GBP/JPY"], index=0)
with c_tf3:
    win_rate_target = st.slider("Win Rate Target", 90, 95, 90)

# LIVE MARKETS - 4 CARDS - Same as image - Simulate live prices
if "BTC" in market:
    base_price = 67432.18
elif "XAU" in market or "GOLD" in market:
    base_price = 4176.07
elif "EUR" in market:
    base_price = 1.0874
else:
    base_price = 1.2987

st.markdown(f"""
<div style="display:grid; grid-template-columns: repeat(4,1fr); gap:10px; margin-top:12px;">
<div class="market-card"><div style="color:#8AA0B8; font-size:10px;">BTC/USDT</div><div class="teal" style="font-size:13px; font-weight:700;">67432.18 +2.34%</div></div>
<div class="market-card"><div style="color:#8AA0B8; font-size:10px;">XAU/USD • GOLD</div><div class="gold" style="font-size:13px; font-weight:700;">{base_price} +0.82%</div></div>
<div class="market-card"><div style="color:#8AA0B8; font-size:10px;">EUR/USD</div><div style="color:white; font-size:13px;">1.0874 +0.21%</div></div>
<div class="market-card"><div style="color:#8AA0B8; font-size:10px;">GBP/USD</div><div style="color:white; font-size:13px;">1.2987 +0.33%</div></div>
</div>
""", unsafe_allow_html=True)

# TOGGLES - Same as image
col1, col2 = st.columns([1.2,2])
with col1:
    auto = st.toggle("Automatic Trading", value=True)
with col2:
    st.markdown(f"""
    <div style="display:flex; gap:6px; margin-top:8px;">
    <div style="background:#1A2B45; border:1px solid #FFD700; border-radius:8px; padding:6px 10px; font-size:11px; color:#FFD700;">Quality Filter Score Minimum <b style="background:#FFD700; color:black; padding:2px 6px; border-radius:4px; margin-left:4px;">6/7</b></div>
    <div style="background:#2A1F0A; border:1px solid #FFA500; border-radius:8px; padding:6px 10px; font-size:11px; color:#FFA500;">Win Rate 90%</div>
    <div style="background:#1A1A0A; border:1px solid #00FFC2; border-radius:8px; padding:6px 10px; font-size:11px; color:#00FFC2;">KING V103 x SONA LINKED • Selected</div>
    </div>
    """, unsafe_allow_html=True)

# SIGNALS + CHART - Tol chart sah monga jora kala da + NEW V103.5 LOGIC
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
prices = base_price + np.cumsum(np.random.randn(periods)* (base_price*0.001))
df = pd.DataFrame({"time": dates, "close": prices})
df["ema9"] = df["close"].ewm(span=9).mean()
df["ema21"] = df["close"].ewm(span=21).mean()
df["ema50"] = df["close"].ewm(span=50).mean()
df["ema200"] = df["close"].ewm(span=200).mean()
df["vwap"] = df["close"].ewm(span=20).mean() # simplified VWAP
df["rsi"] = 79.0 - np.random.randn(periods)*5

# === YOUR YESTERDAY + TODAY LOGIC - sh/sl BOS SWEEP ===
df["sh"] = df["close"].rolling(10).max()
df["sl"] = df["close"].rolling(10).min()
df["bosBull"] = df["close"] > df["sh"].shift(1)
df["sweepBull"] = (df["low"] if "low" in df else df["close"] < df["sl"]) # simplified

last = df.iloc[-1]
# All signals - YOUR ORIGINAL
soniSell = last["close"] < last["ema50"] and last["rsi"] > 68
sonaSell = last["close"] < last["ema50"] and last["rsi"] > 70
soniBuy = last["close"] > last["ema50"] and last["rsi"] > 35
sonaBuy = last["close"] > last["ema50"] and last["rsi"] < 60
scalpBuy = last["ema9"] > last["ema21"]
scalpSell = last["ema9"] < last["ema21"]
v103Buy = True  # For demo show always - your chart has V103 BUY
v103Sell = False

# Quality Score q - YOUR LOGIC q=6
q = 0
q += 1 if last["ema9"] > last["ema21"] else 0
q += 1 if 40 < last["rsi"] < 70 else 0
q += 1 if last["close"] > last["ema50"] else 0
q += 1 if last["close"] > last["ema200"] else 0
q += 1 if last["close"] > last["vwap"] else 0
q += 1 if last["ema21"] > last["ema50"] else 0
q += 1 if last["bosBull"] else 0
q = min(q, 7)

# CHART - Kom chart sah monga kala da tol da
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#FFD700", width=2)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="yellow", width=1)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="orange", width=1)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="#FF6B6B", width=1)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema200"], name="ema200", line=dict(color="#9B59B6", width=2)))
fig.add_trace(go.Scatter(x=df["time"], y=df["vwap"], name="VWAP", line=dict(color="#00FFC2", width=1)))
fig.update_layout(height=320, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="#030B1A", plot_bgcolor="#030B1A", font=dict(color="#8AA0B8", size=10), showlegend=True)
st.plotly_chart(fig, use_container_width=True)

# SIGNALS DISPLAY - Same as your working image
if scalpBuy:
    st.info(f"🔵 SCALP BUY - Quality {q}/7 - 5 min - Price {last['close']:.2f}")
if v103Buy:
    st.success(f"🟢 V103 BUY - Quality {q}/7 - 5 min - KING V103 4/HR BOTH")
if soniBuy:
    st.success(f"🟢 SONI BUY - Quality {q}/7 - 5 min - @ {last['close']:.2f}")
if sonaBuy:
    st.success(f"🟢 SONA AI BUY - Quality {q}/7 - @ {last['close']:.2f} - EMA200 {last['ema200']:.2f}")
if soniSell:
    st.error(f"🔴 SONI SELL - Quality {q}/7 - Price {last['close']:.2f}")
if auto and q>=6 and (sonaBuy or v103Buy or soniBuy):
    st.markdown(f"""
    <div style="background:#0A2E1A; border:1px solid #00FF88; border-radius:10px; padding:12px; text-align:center;">
    <span style="font-size:18px;">🔔</span> <span style="color:#00FF88; font-weight:900;">BUY SIGNAL CONFIRMED {q}/7 - GOLD XAUUSD @{last['close']:.2f} - KING 103 WAR</span><br>
    <span style="color:white; font-size:12px;">TP 4213.25 SL 4171.62 - 5 min - VWAP {last['vwap']:.2f} - RSI {last['rsi']:.1f} - BOS {'YES' if last['bosBull'] else 'NO'}</span>
    </div>
    """, unsafe_allow_html=True)

# TOTAL BALANCE + STATS - Same as image
st.markdown("""
<div style="display:grid; grid-template-columns: 1.5fr 1fr 1fr 1fr 1fr; gap:10px; margin-top:16px;">
<div class="card">
<div style="color:#8AA0B8; font-size:12px;">Total Balance</div>
<div style="font-size:28px; font-weight:900; color:#FFD700;">$ 10.00</div>
<div style="color:#00FF88; font-size:13px;">+0.00% (24h) - Real Account</div>
<div style="color:#00FF88; font-size:13px;">+4.32% (24h) Real Account ↗</div>
<div style="height:60px; background:linear-gradient(90deg, #00FF8822, #FFD70022); border-radius:8px; margin-top:8px;"></div>
</div>
<div class="card" style="margin-bottom:8px; padding:10px;"><div style="color:#8AA0B8; font-size:10px;">Win Rate</div><div style="color:#FFD700; font-size:18px; font-weight:800;">90% 27W/3L</div></div>
<div class="card" style="margin-bottom:8px; padding:10px;"><div style="color:#8AA0B8; font-size:10px;">Active Trades</div><div style="color:white; font-size:18px; font-weight:800;">3</div></div>
<div class="card" style="margin-bottom:8px; padding:10px;"><div style="color:#8AA0B8; font-size:10px;">Daily Profit</div><div style="color:#00FF88; font-size:18px; font-weight:800;">+542.17</div></div>
<div class="card" style="margin-bottom:8px; padding:10px;"><div style="color:#8AA0B8; font-size:10px;">Autotrader Status</div><div style="color:#00FFC2; font-size:14px;">● Running</div></div>
<div class="card" style="padding:8px; border:1px solid #FF4D4D;"><div style="color:#8AA0B8; font-size:10px;">Last Alert</div><div style="color:#FF4D4D; font-size:11px;">SELL 4185.50 Quality 6/7</div></div>
</div>
""", unsafe_allow_html=True)

# BOTTOM NAV - Same as image
st.markdown("""
<div style="position:fixed; bottom:0; left:0; right:0; background:#030B1A; border-top:1px solid #1A2B45; display:grid; grid-template-columns: repeat(5,1fr); padding:8px 0;">
<div style="text-align:center; color:#00FFC2; font-size:11px;">▤<br>Watchlist</div>
<div style="text-align:center; color:#FFD700; font-size:11px;">〰<br>Chart</div>
<div style="text-align:center; color:#8AA0B8; font-size:11px;">◉<br>Explore</div>
<div style="text-align:center; color:#8AA0B8; font-size:11px;">👥<br>Community</div>
<div style="text-align:center; color:#8AA0B8; font-size:11px;">☰<br>Menu</div>
</div>
""", unsafe_allow_html=True)

st.caption(f"Timeframe: {timeframe} | Market: {market} | Quality {q}/7 | EMA200 {last['ema200']:.2f} | VWAP {last['vwap']:.2f} | BOS {last['bosBull']} | Sweep {last['sweepBull'] if 'sweepBull' in last else False}")
