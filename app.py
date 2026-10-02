import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="WASE SAH BHERA GOLD PRO", page_icon="🔥")
st.title("🔥 WASE SAH BHERA GOLD PRO 🔥")

SYMBOL="GC=F"

# Gold Data Download
data=yf.download(SYMBOL, period="5d", interval="5m", auto_adjust=True)

if data.empty:
    st.error("Market band hai Wase sah")
    st.stop()

# Wase sah ye naya fix hai yfinance ke liye
close_col = data['Close']
if isinstance(close_col, pd.DataFrame):
    close_col = close_col.squeeze()

price = float(close_col.iloc[-1])
st.metric("Gold Price (GC=F)", f"${price:.2f}")

data['EMA9']=close_col.ewm(span=9).mean()
data['EMA21']=close_col.ewm(span=21).mean()

# Signal
if data['EMA9'].iloc[-1] > data['EMA21'].iloc[-1]:
    signal="STRONG BUY"
    color="green"
else:
    signal="STRONG SELL"
    color="red"

st.markdown(f"<h2 style='color:{color}'>Signal: {signal} Wase sah</h2>", unsafe_allow_html=True)

st.line_chart(data[['EMA9','EMA21']])
st.dataframe(data.tail())
st.success("Wase sah Bhera Gold Pro Running ✅")
