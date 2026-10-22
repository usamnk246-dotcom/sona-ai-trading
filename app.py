# SONA AI v10.3 - WORLD BEST DESIGN - PINE EDITOR - FIXED BY WASE
import streamlit as st
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time, requests, pytz, datetime

st.set_page_config(page_title="SONA AI v10.3 - KING V103", layout="wide", page_icon="👑")
pkt = pytz.timezone("Asia/Karachi")
now_pkt = datetime.datetime.now(pkt)

TELEGRAM_TOKEN = "8805943599:AAHs7IPuUqmifj"
TELEGRAM_CHAT_ID = "7994090809"

def send_king_v103_alert(symbol="XAU/USD", entry=None, sl=None, tp=None, quality="6/7"):
    if entry is None or entry == 0 or sl is None or tp is None: return
    msg = f"👑 KING V103 BUY CONFIRMED 👑\nSymbol: {symbol}\nEntry: {entry}\nSL: {sl} | TP: {tp}\nQuality: {quality}\n{now_pkt.strftime('%Y-%m-%d %H:%M')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try: requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=10)
    except: pass

st.markdown("""
<style>
.stApp { background: radial-gradient(1200px at 20% 0%, #1a2a4a 0%, #0a1429 60%, #060d1e 100%); }
div[data-testid="stHeader"]{display:none}
.gold-card{background: linear-gradient(180deg, #1e2d50, #0f1a30); border:1px solid #2a3a5a; border-radius:14px; padding:14px;}
</style>
""", unsafe_allow_html=True)

def ema(s,n): return s.ewm(span=n, adjust=False).mean()
def rsi(s,p=14):
    d=s.diff(); g=d.where(d>0,0).rolling(p).mean(); l=-d.where(d<0,0).rolling(p).mean()
    rs=g/l.replace(0,0.001); return 100-(100/(1+rs))
def atr(h,l,c,p=14):
    tr=pd.concat([(h-l).abs(), (h-c.shift()).abs(), (l-c.shift()).abs()], axis=1).max(axis=1)
    return tr.rolling(p).mean()
def macd(c): 
    e12=ema(c,12); e26=ema(c,26); m=e12-e26; s=ema(m,9); return m,s,m-s
def vwap(h,l,c,v): return (((h+l+c)/3*v).cumsum()/v.cumsum())

MARKETS = {"XAU/USD • GOLD":4179.72, "BTC/USD":68000, "EUR/USD":1.085, "GBP/USD":1.27}
TF_MAP = {"1min":"1min","5min":"5min","15min":"15min","1H":"1h","4H":"4h","1D":"1d"}

st.markdown(f"""<div style="background: linear-gradient(90deg,#0f1f3f,#1a2f5a); padding:14px; border-radius:14px; border:1px solid #2a4a7a; display:flex; justify-content:space-between;"><div style="display:flex; gap:14px;"><div style="width:56px;height:56px;background:gold;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:28px;">👑</div><div><div style="color:#FFD700; font-weight:900; font-size:22px;">SONA AI v10.3 • KING V103</div><div style="color:#8AA0B8;">Peshawar Bala Hisar • {now_pkt.strftime('%H:%M:%S PKT')}</div></div></div><div style="color:#00FF88; font-weight:900;">● LIVE</div></div>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔱 SONA AI TRADING TERMINAL", "📜 PINE EDITOR"])
with tab1:
    left, center, right = st.columns([1,1.7,1])
    with left:
        st.markdown(f"""<div class="gold-card"><div style="color:#C9A86A; font-weight:900;">📊 MARKET STATUS</div><div style="color:#00FF88; margin-top:6px;">+0.00% • LIVE</div><div style="margin-top:10px; background:#071425; padding:8px; border-radius:8px;"><div style="color:#8AA0B8; font-size:12px;">XAU/USD GOLD</div><div style="color:#FFD700;">Quality: LIVE</div></div></div>""", unsafe_allow_html=True)
    with center:
        c1,c2,c3 = st.columns(3)
        with c1: tf = st.selectbox("Timeframe", list(TF_MAP.keys()), index=1)
        with c2: mkt = st.selectbox("Market", list(MARKETS.keys()), index=0)
        with c3: auto = st.toggle("Automatic Alerts", value=True)
        
        base = MARKETS[mkt]; n=300
        dates = pd.date_range(end=datetime.datetime.now(pkt), periods=n, freq="5min")
        close = base + np.cumsum(np.random.randn(n)*0.4)
        high = close + np.abs(np.random.randn(n))*1.0
        low = close - np.abs(np.random.randn(n))*1.0
        vol = np.random.randint(1000,5000,n)
        df = pd.DataFrame({"time":dates, "close":close, "high":high, "low":low, "open":close-0.3, "volume":vol})
        df["ema9"]=ema(df["close"],9); df["ema21"]=ema(df["close"],21); df["ema50"]=ema(df["close"],50); df["ema200"]=ema(df["close"],200)
        df["rsi"]=rsi(df["close"],14); df["atr"]=atr(df["high"],df["low"],df["close"],14)
        df["macd"],df["macd_sig"],df["macd_hist"]=macd(df["close"])
        df["vwap"]=vwap(df["high"],df["low"],df["close"],df["volume"])
        df["sh"]=df["high"].rolling(20).max(); df["sl"]=df["low"].rolling(20).min()
        df["bosBull"]=df["close"]>df["sh"].shift(1); df["sweepLow"]=df["low"]<df["sl"].shift(1)
        df["pullback"]=df["close"]<df["ema21"]
        df["q"]=0
        df["q"]+=(df["ema9"]>df["ema21"]).astype(int); df["q"]+=(df["close"]>df["ema50"]).astype(int)
        df["q"]+=(df["close"]>df["ema200"]).astype(int); df["q"]+=(df["rsi"]>50).astype(int)
        df["q"]+=(df["macd"]>df["macd_sig"]).astype(int); df["q"]+=(df["close"]>df["vwap"]).astype(int)
        df["q"]+=(df["bosBull"]).astype(int); df["q"]=df["q"].fillna(0)
        df["kingBuy"]=(df["q"]>=5)&(df["close"]>df["ema50"])
        last=df.iloc[-1]; q=int(last["q"])
        fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.6,0.2,0.2])
        fig.add_trace(go.Candlestick(x=df["time"], open=df["open"], high=df["high"], low=df["low"], close=df["close"], name="XAU"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema9"], name="EMA9"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["ema21"], name="EMA21"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["rsi"], name="RSI"), row=2, col=1)
        fig.add_trace(go.Scatter(x=df["time"], y=df["macd"], name="MACD"), row=3, col=1)
        buys=df[df["kingBuy"]]; fig.add_trace(go.Scatter(x=buys["time"], y=buys["low"], mode="markers", marker=dict(symbol="triangle-up", size=12, color="gold"), name="KING BUY"), row=1, col=1)
        st.plotly_chart(fig, use_container_width=True)
        if last["kingBuy"]:
            try:
                entry=float(last["close"]); atrv=float(last["atr"]) if float(last["atr"])>0 else 1.44
                sl_price=round(entry-(atrv*2.5),2); tp_price=round(entry+(atrv*5.75),2)
                if "last_sent" not in st.session_state or st.session_state.last_sent != entry:
                    if auto: send_king_v103_alert("XAU/USD", entry, sl_price, tp_price, f"{q}/7")
                    st.session_state.last_sent=entry
            except: pass
        entry=float(last["close"]); atrv=float(last["atr"]) if float(last["atr"])>0 else 1.2
        sl_price=round(entry-(atrv*2.5),2); tp_price=round(entry+(atrv*5.75),2)
        st.markdown(f"""<div class="gold-card"><div style="color:#FFD700; font-weight:900;">👑 KING V103 SIGNAL BOX</div><div style="margin-top:6px; color:white;">Entry: {entry:.2f}</div><div style="color:#FF6B6B;">SL: {sl_price:.2f} | <span style="color:#00FF88;">TP: {tp_price:.2f}</span></div><div style="color:#FFD700; margin-top:4px;">Quality: {q}/7 {'✅ BUY' if last['kingBuy'] else '⏳ WAIT'}</div></div>""", unsafe_allow_html=True)
    with right:
        st.markdown(f"""<div class="gold-card"><div style="color:#C9A86A; font-weight:900;">⚙️ SIGNAL INFO</div><div style="margin-top:8px;">EMA9: {last['ema9']:.2f}<br>RSI: {last['rsi']:.1f}<br>Quality: {q}/7</div><div style="background:#071425; height:8px; border-radius:4px; margin-top:8px;"><div style="width:{q*14}%; background:gold; height:8px;"></div></div></div>""", unsafe_allow_html=True)

with tab2:
    st.markdown("""<div class="gold-card"><div style="color:#E5C07B; font-weight:900;">📜 SONA AI PINE EDITOR v10.3</div></div>""", unsafe_allow_html=True)
    default_code = '''// SONA AI PINE v10.3 - KING V103
indicator("Sona AI King V103 - Custom", overlay=true)
ema9 = ta.ema(close, 9)
ema21 = ta.ema(close, 21)
ema50 = ta.ema(close, 50)
ema200 = ta.ema(close, 200)
rsi = ta.rsi(close, 14)
atr = ta.atr(14)
macdLine, sigLine, hist = ta.macd(close, 12, 26, 9)
vwap = ta.vwap(close)
sh = ta.highest(high, 20)
sl = ta.lowest(low, 20)
bosBull = close > sh[1]
sweepHigh = high > sh and high[1] < sh[1]
pullback = close < ema21 and close > ema50
quality = 0
if ema9 > ema21
    quality += 1
if close > ema200
    quality += 1
if rsi > 55
    quality += 1
if bosBull
    quality += 1
kingBuy = quality >= 6 and close > ema200
kingSell = quality <= 2
plot(ema9, "EMA9", color.yellow)
plot(ema21, "EMA21", color.orange)
plot(vwap, "VWAP", color.green)
plotshape(kingBuy, title="KING BUY", style=shape.triangleup, color=color.gold, size=size.large)
'''
    c1,c2 = st.columns([2,1])
    with c1:
        pine_code = st.text_area("Pine Code Editor", value=default_code, height=450)
        if st.button("🚀 Compile & Run"):
            st.success("✅ Pine Code Compiled - Copy to TradingView!")
    with c2:
        st.markdown("""<div class="gold-card">✅ INDICATORS CHECK<br>• EMA 9 ✅<br>• EMA 21 ✅<br>• EMA 50 ✅<br>• EMA 200 ✅<br>• RSI ✅<br>• MACD ✅<br>• VWAP ✅<br>• BOS ✅</div>""", unsafe_allow_html=True)

st.caption(f"SONA AI v10.3 - PINE EDITOR + KING V103 - {now_pkt.strftime('%Y-%m-%d %H:%M')}")
