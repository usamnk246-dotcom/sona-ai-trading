import streamlit as st
import yfinance as yf
import pandas as pd
import ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="L6SJ LIVE CHART", layout="wide", page_icon="🏅")
st.markdown("<style>.stApp{background:#0a0e1a;} [data-testid='stMetricValue']{color:white !important;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#FFD700;'>🏅 L6SJ GOLD AI V8.4 - LIVE CHART + FULL</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa;'>LIVE CHART • 15M • 5M • 1M • RSI 70/30 • EMA 9/21/50 • MACD • ATR • SCORE • QUALITY 95% • AUTO</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title("🤖 AUTO")
    auto = st.toggle("Auto Trading ON", False)
    min_q = st.slider("Min Quality", 60,95,80)
    chart_tf = st.selectbox("Live Chart TF", ["1m","5m","15m"], index=2)
    st.info("Tol purana + Live Chart")

@st.cache_data(ttl=30)
def get_tf(tf):
    df = yf.download("GC=F", period="2d", interval=tf, progress=False)
    if df.empty: return None, None
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
    rsi_s="OVERBOUGHT 🔴" if rsi>=70 else "OVERSOLD 🟢" if rsi<=30 else "NEUTRAL ⚪"
    data={"p":price,"e9":ema9,"e21":ema21,"e50":ema50,"rsi":rsi,"rsi_s":rsi_s,"m":macd,"ms":sig,"mh":hist,"atr":atr,"sc":sc,"sig":signal}
    return data, df

d15, df15 = get_tf("15m"); d5, df5 = get_tf("5m"); d1, df1 = get_tf("1m")

if d15 and d5 and d1:
    buy=sum(1 for x in [d15,d5,d1] if x['sig']=="BUY")
    avg_rsi=(d15['rsi']+d5['rsi']+d1['rsi'])/3
    avg_sc=(d15['sc']+d5['sc']+d1['sc'])/3
    avg_atr=(d15['atr']+d5['atr']+d1['atr'])/3
    quality=min(max(buy,3-buy)*25 + 10 + (15 if avg_sc>=3.5 or avg_sc<=1.5 else 5),95)
    main="BUY" if buy>1 else "SELL"
    col_main="#00FF88" if main=="BUY" else "#FF3B30"

    # --- LIVE CHART - NEW ADDITION ---
    st.markdown(f"### 📈 LIVE GOLD CHART - {chart_tf.upper()} - REAL TIME")
    df_map = {"1m":df1, "5m":df5, "15m":df15}
    df_chart = df_map[chart_tf]
    if df_chart is not None and not df_chart.empty:
        df_last = df_chart.tail(100)
        df_last['EMA9'] = ta.trend.ema_indicator(df_last['Close'], 9)
        df_last['EMA21'] = ta.trend.ema_indicator(df_last['Close'], 21)
        df_last['EMA50'] = ta.trend.ema_indicator(df_last['Close'], 50)
        df_last['RSI'] = ta.momentum.rsi(df_last['Close'], 14)
        
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.7,0.3])
        # Candlestick
        fig.add_trace(go.Candlestick(x=df_last.index, open=df_last['Open'], high=df_last['High'], low=df_last['Low'], close=df_last['Close'], name="GOLD"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA9'], line=dict(color='#FFD700', width=1.5), name="EMA 9"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA21'], line=dict(color='#00ff88', width=1.5), name="EMA 21"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA50'], line=dict(color='#ff3b30', width=1.5), name="EMA 50"), row=1, col=1)
        # RSI
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['RSI'], line=dict(color='#8a2be2', width=2), name="RSI 14"), row=2, col=1)
        fig.add_hline(y=70, line_dash="dash", line_color="red", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", row=2, col=1)
        fig.add_hline(y=50, line_dash="dot", line_color="gray", row=2, col=1)
        
        fig.update_layout(height=550, template="plotly_dark", paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a", xaxis_rangeslider_visible=False, margin=dict(l=10,r=10,t=10,b=10), legend=dict(orientation="h", y=1.02))
        fig.update_yaxes(title_text="Price $", row=1, col=1)
        fig.update_yaxes(title_text="RSI", range=[0,100], row=2, col=1)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Chart loading...")

    # --- 3 TF - OLD TOL PAKA ---
    c1,c2,c3=st.columns(3)
    for col,name,d in zip([c1,c2,c3],["15 MIN","5 MIN","1 MIN"],[d15,d5,d1]):
        with col:
            with st.container(border=True):
                st.markdown(f"### {name}")
                if d['sig']=="BUY": st.success(f"🟢 {d['sig']} - {d['sc']}/5")
                else: st.error(f"🔴 {d['sig']} - {d['sc']}/5")
                st.metric("💰 GOLD", f"${d['p']:.2f}")
                st.metric("RSI", f"{d['rsi']:.2f}", d['rsi_s'])
                st.progress(d['rsi']/100)
                st.caption("OB=70 🔴 | OS=30 🟢")
                st.divider()
                st.code(f"EMA 9 : ${d['e9']:.2f}\nEMA 21: ${d['e21']:.2f}\nEMA 50: ${d['e50']:.2f}", language="text")
                trend = "BULLISH 🟢" if d['m']>d['ms'] else "BEARISH 🔴"
                st.code(f"MACD: {d['m']:.4f}\nSignal: {d['ms']:.4f}\nHist: {d['mh']:.4f}\n{trend}", language="text")
                st.code(f"ATR: {d['atr']:.4f}\nScore: {d['sc']}/5", language="text")

    # --- FINAL ---
    st.divider()
    st.markdown(f"<h1 style='text-align:center; color:{col_main}; font-size:36px;'>STRONG {main} - {max(buy,3-buy)}/3 TF</h1>", unsafe_allow_html=True)
    m1,m2,m3,m4=st.columns(4)
    m1.metric("Avg RSI", f"{avg_rsi:.2f}", "70/30")
    m2.metric("Avg Score", f"{avg_sc:.1f}/5", f"{buy}B/{3-buy}S")
    m3.metric("Avg ATR", f"{avg_atr:.4f}")
    m4.metric("QUALITY", f"{quality}%", "95% MAX")
    st.markdown(f"<h1 style='text-align:center; color:#FFD700; font-size:65px;'>{quality}%</h1>", unsafe_allow_html=True)
    
    e1,e2,e3=st.columns(3)
    entry=d15['p']
    sl = entry - avg_atr*1.2 if main=="BUY" else entry + avg_atr*1.2
    tp = entry + avg_atr*1.8 if main=="BUY" else entry - avg_atr*1.8
    e1.metric("ENTRY", f"${entry:.2f}")
    e2.metric("STOP LOSS", f"${sl:.2f}", f"{sl-entry:.2f}", delta_color="inverse")
    e3.metric("TAKE PROFIT", f"${tp:.2f}", f"{tp-entry:.2f}")
    
    if auto and quality>=min_q:
        st.success(f"🤖 AUTO TRADE: {main} @ ${entry:.2f} | Quality {quality}% ✅")
        st.balloons()
    elif auto:
        st.warning(f"⏸️ AUTO ON - Waiting >= {min_q}% | Now {quality}%")
    else:
        st.info(f"💤 AUTO OFF | Quality {quality}%")
    
    if st.button("🔄 REFRESH ALL + CHART", use_container_width=True, type="primary"):
        st.cache_data.clear()
        st.rerun()
else:
    st.warning("Loading Gold Data...")
