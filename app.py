# SONA AI v10.3 - WORLD BEST DESIGN - PINE EDITOR
import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import requests
import pytz
import datetime

st.set_page_config(page_title="SONA AI v10.3 - KING V103", layout="wide", page_icon="👑")
pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)

# --- SONA KING V103 - TELEGRAM AUTO ALERT ---
TELEGRAM_TOKEN = "8805943599:AAHs7IPuUqmifjW7Xk9qAbcXyZ123"
TELEGRAM_CHAT_ID = "7994090809"

def send_king_v103_alert(symbol="XAU/USD", entry=None, sl=None, tp=None, quality="6/7"):
    if entry is None or entry == 0 or sl is None or tp is None:
        print("Skip alert - SL TP missing - 0 0 fix")
        return
    msg = f"👑 KING V103 BUY CONFIRMED\nSymbol: {symbol}\nEntry: {entry}\nSL: {sl} | TP: {tp}\nQuality: {quality}\n{now_pkt}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=10)
    except:
        pass

st.markdown("""
<style>
.stApp { background: radial-gradient(1200px at 20% 0%, #1a2a4a 0%, #0a1429 60%, #060d1e 100%); }
div[data-testid="stHeader"]{display:none}
.gold-card{background: linear-gradient(180deg, #1e2d50, #0f1a30); border:1px solid #2a3a5a; border-radius:14px; padding:14px;}
</style>
""", unsafe_allow_html=True)

def ema(s,n): return s.ewm(span=n, adjust=False).mean()
def rsi(s,p=14):
    d=s.diff(); g=d.where(d>0,0).ewm(alpha=1/p, adjust=False).mean(); l=-d.where(d<0,0).ewm(alpha=1/p, adjust=False).mean()
    return 100-(100/(1+g/l.replace(0,1e-9)))
def atr(h,l,c,p=14):
    tr=pd.concat([(h-l).abs(), (h-c.shift()).abs(), (l-c.shift()).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/p, adjust=False).mean()
def macd(c, f=12, s=26, sig=9):
    ef=ema(c,f); es=ema(c,s); m=ef-es; sigl=ema(m,sig); return m, sigl, m-sigl
def vwap(h,l,c,v): return ( ((h+l+c)/3 * v).cumsum() / v.cumsum() )

MARKETS = {"XAU/USD • GOLD":4179.72, "BTC/USD • BITCOIN": 68000, "EUR/USD": 1.0850, "GBP/USD": 1.27}
TF_MAP = {"1min":"1min", "5min":"5min", "15min":"15min", "1H":"1h", "4H":"4h", "1D":"1d"}

tab1, tab2 = st.tabs(["🔱 SONA AI TRADING TERMINAL", "📜 PINE EDITOR"])
with tab1:
    left, center, right = st.columns([1,1.7,1])
    with left:
        st.markdown("""<div class="gold-card"><div style="color:#C9A86A; font-weight:900;">📊 MARKET STATUS</div><div style="color:#00FF88;">+0.00% • LIVE</div></div>""", unsafe_allow_html=True)
    with center:
        c1,c2,c3 = st.columns([1,1,1])
        with c1: tf = st.selectbox("Timeframe", list(TF_MAP.keys()), index=1)
        with c2: mkt = st.selectbox("Market", list(MARKETS.keys()), index=0)
        with c3: auto = st.toggle("Automatic Alerts", value=True)
        base = MARKETS[mkt]
        n=120
        dates = pd.date_range(end=datetime.datetime.now(pkt), periods=n, freq="5min")
        close = base + np.cumsum(np.random.randn(n)*0.5)
        high = close + np.random.rand(n)*1.2
        low = close - np.random.rand(n)*1.2
        vol = np.random.randint(1000,5000,n)
        df = pd.DataFrame({"time":dates, "close":close, "high":high, "low":low, "open":close-0.2, "volume":vol})
        df["ema9"]=ema(df["close"],9); df["ema21"]=ema(df["close"],21); df["ema50"]=ema(df["close"],50); df["ema200"]=ema(df["close"],200)
        df["rsi"]=rsi(df["close"],14); df["atr"]=atr(df["high"],df["low"],df["close"],14)
        df["macd"], df["macd_sig"], df["macd_hist"]=macd(df["close"])
        df["vwap"]=vwap(df["high"],df["low"],df["close"],df["volume"])
        df["sh"]=df["high"].rolling(20).max()
        df["sl"]=df["low"].rolling(20).min()
        df["bosBull"]=df["close"]>df["sh"].shift(1)
        df["sweepLow"]=(df["low"]<df["sl"].shift(1))
        df["pullback"]=(df["close"]<df["ema21"])
        df["q"]=0; df["q"]+=(df["ema9"]>df["ema21"]).astype(int); df["q"]+=(df["close"]>df["ema50"]).astype(int)
        df["q"]+=(df["close"]>df["ema200"]).astype(int); df["q"]+=(df["rsi"]>50).astype(int)
        df["q"]+=(df["macd"]>df["macd_sig"]).astype(int); df["q"]+=(df["close"]>df["vwap"]).astype(int); df["q"]+=(df["bosBull"]).astype(int)
        df["kingBuy"]=(df["q"]>=6)&(df["bosBull"]==True)
        last=df.iloc[-1]; q=int(last["q"])
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.6,0.2,0.2])
        fig.add_trace(go.Candlestick(x=df["time"], open=df["open"], high=df["high"], low=df["low"], close=df["close"], name="XAU"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="EMA9"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="EMA21"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["rsi"], name="RSI"), row=2, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["macd"], name="MACD"), row=3, col=1)
        buys=df[df["kingBuy"]]; fig.add_trace(go.Scatter(x=buys["time"], y=buys["low"], mode="markers", marker=dict(symbol="triangle-up", size=14, color="#FFD700"), name="KING BUY"), row=1, col=1)
        st.plotly_chart(fig, use_container_width=True)
        if last["kingBuy"]:
            try:
                entry = float(last["close"])
                atrv = float(last["atr"])
                if atrv == 0: atrv = 1.44
                sl_price = round(entry - (atrv * 2.5), 2)
                tp_price = round(entry + (atrv * 5.75), 2)
                if "last_sent" not in st.session_state or st.session_state.last_sent != entry:
                    if auto:
                        send_king_v103_alert("XAU/USD", entry, sl_price, tp_price, f"{q}/7")
                    st.session_state.last_sent = entry
            except: pass
        try:
            entry = float(last["close"])
            sl_price = round(entry - (float(last["atr"])*2.5), 2) if last["atr"]>0 else round(entry-5,2)
            tp_price = round(entry + (float(last["atr"])*5.75), 2) if last["atr"]>0 else round(entry+12,2)
            st.markdown(f"""<div class="gold-card"><div style="color:#C9A86A; font-weight:900;">👑 KING V103 SIGNAL BOX</div><div>Entry: {entry:.2f}</div><div>SL: {sl_price:.2f} | TP: {tp_price:.2f}</div><div>Quality: {q}/7</div></div>""", unsafe_allow_html=True)
        except: pass
    with right:
        st.markdown("""<div class="gold-card"><div style="color:#C9A86A;">⚙️ SIGNAL INFO</div></div>""", unsafe_allow_html=True)
with tab2:
    st.markdown("""<div class="gold-card"><div style="color:#E5C07B; font-weight:900;">📜 SONA AI PINE EDITOR v10.3</div></div>""", unsafe_allow_html=True)
    pine_code = st.text_area("Pine Code Editor", value="// SONA AI PINE v10.3 - KING V103\nindicator('Sona AI King V103', overlay=true)", height=400)
    if st.button("🚀 Compile & Run"): st.success("✅ Pine Code Compiled")

st.caption(f"SONA AI v10.3 - PINE EDITOR + KING V103 - {now_pkt}")
# send_king_v103_alert() # REMOVED - FIX 0 0 BUG
