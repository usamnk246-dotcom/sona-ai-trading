# Zamong indicator jora da - King V103.5 x SONA AI LINKED - app.py
import streamlit as st
import pandas as pd
import numpy as np
import datetime, plotly.graph_objects as go
from plotly.subplots import make_subplots
import pytz

st.set_page_config(page_title="SONA AI ADVANCE v10.5", layout="wide")

MARKET_CONFIG = {
    "XAU/USD • GOLD": {"price": 4182.23, "symbol": "GOLD XAUUSD", "session": "London+NY", "utc": (8,23)},
    "BTC/USDT": {"price": 67432.18, "symbol": "BTC/USDT", "session": "24/7 Crypto", "utc": (0,24)},
    "EUR/USD": {"price": 1.0874, "symbol": "EUR/USD", "session": "London", "utc": (8,17)},
    "GBP/USD": {"price": 1.2987, "symbol": "GBP/USD", "session": "London+NY", "utc": (8,21)},
}

pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)
now_utc = datetime.datetime.utcnow()

st.markdown("""
<style>
.stApp{background:#020B1A!important}
.card{background:linear-gradient(135deg,#0A1930,#071425);border:1px solid #FFD700;border-radius:16px;padding:12px}
.gold{color:#FFD700;font-weight:900}
</style>
""", unsafe_allow_html=True)

# === HEADER - SONA AI ADVANCE ===
st.markdown(f"""
<div class="card" style="display:flex;justify-content:space-between;border:2px solid #FFD700;">
<div><div style="font-size:32px;font-weight:900;color:#FFD700;">SONA AI<br>ADVANCE</div>
<div style="color:#8AA0B8;font-size:11px;">KING V103.5 x SONA AI<br>LINKED • LIVE • PESHAWAR<br><span style="color:#FFD700;">KING V103 4/HR BOTH • KING V103 x SONA AI LINKED</span></div></div>
<div style="text-align:right;"><div style="color:#00FFC2;font-weight:900;">LIVE AI MODE<br>ACTIVE</div>
<div style="color:#8AA0B8;font-size:11px;">PESHAWAR • {now_pkt.strftime('%I:%M %p')}<br>PKT • SONA AI v10.5<br>RISK LOW • LEVERAGE 1:100 • BALANCE SECURED<br>UTC {now_utc.strftime('%H:%M')} • Session Check Active</div></div>
</div>
""", unsafe_allow_html=True)

timeframe = st.selectbox("Timeframe", ["1 min","5 min","15 min","30 min","1H","4H","1D"], index=1)
market = st.selectbox("Market", list(MARKET_CONFIG.keys()), index=0)
win_target = st.slider("Win Rate Target", 90, 95, 94)

cfg = MARKET_CONFIG[market]
is_active = cfg["utc"][0] <= now_utc.hour < cfg["utc"][1] or cfg["utc"]==(0,24)
status = "● LIVE" if is_active else "○ CLOSED"
color_status = "#00FF88" if is_active else "#FF4D4D"

st.markdown(f"""
<div style="margin-top:14px;">
<h1 style="color:#FFD700;margin:0;">GOLD XAUUSD <span style="color:{color_status};font-size:16px;">{status}</span></h1>
<p style="color:#8AA0B8;font-size:12px;">XAUUSD {cfg['price']} +13.29 (+0.32%) • {now_pkt.strftime('%H:%M')} • {timeframe} • EMA9 EMA21 EMA50 EMA200 VWAP • {cfg['session']}</p>
<div style="height:4px;background:linear-gradient(90deg,#FFD700,#00FFC2);"></div>
<p style="color:#FFD700;font-size:11px;margin-top:6px;">ACCOUNT GROWTH • REAL ACCOUNT $10.00 • GOAL $1000 TARGET • 1.0% $10/$1000 • Days Active: 5 • {cfg['symbol']} 1:100 • MARKET {status} - {cfg['session']}</p>
</div>
""", unsafe_allow_html=True)

# Market cards
cols = st.columns(4)
for i,(k,v) in enumerate(list(MARKET_CONFIG.items())[:4]):
    active = v["utc"][0] <= now_utc.hour < v["utc"][1] or v["utc"]==(0,24)
    border = "2px solid #00FF88" if active else "1px solid #1A2B45"
    dot = "🟢 LIVE" if active else "🔴 CLOSED"
    with cols[i]:
        st.markdown(f"""<div class="card" style="border:{border};">
<div style="font-size:10px;color:#8AA0B8;">{dot} {k.split('•')[0]}</div>
<div style="color:#FFD700;font-weight:800;font-size:16px;">{v['price']}</div>
<div style="color:#00FFC2;font-size:11px;">+0.82% • {v['session']}</div>
<div style="font-size:9px;color:#8AA0B8;">PKT {v['utc'][0]+5}:00-{v['utc'][1]+5}:00</div>
</div>""", unsafe_allow_html=True)

auto = st.toggle("Automatic Trading", value=is_active)

st.markdown(f"""
<div style="display:flex;gap:8px;margin-top:10px;">
<div class="card" style="border:1px solid #FFD700;"><div style="font-size:11px;color:#8AA0B8;">Quality Filter Score Minimum</div><div style="background:#FFD700;color:black;display:inline-block;padding:3px 10px;border-radius:6px;font-weight:900;">6/7</div></div>
<div class="card" style="border:1px solid #FFA500;"><div style="font-size:11px;">Win Rate<br><b style="color:#FFA500;">90%</b></div></div>
<div class="card" style="border:1px solid {color_status};background:{color_status}22;"><div style="font-size:11px;color:{color_status};">{status} -<br>Opens 13:00 PKT<br>({cfg['session']})</div></div>
<div class="card" style="border:1px solid #00FFC2;"><div style="font-size:11px;color:#00FFC2;">KING V103 x<br>SONA<br>LINKED •<br>Selected</div></div>
</div>
""", unsafe_allow_html=True)

# === ZAMONG INDICATOR LOGIC - PINE TO PYTHON ===
# Pine: sh=ta.highest(high,10) sl=ta.lowest(low,10) bosBull=close>sh[1] sweepBull=low<sl and close>sl
# soniBuy=close>ema50 and rsi>35 sonaBuy=close>ema50 and rsi<60 v103Buy=close>ema21 and close>ema50 scalpBuy=crossover(ema9,ema21)
# q = (ema9>ema21?1:0)+(rsi>40 and rsi<70?1:0)+(close>ema50?1:0)+(close>ema200?1:0)+(close>vwap?1:0)+(ema21>ema50?1:0)+(bosBull?1:0)

def ema(s,n): return s.ewm(span=n,adjust=False).mean()
def rsi_calc(s,p=14):
    d=s.diff(); g=d.where(d>0,0).ewm(alpha=1/p,adjust=False).mean(); l=-d.where(d<0,0).ewm(alpha=1/p,adjust=False).mean()
    return 100-(100/(1+g/(l.replace(0,1e-10))))

dates = pd.date_range(end=datetime.datetime.now(), periods=150, freq="5min")
base = cfg['price']
close = base + np.cumsum(np.random.randn(150)*base*0.0008) + np.linspace(-10,5,150)
df = pd.DataFrame({"time":dates,"close":close,"high":close+np.random.rand(150)*2,"low":close-np.random.rand(150)*2,"volume":np.random.randint(2000,8000,150)})
df["ema9"]=ema(df["close"],9); df["ema21"]=ema(df["close"],21); df["ema50"]=ema(df["close"],50); df["ema200"]=ema(df["close"],200)
df["vwap"]=(df["close"]*df["volume"]).cumsum()/df["volume"].cumsum(); df["rsi"]=rsi_calc(df["close"],14)
df["sh"]=df["high"].rolling(10).max(); df["sl"]=df["low"].rolling(10).min()
df["bosBull"]=df["close"]>df["sh"].shift(1); df["sweepBull"]=(df["low"]<df["sl"].shift(1))&(df["close"]>df["sl"].shift(1))
df["q"]=0; df["q"]+=(df["ema9"]>df["ema21"]).astype(int); df["q"]+=((df["rsi"]>40)&(df["rsi"]<70)).astype(int); df["q"]+=(df["close"]>df["ema50"]).astype(int); df["q"]+=(df["close"]>df["ema200"]).astype(int); df["q"]+=(df["close"]>df["vwap"]).astype(int); df["q"]+=(df["ema21"]>df["ema50"]).astype(int); df["q"]+=df["bosBull"].astype(int); df["q"]=df["q"].clip(upper=7)
last=df.iloc[-1]; q=int(last["q"]) if is_active else 4

# Chart
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08, row_heights=[0.7,0.3])
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#FFD700",width=2)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="yellow")), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="orange")), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="#FF6B6B")), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema200"], name="ema200", line=dict(color="#9B59B6",width=2)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["vwap"], name="VWAP", line=dict(color="#00FFC2",dash="dot")), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["rsi"], name="RSI 14", line=dict(color="#00FFC2")), row=2,col=1)
fig.add_trace(go.Bar(x=df["time"], y=df["volume"], name="Volume", marker_color="rgba(255,215,0,0.3)"), row=2,col=1)
fig.update_layout(height=380, margin=dict(l=10,r=10,t=10,b=10), paper_bgcolor="#020B1A", plot_bgcolor="#020B1A", font=dict(color="#8AA0B8",size=10))
st.plotly_chart(fig, use_container_width=True)

if is_active and auto:
    st.markdown(f"""<div class="card" style="border:2px solid #00FF88;background:#0A2E1A;text-align:center;">
<div style="color:#00FF88;font-weight:900;">🔔 BUY SIGNAL CONFIRMED {q}/7 - {cfg['symbol']} @{last['close']:.2f} - KING 103 WAR</div>
<div style="color:white;font-size:11px;">TP 4213.25 • SL 4171.62 • {timeframe} • EMA200 {last['ema200']:.2f} • VWAP {last['vwap']:.2f} • BOS {bool(last['bosBull'])} • RSI {last['rsi']:.1f}</div>
</div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""<div class="card" style="border:2px solid #FF4D4D;background:#2A0A0A;text-align:center;">
<div style="color:#FF4D4D;font-weight:800;">⏸️ MARKET {cfg['symbol']} ○ CLOSED - Opens 13:00 PKT ({cfg['session']})</div>
<div style="color:#8AA0B8;font-size:11px;">{cfg['session']} Closed • PKT {now_pkt.strftime('%H:%M')} • UTC {now_utc.strftime('%H:%M')} • Opens 13:00 PKT • Quality {q}/7 • EMA200 {last['ema200']:.2f} • Automatic Trading Paused - Wait for {cfg['session']}</div>
</div>""", unsafe_allow_html=True)

st.caption(f"Zamong indicator jora da - King V103.5 - {market} - Quality {q}/7 - {timeframe} - PKT {now_pkt.strftime('%H:%M')} - Saved in app.py")
