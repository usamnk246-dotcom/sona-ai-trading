import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Wase AI PRO MAX", page_icon="🔥")
st_autorefresh(interval=30000, key="refresh") # 30 sec auto refresh

st.markdown("<h1 style='text-align:center; color:gold;'>🔥 Wase AI PRO MAX - Next Level</h1>", unsafe_allow_html=True)

def get_signal(symbol, name):
    data = yf.download(symbol, period="5d", interval="30m", progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data['MA20'] = data['Close'].rolling(20).mean()
    data['MA50'] = data['Close'].rolling(50).mean()
    
    price = float(data['Close'].iloc[-1])
    ma20 = float(data['MA20'].iloc[-1])
    ma50 = float(data['MA50'].iloc[-1])

    if price > ma20 and ma20 > ma50:
        signal = "BUY 🟢"; color="green"; bg="#d4edda"
        target = price * 1.005; sl = price * 0.998
    elif price < ma20 and ma20 < ma50:
        signal = "SELL 🔴"; color="red"; bg="#f8d7da"
        target = price * 0.995; sl = price * 1.002
    else:
        signal = "WAIT 🟡"; color="#856404"; bg="#fff3cd"
        target = price; sl = price

    return price, signal, color, bg, target, sl

col1, col2 = st.columns(2)

with col1:
    p, s, c, bg, tgt, sl = get_signal("GC=F", "Gold")
    st.markdown(f"<div style='text-align:center; background:{bg}; padding:20px; border-radius:15px;'><h3>GOLD ${p:.2f}</h3><h1 style='color:{c}'>{s}</h1><p>Target: ${tgt:.2f}<br>SL: ${sl:.2f}</p></div>", unsafe_allow_html=True)

with col2:
    p, s, c, bg, tgt, sl = get_signal("BTC-USD", "Bitcoin")
    st.markdown(f"<div style='text-align:center; background:{bg}; padding:20px; border-radius:15px;'><h3>BTC ${p:.2f}</h3><h1 style='color:{c}'>{s}</h1><p>Target: ${tgt:.2f}<br>SL: ${sl:.2f}</p></div>", unsafe_allow_html=True)

st.success("Wase sah - Auto Refresh ON hai (30 sec) - Alert system next step me lagayenge!")
