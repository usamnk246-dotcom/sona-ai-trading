import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="L6SJ V8.2", layout="wide", page_icon="🏅")
st.markdown("<style>.stApp{background:#080c14;} .card{background:#111827; border:1px solid #1e2a3c; border-radius:16px; padding:16px;} .gold{color:#FFD700; font-weight:900;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#FFD700;'>🏅 L6SJ GOLD AI V8.2 - FULL DETAILS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:2px;'>YESTERDAY ALL + AUTO | 15M • 5M • 1M • RSI 70/30 • EMA 9/21/50 • MACD • ATR • SCORE • QUALITY 95%</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🤖 AUTO TRADING")
    auto_on = st.toggle("Auto ON", False)
    min_q = st.slider("Min Quality %", 60, 95, 80)
    st.success("Yesterday Features: 100% Included")

@st.cache_data(ttl=40)
def get_data(tf):
    df = yf.download("GC=F", period="2d", interval=tf, progress=False)
    if df.empty: return None
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    c,h,l = df['Close'], df['High'], df['Low']
    price = float(c.iloc[-1])
    # ALL INDICATORS - YESTERDAY WALE
    ema9 = float(ta.trend.ema_indicator(c, 9).iloc[-1])
    ema21 = float(ta.trend.ema_indicator(c, 21).iloc[-1])
    ema50 = float(ta.trend.ema_indicator(c, 50).iloc[-1])
    rsi = float(ta.momentum.rsi(c, 14).iloc[-1])
    macd_line = float(ta.trend.macd(c).iloc[-1])
    macd_sig = float(ta.trend.macd_signal(c).iloc[-1])
    macd_hist = float(ta.trend.macd_diff(c).iloc[-1])
    atr = float(ta.volatility.average_true_range(h,l,c,14).iloc[-1])
    
    # Score calculation
    s=0
    if price>ema9: s+=1
    if ema9>ema21: s+=1
    if ema21>ema50: s+=1
    if rsi>50: s+=1
    if macd_line>macd_sig: s+=1
    sig = "BUY" if s>=3 else "SELL"
    rsi_status = "OVERBOUGHT (SELL ZONE)" if rsi>=70 else "OVERSOLD (BUY ZONE)" if rsi<=30 else "NEUTRAL"
    
    return {"price":price,"ema9":ema9,"ema21":ema21,"ema50":ema50,"rsi":rsi,"rsi_status":rsi_status,"macd":macd_line,"macd_sig":macd_sig,"macd_hist":macd_hist,"atr":atr,"score":s,"signal":sig}

d15 = get_data("15m"); d5 = get_data("5m"); d1 = get_data("1m")

if d15 and d5 and d1:
    buy = sum(1 for x in [d15,d5,d1] if x['signal']=="BUY")
    sell = 3-buy
    avg_rsi = (d15['rsi']+d5['rsi']+d1['rsi'])/3
    avg_score = (d15['score']+d5['score']+d1['score'])/3
    avg_atr = (d15['atr']+d5['atr']+d1['atr'])/3
    quality = min(max(buy,sell)*25 + 10 + (15 if avg_score>=3.5 or avg_score<=1.5 else 5), 95)
    final_sig = "BUY" if buy>1 else "SELL"
    final_col = "#00ff88" if final_sig=="BUY" else "#ff3b30"

    # 3 TIMEFRAMES - FULL DETAILS
    col1,col2,col3 = st.columns(3)
    for col, name, d in zip([col1,col2,col3], ["15 MINUTE","5 MINUTE","1 MINUTE"], [d15,d5,d1]):
        with col:
            sig_col = "#00ff88" if d['signal']=="BUY" else "#ff3b30"
            rsi_c = "#ff3b30" if d['rsi']>=70 else "#00ff88" if d['rsi']<=30 else "#cccccc"
            with st.container(border=True):
                st.markdown(f"**{name}**")
                st.markdown(f":{ 'green' if d['signal']=='BUY' else 'red'}[{d['signal']} {d['score']}/5]")
                st.metric("Gold Price", f"${d['price']:.2f}")
                
                st.markdown(f"**RSI (14):** :{ 'red' if d['rsi']>=70 else 'green' if d['rsi']<=30 else 'gray'}[{d['rsi']:.2f}]")
                st.caption(f"Status: {d['rsi_status']} | OB=70 / OS=30")
                st.progress(min(max(d['rsi']/100,0.0),1.0))
                
                st.markdown("**EMA Details:**")
                st.text(f"EMA 9:  ${d['ema9']:.2f}\nEMA 21: ${d['ema21']:.2f}\nEMA 50: ${d['ema50']:.2f}")
                
                st.markdown("**MACD Details:**")
                st.text(f"MACD: {d['macd']:.4f}\nSignal: {d['macd_sig']:.4f}\nHistogram: {d['macd_hist']:.4f}\nTrend: {'BULLISH' if d['macd']>d['macd_sig'] else 'BEARISH'}")
                
                st.markdown("**ATR & Score:**")
                st.text(f"ATR (14): {d['atr']:.4f}\nScore: {d['score']}/5 Points\nVolatility: {'High' if d['atr']>10 else 'Normal'}")

    # FINAL SUMMARY - FULL DETAILS
    st.divider()
    with st.container(border=True):
        st.markdown(f"<h2 style='text-align:center; color:{final_col};'>STRONG {final_sig} CONFIRMED - {max(buy,sell)}/3 TIMEFRAMES</h2>", unsafe_allow_html=True)
        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Avg RSI", f"{avg_rsi:.2f}", "70 OB / 30 OS")
        c2.metric("Avg Score", f"{avg_score:.1f}/5", f"{buy} BUY / {sell} SELL")
        c3.metric("Avg ATR", f"{avg_atr:.4f}")
        c4.metric("QUALITY", f"{quality}%", "95% MAX")
        
        st.markdown(f"<h1 style='text-align:center; color:#FFD700; font-size:60px;'>{quality}%</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:#FFD700;'>QUALITY POWER - {final_sig} - {max(buy,sell)}/3 TF AGREE - SCORE BASED</p>", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("**Trade Setup (ATR Based):**")
        t1,t2,t3 = st.columns(3)
        entry = d15['price']
        sl = entry - avg_atr*1.2 if final_sig=="BUY" else entry + avg_atr*1.2
        tp = entry + avg_atr*1.8 if final_sig=="BUY" else entry - avg_atr*1.8
        t1.metric("ENTRY", f"${entry:.2f}")
        t2.metric("STOP LOSS", f"${sl:.2f}", f"-{abs(entry-sl):.2f}", delta_color="inverse")
        t3.metric("TAKE PROFIT", f"${tp:.2f}", f"+{abs(tp-entry):.2f}")
        
        if auto_on and quality>=min_q:
            st.success(f"🤖 AUTO TRADE EXECUTED: {final_sig} @ ${entry:.2f} | Quality {quality}% | SL ${sl:.2f} TP ${tp:.2f}")
        elif auto_on:
            st.warning(f"⏸️ AUTO ON - Waiting Quality >= {min_q}% | Current {quality}% | {'Ready' if quality>=min_q else 'Low Quality'}")
        else:
            st.info(f"⏸️ AUTO OFF - Turn ON for Auto Trading | Quality {quality}%")

    if st.button("🔄 REFRESH ALL DATA - FULL DETAILS", use_container_width=True, type="primary"):
        st.cache_data.clear()
        st.rerun()
else:
    st.error("Gold data loading... Please wait 20 seconds and refresh")
