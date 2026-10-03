import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go

st.set_page_config(page_title="Wase AI PRO MAX V2", layout="centered")
st_autorefresh(interval=60000, key="refresh")

st.markdown("<h1 style='text-align:center;color:#FFD700;'>🔥 Wase AI PRO MAX V2 - Chart + History</h1>", unsafe_allow_html=True)

def get_data_and_signal(symbol):
    try:
        data = yf.Ticker(symbol).history(period="1d", interval="5m")
        price = data['Close'].iloc[-1]
        # Simple RSI logic
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        last_rsi = rsi.iloc[-1]
        
        if last_rsi > 70:
            signal, color = "SELL", "#FFCDD2"
            target = price * 0.995
            sl = price * 1.002
        elif last_rsi < 30:
            signal, color = "BUY", "#C8E6C9"
            target = price * 1.005
            sl = price * 0.998
        else:
            signal, color = "WAIT", "#FFF9C4"
            target = price
            sl = price
        return price, signal, color, target, sl, data, last_rsi
    except:
        return 0, "WAIT", "#FFF9C4", 0, 0, pd.DataFrame(), 50

# --- GOLD ---
gold_price, gold_sig, gold_color, gold_tgt, gold_sl, gold_data, gold_rsi = get_data_and_signal("GC=F")
st.markdown(f"<div style='background:{gold_color};padding:20px;border-radius:20px;text-align:center;'><h2>GOLD ${gold_price:.2f}</h2><h1 style='color:{'red' if gold_sig=='SELL' else 'green' if gold_sig=='BUY' else '#B8860B'}'>{gold_sig} {'🔴' if gold_sig=='SELL' else '🟢' if gold_sig=='BUY' else '🟡'}</h1><p>Target: ${gold_tgt:.2f} | SL: ${gold_sl:.2f} | RSI: {gold_rsi:.1f}</p></div>", unsafe_allow_html=True)

if not gold_data.empty:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data['Close'], name="GOLD", line=dict(color="gold", width=3)))
    fig.add_hline(y=gold_tgt, line_dash="dash", line_color="green", annotation_text="Target")
    fig.add_hline(y=gold_sl, line_dash="dash", line_color="red", annotation_text="SL")
    fig.update_layout(height=300, margin=dict(l=0,r=0,t=30,b=0), template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

st.write("---")

# --- BTC ---
btc_price, btc_sig, btc_color, btc_tgt, btc_sl, btc_data, btc_rsi = get_data_and_signal("BTC-USD")
st.markdown(f"<div style='background:{btc_color};padding:20px;border-radius:20px;text-align:center;'><h2>BTC ${btc_price:.2f}</h2><h1 style='color:{'red' if btc_sig=='SELL' else 'green' if btc_sig=='BUY' else '#B8860B'}'>{btc_sig} {'🔴' if btc_sig=='SELL' else '🟢' if btc_sig=='BUY' else '🟡'}</h1><p>Target: ${btc_tgt:.2f} | SL: ${btc_sl:.2f} | RSI: {btc_rsi:.1f}</p></div>", unsafe_allow_html=True)

if not btc_data.empty:
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=btc_data.index, y=btc_data['Close'], name="BTC", line=dict(color="orange", width=3)))
    fig2.update_layout(height=300, margin=dict(l=0,r=0,t=30,b=0), template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

# --- HISTORY TABLE ---
st.subheader("📜 Last Signals History (Today)")
history = pd.DataFrame({
    "Time": gold_data.index[-5:].strftime("%H:%M") if not gold_data.empty else [],
    "GOLD Price": gold_data['Close'].tail(5).round(2).values if not gold_data.empty else [],
    "Signal": [gold_sig]*5
})
st.table(history)
st.caption("Auto-refresh every 60 sec | Wase AI PRO MAX V2")
