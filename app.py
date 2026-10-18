import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="Sona AI King V71 Pro", layout="wide", initial_sidebar_state="expanded")

# === ADVANCE DARK KING CSS ===
st.markdown("""
<style>
.stApp { background: #0b0e11; color: #eaecef; }
h1, h2, h3 { color: #f0b90b !important; }
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e2329 0%, #2b3139 100%);
    padding: 15px; border-radius: 12px; border: 1px solid #474d57;
}
.signal-box-buy {
    background: linear-gradient(90deg, #02c076 0%, #0ecb81 100%);
    color: white; padding: 18px; border-radius: 14px; text-align: center;
    font-size: 26px; font-weight: 800; box-shadow: 0 0 20px #0ecb81;
    animation: pulse 2s infinite;
}
.signal-box-sell {
    background: linear-gradient(90deg, #cf304a 0%, #f6465d 100%);
    color: white; padding: 18px; border-radius: 14px; text-align: center;
    font-size: 26px; font-weight: 800; box-shadow: 0 0 20px #f6465d;
    animation: pulse 2s infinite;
}
.signal-box-wait {
    background: #2b3139; color: #848e9c; padding: 18px; border-radius: 14px;
    text-align: center; font-size: 22px; font-weight: 700; border: 1px solid #474d57;
}
@keyframes pulse { 0%{opacity:1} 50%{opacity:0.8} 100%{opacity:1} }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>👑 SONA AI • KING V71 ADVANCE</h1><p style='text-align:center; color:#848e9c;'>EMA 9/21/200 • RSI14 • MACD • VWAP • ATR • Auto SL/TP</p>", unsafe_allow_html=True)

markets = {"GOLD XAUUSD":"GC=F","SILVER":"SI=F","BTC/USD":"BTC-USD","ETH/USD":"ETH-USD","EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","US100":"^NDX"}
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/138/138292.png", width=60)
    st.markdown("### 👑 KING V71 CONTROL")
    market_name = st.selectbox("🎯 MARKET", list(markets.keys()), index=0)
    timeframe = st.select_slider("⏰ TIMEFRAME", options=["1m","5m","15m","30m","1h","4h","1d"], value="1m")
    st.divider()
    sl_atr = st.slider("🛑 SL ATR x", 0.5, 3.0, 1.5, 0.1)
    tp_atr = st.slider("🎯 TP ATR x", 1.0, 5.0, 3.0, 0.1)
    st.markdown(f"<p style='color:#f0b90b;'>Active: {market_name} | TF: {timeframe}</p>", unsafe_allow_html=True)

tf_map = {"1m":("1m","1d"),"5m":("5m","5d"),"15m":("15m","5d"),"30m":("30m","1mo"),"1h":("60m","1mo"),"4h":("60m","3mo"),"1d":("1d","1y")}
interval, period = tf_map[timeframe]
symbol = markets[market_name]

@st.cache_data(ttl=45)
def get_data(sym, per, inter):
    df = yf.download(sym, period=per, interval=inter, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True)
    return df

df = get_data(symbol, period, interval)
if len(df) < 205:
    st.warning("Data kam hai - 15m, 1h ya 1d try karo")
    st.stop()

# === INDICATORS ===
df['EMA9'] = df['Close'].ewm(span=9).mean()
df['EMA21'] = df['Close'].ewm(span=21).mean()
df['EMA200'] = df['Close'].ewm(span=200).mean()
d = df['Close'].diff()
gain = d.where(d>0,0).rolling(14).mean()
loss = -d.where(d<0,0).rolling(14).mean()
df['RSI'] = 100 - (100/(1+gain/loss))
df['MACD'] = df['Close'].ewm(12).mean() - df['Close'].ewm(26).mean()
df['MACD_SIG'] = df['MACD'].ewm(9).mean()
df['HIST'] = df['MACD'] - df['MACD_SIG']
df['TPp'] = (df['High']+df['Low']+df['Close'])/3
df['VWAP'] = (df['TPp']*df['Volume']).cumsum() / df['Volume'].cumsum()
df['VWAP'].fillna(df['Close'].ewm(20).mean(), inplace=True)
df['TR'] = pd.concat([df['High']-df['Low'], (df['High']-df['Close'].shift(1)).abs(), (df['Low']-df['Close'].shift(1)).abs()], axis=1).max(axis=1)
df['ATR'] = df['TR'].rolling(14).mean()

L = df.iloc[-1]
price=float(L['Close']); ema9=float(L['EMA9']); ema21=float(L['EMA21']); ema200=float(L['EMA200']); rsi=float(L['RSI']); macd=float(L['MACD']); sig=float(L['MACD_SIG']); vwap=float(L['VWAP']); atr=float(L['ATR'])

# === LOGIC - SINGLE MARKET ===
buy = (ema9 > ema21) and (price > ema200) and (price > vwap) and (50 < rsi < 72) and (macd > sig)
sell = (ema9 < ema21) and (price < ema200) and (price < vwap) and (28 < rsi < 50) and (macd < sig)

if buy:
    signal_html = f"<div class='signal-box-buy'>🟢 BUY NOW • {market_name} • {timeframe} • RSI {rsi:.1f}</div>"
    sl = price - atr*sl_atr; tp = price + atr*tp_atr
elif sell:
    signal_html = f"<div class='signal-box-sell'>🔴 SELL NOW • {market_name} • {timeframe} • RSI {rsi:.1f}</div>"
    sl = price + atr*sl_atr; tp = price - atr*tp_atr
else:
    signal_html = f"<div class='signal-box-wait'>⚪ WAIT • {market_name} • {timeframe} • No Confirmation</div>"
    sl = price - atr*sl_atr; tp = price + atr*tp_atr

st.markdown(signal_html, unsafe_allow_html=True)
st.write("")

# === METRICS - SINGLE MARKET ONLY ===
m1,m2,m3,m4,m5 = st.columns(5)
m1.metric(f"💰 {market_name}", f"{price:.2f}", f"{(price - float(df.iloc[-2]['Close'])):.2f}")
m2.metric("📈 EMA 9/21/200", f"{ema9:.1f} / {ema21:.1f} / {ema200:.1f}")
m3.metric("📊 RSI14", f"{rsi:.1f}", "BUY ZONE" if 50<rsi<70 else "SELL ZONE" if 30<rsi<50 else "EXTREME")
m4.metric("🛑 SL", f"{sl:.2f}", f"-{abs(price-sl):.2f}")
m5.metric("🎯 TP", f"{tp:.2f}", f"+{abs(tp-price):.2f}")

# === ADVANCE CHART ===
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=f"{market_name}"))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA9'], line=dict(color='#00D1FF', width=1.6), name='EMA 9'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA21'], line=dict(color='#FFA800', width=1.6), name='EMA 21'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA200'], line=dict(color='#FF00E6', width=2.4), name='EMA 200'))
fig.add_trace(go.Scatter(x=df.index, y=df['VWAP'], line=dict(color='#F0B90B', width=1.2, dash='dot'), name='VWAP'))
fig.add_hline(y=sl, line_dash="dash", line_color="#F6465D", line_width=2, annotation_text=f" SL {sl:.2f} ")
fig.add_hline(y=tp, line_dash="dash", line_color="#0ECB81", line_width=2, annotation_text=f" TP {tp:.2f} ")
fig.update_layout(height=620, xaxis_rangeslider_visible=False, template="plotly_dark", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11", legend=dict(orientation="h", y=1.02), margin=dict(l=10,r=10,t=30,b=10), title=f"{market_name} • {timeframe} • VWAP {vwap:.2f} • ATR {atr:.2f}")
st.plotly_chart(fig, use_container_width=True)

# === RSI + MACD ===
c1,c2 = st.columns(2)
with c1:
    fr=go.Figure()
    fr.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#F0B90B', width=2.5), fill='tozeroy', name=f'RSI {rsi:.1f}'))
    fr.add_hline(y=70, line_dash="dash", line_color="#F6465D"); fr.add_hline(y=30, line_dash="dash", line_color="#0ECB81")
    fr.update_layout(height=300, template="plotly_dark", title=f"RSI 14 - {market_name} {timeframe}", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11")
    st.plotly_chart(fr, use_container_width=True)
with c2:
    fm=go.Figure()
    fm.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='#00D1FF', width=2), name='MACD'))
    fm.add_trace(go.Scatter(x=df.index, y=df['MACD_SIG'], line=dict(color='#FFA800', width=2), name='Signal'))
    fm.add_trace(go.Bar(x=df.index, y=df['HIST'], name='Hist', marker_color=df['HIST'].apply(lambda x: '#0ECB81' if x>0 else '#F6465D')))
    fm.update_layout(height=300, template="plotly_dark", title=f"MACD 12,26,9 - {market_name} {timeframe}", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11")
    st.plotly_chart(fm, use_container_width=True)

st.caption(f"👑 King V71 Advance | {market_name}={symbol} | TF:{timeframe}({interval}) | Price:{price:.2f} EMA9:{ema9:.2f} EMA21:{ema21:.2f} EMA200:{ema200:.2f} RSI:{rsi:.1f} MACD:{macd:.3f} VWAP:{vwap:.2f} ATR:{atr:.3f} | Signal Updates Every 45s")
