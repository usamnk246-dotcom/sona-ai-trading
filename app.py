import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from ta.momentum import RSIIndicator

st.set_page_config(page_title="Wase AI Trading PRO", layout="wide")
st.markdown("<h1 style='text-align:center;color:gold'>🔥 Wase AI Trading PRO - Bhera</h1>", unsafe_allow_html=True)

market = st.selectbox("Market Select karo Wase sah:", ["Gold","Silver","Bitcoin","Oil","EUR/USD"])
symbols = {"Gold":"GC=F","Silver":"SI=F","Bitcoin":"BTC-USD","Oil":"CL=F","EUR/USD":"EURUSD=X"}
sym = symbols[market]

@st.cache_data(ttl=60)
def get_data(s):
    d = yf.download(s, period="5d", interval="15m")
    if isinstance(d.columns, pd.MultiIndex):
        d.columns = d.columns.get_level_values(0)
    return d.dropna()

data = get_data(sym)
price = float(data['Close'].iloc[-1])
ma20 = float(data['Close'].rolling(20).mean().iloc[-1])
ma50 = float(data['Close'].rolling(50).mean().iloc[-1])
rsi = float(RSIIndicator(data['Close']).rsi().iloc[-1])

col1,col2,col3,col4 = st.columns(4)
col1.metric(f"{market} Price", f"{price:.2f}")
col2.metric("MA 20", f"{ma20:.2f}")
col3.metric("MA 50", f"{ma50:.2f}")
col4.metric("RSI", f"{rsi:.1f}")

st.divider()

# BUY / SELL LOGIC ADVANCE
if price > ma20 and rsi < 70 and price > ma50:
    st.success(f"✅ STRONG BUY - Wase sah {market} UPAR jayega! Target: {price*1.01:.2f}")
    st.balloons()
    signal = "BUY"
elif price < ma20 and rsi > 30:
    st.error(f"❌ STRONG SELL - Wase sah {market} NEECHE ayega! Target: {price*0.99:.2f}")
    signal = "SELL"
else:
    st.warning(f"⚠️ WAIT - Wase sah Sideways hai, thoda sabar karo")
    signal = "WAIT"

# CHART MODERN
fig = go.Figure()
fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name="Price"))
fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(20).mean(), line=dict(color='orange',width=2), name="MA 20"))
fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(50).mean(), line=dict(color='blue',width=2), name="MA 50"))
fig.update_layout(height=500, template="plotly_dark", xaxis_rangeslider_visible=False)
st.plotly_chart(fig, use_container_width=True)

st.info(f"Signal: {signal} | RSI: {rsi:.1f} | Wase sah Bhera ka Sona AI Bot")
