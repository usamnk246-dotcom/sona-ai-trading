"""
💛 SONA AI - KING V71 ULTRA ADVANCE
Munga Kor Wala Asli Indicator - Full SMC Pro
Features: EMA9/21/200, RSI14, MACD, VWAP, ATR, BOS, CHOCH, Liquidity Sweep, Order Block, FVG, Pullback, Scalping 5M
OlympTrade Style Click System
"""
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ================= PAGE CONFIG =================
st.set_page_config(page_title="SONA AI - KING V71 ADVANCE", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp { background: #0b0e11; }
h1 { color: #f0b90b !important; }
.stButton>button { background: linear-gradient(135deg, #1e2329, #2b3139); color: #eaecef; border: 1px solid #474d57; border-radius: 12px; padding: 10px; font-weight: 800; transition: 0.3s; }
.stButton>button:hover { border-color: #f0b90b; color: #f0b90b; box-shadow: 0 0 12px #f0b90b; transform: translateY(-2px); }
.active-btn>button { background: #f0b90b !important; color: #000 !important; border: 1px solid #f0b90b !important; }
.metric-card { background: #1e2329; border: 1px solid #2b3139; border-radius: 12px; padding: 12px; }
.signal-buy { background: linear-gradient(90deg, #0ecb81, #02c076); padding: 20px; border-radius: 16px; text-align: center; color: white; font-size: 28px; font-weight: 900; box-shadow: 0 0 30px #0ecb81; }
.signal-sell { background: linear-gradient(90deg, #f6465d, #cf304a); padding: 20px; border-radius: 16px; text-align: center; color: white; font-size: 28px; font-weight: 900; box-shadow: 0 0 30px #f6465d; }
.signal-wait { background: #2b3139; padding: 18px; border-radius: 16px; text-align: center; color: #848e9c; font-size: 22px; font-weight: 700; }
.badge { padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 800; margin: 2px; display: inline-block; }
.timer-box { background: #1e2329; border: 2px solid #f0b90b; border-radius: 14px; padding: 14px; text-align: center; color: #f0b90b; font-size: 24px; font-weight: 900; }
</style>
""", unsafe_allow_html=True)

# ================= SESSION =================
if 'market' not in st.session_state: st.session_state.market = "GOLD XAUUSD"
if 'tf' not in st.session_state: st.session_state.tf = "5m"
if 'strat' not in st.session_state: st.session_state.strat = "KING V71 SCALP 5M"
if 't0' not in st.session_state: st.session_state.t0 = datetime.now()

MARKETS = {"GOLD XAUUSD":"GC=F","SILVER":"SI=F","BTC/USD":"BTC-USD","ETH/USD":"ETH-USD","EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","US100":"^NDX","US30":"^DJI"}
TFS = ["1m","5m","15m","30m","1h","4h","1d"]
TF_MAP = {"1m":("1m","1d"),"5m":("5m","5d"),"15m":("15m","5d"),"30m":("30m","1mo"),"1h":("60m","1mo"),"4h":("60m","3mo"),"1d":("1d","1y")}
STRATEGIES = ["KING V71 SCALP 5M","LIQUIDITY SWEEP PRO","BOS + CHOCH + PULLBACK","ORDER BLOCK + FVG","EMA CROSS + VWAP"]

# ================= HEADER =================
st.markdown("<h1 style='text-align:center;'>💛 SONA AI • KING V71 ULTRA ADVANCE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#848e9c;margin-top:-15px;'>Munga Kor Wala Original Indicator | EMA 9/21/200 | RSI14 | MACD | VWAP | ATR | BOS | CHOCH | Liquidity | OB | FVG | 5M Scalping</p>", unsafe_allow_html=True)

# ================= OLYMP BUTTONS =================
st.markdown("#### 🎯 MARKET SELECT - Click to Change")
m_cols = st.columns(len(MARKETS))
for i, m in enumerate(MARKETS.keys()):
    with m_cols[i]:
        if st.button(f"{'✅ ' if m==st.session_state.market else ''}{m}", key=f"m_{m}", use_container_width=True):
            st.session_state.market = m
            st.session_state.t0 = datetime.now()
            st.rerun()

st.markdown("#### ⏰ TIMEFRAME + STRATEGY - Click to Change")
t_cols = st.columns(8)
for i, tf in enumerate(TFS):
    with t_cols[i]:
        if st.button(f"{'✅ ' if tf==st.session_state.tf else ''}{tf}", key=f"tf_{tf}"):
            st.session_state.tf = tf
            st.session_state.t0 = datetime.now()
            st.rerun()
with t_cols[7]:
    strat = st.selectbox("Strategy", STRATEGIES, index=STRATEGIES.index(st.session_state.strat) if st.session_state.strat in STRATEGIES else 0, label_visibility="collapsed")
    st.session_state.strat = strat

symbol = MARKETS[st.session_state.market]
interval, period = TF_MAP[st.session_state.tf]

# ================= DATA =================
@st.cache_data(ttl=25)
def load(sym, per, inter):
    df = yf.download(sym, period=per, interval=inter, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    return df.dropna()

df = load(symbol, period, interval)
if len(df) < 210:
    st.warning(f"⚠️ King V71 ko 200 candles chahiye, abhi {len(df)} hai. 15m / 1h / 1d try karo")
    st.stop()

# ================= KING V71 INDICATORS =================
df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()
df['EMA200'] = df['Close'].ewm(span=200, adjust=False).mean()
# RSI14
delta = df['Close'].diff()
gain = delta.where(delta>0,0).ewm(alpha=1/14).mean()
loss = (-delta.where(delta<0,0)).ewm(alpha=1/14).mean()
df['RSI'] = 100 - (100/(1+gain/loss))
# MACD
df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
df['MACD_SIG'] = df['MACD'].ewm(span=9).mean()
df['MACD_HIST'] = df['MACD'] - df['MACD_SIG']
# VWAP
df['TP'] = (df['High']+df['Low']+df['Close'])/3
df['VWAP'] = (df['TP']*df['Volume']).cumsum() / df['Volume'].cumsum()
df['VWAP'] = df['VWAP'].fillna(df['EMA21'])
# ATR14
df['TR'] = pd.concat([df['High']-df['Low'], (df['High']-df['Close'].shift(1)).abs(), (df['Low']-df['Close'].shift(1)).abs()], axis=1).max(axis=1)
df['ATR'] = df['TR'].ewm(span=14).mean()

# ================= ADVANCE SMC =================
# Swing High/Low
df['SwingHigh'] = df['High'].rolling(5, center=True).max()
df['SwingLow'] = df['Low'].rolling(5, center=True).min()
# BOS / CHOCH
df['BOS_BULL'] = df['Close'] > df['SwingHigh'].shift(1)
df['BOS_BEAR'] = df['Close'] < df['SwingLow'].shift(1)
df['CHOCH_BULL'] = (df['BOS_BULL']) & (df['Close'].shift(1) < df['SwingLow'].shift(2))
df['CHOCH_BEAR'] = (df['BOS_BEAR']) & (df['Close'].shift(1) > df['SwingHigh'].shift(2))
# Liquidity Sweep
df['LIQ_SWEEP_BUY'] = (df['Low'] < df['SwingLow'].shift(1)) & (df['Close'] > df['SwingLow'].shift(1)) & (df['Volume'] > df['Volume'].rolling(20).mean())
df['LIQ_SWEEP_SELL'] = (df['High'] > df['SwingHigh'].shift(1)) & (df['Close'] < df['SwingHigh'].shift(1)) & (df['Volume'] > df['Volume'].rolling(20).mean())
# Pullback
df['PULLBACK_BUY'] = (df['Low'] <= df['EMA21']) & (df['Close'] > df['EMA21']) & (df['EMA9'] > df['EMA21'])
df['PULLBACK_SELL'] = (df['High'] >= df['EMA21']) & (df['Close'] < df['EMA21']) & (df['EMA9'] < df['EMA21'])
# Order Block (Last bearish/bullish candle before impulse)
df['OB_BULL'] = (df['Close'].shift(1) < df['Open'].shift(1)) & (df['Close'] > df['High'].shift(1))
df['OB_BEAR'] = (df['Close'].shift(1) > df['Open'].shift(1)) & (df['Close'] < df['Low'].shift(1))
# FVG (Fair Value Gap)
df['FVG_BULL'] = df['Low'] > df['High'].shift(2)
df['FVG_BEAR'] = df['High'] < df['Low'].shift(2)

L = df.iloc[-1]
price=float(L['Close']); ema9=float(L['EMA9']); ema21=float(L['EMA21']); ema200=float(L['EMA200']); rsi=float(L['RSI']); vwap=float(L['VWAP']); atr=float(L['ATR']); macd=float(L['MACD']); sig=float(L['MACD_SIG'])
bos_bull=bool(L['BOS_BULL']); bos_bear=bool(L['BOS_BEAR']); choch_bull=bool(L['CHOCH_BULL']); choch_bear=bool(L['CHOCH_BEAR'])
sweep_buy=bool(L['LIQ_SWEEP_BUY']); sweep_sell=bool(L['LIQ_SWEEP_SELL']); pull_buy=bool(L['PULLBACK_BUY']); pull_sell=bool(L['PULLBACK_SELL'])
ob_bull=bool(L['OB_BULL']); ob_bear=bool(L['OB_BEAR']); fvg_bull=bool(L['FVG_BULL']); fvg_bear=bool(L['FVG_BEAR'])

# ================= STRATEGY LOGIC =================
if strat == "KING V71 SCALP 5M":
    buy_logic = (ema9 > ema21) and (price > ema200) and (price > vwap) and (50 < rsi < 71) and (macd > sig) and (pull_buy or sweep_buy or bos_bull)
    sell_logic = (ema9 < ema21) and (price < ema200) and (price < vwap) and (29 < rsi < 50) and (macd < sig) and (pull_sell or sweep_sell or bos_bear)
elif strat == "LIQUIDITY SWEEP PRO":
    buy_logic = sweep_buy and (rsi < 45) and (price > ema200)
    sell_logic = sweep_sell and (rsi > 55) and (price < ema200)
elif strat == "BOS + CHOCH + PULLBACK":
    buy_logic = (bos_bull or choch_bull) and pull_buy
    sell_logic = (bos_bear or choch_bear) and pull_sell
elif strat == "ORDER BLOCK + FVG":
    buy_logic = (ob_bull or fvg_bull) and (price > vwap)
    sell_logic = (ob_bear or fvg_bear) and (price < vwap)
else:
    buy_logic = (ema9 > ema21) and (price > vwap) and (macd > sig)
    sell_logic = (ema9 < ema21) and (price < vwap) and (macd < sig)

# ================= SIGNAL BOX =================
if buy_logic:
    sl = price - atr*1.5; tp = price + atr*3.0
    rr = abs(tp-price)/abs(price-sl) if price!=sl else 0
    st.markdown(f"<div class='signal-buy'>🟢 BUY NOW • {st.session_state.market} • {st.session_state.tf} • {strat} • 5M EXPIRY • RR 1:{rr:.1f}</div>", unsafe_allow_html=True)
elif sell_logic:
    sl = price + atr*1.5; tp = price - atr*3.0
    rr = abs(tp-price)/abs(price-sl) if price!=sl else 0
    st.markdown(f"<div class='signal-sell'>🔴 SELL NOW • {st.session_state.market} • {st.session_state.tf} • {strat} • 5M EXPIRY • RR 1:{rr:.1f}</div>", unsafe_allow_html=True)
else:
    sl = price - atr*1.5; tp = price + atr*3.0
    st.markdown(f"<div class='signal-wait'>⚪ WAIT • {st.session_state.market} • {st.session_state.tf} • {strat} • No Setup</div>", unsafe_allow_html=True)

# ================= BADGES + TIMER =================
b1,b2,b3,b4,b5 = st.columns(5)
if bos_bull: b1.markdown("<span class='badge' style='background:#0ecb81;color:white;'>BOS BULL</span>", unsafe_allow_html=True)
if bos_bear: b1.markdown("<span class='badge' style='background:#f6465d;color:white;'>BOS BEAR</span>", unsafe_allow_html=True)
if choch_bull: b1.markdown("<span class='badge' style='background:#0ecb81;color:white;'>CHOCH BULL</span>", unsafe_allow_html=True)
if choch_bear: b1.markdown("<span class='badge' style='background:#f6465d;color:white;'>CHOCH BEAR</span>", unsafe_allow_html=True)
if sweep_buy: b2.markdown("<span class='badge' style='background:#7c3aed;color:white;'>LIQ SWEEP BUY 💧</span>", unsafe_allow_html=True)
if sweep_sell: b2.markdown("<span class='badge' style='background:#f6465d;color:white;'>LIQ SWEEP SELL 💧</span>", unsafe_allow_html=True)
if pull_buy: b3.markdown("<span class='badge' style='background:#0ecb81;color:white;'>PULLBACK BUY</span>", unsafe_allow_html=True)
if pull_sell: b3.markdown("<span class='badge' style='background:#f6465d;color:white;'>PULLBACK SELL</span>", unsafe_allow_html=True)
if ob_bull: b4.markdown("<span class='badge' style='background:#f0b90b;color:black;'>OB BULL</span>", unsafe_allow_html=True)
if ob_bear: b4.markdown("<span class='badge' style='background:#f0b90b;color:black;'>OB BEAR</span>", unsafe_allow_html=True)
if fvg_bull: b4.markdown("<span class='badge' style='background:#00D1FF;color:black;'>FVG BULL</span>", unsafe_allow_html=True)
if fvg_bear: b4.markdown("<span class='badge' style='background:#00D1FF;color:black;'>FVG BEAR</span>", unsafe_allow_html=True)

# 5M Timer
rem = st.session_state.t0 + timedelta(minutes=5) - datetime.now()
if rem.total_seconds() <= 0:
    st.session_state.t0 = datetime.now()
    rem = timedelta(minutes=5)
mm, ss = divmod(int(rem.total_seconds()), 60)
b5.markdown(f"<div class='timer-box'>⏱️ {mm:02d}:{ss:02d} / 5M SCALP</div>", unsafe_allow_html=True)

# ================= METRICS =================
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric(f"💰 {st.session_state.market}", f"{price:.2f}", f"{float(df['Close'].iloc[-1]-df['Close'].iloc[-2]):+.2f}")
m2.metric("📈 EMA 9/21/200", f"{ema9:.1f} / {ema21:.1f} / {ema200:.1f}", "Bullish" if ema9>ema21>ema200 else "Bearish" if ema9<ema21<ema200 else "Mixed")
m3.metric(f"📊 RSI14 {rsi:.1f} | MACD {macd:.3f}", f"VWAP {vwap:.2f}", f"ATR {atr:.3f}")
m4.metric(f"🛑 SL {sl:.2f}", f"TP {tp:.2f}", f"RR 1:{abs(tp-price)/abs(price-sl):.1f}" if price!=sl else "RR -")
m5.metric("💧 Liquidity", "SWEEP" if sweep_buy or sweep_sell else "No Sweep", "BOS" if bos_bull or bos_bear else "No BOS")

# ================= MAIN CHART =================
fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=f"{st.session_state.market}"))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA9'], line=dict(color='#00D1FF', width=1.6), name='EMA9'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA21'], line=dict(color='#FFA800', width=1.6), name='EMA21'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA200'], line=dict(color='#FF00E6', width=2.8), name='EMA200'))
fig.add_trace(go.Scatter(x=df.index, y=df['VWAP'], line=dict(color='#F0B90B', width=1.2, dash='dot'), name='VWAP'))
# Liquidity lines
fig.add_hline(y=sl, line_dash="dash", line_color="#F6465D", line_width=2, annotation_text=f" SL {sl:.2f} ")
fig.add_hline(y=tp, line_dash="dash", line_color="#0ECB81", line_width=2, annotation_text=f" TP {tp:.2f} ")
fig.update_layout(height=650, xaxis_rangeslider_visible=False, template="plotly_dark", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11", legend=dict(orientation="h", y=1.02, x=0))
st.plotly_chart(fig, use_container_width=True)

# ================= RSI + MACD =================
c1,c2 = st.columns(2)
with c1:
    fr = go.Figure()
    fr.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#F0B90B', width=2.5), fill='tozeroy', name=f'RSI {rsi:.1f}'))
    fr.add_hline(y=70, line_dash="dash", line_color="#F6465D"); fr.add_hline(y=30, line_dash="dash", line_color="#0ECB81"); fr.add_hline(y=50, line_dash="dot", line_color="#848e9c")
    fr.update_layout(height=300, template="plotly_dark", title=f"RSI14 - {st.session_state.market} | Liq Sweep", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11")
    st.plotly_chart(fr, use_container_width=True)
with c2:
    fm = go.Figure()
    fm.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='#00D1FF', width=2), name='MACD'))
    fm.add_trace(go.Scatter(x=df.index, y=df['MACD_SIG'], line=dict(color='#FFA800', width=2), name='Signal'))
    fm.add_trace(go.Bar(x=df.index, y=df['MACD_HIST'], name='Hist', marker=dict(color=['#0ECB81' if v>=0 else '#F6465D' for v in df['MACD_HIST']])))
    fm.update_layout(height=300, template="plotly_dark", title=f"MACD 12,26,9 - {st.session_state.market}", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11")
    st.plotly_chart(fm, use_container_width=True)

# ================= FOOTER DETAIL =================
st.divider()
st.markdown(f"""
**💛 SONA AI - KING V71 ADVANCE DETAIL:**
- **Market:** {st.session_state.market} ({symbol}) | **TF:** {st.session_state.tf} | **Strategy:** {strat}
- **Price:** {price:.2f} | **EMA9:** {ema9:.2f} | **EMA21:** {ema21:.2f} | **EMA200:** {ema200:.2f} | **VWAP:** {vwap:.2f} | **RSI:** {rsi:.1f} | **ATR:** {atr:.4f}
- **SMC:** BOS Bull:{bos_bull} Bear:{bos_bear} | CHOCH Bull:{choch_bull} Bear:{choch_bear} | Sweep Buy:{sweep_buy} Sell:{sweep_sell} | Pull Buy:{pull_buy} Sell:{pull_sell} | OB Bull:{ob_bull} Bear:{ob_bear} | FVG Bull:{fvg_bull} Bear:{fvg_bear}
- **Signal:** {"BUY" if buy_logic else "SELL" if sell_logic else "WAIT"} | **SL:** {sl:.2f} | **TP:** {tp:.2f} | **RR:** 1:{abs(tp-price)/abs(price-sl):.2f}
- **Liquidity:** Straight detection via Swing High/Low sweep + Volume confirmation
""")

st.success(f"✅ SONA AI KING V71 Active | Click Market/TF to Change | Tol Indicator Auto Update | 5M Scalp Timer {mm:02d}:{ss:02d}")
