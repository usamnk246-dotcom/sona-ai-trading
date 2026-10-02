import streamlit as st
import yfinance as yf
import urllib.parse

st.set_page_config(page_title="Wase Sah Bhera PRO", layout="wide")
st.title("🔥 WASE SAH BHERA GOLD PRO 🔥")

SYMBOL="GC=F"
data=yf.download(SYMBOL, period="5d", interval="5m")
price=float(data['Close'].iloc[-1])
data['EMA9']=data['Close'].ewm(span=9).mean()
data['EMA21']=data['Close'].ewm(span=21).mean()
signal="STRONG BUY" if data['EMA9'].iloc[-1] > data['EMA21'].iloc[-1] else "STRONG SELL"

st.metric("Gold Price", f"${price:.2f}")
st.markdown(f"## {signal}")
st.line_chart(data['Close'])

st.divider()
st.subheader("📲 WhatsApp Alert Bhejo")
wa_number=st.text_input("Apna WhatsApp Number (92 se start)", "923XXXXXXXXX")
if wa_number:
    msg=f"Wase Sah Alert Gold ${price:.2f} - {signal} https://l6sj.streamlit.app"
    link=f"https://wa.me/{wa_number}?text={urllib.parse.quote(msg)}"
    st.link_button("🚀 WhatsApp Pe Bhejo", link, use_container_width=True)
