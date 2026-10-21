# Sona AI Advance v10.3 - 5 Day Complete Works 100 - Premium Design
import streamlit as st
import pandas as pd
import numpy as np
import datetime, pytz, plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

st.set_page_config(page_title="Sona AI Advance v10.3", layout="wide", initial_sidebar_state="collapsed")

# Peshawar Time
pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)
now_str = now_pkt.strftime("%I:%M %p PKT")

MARKETS = {
    "XAU/USD • GOLD": 4179.72,
    "BTC/USDT": 67432.18,
    "XAU/USD": 4176.07,
    "EUR/USD": 1.0874,
    "GBP/USD": 1.2987,
}

st.markdown("""
<style>
.stApp { background: #020A14 !important; }
div[data-testid="stHeader"] { display: none; }
.gold-card { background: linear-gradient(135deg, #0D1B2E 0%, #0A1424 100%); border: 1px solid #C9A86A; border-radius: 16px; padding: 14px; box-shadow: 0 0 20px rgba(201,168,106,0.15); }
.time-btn { background: #1A2B45; border: 1px solid #2A3B55; border-radius: 8px; padding: 6px 14px; color: white; font-weight: 600; font-size: 13px; }
.time-btn-active { background: #E5C07B !important; color: black !important; border: 1px solid #E5C07B; }
.stSelectbox > div > div { background: #1A2B45 !important; color: white !important; border-radius: 8px !important; }
</style>
""", unsafe_allow_html=True)

# HEADER - SONA AI ADVANCE + Bala Hisar Fort + LIVE AI MODE
st.markdown(f"""
<div style="background: linear-gradient(90deg, #0A1A2E 0%, #0D2137 100%); border-bottom: 1px solid #C9A86A; border-radius: 0 0 16px 16px; padding: 16px 20px; display:flex; justify-content:space-between; align-items:center;">
<div style="display:flex; align-items:center; gap:16px;">
<div style="width:56px; height:56px; background: linear-gradient(135deg, #C9A86A, #8A6D3B); border-radius: 12px; display:flex; align-items:center; justify-content:center; font-size:28px;">⬡</div>
<div><div style="font-size:32px; font-weight:900; color:#E5C07B; line-height:1.1;">SONA AI<br>ADVANCE</div></div>
</div>
<div style="text-align:right;">
<div style="color:#00FF88; font-weight:900; font-size:14px; letter-spacing:1px;">||| LIVE AI MODE <span style="background:#00FF88; color:black; padding:2px 10px; border-radius:6px; margin-left:6px;">ACTIVE</span></div>
<div style="color:white; font-size:13px; margin-top:4px;">PESHAWAR • {now_pkt.strftime('%I:%M %p PKT').upper()}</div>
<div style="color:#8AA0B8; font-size:10px; margin-top:6px; border-top:1px solid #C9A86A; padding-top:4px;">SONA AI v10.3 • RISK LOW • LEVERAGE 1:100 • BALANCE SECURED</div>
</div>
</div>
""", unsafe_allow_html=True)

# LAYOUT 3 COLUMNS - As per your design image
left, center, right = st.columns([1, 1.6, 1])

# LEFT - ACCOUNT GROWTH
with left:
    st.markdown(f"""
    <div class="gold-card">
    <div style="color:#C9A86A; font-weight:800; font-size:13px; margin-bottom:12px;">📈 ACCOUNT GROWTH</div>
    <div style="background:#071425; border:1px solid #C9A86A; border-radius:12px; padding:14px;">
    <div style="color:#8AA0B8; font-size:11px;">REAL ACCOUNT</div>
    <div style="font-size:42px; font-weight:900; color:#E5C07B;">$10.00</div>
    <div style="color:#00FF88; font-size:14px;">+0.00% (24h)</div>
    <div style="color:white; font-size:12px; margin-top:10px;">Real Account <span style="color:#00FF88; font-weight:800;">+4.32% <span style="font-size:16px;">↗</span></span></div>
    </div>
    <div style="background:#071425; border:1px solid #C9A86A; border-radius:12px; padding:12px; margin-top:12px;">
    <div style="display:flex; gap:10px; align-items:center;"><div style="font-size:20px;">💳</div><div><div style="color:#8AA0B8; font-size:11px;">Starting Balance</div><div style="color:white; font-weight:700;">$10</div></div></div>
    <div style="display:flex; gap:10px; align-items:center; margin-top:12px;"><div style="font-size:20px;">📅</div><div><div style="color:#8AA0B8; font-size:11px;">Initial</div><div style="color:white; font-weight:700;">5 days ago</div></div></div>
    <div style="margin-top:16px;"><div style="display:flex; justify-content:space-between; color:#8AA0B8; font-size:12px;"><span>Goal</span><span><b style="color:white;">$1000</b> Target</span></div>
    <div style="height:8px; background:#1A2B45; border-radius:10px; margin-top:6px;"><div style="width:60%; height:100%; background:linear-gradient(90deg,#C9A86A,#E5C07B); border-radius:10px;"></div></div>
    <div style="height:6px; background:#1A2B45; border-radius:10px; margin-top:6px;"><div style="width:15%; height:100%; background:#4A5A75; border-radius:10px;"></div></div>
    <div style="color:#8AA0B8; font-size:11px; margin-top:6px;">1.0% • $10 / $1000</div></div>
    <div style="color:#8AA0B8; font-size:11px; margin-top:14px;">Days Active: 5 • Daily Target: +$198.00</div>
    <div style="background:#071425; border:1px solid #C9A86A; border-radius:10px; padding:8px; margin-top:12px; display:flex; justify-content:space-between; align-items:center;">
    <div style="color:#8AA0B8; font-size:11px;">🔗 KING V103 x SONA LINKED •</div><div style="color:#00FF88; font-size:11px;">● Selected</div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# CENTER - GOLD XAUUSD - Chart
with center:
    timeframe = st.radio("Timeframe", ["1min", "5min", "15min", "30min", "1H", "4H", "1D"], index=1, horizontal=True)
    market = st.selectbox("Market:", list(MARKETS.keys()), index=0)
    
    # Market mini cards - Clickable
    mc1, mc2, mc3, mc4 = st.columns(4)
    with mc1: st.markdown(f"""<div style="background:#0A1930; border-radius:8px; padding:6px; text-align:center;"><div style="color:#8AA0B8; font-size:10px;">BTC/USDT</div><div style="color:#00FF88; font-size:11px; font-weight:700;">67432.18 +2.34%</div></div>""", unsafe_allow_html=True)
    with mc2: st.markdown(f"""<div style="background:#0A1930; border-radius:8px; padding:6px; text-align:center;"><div style="color:#8AA0B8; font-size:10px;">XAU/USD</div><div style="color:#00FF88; font-size:11px; font-weight:700;">4176.07 +0.82%</div></div>""", unsafe_allow_html=True)
    with mc3: st.markdown(f"""<div style="background:#0A1930; border-radius:8px; padding:6px; text-align:center;"><div style="color:#8AA0B8; font-size:10px;">EUR/USD</div><div style="color:#00FF88; font-size:11px; font-weight:700;">1.0874 +0.21%</div></div>""", unsafe_allow_html=True)
    with mc4: st.markdown(f"""<div style="background:#0A1930; border-radius:8px; padding:6px; text-align:center;"><div style="color:#8AA0B8; font-size:10px;">GBP/USD</div><div style="color:#00FF88; font-size:11px; font-weight:700;">1.2987 +0.33%</div></div>""", unsafe_allow_html=True)

    col_a, col_b = st.columns([1,1])
    with col_a: auto = st.toggle("Automatic Trading", value=True)
    with col_b: st.markdown("""<div style="display:flex; gap:6px; align-items:center; margin-top:8px;"><div style="color:#8AA0B8; font-size:11px;">Quality Filter Score Minimum</div><div style="background:#E5C07B; color:black; padding:2px 8px; border-radius:6px; font-weight:900; font-size:12px;">6/7</div><div style="color:#8AA0B8; font-size:11px;">Win Rate 90%</div></div>""", unsafe_allow_html=True)

    # Chart Data - King V103 - EMA9/21/50
    def ema(s,n): return s.ewm(span=n, adjust=False).mean()
    base = MARKETS[market]
    dates = pd.date_range(end=datetime.datetime.now(), periods=80, freq="15min")
    close = base + np.cumsum(np.random.randn(80)*0.8) + np.linspace(-8, 6, 80)
    df = pd.DataFrame({"time": dates, "close": close, "open": close-0.3, "high": close+0.8, "low": close-0.8})
    df["ema9"] = ema(df["close"],9)
    df["ema21"] = ema(df["close"],21)
    df["ema50"] = ema(df["close"],50)
    
    # Candlestick + EMAs - Same as image - Gold candles
    fig = go.Figure()
    fig.add_trace(go.Candlestick(x=df["time"], open=df["open"], high=df["high"], low=df["low"], close=df["close"], increasing_line_color="#E5C07B", decreasing_line_color="#FF4D4D", name="GOLD"))
    fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="EMA9", line=dict(color="#E5C07B", width=1.5)))
    fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="EMA21", line=dict(color="#4FC3F7", width=1.5)))
    fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="EMA50", line=dict(color="#AB47BC", width=1.5)))
    fig.update_layout(height=380, paper_bgcolor="#071425", plot_bgcolor="#071425", font=dict(color="#8AA0B8", size=10), margin=dict(l=10,r=60,t=10,b=10), xaxis_rangeslider_visible=False, legend=dict(orientation="v", x=0.8, y=0.5))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    st.markdown(f"""
    <div style="background:linear-gradient(90deg, #C9A86A, #E5C07B); border-radius:10px; padding:10px; margin-top:-10px; text-align:left; color:black; font-weight:800; font-size:12px; position:relative;">
    BUY SIGNAL CONFIRMED 6/7 • GOLD XAUUSD @{df.iloc[-1]['close']:.2f} • KING 103 WAR<br>TP 4213.25 • SL 4171.62 • 5 min
    <span style="position:absolute; right:10px; top:10px; background:black; color:#C9A86A; border-radius:50%; width:22px; height:22px; display:flex; align-items:center; justify-content:center;">✓</span>
    </div>
    """, unsafe_allow_html=True)

# RIGHT - PERFORMANCE STATS + HOLOGRAPHIC HOLDINGS + LOCATION
with right:
    st.markdown("""
    <div class="gold-card">
    <div style="color:#C9A86A; font-weight:800; font-size:13px;">◈ PERFORMANCE STATS</div>
    <div style="margin-top:12px;"><div style="color:#8AA0B8; font-size:12px;">Win Rate</div><div style="font-size:28px; font-weight:900; color:#E5C07B;">90%</div><div style="color:#8AA0B8; font-size:11px;">27W / 3L</div></div>
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:12px;">
    <div><div style="color:#8AA0B8; font-size:11px;">Active Trades</div><div style="color:white; font-weight:700;">3</div></div>
    <div><div style="color:#8AA0B8; font-size:11px;">Daily Profit</div><div style="color:#00FF88; font-weight:700;">+$542.17 <span>↗</span></div></div>
    </div>
    <div style="margin-top:10px;"><div style="color:#8AA0B8; font-size:11px;">Autotrader Status:</div><div style="color:#00FF88; font-size:13px;">● Running</div></div>
    <div style="margin-top:10px;"><div style="color:#8AA0B8; font-size:11px;">Last Alert</div><div style="color:#FF4D4D; font-size:12px; font-weight:700;">SELL • 4185.50 • Quality 6/7</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="gold-card" style="margin-top:12px;">
    <div style="color:#C9A86A; font-weight:800; font-size:13px;">☰ HOLOGRAPHIC HOLDINGS</div>
    <div style="text-align:center; margin-top:10px;">
    <div style="font-size:50px;">🪙🪙🪙</div>
    <div style="color:white; font-weight:700; font-size:14px; margin-top:6px;">Gold Bar 1oz</div>
    <div style="color:#8AA0B8; font-size:11px;">x2 • 4179.72 oz • Secured</div>
    <div style="color:#C9A86A; font-size:11px; margin-top:4px;">Total Holdings Value: $8,359.44</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="gold-card" style="margin-top:12px;">
    <div style="display:flex; justify-content:space-between;"><div style="color:#C9A86A; font-weight:800; font-size:12px;">LOCATION • PESHAWAR</div><div style="color:#8AA0B8;">⌄</div></div>
    <div style="background:#071425; border-radius:10px; height:120px; margin-top:8px; position:relative; overflow:hidden; background-image: linear-gradient(rgba(201,168,106,0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(201,168,106,0.2) 1px, transparent 1px); background-size: 20px 20px;">
    <div style="position:absolute; top:20%; right:20%; color:#8AA0B8; font-size:10px;">Bala Hisar Fort</div>
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);"><div style="width:24px; height:24px; background:#E5C07B; border-radius:50% 50% 50% 0; transform:rotate(-45deg); display:flex; align-items:center; justify-content:center;"><span style="transform:rotate(45deg);">📍</span></div></div>
    <div style="position:absolute; bottom:20%; left:30%; width:6px; height:6px; background:#00FF88; border-radius:50%;"></div>
    </div>
    <div style="color:#8AA0B8; font-size:10px; margin-top:8px;">Session: Overnight • UTC+5 PKT</div>
    </div>
    """, unsafe_allow_html=True)

st.caption(f"SONA AI v10.3 • {timeframe} • {market} • Quality 6/7 • Win Rate 90% • KING V103 x SONA LINKED • 5 Day Complete Works 100 • Peshawar {now_str}")
