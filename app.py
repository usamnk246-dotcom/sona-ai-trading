import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI Trading", layout="wide")
st.title("💰 Sona AI Trading")

market = st.selectbox("Market Select Karo:", ["Gold", "EUR/USD", "BTC"])
map_t = {"Gold":"GC=F", "EUR/USD":"EURUSD=X", "BTC":"BTC-USD"}
ticker = map_t[market]

data = yf.download(ticker, period="1mo", interval="1d")
st.write(f"Live Price: {market}")

if not data.empty:
    fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
    fig.update_layout(xaxis_rangeslider_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    last = float(data['Close'].iloc[-1])
    sma = float(data['Close'].rolling(20).mean().iloc[-1])
    if last > sma:
        st.success(f"✅ BUY SIGNAL - Price {last:.2f} > SMA {sma:.2f}")
    else:
        st.error(f"❌ SELL SIGNAL - Price {last:.2f} < SMA {sma:.2f}")
    st.dataframe(data.tail())
else:
    st.error("Data loading...")
  
