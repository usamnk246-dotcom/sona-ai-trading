import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="King V72 OLYMP SMC", layout="wide")

# === OLYMPTRADE ADVANCE CSS ===
st.markdown("""
<style>
.stApp { background: #0b0e11; }
.market-btn { background: #1e2329; border: 1px solid #474d57; color: #848e9c; padding: 8px 16px; border-radius: 20px; margin: 4px; }
.market-active { background: #f0b90b !important; color: #000 !important; font-weight: bold; border: 1px solid #f0b90b; }
.tf-btn { background: #2b3139; border-radius: 8px; padding: 6px 14px; color: #848e9c; border: none; }
.tf-active { background: #f0b90b; color: #000; font-weight: bold; }
.liquidity-tag { background: #7c3aed; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; }
.bos-tag { background: #0ecb81; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; }
.sweep-tag { background: #f6465d; color: white; padding: 4px 10px; border-radius: 12px; font-size: 12px; }
.timer-box { background: linear-gradient(90deg, #111827, #1f2937); border: 2px solid #f0b90b; padding: 10px; border-radius: 10px; text-align: center; color: #f0b90b; font-weight: bold; font-size: 20px; }
</style>
""", unsafe_allow_html=True)

# === SESSION STATE FOR OLYMP CLICK ===
if 'active_market' not in st.session_state: st.session_state.active_market = "GOLD XAUUSD"
if 'active_tf' not in st.session_state: st.session_state.active_tf = "1m"
if 'strategy' not in st.session_state: st.session_state.strategy = "SCALPING 5M"

markets = {"GOLD XAUUSD":"GC=F","SILVER":"SI=F","BTC/USD":"BTC-USD","ETH/USD":"ETH-USD","EUR/USD":"EURUSD=X","GBP/USD":"GBPUSD=X","US100":"^NDX"}
tf_list = ["1m","5m","15m","30m","1h","4h","1d"]
tf_map = {"1m":("1m","1d"),"5m":("5m","5d"),"15m":("15m","5d"),"30m":("30m","1mo"),"1h":("60m","1mo"),"4h":("60m","3mo"),"1d":("1d","1y")}

# === TOP OLYMP MARKET BUTTONS ===
st.markdown("<h3 style='color:#f0b90b; margin-bottom:0;'>👑 KING V72 • OLYMPTRADE PRO + SMC</h3>", unsafe_allow_html=True)
cols = st.columns(len(markets))
for i, (m_name) in enumerate(markets.keys()):
    if cols[i].button(m_name, key=f"m_{m_name}", use_container_width=True):
        st.session_state.active_market = m_name
        st.rerun()

# === TIMEFRAME BUTTONS LIKE OLYMP ===
st.write("")
tf_cols = st.columns(len(tf_list)+1)
for i, tf in enumerate(tf_list):
    label = f"✅ {tf}" if tf == st.session_state.active_tf else tf
    if tf_cols[i].button(label, key=f"tf_{tf}"):
        st.session_state.active_tf = tf
        st.rerun()

# Strategy selector
strat = tf_cols[-1].selectbox("Strategy", ["SCALPING 5M","LIQUIDITY SWEEP","BOS + PULLBACK","EMA CROSS"], index=0, label_visibility="collapsed")
st.session_state.strategy = strat

market_name = st.session_state.active_market
timeframe = st.session_state.active_tf
symbol = markets[market_name]
interval, period = tf_map[timeframe]

@st.cache_data(ttl=30)
def load_data(sym, per, inter):
    df = yf.download(sym, period=per, interval=inter, auto_adjust=True, progress=False)
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True)
    return df

df = load_data(symbol, period, interval)
if len(df) < 50: st.stop()

# === INDICATORS ===
df['EMA9'] = df['Close'].ewm(9).mean()
df['EMA21'] = df['Close'].ewm(21).mean()
df['EMA200'] = df['Close'].ewm(200).mean()
d = df['Close'].diff()
gain = d.where(d>0,0).rolling(14).mean()
loss = -d.where(d<0,0).rolling(14).mean()
df['RSI'] = 100 - (100/(1+gain/loss))
df['MACD'] = df['Close'].ewm(12).mean() - df['Close'].ewm(26).mean()
df['SIG'] = df['MACD'].ewm(9).mean()
df['TPp'] = (df['High']+df['Low']+df['Close'])/3
df['VWAP'] = (df['TPp']*df['Volume']).cumsum()/df['Volume'].cumsum()
df['VWAP'].fillna(df['EMA21'], inplace=True)
df['TR'] = pd.concat([df['High']-df['Low'], (df['High']-df['Close'].shift(1)).abs(), (df['Low']-df['Close'].shift(1)).abs()], axis=1).max(axis=1)
df['ATR'] = df['TR'].rolling(14).mean()

# === SMC LOGIC ===
# Swing High/Low
df['SwingHigh'] = df['High'].rolling(5, center=True).max()
df['SwingLow'] = df['Low'].rolling(5, center=True).min()

# BOS Detection
df['BOS_Bull'] = df['Close'] > df['SwingHigh'].shift(1)
df['BOS_Bear'] = df['Close'] < df['SwingLow'].shift(1)

# Liquidity Sweep (Wick exceeds prev high/low then close back)
df['Liq_Sweep_Buy'] = (df['Low'] < df['SwingLow'].shift(1)) & (df['Close'] > df['SwingLow'].shift(1))
df['Liq_Sweep_Sell'] = (df['High'] > df['SwingHigh'].shift(1)) & (df['Close'] < df['SwingHigh'].shift(1))

# Pullback to EMA21/VWAP
df['Pullback_Buy'] = (df['Low'] <= df['EMA21']) & (df['Close'] > df['EMA21']) & (df['EMA9'] > df['EMA21'])
df['Pullback_Sell'] = (df['High'] >= df['EMA21']) & (df['Close'] < df['EMA21']) & (df['EMA9'] < df['EMA21'])

L = df.iloc[-1]
price=float(L['Close']); ema9=float(L['EMA9']); ema21=float(L['EMA21']); ema200=float(L['EMA200']); rsi=float(L['RSI']); macd=float(L['MACD']); sig=float(L['SIG']); vwap=float(L['VWAP']); atr=float(L['ATR'])
bos_bull=bool(L['BOS_Bull']); bos_bear=bool(L['BOS_Bear']); sweep_buy=bool(L['Liq_Sweep_Buy']); sweep_sell=bool(L['Liq_Sweep_Sell']); pull_buy=bool(L['Pullback_Buy']); pull_sell=bool(L['Pullback_Sell'])

# === STRATEGY SIGNAL ===
if st.session_state.strategy == "SCALPING 5M":
    buy_logic = (ema9 > ema21) and (price > vwap) and (rsi > 50) and (pull_buy or sweep_buy)
    sell_logic = (ema9 < ema21) and (price < vwap) and (rsi < 50) and (pull_sell or sweep_sell)
elif st.session_state.strategy == "LIQUIDITY SWEEP":
    buy_logic = sweep_buy and (rsi < 40)
    sell_logic = sweep_sell and (rsi > 60)
elif st.session_state.strategy == "BOS + PULLBACK":
    buy_logic = bos_bull and pull_buy
    sell_logic = bos_bear and pull_sell
else:
    buy_logic = (ema9 > ema21) and (macd > sig) and (rsi > 50)
    sell_logic = (ema9 < ema21) and (macd < sig) and (rsi < 50)

if buy_logic:
    signal = f"🟢 BUY • {market_name} • {timeframe}"; sig_color="#0ecb81"; sl=price-atr*1.5; tp=price+atr*3
    st.markdown(f"<div style='background:{sig_color};padding:18px;border-radius:14px;text-align:center;color:white;font-size:26px;font-weight:900;'>{signal} • 5M EXPIRY</div>", unsafe_allow_html=True)
elif sell_logic:
    signal = f"🔴 SELL • {market_name} • {timeframe}"; sig_color="#f6465d"; sl=price+atr*1.5; tp=price-atr*3
    st.markdown(f"<div style='background:{sig_color};padding:18px;border-radius:14px;text-align:center;color:white;font-size:26px;font-weight:900;'>{signal} • 5M EXPIRY</div>", unsafe_allow_html=True)
else:
    signal = f"⚪ WAIT • {market_name}"; sl=price-atr*1.5; tp=price-atr*3
    st.markdown(f"<div style='background:#2b3139;padding:18px;border-radius:14px;text-align:center;color:#848e9c;font-size:22px;font-weight:700;'>{signal}</div>", unsafe_allow_html=True)

# === SMC TAGS + TIMER ===
c_tag1,c_tag2,c_tag3,c_tag4 = st.columns([1,1,1,1])
if bos_bull or bos_bear: c_tag1.markdown(f"<span class='bos-tag'>BOS {'BULL' if bos_bull else 'BEAR'}</span>", unsafe_allow_html=True)
if sweep_buy: c_tag2.markdown("<span class='sweep-tag'>LIQ SWEEP BUY 💧</span>", unsafe_allow_html=True)
if sweep_sell: c_tag2.markdown("<span class='sweep-tag'>LIQ SWEEP SELL 💧</span>", unsafe_allow_html=True)
if pull_buy or pull_sell: c_tag3.markdown(f"<span class='liquidity-tag'>PULLBACK {'BUY' if pull_buy else 'SELL'}</span>", unsafe_allow_html=True)

# 5 Min Timer
if 'timer_start' not in st.session_state: st.session_state.timer_start = datetime.now()
remaining = (st.session_state.timer_start + timedelta(minutes=5) - datetime.now())
if remaining.total_seconds() <= 0:
    st.session_state.timer_start = datetime.now()
    remaining = timedelta(minutes=5)
mins, secs = divmod(int(remaining.total_seconds()), 60)
c_tag4.markdown(f"<div class='timer-box'>⏱️ {mins:02d}:{secs:02d} / 5M</div>", unsafe_allow_html=True)

# === METRICS ===
m1,m2,m3,m4 = st.columns(4)
m1.metric(f"{market_name}", f"{price:.2f}")
m2.metric("EMA9/21/200", f"{ema9:.1f}/{ema21:.1f}/{ema200:.1f}")
m3.metric(f"RSI {rsi:.1f} | VWAP {vwap:.1f}", f"{'BOS' if bos_bull or bos_bear else 'No BOS'}")
m4.metric(f"SL {sl:.2f} / TP {tp:.2f}", f"ATR {atr:.2f}")

# === CHART WITH SMC ===
fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=market_name))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA9'], line=dict(color='#00D1FF', width=1.4), name='EMA9'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA21'], line=dict(color='#FFA800', width=1.4), name='EMA21'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA200'], line=dict(color='#FF00E6', width=2), name='EMA200'))
fig.add_trace(go.Scatter(x=df.index, y=df['VWAP'], line=dict(color='#F0B90B', dash='dot'), name='VWAP'))

# Mark Liquidity Sweeps
sweep_df = df[df['Liq_Sweep_Buy'] | df['Liq_Sweep_Sell']].tail(10)
fig.add_trace(go.Scatter(x=sweep_df.index, y=sweep_df['Low']-atr*0.2, mode='markers', marker=dict(symbol='triangle-up', size=12, color='#0ecb81'), name='Sweep Buy'))
fig.add_trace(go.Scatter(x=sweep_df.index, y=sweep_df['High']+atr*0.2, mode='markers', marker=dict(symbol='triangle-down', size=12, color='#f6465d'), name='Sweep Sell'))

fig.add_hline(y=sl, line_dash="dash", line_color="#F6465D", annotation_text=f"SL {sl:.2f}")
fig.add_hline(y=tp, line_dash="dash", line_color="#0ECB81", annotation_text=f"TP {tp:.2f}")
fig.update_layout(height=600, xaxis_rangeslider_visible=False, template="plotly_dark", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11", legend=dict(orientation="h", y=1.02))
st.plotly_chart(fig, use_container_width=True)

# === RSI + MACD ===
a,b = st.columns(2)
with a:
    fr=go.Figure(); fr.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#F0B90B', width=2.5), fill='tozeroy')); fr.add_hline(y=70, line_dash="dash", line_color="#F6465D"); fr.add_hline(y=30, line_dash="dash", line_color="#0ECB81"); fr.update_layout(height=280, template="plotly_dark", title=f"RSI 14 - {market_name} • Liq Level", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11"); st.plotly_chart(fr, use_container_width=True)
with b:
    fm=go.Figure(); fm.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='#00D1FF'))); fm.add_trace(go.Scatter(x=df.index, y=df['SIG'], line=dict(color='#FFA800'))); fm.add_trace(go.Bar(x=df.index, y=df['HIST'], marker_color=df['HIST'].apply(lambda x: '#0ECB81' if x>0 else '#F6465D'))); fm.update_layout(height=280, template="plotly_dark", title=f"MACD • {market_name}", paper_bgcolor="#0b0e11", plot_bgcolor="#0b0e11"); st.plotly_chart(fm, use_container_width=True)

st.caption(f"King V72 OLYMP SMC | Market:{market_name} TF:{timeframe} Strategy:{st.session_state.strategy} | Price:{price} EMA:{ema9:.1f}/{ema21:.1f} BOS:{bos_bull}/{bos_bear} Sweep:{sweep_buy}/{sweep_sell} Pull:{pull_buy}/{pull_sell}")
