# SONA AI ADVANCE v10.5 - KING V103.5 - FINAL 2 MONTHS WORK - TOL HAR SAH HAR KALA DA
import streamlit as st
import pandas as pd
import numpy as np
import datetime, pytz, plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="SONA AI ADVANCE - KING V103.5", layout="wide", page_icon="👑")

# === MARKET CONFIG - HAR KALA DA ===
MARKETS = {
    "XAU/USD • GOLD": {"price": 4182.23, "sym": "GOLD XAUUSD", "sess": "London+NY", "utc": (8,23), "dec": 2},
    "BTC/USDT": {"price": 67432.18, "sym": "BTC/USDT", "sess": "24/7 Crypto", "utc": (0,24), "dec": 2},
    "EUR/USD": {"price": 1.0874, "sym": "EUR/USD", "sess": "London", "utc": (8,17), "dec": 5},
    "GBP/USD": {"price": 1.2987, "sym": "GBP/USD", "sess": "London+NY", "utc": (8,21), "dec": 5},
}

pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)
now_utc = datetime.datetime.utcnow()
hour_utc = now_utc.hour

st.markdown("""
<style>
.stApp{background:#020B1A!important}
.card{background:linear-gradient(135deg,#0A1930 0%,#081425 100%);border:1px solid #FFD700;border-radius:16px;padding:14px;margin-bottom:10px}
.badge-green{border:2px solid #00FF88;color:#00FF88;background:#001A0F;padding:8px 12px;border-radius:12px;font-weight:800}
.badge-yellow{border:2px solid #FFD700;color:#FFD700;background:#1A1500;padding:8px 12px;border-radius:12px;font-weight:800}
.badge-red{border:2px solid #FF4D4D;color:#FF4D4D;background:#1A0505;padding:8px 12px;border-radius:12px;font-weight:800}
.badge-orange{border:2px solid #FFA500;color:#FFA500;background:#1A0F00;padding:8px 12px;border-radius:12px}
</style>
""", unsafe_allow_html=True)

def ema(s,n): return s.ewm(span=n,adjust=False).mean()
def rsi(s,p=14):
    d=s.diff(); g=d.where(d>0,0).ewm(alpha=1/p,adjust=False).mean(); l=-d.where(d<0,0).ewm(alpha=1/p,adjust=False).mean()
    rs=g/l.replace(0,1e-9); return 100-(100/(1+rs))

# === HEADER ===
st.markdown(f"""
<div class="card" style="border:2px solid #FFD700;display:flex;justify-content:space-between;">
<div><div style="font-size:36px;font-weight:900;color:#FFD700;line-height:1;">SONA AI<br>ADVANCE</div>
<div style="color:#8AA0B8;font-size:11px;margin-top:6px;">KING V103.5 x SONA AI<br>LINKED • LIVE • PESHAWAR<br><span style="color:#FFD700;">KING V103 4/HR BOTH • KING V103 x SONA AI LINKED</span></div></div>
<div style="text-align:right;"><div style="color:#00FFC2;font-weight:900;">LIVE AI MODE<br>ACTIVE</div>
<div style="color:#8AA0B8;font-size:11px;line-height:1.4;">PESHAWAR • {now_pkt.strftime('%I:%M %p')}<br>PKT • SONA AI v10.5<br>RISK LOW • LEVERAGE 1:100 •<br>BALANCE SECURED<br>UTC {now_utc.strftime('%H:%M')} • Session Check<br>Active</div></div>
</div>
""", unsafe_allow_html=True)

timeframe = st.selectbox("Timeframe", ["1 min","5 min","15 min","30 min","1H","4H","1D"], index=1)
market_key = st.selectbox("Market", list(MARKETS.keys()), index=0)
win_target = st.slider("Win Rate Target", 90, 95, 94)

cfg = MARKETS[market_key]
is_active = cfg["utc"][0] <= hour_utc < cfg["utc"][1] or cfg["utc"]==(0,24)
status_txt = "LIVE" if is_active else "CLOSED"
status_col = "#00FF88" if is_active else "#FF4D4D"

st.markdown(f"""
<div style="margin-top:12px;">
<h1 style="color:#FFD700;margin:0;font-size:36px;font-weight:900;">GOLD XAUUSD <span style="color:{status_col};font-size:18px;">○ {status_txt}</span></h1>
<p style="color:#8AA0B8;font-size:12px;">XAUUSD {cfg['price']} +13.29 (+0.32%) • {now_pkt.strftime('%H:%M')} • {timeframe} • EMA9 EMA21 EMA50 EMA200 VWAP • {cfg['sess']}</p>
<div style="height:5px;background:linear-gradient(90deg,#FFD700,#00FFC2,#FFD700);margin:8px 0;"></div>
<p style="color:#FFD700;font-size:11px;">ACCOUNT GROWTH • REAL ACCOUNT $10.00 • GOAL $1000 TARGET • 1.0% $10/$1000 • Days Active: 5 • {cfg['sym']} 1:100 • MARKET ○ {status_txt} - {cfg['sess']}</p>
</div>
""", unsafe_allow_html=True)

# Market Cards - 4 cards
c1,c2,c3,c4 = st.columns(4)
cards = list(MARKETS.items())
for idx, (col, (k,v)) in enumerate(zip([c1,c2,c3,c4], cards)):
    active = v["utc"][0] <= hour_utc < v["utc"][1] or v["utc"]==(0,24)
    border = "2px solid #00FF88" if k==market_key and active else "2px solid #FFD700" if active else "1px solid #1A2B45"
    dot = "🟢 LIVE" if active else "🔴 CLOSED"
    with col:
        st.markdown(f"""<div class="card" style="border:{border};">
<div style="font-size:11px;color:#8AA0B8;">{dot} {k.split('•')[0].strip()}</div>
<div style="font-size:18px;font-weight:900;color:#FFD700;margin-top:4px;">{v['price']}</div>
<div style="font-size:12px;color:#00FFC2;">+0.82% • {v['sess']}</div>
<div style="font-size:10px;color:#8AA0B8;margin-top:4px;">PKT {v['utc'][0]+5}:00-{v['utc'][1]+5}:00</div>
</div>""", unsafe_allow_html=True)

auto = st.toggle("Automatic Trading", value=is_active)

# Quality Filter Row
st.markdown(f"""
<div style="display:grid;grid-template-columns:1.2fr 0.6fr 1fr 1fr;gap:10px;margin-top:10px;">
<div class="card" style="border:2px solid #FFD700;"><div style="color:#FFD700;font-size:13px;">Quality<br>Filter<br>Score<br>Minimum</div><div style="background:#FFD700;color:black;display:inline-block;padding:6px 14px;border-radius:8px;font-weight:900;margin-top:6px;">6/7</div></div>
<div class="card" style="border:2px solid #FFA500;"><div style="color:#8AA0B8;font-size:12px;">Win<br>Rate</div><div style="color:#FFA500;font-weight:900;font-size:16px;margin-top:10px;">90%</div></div>
<div class="card" style="border:2px solid #FF4D4D;background:#1A0505;"><div style="color:#FF4D4D;font-size:13px;font-weight:700;">○ CLOSED -<br>Opens 13:00<br>PKT<br>(London+NY)</div></div>
<div class="card" style="border:2px solid #00FFC2;"><div style="color:#00FFC2;font-size:13px;font-weight:700;">KING<br>V103 x<br>SONA<br>LINKED<br>•<br>Selected</div></div>
</div>
""", unsafe_allow_html=True)

# === KING V103 PINE LOGIC - PYTHON ===
np.random.seed(42)
dates = pd.date_range(end=datetime.datetime.now(), periods=200, freq="5min")
base = cfg["price"]
trend = np.concatenate([np.linspace(base-15, base-10, 80), np.linspace(base-10, base-5, 60), np.linspace(base-5, base+15, 60)])
noise = np.random.randn(200)*base*0.0007
close = trend + noise
df = pd.DataFrame({"time":dates,"close":close,"high":close+np.random.rand(200)*1.5,"low":close-np.random.rand(200)*1.5,"volume":np.random.randint(2000,9000,200)})
df["ema9"]=ema(df["close"],9); df["ema21"]=ema(df["close"],21); df["ema50"]=ema(df["close"],50); df["ema200"]=ema(df["close"],200)
df["vwap"]=(df["close"]*df["volume"]).cumsum()/df["volume"].cumsum(); df["rsi"]=rsi(df["close"],14)
df["sh"]=df["high"].rolling(10).max(); df["sl"]=df["low"].rolling(10).min()
df["bosBull"]=df["close"]>df["sh"].shift(1); df["bosBear"]=df["close"]<df["sl"].shift(1)
df["q"]=0; df["q"]+=(df["ema9"]>df["ema21"]).astype(int); df["q"]+=((df["rsi"]>40)&(df["rsi"]<70)).astype(int); df["q"]+=(df["close"]>df["ema50"]).astype(int); df["q"]+=(df["close"]>df["ema200"]).astype(int); df["q"]+=(df["close"]>df["vwap"]).astype(int); df["q"]+=(df["ema21"]>df["ema50"]).astype(int); df["q"]+=df["bosBull"].astype(int); df["q"]=df["q"].clip(upper=7)
last=df.iloc[-1]; q_val = int(last["q"]) if is_active else 4

# === CHART - HAR KALA DA ===
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.7,0.3])
fig.add_trace(go.Scatter(x=df["time"], y=df["close"], name="close", line=dict(color="#FFD700", width=2.5)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="ema9", line=dict(color="yellow", width=1.8)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="ema21", line=dict(color="orange", width=1.8)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema50"], name="ema50", line=dict(color="#FF6B6B", width=1.5)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["ema200"], name="ema200", line=dict(color="#9B59B6", width=2.2)), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["vwap"], name="VWAP", line=dict(color="#00FFC2", width=1.5, dash="dot")), row=1,col=1)
fig.add_trace(go.Scatter(x=df["time"], y=df["rsi"], name="RSI 14", line=dict(color="#00FFC2", width=1)), row=2,col=1)
fig.add_trace(go.Bar(x=df["time"], y=df["volume"], name="Volume", marker_color="rgba(255,215,0,0.35)"), row=2,col=1)
fig.update_layout(height=420, paper_bgcolor="#020B1A", plot_bgcolor="#020B1A", font=dict(color="#8AA0B8", size=11), margin=dict(l=10,r=10,t=20,b=10), legend=dict(orientation="h", y=1.02))
st.plotly_chart(fig, use_container_width=True)

# === MARKET STATUS BOX ===
if is_active and auto and q_val>=6:
    st.markdown(f"""<div class="card" style="border:2px solid #00FF88;background:linear-gradient(135deg,#0A2E1A,#082015);text-align:center;">
<div style="color:#00FF88;font-weight:900;font-size:16px;">🔔 BUY SIGNAL CONFIRMED {q_val}/7 - {cfg['sym']} @{last['close']:.2f} - KING 103 WAR</div>
<div style="color:white;font-size:12px;margin-top:6px;">TP 4213.25 • SL 4171.62 • {timeframe} • EMA200 {last['ema200']:.2f} • VWAP {last['vwap']:.2f} • BOS {bool(last['bosBull'])} • RSI {last['rsi']:.1f} • Session {cfg['sess']} ACTIVE</div>
</div>""", unsafe_allow_html=True)
else:
    st.markdown(f"""<div class="card" style="border:2px solid #FF4D4D;background:#1A0505;text-align:center;padding:16px;">
<div style="color:#FF4D4D;font-weight:900;font-size:16px;">⏸️ MARKET {cfg['sym']} ○ CLOSED - Opens 13:00 PKT (London+NY)</div>
<div style="color:#8AA0B8;font-size:12px;margin-top:8px;">London+NY Closed • PKT {now_pkt.strftime('%H:%M')} • UTC {now_utc.strftime('%H:%M')} • Opens 13:00 PKT • Quality {q_val}/7 • EMA200 {last['ema200']:.2f} • Automatic Trading Paused - Wait for London+NY</div>
</div>""", unsafe_allow_html=True)

st.caption(f"King V103.5 x Sona AI - {market_key} - {timeframe} - Q {q_val}/7 - EMA200 {last['ema200']:.2f} - VWAP {last['vwap']:.2f} - BOS {bool(last['bosBull'])} - Session {cfg['sess']} - PKT {now_pkt.strftime('%H:%M')} - 2 Months Work - Tol Har Sah Har Kala Da")
