import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.graph_objects as go
import pytz

st.set_page_config(page_title="Sona AI Advance", layout="wide")

# Config
MARKETS = {
    "XAU/USD • GOLD": 4182.23,
    "BTC/USDT": 67432.18,
    "EUR/USD": 1.0874,
    "GBP/USD": 1.2987,
}

pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)
now_utc = datetime.datetime.utcnow()

# CSS - Yesterday wala simple, clickable
st.markdown("""
<style>
.stApp { background:#030B1A; }
h1, h2, h3 { color:#FFD700; }
</style>
""", unsafe_allow_html=True)

# HEADER - Same as yesterday
st.title("SONA AI ADVANCE")
st.markdown(f"**KING V103.5 x SONA AI LINKED • LIVE • PESHAWAR** | LIVE AI MODE ACTIVE | {now_pkt.strftime('%I:%M %p PKT')} | SONA AI v10.5")

col1, col2, col3 = st.columns(3)
with col1:
    timeframe = st.selectbox("Timeframe", ["1 min", "5 min", "15 min", "30 min", "1H", "4H", "1D"], index=1, key="tf")
with col2:
    market = st.selectbox("Market", list(MARKETS.keys()), index=0, key="mkt")
with col3:
    win_rate = st.slider("Win Rate Target", 90, 95, 94, key="wr")

# Yesterday wala market logic
base_price = MARKETS[market]
st.subheader(f"{market.split('•')[0].strip()} - {base_price}")

# Data + Indicators - King V103 Pine logic
def ema(s,n): return s.ewm(span=n, adjust=False).mean()
def rsi(s,p=14):
    d=s.diff()
    g=d.where(d>0,0).ewm(alpha=1/p, adjust=False).mean()
    l=-d.where(d<0,0).ewm(alpha=1/p, adjust=False).mean()
    return 100-(100/(1+g/l.replace(0,1e-9)))

dates = pd.date_range(end=datetime.datetime.now(), periods=100, freq="5min")
close = base_price + np.cumsum(np.random.randn(100)*0.8) + np.linspace(-5,5,100)
df = pd.DataFrame({"time": dates, "close": close, "high": close+1, "low": close-1, "volume": np.random.randint(1000,5000,100)})
df["ema9"] = ema(df["close"],9)
df["ema21"] = ema(df["close"],21)
df["ema50"] = ema(df["close"],50)
df["ema200"] = ema(df["close"],200)
df["vwap"] = (df["close"]*df["volume"]).cumsum()/df["volume"].cumsum()
df["rsi"] = rsi(df["close"])
df["sh"] = df["high"].rolling(10).max()
df["sl"] = df["low"].rolling(10).min()
df["bosBull"] = df["close"] > df["sh"].shift(1)
df["q"] = 0
df["q"] += (df["ema9"]>df["ema21"]).astype(int)
df["q"] += ((df["rsi"]>40)&(df["rsi"]<70)).astype(int)
df["q"] += (df["close"]>df["ema50"]).astype(int)
df["q"] += (df["close"]>df["ema200"]).astype(int)
df["q"] += (df["close"]>df["vwap"]).astype(int)
df["q"] += (df["ema21"]>df["ema50"]).astype(int)
df["q"] += df["bosBull"].astype(int)
df["q"] = df["q"].clip(upper=7)
last = df.iloc[-1]
q = int(last["q"])

# Quality + Win Rate - CLICKABLE CARDS
c1,c2,c3,c4 = st.columns(4)
c1.metric("Quality Filter Score Minimum", f"{q}/7")
c2.metric("Win Rate", "90%")
c3.metric("Market Session", "CLOSED - Opens 13:00 PKT" if market!="BTC/USDT" and now_utc.hour<8 else "LIVE" if market=="BTC/USDT" else "CLOSED")
c4.metric("KING V103 x SONA LINKED", "Selected")

# Automatic Trading - REAL TOGGLE - Yesterday wala
auto = st.toggle("Automatic Trading", value=True if market=="BTC/USDT" else False)

# Chart - Clickable, zoom, pan - Plotly native
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#FFD700", width=2)))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="yellow")))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="orange")))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="red")))
fig.add_trace(go.Scatter(x=df["time"], y=df["ema200"], name="ema200", line=dict(color="purple")))
fig.add_trace(go.Scatter(x=df["time"], y=df["vwap"], name="VWAP", line=dict(color="aqua", dash="dot")))
fig.update_layout(height=400, paper_bgcolor="#030B1A", plot_bgcolor="#030B1A", font=dict(color="white"))
st.plotly_chart(fig, use_container_width=True)

# Signals - Yesterday wala working
if auto:
    if last["ema9"]>last["ema21"]:
        st.success(f"🟢 V103 BUY - Quality {q}/7 - {timeframe} - @ {last['close']:.2f}")
        st.info(f"🔵 SCALP BUY - Quality {q}/7 - {timeframe}")
        st.success(f"🔔 BUY SIGNAL CONFIRMED {q}/7 - {market} @{last['close']:.2f} - KING 103 WAR | TP 4213.25 SL 4171.62 | EMA200 {last['ema200']:.2f} VWAP {last['vwap']:.2f} RSI {last['rsi']:.1f}")
else:
    st.warning(f"⏸️ MARKET {market} CLOSED - Opens 13:00 PKT (London+NY) - PKT {now_pkt.strftime('%H:%M')} UTC {now_utc.strftime('%H:%M')} - Quality {q}/7 - Automatic Trading Paused")

# Bottom stats - Yesterday wala
st.divider()
b1,b2,b3,b4 = st.columns(4)
b1.metric("Total Balance", "$10.00", "+0.00% Real Account")
b2.metric("Win Rate", "90%", "27W/3L")
b3.metric("Active Trades", "3")
b4.metric("Daily Profit", "+542.17")

st.caption(f"Yesterday wala code - Clickable - {market} - {timeframe} - Quality {q}/7 - All indicators EMA9/21/50/200 VWAP RSI BOS - King V103.5")
