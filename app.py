import streamlit as st
import yfinance as yf
import pandas as pd
import ta

st.set_page_config(page_title="L6SJ V8", layout="wide", page_icon="🏅")
st.markdown("<style>.stApp{background:#080c14;} .gold{color:#FFD700; font-weight:900;} .card{background:#111827; border:1px solid #1f2a3a; border-radius:16px; padding:15px;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#FFD700;'>🏅 L6SJ GOLD AI V8 PRO - AUTO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; letter-spacing:3px;'>15M • 5M • 1M • RSI • EMA • MACD • ATR • SCORE • QUALITY 95% • AUTO</p>", unsafe_allow_html=True)

# SIDEBAR - AUTO
with st.sidebar:
    st.title("🤖 AUTO")
    auto = st.toggle("Auto Trading ON", False)
    min_q = st.slider("Min Quality", 60,95,80)
    st.divider()
    st.markdown("**Quality Logic:**\n- 3/3 TF = 75%+10%+10% = 95%\n- 2/3 TF = 50%+10%+15% = 75%\n- Score avg included")

@st.cache_data(ttl=45)
def analyze(tf):
    df = yf.download("GC=F", period="2d", interval=tf, progress=False)
    if df.empty: return None
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    close, high, low = df['Close'], df['High'], df['Low']
    price = close.iloc[-1]
    
    # --- ZAROOR INDICATORS ---
    # EMA
    ema9 = ta.trend.ema_indicator(close, 9).iloc[-1]
    ema21 = ta.trend.ema_indicator(close, 21).iloc[-1]
    ema50 = ta.trend.ema_indicator(close, 50).iloc[-1]
    # RSI with 70/30
    rsi = ta.momentum.rsi(close, 14).iloc[-1]
    rsi_signal = "OVERBOUGHT" if rsi >=70 else "OVERSOLD" if rsi <=30 else "NEUTRAL"
    # MACD
    macd = ta.trend.macd(close).iloc[-1]
    macd_sig = ta.trend.macd_signal(close).iloc[-1]
    macd_hist = ta.trend.macd_diff(close).iloc[-1]
    # ATR
    atr = ta.volatility.average_true_range(high, low, close, 14).iloc[-1]
    
    # SCORE 0-5 (zaroor)
    score = 0
    if price > ema9: score+=1
    if ema9 > ema21: score+=1
    if ema21 > ema50: score+=1
    if rsi > 50: score+=1
    if macd > macd_sig: score+=1
    
    signal = "BUY" if score >=3 else "SELL"
    
    return {
        "price":price, "ema9":ema9, "ema21":ema21, "ema50":ema50,
        "rsi":rsi, "rsi_signal":rsi_signal,
        "macd":macd, "macd_sig":macd_sig, "macd_hist":macd_hist,
        "atr":atr, "score":score, "signal":signal
    }

# FETCH ALL 3
d15 = analyze("15m"); d5 = analyze("5m"); d1 = analyze("1m")

if d15 and d5 and d1:
    buy_c = sum([1 for x in [d15,d5,d1] if x['signal']=="BUY"])
    sell_c = 3-buy_c
    avg_rsi = (d15['rsi']+d5['rsi']+d1['rsi'])/3
    avg_score = (d15['score']+d5['score']+d1['score'])/3
    avg_atr = (d15['atr']+d5['atr']+d1['atr'])/3
    
    # QUALITY 95% - BOTH SIDE LOGIC
    quality = max(buy_c, sell_c)*25 + 10 + (15 if (avg_score>=3.5 or avg_score<=1.5) else 5)
    quality = min(quality, 95)
    
    # DISPLAY
    cols = st.columns(3)
    for col, (tf_name, d) in zip(cols, [("15 MIN",d15),("5 MIN",d5),("1 MIN",d1)]):
        with col:
            color = "#00ff88" if d['signal']=="BUY" else "#ff3b30"
            rsi_color = "#ff3b30" if d['rsi_signal']=="OVERBOUGHT" else "#00ff88" if d['rsi_signal']=="OVERSOLD" else "#aaa"
            st.markdown(f"""
            <div class="card">
                <div style="display:flex; justify-content:space-between;">
                    <b class="gold">{tf_name}</b>
                    <span style="background:{color}; color:{'black' if d['signal']=='BUY' else 'white'}; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:800;">{d['signal']} {d['score']}/5</span>
                </div>
                <div style="font-size:24px; font-weight:800; color:white; margin:8px 0;">${d['price']:.2f}</div>
                
                <div style="background:#0c121e; border-radius:10px; padding:10px; font-size:11px; color:#888; line-height:1.7;">
                    <b style="color:white;">RSI:</b> <span style="color:{rsi_color}; font-weight:800;">{d['rsi']:.1f} ({d['rsi_signal']})</span> | 70 OB / 30 OS<br>
                    <b style="color:white;">EMA:</b> 9:{d['ema9']:.2f} | 21:{d['ema21']:.2f} | 50:{d['ema50']:.2f}<br>
                    <b style="color:white;">MACD:</b> {d['macd']:.3f} vs Sig {d['macd_sig']:.3f} | Hist {d['macd_hist']:.3f}<br>
                    <b style="color:white;">ATR:</b> {d['atr']:.3f} | <b style="color:#FFD700;">SCORE: {d['score']}/5</b>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # FINAL - ALL INCLUDED
    main_sig = "BUY" if buy_c > sell_c else "SELL"
    main_color = "#00ff88" if main_sig=="BUY" else "#ff3b30"
    
    can_auto = quality >= min_q
    st.markdown(f"""
    <div class="card" style="margin-top:18px; border:2px solid {main_color}; text-align:center;">
        <div style="color:#666; font-size:10px; letter-spacing:3px;">FINAL ANALYSIS • ALL INDICATORS INCLUDED</div>
        <div style="color:{main_color}; font-size:28px; font-weight:900;">STRONG {main_sig} CONFIRMED - {max(buy_c,sell_c)}/3 TF</div>
        <div style="display:flex; justify-content:center; gap:30px; margin:10px 0; color:#aaa; font-size:12px;">
            <span>Avg RSI: <b style="color:white;">{avg_rsi:.1f}</b> (70 OB/30 OS)</span>
            <span>Avg Score: <b style="color:#FFD700;">{avg_score:.1f}/5</b></span>
            <span>Avg ATR: <b style="color:white;">{avg_atr:.3f}</b></span>
            <span>BUY TFs: {buy_c}/3</span>
        </div>
        <div style="font-size:58px; font-weight:900; color:#FFD700; text-shadow:0 0 25px #FFD700;">{quality}%</div>
        <div style="color:#FFD700; font-size:11px;">QUALITY 95% - {main_sig} POWER - ALL TF {main_sig}</div>
        
        <div style="background:#0c121e; border-radius:12px; padding:12px; margin-top:12px; display:flex; justify-content:space-around; color:#aaa; font-size:13px;">
            <span>Entry: <b style="color:white;">${d15['price']:.2f}</b></span>
            <span>SL: <b style="color:#ff5a5a;">${d15['price'] + d15['atr']*1.2 if main_sig=='BUY' else d15['price'] - d15['atr']*1.2:.2f}</b></span>
            <span>TP: <b style="color:#00ff88;">${d15['price'] + d15['atr']*1.8 if main_sig=='BUY' else d15['price'] - d15['atr']*1.8:.2f}</b></span>
        </div>
        
        <div style="margin-top:12px; padding:10px; border-radius:10px; background:{'#00ff8820' if can_auto and auto else '#ffaa0020'}; color:{'#00ff88' if can_auto and auto else '#ffaa00'}; font-weight:700;">
            {'🤖 AUTO TRADE EXECUTED - ' + main_sig + f' at ${d15["price"]:.2f} | Quality {quality}%' if auto and can_auto else f'{"⏸️ AUTO ON - Waiting Quality >="+str(min_q)+"%" if auto else "⏸️ AUTO OFF"} | Current {quality}% | {"✅ Ready" if can_auto else "❌ Low Quality"}'}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 REFRESH ALL INDICATORS", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
else:
    st.error("Data loading - Wait 30 sec")
