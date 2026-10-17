import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI + King V71", layout="wide")
st.title("👑 Sona AI Trading - King V71")

markets = {
    "Gold (XAUUSD)": "GC=F",
    "Silver": "SI=F",
    "BTC": "BTC-USD",
    "EURUSD": "EURUSD=X",
    "GBPUSD": "GBPUSD=X",
    "US100 (Nasdaq)": "^NDX"
}

st.sidebar.header("Settings")
market_name = st.sidebar.selectbox("Market Select", list(markets.keys()))
timeframe = st.sidebar.selectbox("Timeframe", ["1m","5m","15m","1h","4h","1d"])
rsi_period = st.sidebar.slider("RSI Period", 7, 21, 14)
ema_fast = st.sidebar.slider("EMA Fast", 10, 50, 20)
ema_slow = st.sidebar.slider("EMA Slow", 50, 250, 50)
ema_long = st.sidebar.slider("EMA Long", 100, 300, 200)
atr_mult_sl = st.sidebar.slider("SL ATR x", 0.5, 3.0, 1.5)
atr_mult_tp = st.sidebar.slider("TP ATR x", 0.5, 5.0, 3.0)

symbol = markets[market_name]
tf_map = {
    "1m": ("1m", "1d"),
    "5m": ("5m", "5d"),
    "15m": ("15m", "5d"),
    "1h": ("60m", "1mo"),
    "4h": ("60m", "1mo"),
    "1d": ("1d", "1y")
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

df[f'EMA{ema_fast}'] = df['Close'].ewm(span=ema_fast).mean()
df[f'EMA{ema_slow}'] = df['Close'].ewm(span=ema_slow).mean()
df[f'EMA{ema_long}'] = df['Close'].ewm(span=ema_long).mean()

delta = df['Close'].diff()
gain = delta.where(delta>0, 0).rolling(rsi_period).mean()
loss = -delta.where(delta<0, 0).rolling(rsi_period).mean()
rs = gain / loss
df['RSI'] = 100 - (100 / (1 + rs))

df['H-L'] = df['High'] - df['Low']
df['H-PC'] = abs(df['High'] - df['Close'].shift(1))
df['L-PC'] = abs(df['Low'] - df['Close'].shift(1))
df['TR'] = df[['H-L','H-PC','L-PC']].max(axis=1)
df['ATR'] = df['TR'].rolling(14).mean()

last = df.iloc[-1]
price = float(last['Close'])
rsi = float(last['RSI'])
atr = float(last['ATR'])
ema_f = float(last[f'EMA{ema_fast}'])
ema_s = float(last[f'EMA{ema_slow}'])
ema_l = float(last[f'EMA{ema_long}'])

buy_cond = (ema_f > ema_s) and (rsi > 50 and rsi < 70) and (price > ema_l)
sell_cond = (ema_f < ema_s) and (rsi < 50 and rsi > 30) and (price < ema_l)

if buy_cond:
    signal = "🟢 STRONG BUY"
    sl = price - atr*atr_mult_sl
    tp = price + atr*atr_mult_tp
elif sell_cond:
    signal = "🔴 STRONG SELL"
    sl = price + atr*atr_mult_sl
    tp = price - atr*atr_mult_tp
else:
    signal = "⚪ WAIT / NEUTRAL"
    sl = price - atr*atr_mult_sl
    tp = price + atr*atr_mult_tp

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric(market_name, f"{price:.2f}")
c2.metric("RSI", f"{rsi:.1f}")
c3.metric("Signal", signal)
c4.metric("SL", f"{sl:.2f}")
c5.metric("TP", f"{tp:.2f}")

fig = go.Figure()
fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name="Price"))
fig.add_trace(go.Scatter(x=df.index, y=df[f'EMA{ema_fast}'], line=dict(color='blue', width=1), name=f'EMA{ema_fast}'))
fig.add_trace(go.Scatter(x=df.index, y=df[f'EMA{ema_slow}'], line=dict(color='orange', width=1), name=f'EMA{ema_slow}'))
fig.add_trace(go.Scatter(x=df.index, y=df[f'EMA{ema_long}'], line=dict(color='purple', width=1), name=f'EMA{ema_long}'))
fig.add_hline(y=sl, line_dash="dash", line_color="red", annotation_text=f"SL {sl:.2f}")
fig.add_hline(y=tp, line_dash="dash", line_color="green", annotation_text=f"TP {tp:.2f}")
fig.update_layout(height=600, xaxis_rangeslider_visible=False, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df.index, y=df['RSI'], name="RSI", line=dict(color='yellow')))
fig2.add_hline(y=70, line_dash="dash", line_color="red")
fig2.add_hline(y=30, line_dash="dash", line_color="green")
fig2.update_layout(height=200, template="plotly_dark", title="RSI")
st.plotly_chart(fig2, use_container_width=True)
