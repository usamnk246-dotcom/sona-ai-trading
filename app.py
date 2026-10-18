import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI King V71 Pro", layout="wide")
st.title("👑 Sona AI King V71 - Pro Indicators")

markets = {
    "Gold XAUUSD": "GC=F",
    "Silver": "SI=F", 
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "US100": "^NDX",
    "US30": "^DJI"
}

st.sidebar.header("⚙️ Settings")
market_name = st.sidebar.selectbox("Market", list(markets.keys()))
timeframe = st.sidebar.selectbox("Timeframe", ["1m","5m","15m","30m","1h","4h","1d"])

# Indicator Settings
st.sidebar.divider()
st.sidebar.write("📊 Indicators")
ema9_len = 9
ema21_len = 21
ema200_len = 200
rsi_len = 14
atr_len = 14

sl_atr = st.sidebar.slider("SL ATR x", 0.5, 3.0, 1.5)
tp_atr = st.sidebar.slider("TP ATR x", 1.0, 5.0, 3.0)

symbol = markets[market_name]
tf_map = {
    "1m": ("1m","1d"), "5m": ("5m","5d"), "15m": ("15m","5d"),
    "30m": ("30m","1mo"), "1h": ("60m","1mo"), "4h": ("60m","3mo"), "1d": ("1d","1y")
}
interval, period = tf_map[timeframe]

@st.cache_data(ttl=60)
def load_data(sym, per, inter):
    df = yf.download(sym, period=per, interval=inter, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True)
    return df

df = load_data(symbol, period, interval)
if df.empty or len(df) < 210:
    st.error("Data kam hai, 1h ya 1d timeframe try karo")
    st.stop()

# --- EMA 9,21,200 ---
df['EMA9'] = df['Close'].ewm(span=9).mean()
df['EMA21'] = df['Close'].ewm(span=21).mean()
df['EMA200'] = df['Close'].ewm(span=200).mean()

# --- RSI 14 ---
delta = df['Close'].diff()
gain = delta.where(delta>0, 0).rolling(14).mean()
loss = -delta.where(delta<0, 0).rolling(14).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

# --- MACD 12,26,9 ---
ema12 = df['Close'].ewm(span=12).mean()
ema26 = df['Close'].ewm(span=26).mean()
df['MACD'] = ema12 - ema26
df['MACD_Signal'] = df['MACD'].ewm(span=9).mean()
df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']

# --- VWAP ---
df['TP'] = (df['High'] + df['Low'] + df['Close'])/3
df['TPV'] = df['TP'] * df['Volume']
df['VWAP'] = df['TPV'].cumsum() / df['Volume'].cumsum()
df['VWAP'].fillna(df['Close'].ewm(span=20).mean(), inplace=True)

# --- ATR 14 ---
df['H-L'] = df['High'] - df['Low']
df['H-PC'] = abs(df['High'] - df['Close'].shift(1))
df['L-PC'] = abs(df['Low'] - df['Close'].shift(1))
df['TR'] = df[['H-L','H-PC','L-PC']].max(axis=1)
df['ATR'] = df['TR'].rolling(14).mean()

last = df.iloc[-1]
price = float(last['Close'])
ema9 = float(last['EMA9'])
ema21 = float(last['EMA21'])
ema200 = float(last['EMA200'])
rsi = float(last['RSI'])
macd = float(last['MACD'])
macd_sig = float(last['MACD_Signal'])
vwap = float(last['VWAP'])
atr = float(last['ATR'])

# --- BUY/SELL Logic ---
# Buy: EMA9>EMA21, Price>EMA200, Price>VWAP, RSI 50-70, MACD>Signal
buy_cond = (ema9 > ema21) and (price > ema200) and (price > vwap) and (rsi > 50 and rsi < 72) and (macd > macd_sig)
sell_cond = (ema9 < ema21) and (price < ema200) and (price < vwap) and (rsi < 50 and rsi > 28) and (macd < macd_sig)

if buy_cond:
    signal = "🟢 STRONG BUY"
    sl = price - atr*sl_atr
    tp = price + atr*tp_atr
    sig_color = "green"
elif sell_cond:
    signal = "🔴 STRONG SELL"
    sl = price + atr*sl_atr
    tp = price - atr*tp_atr
    sig_color = "red"
else:
    signal = "⚪ WAIT"
    sl = price - atr*sl_atr
    tp = price + atr*tp_atr
    sig_color = "gray"

# --- Metrics ---
c1,c2,c3,c4,c5,c6 = st.columns(6)
c1.metric(market_name, f"{price:.2f}")
c2.metric("EMA9/21/200", f"{ema9:.1f} / {ema21:.1f} / {ema200:.1f}")
c3.metric("RSI14", f"{rsi:.1f}")
c4.metric(f"Signal", signal)
c5.metric("SL", f"{sl:.2f}")
c6.metric("TP", f"{tp:.2f}")

# --- Main Chart ---
fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="Price"))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA9'], line=dict(color='#00BFFF', width=1.5), name='EMA9'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA21'], line=dict(color='#FFA500', width=1.5), name='EMA21'))
fig.add_trace(go.Scatter(x=df.index, y=df['EMA200'], line=dict(color='#FF00FF', width=2), name='EMA200'))
fig.add_trace(go.Scatter(x=df.index, y=df['VWAP'], line=dict(color='yellow', width=1, dash='dot'), name='VWAP'))
fig.add_hline(y=sl, line_dash="dash", line_color="red", annotation_text=f"SL {sl:.2f}")
fig.add_hline(y=tp, line_dash="dash", line_color="green", annotation_text=f"TP {tp:.2f}")
fig.update_layout(height=650, xaxis_rangeslider_visible=False, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# --- RSI + MACD ---
colA, colB = st.columns(2)
with colA:
    fig_rsi = go.Figure()
    fig_rsi.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='yellow'), name='RSI14'))
    fig_rsi.add_hline(y=70, line_dash="dash", line_color="red")
    fig_rsi.add_hline(y=30, line_dash="dash", line_color="green")
    fig_rsi.update_layout(height=250, template="plotly_dark", title="RSI 14")
    st.plotly_chart(fig_rsi, use_container_width=True)
with colB:
    fig_macd = go.Figure()
    fig_macd.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='blue'), name='MACD'))
    fig_macd.add_trace(go.Scatter(x=df.index, y=df['MACD_Signal'], line=dict(color='orange'), name='Signal'))
    fig_macd.add_trace(go.Bar(x=df.index, y=df['MACD_Hist'], name='Hist'))
    fig_macd.update_layout(height=250, template="plotly_dark", title="MACD 12,26,9")
    st.plotly_chart(fig_macd, use_container_width=True)

st.caption(f"King V71 | EMA9:{ema9:.2f} EMA21:{ema21:.2f} EMA200:{ema200:.2f} | RSI:{rsi:.1f} MACD:{macd:.3f} VWAP:{vwap:.2f} ATR:{atr:.2f}")
