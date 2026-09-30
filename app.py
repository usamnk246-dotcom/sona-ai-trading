import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
st.title("Sona AI Trading")
m = st.selectbox("Market:",["Gold","Bitcoin","EUR/USD"])
t = {"Gold":"GC=F","Bitcoin":"BTC-USD","EUR/USD":"EURUSD=X"}[m]
d = yf.download(t, period="1d", interval="5m", auto_adjust=True)
if isinstance(d.columns, pd.MultiIndex):
    d.columns = d.columns.get_level_values(0)
d = d.dropna()
st.metric(m, float(d['Close'].iloc[-1]))
fig = go.Figure([go.Candlestick(x=d.index, open=d['Open'], high=d['High'], low=d['Low'], close=d['Close'])])
st.plotly_chart(fig)
