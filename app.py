import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="L6SJ CLEAR", layout="wide", page_icon="🏅")

# --- CLEAR DESIGN - BRIGHT ---
st.markdown("""
<style>
.stApp{background:#0a0e1a !important;}
[data-testid="stMetricValue"]{color:white !important; font-size:28px !important; font-weight:900 !important;}
[data-testid="stMetricLabel"]{color:#FFD700 !important; font-weight:700 !important;}
p, span, div{color:#e0e0e0 !important;}
h1,h2,h3{color:#FFD700 !important;}
.stCaption{color:#aaaaaa !important;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#FFD700; font-size:32px;'>🏅 L6SJ GOLD AI V8.3 - CLEAR HD</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FFD700; font-size:12px;'>✨ CLEAR VIEW • 15M • 5M • 1M • RSI 70/30 • EMA • MACD • ATR • SCORE • QUALITY 95%</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🤖 AUTO")
    auto = st.toggle("Auto Trading ON", False)
    min_q = st.slider("Min Quality", 60,95,80)
    if auto: st.success("✅ AUTO ACTIVE")
    else: st.warning("⏸️ AUTO OFF")

@st.cache_data(ttl=30)
def get_tf(tf):
    df = yf.download("GC=F", period="2d", interval=tf, progress=False)
    if df.empty: return None
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    c,h,l = df['Close'], df['High'], df['Low']
    price=float(c.iloc[-1])
    ema9=float(ta.trend.ema_indicator(c,9).iloc[-1])
    ema21=float(ta.trend.ema_indicator(c,21).iloc[-1])
    ema50=float(ta.trend.ema_indicator(c,50).iloc[-1])
    rsi=float(ta.momentum.rsi(c,14).iloc[-1])
    macd=float(ta.trend.macd(c).iloc[-1])
    sig=float(ta.trend.macd_signal(c).iloc[-1])
    hist=float(ta.trend.macd_diff(c).iloc[-1])
    atr=float(ta.volatility.average_true_range(h,l,c,14).iloc[-1])
    sc=0
    if price>ema9: sc+=1
    if ema9>ema21: sc+=1
    if ema21>ema50: sc+=1
    if rsi>50: sc+=1
    if macd>sig: sc+=1
    signal="BUY" if sc>=3 else "SELL"
    rsi_state="OVERBOUGHT 🔴" if rsi>=70 else "OVERSOLD 🟢" if rsi<=30 else "NEUTRAL ⚪"
    return {"p":price,"e9":ema9,"e21":ema21,"e50":ema50,"rsi":rsi,"rsi_s":rsi_state,"m":macd,"ms":sig,"mh":hist,"atr":atr,"sc":sc,"sig":signal}

d15=get_tf("15m"); d5=get_tf("5m"); d1=get_tf("1m")

if d15 and d5 and d1:
    buy=sum(1 for x in [d15,d5,d1] if x['sig']=="BUY")
    avg_rsi=(d15['rsi']+d5['rsi']+d1['rsi'])/3
    avg_sc=(d15['sc']+d5['sc']+d1['sc'])/3
    avg_atr=(d15['atr']+d5['atr']+d1['atr'])/3
    quality=min(max(buy,3-buy)*25 + 10 + (15 if avg_sc>=3.5 or avg_sc<=1.5 else 5),95)
    main="BUY" if buy>1 else "SELL"
    col_main="#00FF88" if main=="BUY" else "#FF3B30"

    # --- 3 TF CLEAR CARDS ---
    c1,c2,c3=st.columns(3)
    for col,name,d in zip([c1,c2,c3],["15 MIN","5 MIN","1 MIN"],[d15,d5,d1]):
        with col:
            with st.container(border=True):
                st.markdown(f"### {name}")
                if d['sig']=="BUY":
                    st.success(f"🟢 {d['sig']} - {d['sc']}/5")
                else:
                    st.error(f"🔴 {d['sig']} - {d['sc']}/5")
                
                st.metric("💰 GOLD", f"${d['p']:.2f}")
                
                # RSI CLEAR
                rsi_color="red" if d['rsi']>=70 else "green" if d['rsi']<=30 else "blue"
                st.markdown(f"**RSI (14):**")
                st.metric("RSI", f"{d['rsi']:.2f}", d['rsi_s'])
                st.progress(d['rsi']/100)
                st.caption("OB=70 🔴 | OS=30 🟢")
                
                st.divider()
                st.markdown("**📈 EMA - CLEAR**")
                st.code(f"EMA 9 : ${d['e9']:.2f}\nEMA 21: ${d['e21']:.2f}\nEMA 50: ${d['e50']:.2f}", language="text")
                
                st.markdown("**📊 MACD - CLEAR**")
                trend = "BULLISH 🟢" if d['m']>d['ms'] else "BEARISH 🔴"
                st.code(f"MACD: {d['m']:.4f}\nSignal: {d['ms']:.4f}\nHist: {d['mh']:.4f}\nTrend: {trend}", language="text")
                
                st.markdown("**📉 ATR & SCORE**")
                st.code(f"ATR: {d['atr']:.4f}\nScore: {d['sc']}/5\nVol: {'HIGH' if d['atr']>8 else 'NORMAL'}", language="text")

    # --- FINAL - SUPER CLEAR ---
    st.divider()
    st.markdown(f"<h1 style='text-align:center; color:{col_main}; font-size:38px; font-weight:900;'>STRONG {main} - {max(buy,3-buy)}/3 TF</h1>", unsafe_allow_html=True)
    
    m1,m2,m3,m4=st.columns(4)
    m1.metric("Avg RSI", f"{avg_rsi:.2f}", "70 OB / 30 OS")
    m2.metric("Avg Score", f"{avg_sc:.1f}/5", f"{buy} BUY / {3-buy} SELL")
    m3.metric("Avg ATR", f"{avg_atr:.4f}")
    m4.metric("QUALITY", f"{quality}%", "95% MAX")
    
    st.markdown(f"<h1 style='text-align:center; color:#FFD700; font-size:70px; text-shadow:0 0 20px #FFD700;'>{quality}%</h1>", unsafe_allow_html=True)
    
    # Entry SL TP - CLEAR
    st.markdown("### 🎯 TRADE SETUP - CLEAR")
    e1,e2,e3=st.columns(3)
    entry=d15['p']
    sl = entry - avg_atr*1.2 if main=="BUY" else entry + avg_atr*1.2
    tp = entry + avg_atr*1.8 if main=="BUY" else entry - avg_atr*1.8
    e1.metric("ENTRY", f"${entry:.2f}", "GOLD PRICE")
    e2.metric("STOP LOSS", f"${sl:.2f}", f"{sl-entry:.2f}", delta_color="inverse")
    e3.metric("TAKE PROFIT", f"${tp:.2f}", f"{tp-entry:.2f}")
    
    if auto and quality>=min_q:
        st.success(f"🤖 AUTO TRADE LIVE: {main} @ ${entry:.2f} | Quality {quality}% | SL ${sl:.2f} TP ${tp:.2f} ✅")
        st.balloons()
    elif auto:
        st.warning(f"⏸️ AUTO ON - Waiting Quality >= {min_q}% | Now {quality}%")
    else:
        st.info(f"💤 AUTO OFF - Quality {quality}% | Turn ON Sidebar for Auto")

    if st.button("🔄 REFRESH - CLEAR DATA", use_container_width=True, type="primary"):
        st.cache_data.clear()
        st.rerun()
else:
    st.warning("Loading... 15 sec")
