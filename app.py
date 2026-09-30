import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI Trading", page_icon="💰")
st.title("💰 Sona AI Trading")

market = st.selectbox("Market Select Karo:", ["Gold", "Bitcoin", "EUR/USD"])
map_t = {"Gold":"GC=F", "Bitcoin":"BTC-USD", "EUR/USD":"EURUSD=X"}
ticker = map_t[market]

st.write(f"Live Price: {market}")

try:
    data = yf.download(ticker, period="1d", interval="5m", progress=False, auto_adjust=True)
    if data.empty:
        st.warning("Data nahi mila - Refresh karo")
    else:
        close_price = data['Close'].iloc[-1]
        if hasattr(close_price, '__len__'):
            close_price = float(close_price.iloc[0])
        else:
            close_price = float(close_price)

        st.metric(market, f"{close_price:.2f}")

        fig = go.Figure(data=[go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])])
        fig.update_layout(xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
        st.success("✅ App Fixed!")
except Exception as e:
    st.error(f"Error: {e}")
