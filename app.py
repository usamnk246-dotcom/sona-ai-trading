import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="Wase AI Trading PRO - Bhera", layout="wide", page_icon="🔥")

st.markdown("""
<style>
.big-signal {font-size: 45px; font-weight: 900; text-align: center; padding: 25px; border-radius: 20px; margin: 20px 0;}
.buy {background: linear-gradient(135deg, #00c853, #009624); color: white; animation: pulse 1.5s infinite;}
.sell {background: linear-gradient(135deg, #ff1744, #d50000); color: white; animation: pulse 1.5s infinite;}
@keyframes pulse {0%{transform:scale(1)} 50%{transform:scale(1.05)} 100%{transform:scale(1)}}
.price-box {background: #111; padding: 15px; border-radius: 15px; text-align: center; border: 2px solid gold;}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Wase AI Trading PRO - Bhera Next Level")
st.caption("Gold | Silver | BTC | Oil - Live AI Signals")

# Sidebar - Next Level
asset = st.sidebar.selectbox("Asset Chunoo Wase sah:", ["Gold (GC=F)", "Silver (SI=F)", "Bitcoin (BTC-USD)", "Oil (CL=F)"])
tola = st.sidebar.number_input("Kitna Tola / Quantity?", value=1.0)

# Live Data
symbol = asset.split("(")[1].replace(")","")
data = yf.download(symbol, period="1mo", interval="1h")
if len(data) == 0:
    st.error("Net check ka Wase sah!")
    st.stop()

close = data['Close'].squeeze()
price = float(close.iloc[-1])
ma20 = float(close.rolling(20).mean().iloc[-1])
ma50 = float(close.rolling(50).mean().iloc[-1])
rsi = float(ta.momentum.RSIIndicator(close).rsi().iloc[-1])

# Signal Logic - Next Level
if price > ma20 and price > ma50 and rsi < 70:
    signal, cls, msg = "🚀 STRONG BUY", "buy", "Wase sah UP jayega! Kharido!"
elif price < ma20 and price < ma50 and rsi > 30:
    signal, cls, msg = "🔻 STRONG SELL", "sell", "Wase sah NEECHE ayega! Becho!"
else:
    signal, cls, msg = "⏸️ WAIT", "sell", "Wase sah Thora Wait Karo!"

# Display
c1, c2, c3, c4 = st.columns(4)
c1.markdown(f'<div class="price-box"><h3>Price</h3><h2>${price:.2f}</h2></div>', unsafe_allow_html=True)
c2.markdown(f'<div class="price-box"><h3>MA20</h3><h2>${ma20:.2f}</h2></div>', unsafe_allow_html=True)
c3.markdown(f'<div class="price-box"><h3>MA50</h3><h2>${ma50:.2f}</h2></div>', unsafe_allow_html=True)
c4.markdown(f'<div class="price-box"><h3>RSI</h3><h2>{rsi:.1f}</h2></div>', unsafe_allow_html=True)

st.markdown(f'<div class="big-signal {cls}">{signal}<br><span style="font-size:20px">{msg}</span></div>', unsafe_allow_html=True)

st.line_chart(data['Close'])

# Bhera Profit Calculator
st.divider()
st.subheader(f"💰 Bhera Profit Calculator - {tola} Tola ka")
buy_price = st.number_input("Kharidne ka Rate?", value=price)
profit = (price - buy_price) * tola * 11.66 # 1 tola = 11.66g approx for Gold calc
st.metric(f"{tola} Tola ka Munafa / Nuqsan", f"${profit:.2f} | Rs {profit*280:.0f}")

st.success(f"Wase sah App Next Level pe hai! Link: l6sj.streamlit.app")
# --- WASE SAH WHATSAPP ALERT ---
st.divider()
st.subheader("📲 WhatsApp Alert Bhejo")
wa_number = st.text_input("Apna WhatsApp Number (92 se start)", "92XXXXXXXXXX")
alert_text = f"WASE SAH ALERT: {SYMBOL} {last_price:.2f} - {signal}! https://l6sj.streamlit.app"
wa_link = f"https://wa.me/{wa_number}?text={alert_text.replace(' ', '%20')}"
st.link_button("🚀 WhatsApp Pe Alert Bhejo", wa_link)
if "STRONG" in signal:
    st.toast(f"🚨 {signal} - WhatsApp Alert Ready!", icon="📲")
