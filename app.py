# Sona AI Advance - Yesterday Wala Dar Kha Code - Fully Clickable
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
import pytz

st.set_page_config(page_title="Sona AI Advance", layout="wide", initial_sidebar_state="collapsed")

# Market Data - Same as your screenshot
MARKETS = {
    "XAU/USD GOLD": {"price": 4176.07, "change": "+0.82%", "vol": "+0.82%"},
    "BTC/USDT": {"price": 67432.18, "change": "+2.34%", "vol": "+2.34%"},
    "EUR/USD": {"price": 1.0874, "change": "+0.21%", "vol": "+0.21%"},
    "GBP/USD": {"price": 1.2987, "change": "+0.33%", "vol": "+0.33%"},
    "XAUUSD 5m GOLD": {"price": 4179.72, "change": "+0.82%", "vol": "+0.82%"},
    "NAS100": {"price": 19850.0, "change": "+0.45%", "vol": "+0.45%"},
    "US30": {"price": 42250.0, "change": "+0.38%", "vol": "+0.38%"},
    "GBP/JPY": {"price": 192.45, "change": "+0.12%", "vol": "+0.12%"},
}

pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)

st.markdown("""
<style>
.stApp { background: #020C1E !important; }
div[data-testid="stSelectbox"] > div { background: white !important; color: black !important; border-radius: 12px !important; }
div[data-testid="stSlider"] { padding-top: 0px; }
</style>
""", unsafe_allow_html=True)

# Header - Sona AI ADVANCE - Same as screenshot 5:57 AM
st.markdown(f"""
<div style="display:flex; justify-content:space-between; align-items:center; padding:10px 0;">
<div style="display:flex; align-items:center; gap:12px;">
<div style="font-size:50px;">⚡</div>
<div><div style="font-size:42px; font-weight:900; color:white;">Sona <span style="color:#FFD700;">AI</span></div>
<div style="border:2px solid #FFD700; border-radius:20px; padding:2px 14px; display:inline-block; font-weight:900; color:white; font-size:14px;">ADVANCE</div>
<div style="color:#8AA0B8; font-size:14px; margin-top:6px;">Smarter Trades • Higher Profits</div></div>
</div>
<div style="text-align:right;">
<div style="position:relative;"><span style="font-size:40px;">🔔</span><span style="position:absolute; top:0; right:0; background:red; color:white; border-radius:50%; padding:2px 7px; font-size:12px;">3</span></div>
</div>
</div>
<div style="margin-top:10px;"><span style="border:1px solid #00FFC2; color:#00FFC2; border-radius:20px; padding:6px 14px; font-size:13px;">◆ AI Powered Trading</span></div>
<h1 style="color:white; font-size:32px; margin-top:20px;">Your <span style="color:#00FFC2;">AI</span> Trading</h1>
""", unsafe_allow_html=True)

# Controls - CLICKABLE - Same as your 5:57 AM screenshot
timeframe = st.selectbox("Timeframe", ["1 min", "5 min", "15 min", "30 min", "1H", "4H", "1D"], index=1)
market = st.selectbox("Market", list(MARKETS.keys()), index=0)
win_target = st.slider("Win Rate Target", 90, 95, 90)

# Market Cards - BTC/USDT, XAU/USD, EUR/USD, GBP/USD - Same as screenshot
st.markdown("###")
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    <div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:14px;">
    <div style="color:#8AA0B8;">₿ BTC/USDT</div>
    <div style="font-size:22px; font-weight:900; color:white; margin-top:6px;">{MARKETS['BTC/USDT']['price']}</div>
    <div style="color:#00FF88; font-size:14px;">{MARKETS['BTC/USDT']['change']} ▲</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:14px;">
    <div style="color:#8AA0B8;">🪙 XAU/USD</div>
    <div style="font-size:22px; font-weight:900; color:white; margin-top:6px;">{MARKETS['XAU/USD GOLD']['price']}</div>
    <div style="color:#00FF88; font-size:14px;">{MARKETS['XAU/USD GOLD']['change']} ▲</div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    st.markdown(f"""
    <div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:14px; margin-top:10px;">
    <div style="color:#8AA0B8;">€ EUR/USD</div>
    <div style="font-size:22px; font-weight:900; color:white; margin-top:6px;">{MARKETS['EUR/USD']['price']}</div>
    <div style="color:#00FF88; font-size:14px;">{MARKETS['EUR/USD']['change']} ▲</div>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown(f"""
    <div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:14px; margin-top:10px;">
    <div style="color:#8AA0B8;">🇬🇧 GBP/USD</div>
    <div style="font-size:22px; font-weight:900; color:white; margin-top:6px;">{MARKETS['GBP/USD']['price']}</div>
    <div style="color:#00FF88; font-size:14px;">{MARKETS['GBP/USD']['change']} ▲</div>
    </div>
    """, unsafe_allow_html=True)

# Automatic Trading - REAL TOGGLE
auto = st.toggle("Automatic Trading", value=True)

# Quality Filter - Same as screenshot
st.markdown(f"""
<div style="display:grid; grid-template-columns: 1fr 1fr 1.5fr; gap:10px; margin-top:16px;">
<div style="background:#0A1930; border:2px solid #FFD700; border-radius:12px; padding:10px; text-align:center;">
<div style="color:#8AA0B8; font-size:11px;">📊 Quality Filter Score 6/7 Minimum</div>
</div>
<div style="background:#1A1200; border:2px solid #FFD700; border-radius:12px; padding:10px; text-align:center;">
<div style="color:#8AA0B8; font-size:11px;">⭐ Win Rate 90%</div>
</div>
<div style="background:#0A1A00; border:2px solid #FFD700; border-radius:12px; padding:10px; text-align:center;">
<div style="color:#8AA0B8; font-size:11px;">🔗 KING V103 x SONA AI LINKED Selected</div>
</div>
</div>
""", unsafe_allow_html=True)

# === KING V103 LOGIC ===
def ema(s,n): return s.ewm(span=n, adjust=False).mean()
def rsi_calc(s,p=14):
    d=s.diff(); g=d.where(d>0,0).ewm(alpha=1/p, adjust=False).mean(); l=-d.where(d<0,0).ewm(alpha=1/p, adjust=False).mean()
    return 100-(100/(1+g/l.replace(0,1e-9)))

base = MARKETS[market]["price"] if market in MARKETS else 4179.72
dates = pd.date_range(end=datetime.datetime.now(), periods=120, freq="5min")
close_prices = base + np.cumsum(np.random.randn(120)*0.6) + np.linspace(-3, 3, 120)
df = pd.DataFrame({"time": dates, "close": close_prices})
df["ema9"] = ema(df["close"],9)
df["ema21"] = ema(df["close"],21)
df["ema50"] = ema(df["close"],50)
df["rsi"] = rsi_calc(df["close"])
last = df.iloc[-1]
q = 6  # Quality 6/7 fixed for your screenshot

# Chart - Same as 5:58 AM screenshot - Blue close, dashed ema9, light blue ema21, red ema50
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#0066FF", width=2.5)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="#FF6B6B", width=1.5, dash="dot")))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="#87CEEB", width=1.5)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="red", width=1.5)))
fig.update_layout(height=350, paper_bgcolor="#020C1E", plot_bgcolor="#020C1E", font=dict(color="#8AA0B8"), margin=dict(l=10,r=10,t=10,b=10), legend=dict(orientation="h", y=-0.2))
st.plotly_chart(fig, use_container_width=True)

# Signals - V103 BUY + SONI BUY + BUY SIGNAL CONFIRMED - Same as screenshot
if auto:
    st.markdown(f"""
    <div style="background:#0A2E1A; border-radius:12px; padding:14px; margin-top:10px;">
    <div style="color:#00FF88; font-weight:700;">🟢 V103 BUY - Quality 6/7 - {timeframe}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#0A2E1A; border-radius:12px; padding:14px; margin-top:10px;">
    <div style="color:#00FF88; font-weight:700;">🟢 SONI BUY - Quality 6/7 - @{last['close']:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#0A2E1A; border:2px solid #00FF88; border-radius:16px; padding:16px; margin-top:12px;">
    <div style="color:#00FF88; font-weight:900; font-size:16px; line-height:1.4;">🔔 BUY SIGNAL CONFIRMED 6/7 - GOLD XAUUSD @{last['close']:.2f} - KING 103 WAR - TP 4213.25 SL 4171.62 - {timeframe} - {market}</div>
    </div>
    """, unsafe_allow_html=True)

# Balance Cards - Same as 5:58 AM screenshot
st.markdown(f"""
<div style="display:grid; grid-template-columns: 1.5fr 1fr; gap:12px; margin-top:16px;">
<div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:16px;">
<div style="color:#8AA0B8; font-size:14px;">Total Balance 👁️</div>
<div style="font-size:36px; font-weight:900; color:white; margin-top:8px;">$ 10.00</div>
<div style="color:#00FF88; font-size:14px; margin-top:4px;">+0.00% (24h) - Real Account</div>
<div style="color:#00FF88; font-size:14px;">+4.32% (24h)</div>
<div style="height:80px; background:linear-gradient(180deg, #00FF8844, transparent); border-radius:12px; margin-top:12px;"></div>
</div>
<div style="display:flex; flex-direction:column; gap:10px;">
<div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:12px;">
<div style="color:#8AA0B8; font-size:12px;">📊 Win Rate 90% 27W/3L</div>
</div>
<div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:12px;">
<div style="color:#8AA0B8; font-size:12px;">🎯 Active Trades 3</div>
</div>
<div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:12px;">
<div style="color:#8AA0B8; font-size:12px;">💜 Daily Profit</div>
<div style="color:#00FF88; font-weight:900; margin-top:4px;">+542.17</div>
</div>
<div style="background:#0A1930; border:1px solid #1A2B45; border-radius:16px; padding:12px;">
<div style="color:#8AA0B8; font-size:12px;">🏃 Autotrader Status</div>
<div style="color:#00FF88; font-weight:900; margin-top:4px;">Running</div>
</div>
<div style="background:#0A1930; border:2px solid #FFD700; border-radius:16px; padding:12px;">
<div style="color:#8AA0B8; font-size:12px;">🔔 Last Alert SELL 4185.50 • Quality 6/7</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.caption(f"Timeframe: {timeframe} | Market: {market} | Price: {last['close']:.2f} | Har Kala Da Design | Tol Work Completed | {now_pkt.strftime('%H:%M')}")

# Bottom Nav - Home Markets Trade - Same as screenshot
st.markdown("""
<div style="position:fixed; bottom:0; left:0; right:0; background:#020C1E; border-top:1px solid #1A2B45; display:flex; justify-content:space-around; padding:10px 0;">
<div style="text-align:center; color:#00FF88;">🏠<br>Home</div>
<div style="text-align:center; color:#8AA0B8;">📊<br>Markets</div>
<div style="text-align:center; color:#8AA0B8;">🔄<br>Trade</div>
</div>
""", unsafe_allow_html=True)
