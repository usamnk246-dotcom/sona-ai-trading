import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

st.set_page_config(page_title="SONA AI x KING 103 - ALERT", layout="wide", page_icon="👑")

st.markdown("""
<style>
.stApp { background:#0E0E0E; color:#D1D4DC; }
.card { background:#1E222D; border-radius:12px; padding:16px; margin:8px 0; border:1px solid #2A2E39; }
.alert-box { background: linear-gradient(90deg, #FFD700, #FF8C00); color:black; padding:15px; border-radius:12px; text-align:center; font-weight:bold; animation: blink 1s infinite; }
@keyframes blink { 50% { opacity: 0.7; } }
</style>
""", unsafe_allow_html=True)

st.markdown('<p style="color:#8B8E9B; text-align:center;">| RSI14 | MACD | VWAP | ATR | BOS | CHOCH | Liquidity | OB | FVG | 5M Scalping</p>', unsafe_allow_html=True)

if 'market' not in st.session_state: st.session_state.market = "GOLD XAUUSD"
if 'tf' not in st.session_state: st.session_state.tf = "30m"
symbol_map = {"GOLD XAUUSD": "GC=F", "SILVER": "SI=F", "BTC/USD": "BTC-USD", "ETH/USD": "ETH-USD", "EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X", "US100": "^NDX", "US30": "^DJI"}

# MARKET SELECT
for m in ["GOLD XAUUSD","SILVER","BTC/USD","ETH/USD","EUR/USD","GBP/USD","US100","US30"]:
    label = f"✅ {m}" if st.session_state.market == m else m
    if st.button(label, key=f"m_{m}", use_container_width=True):
        st.session_state.market = m; st.rerun()

# TIMEFRAME
st.markdown('### ⏰ TIMEFRAME + STRATEGY - Click to Change')
for tf in ["1m","5m","15m","30m","1h","4h","1d"]:
    lab = f"✅ {tf}" if st.session_state.tf == tf else tf
    if st.button(lab, key=f"tf_{tf}"):
        st.session_state.tf = tf; st.rerun()

strategy = st.selectbox("Strategy", ["KING V71 SCALP 5M","KING V103 4/HR BOTH","KING V103 x SONA AI LINKED"], index=2)

@st.cache_data(ttl=60)
def get_full_data(symbol, tf):
    tf_map = {"1m":"1m","5m":"5m","15m":"15m","30m":"30m","1h":"60m","4h":"240m","1d":"1d"}
    period_map = {"1m":"1d","5m":"5d","15m":"5d","30m":"7d","60m":"1mo","240m":"3mo","1d":"6mo"}
    iv = tf_map.get(tf,"30m"); pr = period_map.get(iv,"7d")
    df = yf.download(symbol, period=pr, interval=iv, progress=False)
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df = df.dropna()
    df['EMA9'] = df['Close'].ewm(9).mean(); df['EMA21'] = df['Close'].ewm(21).mean(); df['EMA200'] = df['Close'].ewm(200).mean()
    typical = (df['High']+df['Low']+df['Close'])/3
    df['VWAP'] = (typical*df['Volume']).cumsum()/df['Volume'].cumsum()
    delta = df['Close'].diff(); gain = delta.where(delta>0,0).rolling(14).mean(); loss = -delta.where(delta<0,0).rolling(14).mean()
    rs = gain/loss; df['RSI'] = 100-(100/(1+rs))
    exp1 = df['Close'].ewm(12).mean(); exp2 = df['Close'].ewm(26).mean()
    df['MACD'] = exp1-exp2; df['MACD_SIGNAL']=df['MACD'].ewm(9).mean()
    df['ATR'] = (df['High']-df['Low']).rolling(14).mean()
    df['SwingHigh']=df['High'].rolling(20).max(); df['SwingLow']=df['Low'].rolling(20).min()
    df['BOS']=df['Close']>df['SwingHigh'].shift(1)
    df['LiqSweep']=(df['Low']<df['SwingLow'].shift(1))&(df['Close']>df['SwingLow'].shift(1))
    return df

df = get_full_data(symbol_map[st.session_state.market], st.session_state.tf)
if df is not None:
    last = df.iloc[-1]; price=float(last['Close']); ema9=float(last['EMA9']); ema21=float(last['EMA21']); ema200=float(last['EMA200'])
    vwap=float(last['VWAP']); rsi=float(last['RSI']); macd=float(last['MACD']); atr=float(last['ATR'])
    
    # SCORING - KING V103 x SONA AI LINKED
    score=0
    if price>ema9: score+=1
    if ema9>ema21: score+=1
    if price>ema200: score+=1
    if rsi>50: score+=1
    if macd>float(last['MACD_SIGNAL']): score+=1
    if price>vwap: score+=1
    if bool(last['BOS']): score+=1
    
    signal = "BUY" if score>=4 else "SELL" if score<=2 else "NEUTRAL"
    if bool(last['LiqSweep']) and bool(last['BOS']): signal = "STRONG BUY" if score>=4 else "STRONG SELL"
    
    change = price - float(df['Close'].iloc[-2])
    st.markdown(f'<div class="card"><p>💰 {st.session_state.market}</p><div style="font-size:42px; font-weight:bold;">{price:.2f}</div><span style="background:#184A2E; color:#00FF88; padding:4px 10px; border-radius:20px;">↑ {change:+.2f}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card"><p>📈 EMA 9/21/200</p><div style="font-size:28px;">{ema9:.1f} / {ema21:.1f} / {ema200:.1f}</div><span style="background:#184A2E; color:#00FF88; padding:4px 10px; border-radius:20px;">↑ Mixed</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card"><p>📊 RSI14 {rsi:.1f} | MACD {macd:.3f}</p><div style="font-size:32px;">VWAP {vwap:.2f}</div><span style="background:#184A2E; color:#00FF88; padding:4px 10px; border-radius:20px;">↑ ATR {atr:.3f}</span></div>', unsafe_allow_html=True)
    sl = price - atr*1.5; tp = price + atr*3
    st.markdown(f'<div class="card"><p>🛑 SL {sl:.2f}</p><div style="font-size:36px; color:#00E396;">TP {tp:.2f}</div><span style="background:#184A2E; color:#00FF88; padding:4px 10px; border-radius:20px;">↑ RR 1:2.0</span></div>', unsafe_allow_html=True)
    liq_text = "Sweep Detected" if bool(last['LiqSweep']) else "No Sweep"; bos_text = "BOS Confirmed" if bool(last['BOS']) else "No BOS"
    st.markdown(f'<div class="card"><p>💧 Liquidity</p><div style="font-size:32px;">{liq_text}</div><span style="background:#184A2E; color:#00FF88; padding:4px 10px; border-radius:20px;">↑ {bos_text}</span></div>', unsafe_allow_html=True)
    
    # ===== 🔔 KHAPEL ALERT - HAR KALA DA - NEW =====
    st.divider()
    st.markdown("### 🔔 KHAPEL ALERT - Har Kala Da - King 103")
    col1, col2 = st.columns(2)
    with col1:
        alert_on = st.toggle("🔔 Alert ON Karo", value=True)
    with col2:
        alert_type = st.selectbox("Alert Type", ["BUY/SELL Both", "Only BUY", "Only SELL", "STRONG Only"])
    
    alert_trigger = False
    if "BUY" in signal: alert_trigger = True if alert_type in ["BUY/SELL Both","Only BUY","STRONG Only" if "STRONG" in signal else "BUY/SELL Both"] else False
    if "SELL" in signal: alert_trigger = True if alert_type in ["BUY/SELL Both","Only SELL"] else False
    if "STRONG" in signal: alert_trigger = True
    
    if alert_trigger:
        st.markdown(f'<div class="alert-box">🚨 {signal} ALERT - {st.session_state.market} @ {price:.2f} - Score {score}/7 - KING 103 WAR</div>', unsafe_allow_html=True)
        if signal=="STRONG BUY": st.success(f"✅ STRONG BUY CONFIRMED - Entry {price:.2f} SL {sl:.2f} TP {tp:.2f}")
        elif signal=="STRONG SELL": st.error(f"▼ STRONG SELL CONFIRMED - Entry {price:.2f} SL {sl:.2f} TP {tp:.2f}")
    
    if alert_on and alert_trigger:
        st.balloons()
        st.components.v1.html(f"""
        <script>
        if (Notification.permission !== 'granted') {{ Notification.requestPermission(); }}
        if (Notification.permission === 'granted') {{
            new Notification('👑 {signal} - KING 103!', {{ body: '{st.session_state.market} {price:.2f} Score {score}/7 SL {sl:.2f} TP {tp:.2f}', icon: 'https://cdn-icons-png.flaticon.com/512/1828/1828884.png' }});
        }}
        </script>
        <audio autoplay loop><source src="https://www.soundjay.com/buttons/beep-07a.wav" type="audio/wav"></audio>
        <h3 style="color:#FFD700; text-align:center;">🔔 {signal} BAJA! - {price:.2f}</h3>
        """, height=150)
        st.toast(f"🔔 {signal} ALERT! {price:.2f}", icon="👑")
    elif alert_on:
        st.info(f"🔄 Auto Check ON hai - 60 sec me check hoga - Current: {signal} - {st.session_state.market}")
        time.sleep(60)
        st.rerun()
    else:
        st.warning("⚠️ Alert OFF hai - ON karo taake beep baje!")
    
    # CHART
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.6,0.2,0.2])
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name=st.session_state.market), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA9'], line=dict(color='#00BFFF'), name='EMA9'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA21'], line=dict(color='#FFA500'), name='EMA21'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA200'], line=dict(color='#FF00FF', width=2), name='EMA200'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['VWAP'], line=dict(color='#FFD700', dash='dot'), name='VWAP'), row=1, col=1)
    fig.add_hline(y=tp, line_dash="dash", line_color="#00E396", annotation_text=f"TP {tp:.2f}", row=1, col=1)
    fig.add_hline(y=sl, line_dash="dash", line_color="#FF4560", annotation_text=f"SL {sl:.2f}", row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#FFD700'), fill='tozeroy', name='RSI14'), row=2, col=1)
    fig.add_hline(y=70, line_dash="dash", line_color="#FF4560", row=2, col=1); fig.add_hline(y=30, line_dash="dash", line_color="#00E396", row=2, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD'], line=dict(color='#00BFFF'), name='MACD'), row=3, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD_SIGNAL'], line=dict(color='#FFA500'), name='Signal'), row=3, col=1)
    fig.update_layout(template="plotly_dark", height=900, showlegend=True, xaxis_rangeslider_visible=False, paper_bgcolor="#0E0E0E", plot_bgcolor="#0E0E0E")
    st.plotly_chart(fig, use_container_width=True)

st.caption("👑 KING 103 x SONA AI - Har Kala Alert - Munga Kor Wala - Peshawar")
