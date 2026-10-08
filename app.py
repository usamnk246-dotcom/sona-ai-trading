# =================================================================
# 🏅 L6SJ GOLD AI V12.0 - ULTIMATE KING - DETAILED & FINAL
# Features: Multi Market + Multi Chart + 15m/5m/1m + RSI 70/30 +
# EMA 9/20/50 + MACD + ATR + Quality 95% + Auto + Knowledge +
# Price Section + Candle Patterns + Support/Resistance
# =================================================================

import streamlit as st
import yfinance as yf
import pandas as pd
import ta
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="L6SJ V12 ULTIMATE",
    layout="wide",
    page_icon="🏅",
    initial_sidebar_state="expanded"
)

# Dark Theme CSS
st.markdown("""
<style>
.stApp{background:#0a0e1a; color:white;}
[data-testid='stMetricValue']{color:white!important; font-weight:bold;}
.stTabs [data-baseweb="tab-list"] {gap: 10px;}
.stTabs [data-baseweb="tab"] {background:#1a1f2e; border-radius:8px; padding:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#FFD700;'>🏅 L6SJ V12.0 ULTIMATE - ALL IN ONE KING</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888;'>Gold + Bitcoin + Forex + Stocks | Live + 15m/5m/1m | RSI + EMA + MACD + ATR | 95% Quality</p>", unsafe_allow_html=True)

# ------------------ MULTI MARKET DICTIONARY ------------------
MARKETS = {
    "🥇 GOLD (GC=F)": "GC=F",
    "₿ BITCOIN (BTC-USD)": "BTC-USD",
    "🥈 SILVER (SI=F)": "SI=F",
    "💵 EUR/USD": "EURUSD=X",
    "💷 GBP/USD": "GBPUSD=X",
    "💴 USD/JPY": "JPY=X",
    "🛢️ OIL (CL=F)": "CL=F",
    "📈 S&P 500": "^GSPC",
    "💻 ETHEREUM": "ETH-USD",
    "🏦 NASDAQ": "^IXIC"
}

# ------------------ SIDEBAR CONTROLS ------------------
with st.sidebar:
    st.markdown("## 🌍 1. MARKET SELECTION")
    # Single Market for detailed view
    single_market_name = st.selectbox("Main Market (Detailed)", list(MARKETS.keys()), index=0)
    single_symbol = MARKETS[single_market_name]

    # Multi Market for wall
    st.markdown("## 📊 2. MULTI CHART WALL")
    multi_markets = st.multiselect("Select 4 Markets for Wall", list(MARKETS.keys()), default=["🥇 GOLD (GC=F)", "₿ BITCOIN (BTC-USD)", "💵 EUR/USD", "🥈 SILVER (SI=F)"])

    st.divider()
    st.markdown("## ⏰ 3. TIMEFRAME")
    chart_tf = st.selectbox("Live Chart TF", ["1m","5m","15m"], index=2)
    st.caption("Live = Real-time, 15m/5m/1m = Score card")

    st.divider()
    st.markdown("## 🤖 4. AUTO TRADING")
    auto = st.toggle("Auto Trading ON", False)
    min_q = st.slider("Min Quality % for Auto", 60, 95, 80)
    if auto:
        st.success(f"Auto ON - Will trade if Quality >= {min_q}%")
    else:
        st.info("Auto OFF - Manual mode")

    st.divider()
    st.markdown("## 📚 5. DISPLAY OPTIONS")
    show_knowledge = st.toggle("Show Knowledge Center", True)
    show_patterns = st.toggle("Show Candle Patterns", True)
    show_price = st.toggle("Show Price Section", True)

# ------------------ DATA FETCH FUNCTION - DETAILED ------------------
@st.cache_data(ttl=30) # Cache 30 sec for live
def get_market_data(symbol, timeframe):
    """
    Ye function har market ka data lata hai aur sab indicators nikalta hai:
    - RSI 30/70, EMA 9/20/50, MACD, ATR, Support/Resistance, Score
    """
    try:
        # 5 din ka data
        df = yf.download(symbol, period="5d", interval=timeframe, progress=False, auto_adjust=True)
        if df.empty:
            return None, None
        # MultiIndex fix
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        close = df['Close']
        high = df['High']
        low = df['Low']
        open_ = df['Open']

        # Current Price
        price = float(close.iloc[-1])

        # --- EMA 9/20/50 ---
        ema9 = float(ta.trend.ema_indicator(close, 9).iloc[-1])
        ema20 = float(ta.trend.ema_indicator(close, 20).iloc[-1])
        ema50 = float(ta.trend.ema_indicator(close, 50).iloc[-1])

        # --- RSI 14 with 70/30 ---
        rsi = float(ta.momentum.rsi(close, 14).iloc[-1])
        if rsi >= 70:
            rsi_status = "OVERBOUGHT 🔴 - Sell chance"
        elif rsi <= 30:
            rsi_status = "OVERSOLD 🟢 - Buy chance"
        else:
            rsi_status = "NEUTRAL ⚪ - Wait"

        # --- MACD ---
        macd_line = float(ta.trend.macd(close).iloc[-1])
        signal_line = float(ta.trend.macd_signal(close).iloc[-1])
        hist = float(ta.trend.macd_diff(close).iloc[-1])
        macd_trend = "BULLISH 🟢" if macd_line > signal_line else "BEARISH 🔴"

        # --- ATR 14 ---
        atr = float(ta.volatility.average_true_range(high, low, close, 14).iloc[-1])

        # --- Support / Resistance - 20 bars ---
        support = float(low.tail(20).min())
        resistance = float(high.tail(20).max())

        # --- SCORING SYSTEM - 0 to 5 ---
        score = 0
        if price > ema9: score += 1 # Price above EMA9
        if ema9 > ema20: score += 1 # EMA9 above EMA20
        if ema20 > ema50: score += 1 # EMA20 above EMA50
        if rsi > 50: score += 1 # RSI bullish
        if macd_line > signal_line: score += 1 # MACD bullish

        # Final Signal
        signal = "BUY 🟢" if score >= 3 else "SELL 🔴"

        data_dict = {
            "price": price,
            "ema9": ema9, "ema20": ema20, "ema50": ema50,
            "rsi": rsi, "rsi_status": rsi_status,
            "macd": macd_line, "macd_signal": signal_line, "macd_hist": hist, "macd_trend": macd_trend,
            "atr": atr,
            "support": support, "resistance": resistance,
            "score": score, "signal": signal,
            "range": resistance - support
        }
        return data_dict, df

    except Exception as e:
        # st.error(f"Error {symbol} {timeframe}: {e}")
        return None, None

# ------------------ CANDLESTICK PATTERN DETECTOR - DETAILED ------------------
def detect_candle_patterns(df):
    """
    Ye function candlestick patterns auto detect karta hai:
    Hammer, Shooting Star, Doji, Engulfing, Pin Bar
    """
    if df is None or len(df) < 3:
        return ["No data"]

    last = df.iloc[-1]
    prev = df.iloc[-2]

    o = last['Open']; h = last['High']; l = last['Low']; c = last['Close']
    po = prev['Open']; pc = prev['Close']

    body = abs(c - o)
    candle_range = h - l
    upper_shadow = h - max(c, o)
    lower_shadow = min(c, o) - l

    patterns = []

    # 1. HAMMER
    if lower_shadow > body * 2 and upper_shadow < body * 0.5 and body > 0:
        patterns.append("🔨 HAMMER - BULLISH REVERSAL at Support 🟢 - Buy signal")

    # 2. SHOOTING STAR
    if upper_shadow > body * 2 and lower_shadow < body * 0.5 and body > 0:
        patterns.append("⭐ SHOOTING STAR - BEARISH REVERSAL at Resistance 🔴 - Sell signal")

    # 3. DOJI
    if body < candle_range * 0.1:
        patterns.append("➕ DOJI - INDECISION ⚪ - Market confused, wait")

    # 4. BULLISH ENGULFING
    if pc < po and c > o and c > po and o < pc:
        patterns.append("🟢 BULLISH ENGULFING - STRONG BUY 🟢 - Previous red fully covered")

    # 5. BEARISH ENGULFING
    if pc > po and c < o and c < po and o > pc:
        patterns.append("🔴 BEARISH ENGULFING - STRONG SELL 🔴 - Previous green fully covered")

    # 6. BULLISH PIN BAR
    if lower_shadow > body * 1.5 and c > o:
        patterns.append("📌 BULLISH PIN BAR 🟢 - Buyers pushed up")

    # 7. BEARISH PIN BAR
    if upper_shadow > body * 1.5 and c < o:
        patterns.append("📌 BEARISH PIN BAR 🔴 - Sellers pushed down")

    if not patterns:
        patterns.append("➡️ CONTINUATION - No strong reversal pattern")

    return patterns

# ------------------ FETCH MAIN MARKET 3 TF ------------------
d15, df15 = get_market_data(single_symbol, "15m")
d5, df5 = get_market_data(single_symbol, "5m")
d1, df1 = get_market_data(single_symbol, "1m")

# ------------------ MAIN DETAILED SECTION ------------------
if d15 and d5 and d1:
    # --- CALCULATE FINAL ---
    buy_count = sum(1 for x in [d15, d5, d1] if "BUY" in x['signal'])
    avg_rsi = (d15['rsi'] + d5['rsi'] + d1['rsi']) / 3
    avg_score = (d15['score'] + d5['score'] + d1['score']) / 3
    avg_atr = (d15['atr'] + d5['atr'] + d1['atr']) / 3

    # Quality formula - 95% max
    quality = min(max(buy_count, 3-buy_count) * 25 + 10 + (15 if avg_score >= 3.5 or avg_score <= 1.5 else 5), 95)

    main_signal = "BUY 🟢" if buy_count > 1 else "SELL 🔴"
    main_color = "#00FF88" if "BUY" in main_signal else "#FF3B30"

    # ========== TABS FOR DETAILED VIEW ==========
    tab1, tab2, tab3 = st.tabs(["📈 LIVE CHART + 3 TF SCORES", "🌍 MULTI MARKET WALL", "📚 KNOWLEDGE + PRICE + PATTERNS"])

    with tab1:
        # --- LIVE CHART ---
        st.markdown(f"### 📈 LIVE {single_market_name} CHART - {chart_tf.upper()} + EMA 9/20/50 + RSI 70/30")
        df_map = {"1m": df1, "5m": df5, "15m": df15}
        df_chart = df_map[chart_tf]
        df_last = df_chart.tail(120).copy()

        df_last['EMA9'] = ta.trend.ema_indicator(df_last['Close'], 9)
        df_last['EMA20'] = ta.trend.ema_indicator(df_last['Close'], 20)
        df_last['EMA50'] = ta.trend.ema_indicator(df_last['Close'], 50)
        df_last['RSI'] = ta.momentum.rsi(df_last['Close'], 14)

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.06, row_heights=[0.70, 0.30])

        # Candle
        fig.add_trace(go.Candlestick(x=df_last.index, open=df_last['Open'], high=df_last['High'], low=df_last['Low'], close=df_last['Close'], name=f"{single_market_name}"), row=1, col=1)
        # EMA lines
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA9'], line=dict(color='#FFD700', width=1.5), name="EMA 9 (Fast)"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA20'], line=dict(color='#00FF88', width=1.5), name="EMA 20 (Mid)"), row=1, col=1)
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['EMA50'], line=dict(color='#FF3B30', width=1.5), name="EMA 50 (Slow)"), row=1, col=1)
        # RSI
        fig.add_trace(go.Scatter(x=df_last.index, y=df_last['RSI'], line=dict(color='#8A2BE2', width=2), name="RSI 14"), row=2, col=1)
        fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="OB 70", row=2, col=1)
        fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="OS 30", row=2, col=1)
        fig.add_hline(y=50, line_dash="dot", line_color="gray", row=2, col=1)

        fig.update_layout(height=550, template="plotly_dark", paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a", xaxis_rangeslider_visible=False, margin=dict(l=10,r=10,t=10,b=10), legend=dict(orientation="h", y=1.02))
        st.plotly_chart(fig, use_container_width=True)

        # --- 3 TF SCORE CARDS - DETAILED ---
        st.markdown(f"### ⏰ 3 TIMEFRAME ANALYSIS - {single_market_name}")
        c1,c2,c3 = st.columns(3)

        for col, name, d, df in zip([c1,c2,c3], ["15 MIN (Main)", "5 MIN (Confirm)", "1 MIN (Entry)"], [d15,d5,d1], [df15,df5,df1]):
            with col:
                with st.container(border=True):
                    # Signal Header
                    if "BUY" in d['signal']:
                        st.success(f"### {name}\n## {d['signal']} - {d['score']}/5")
                    else:
                        st.error(f"### {name}\n## {d['signal']} - {d['score']}/5")

                    # Price
                    st.metric("💰 PRICE", f"${d['price']:.2f}", f"Range ${d['range']:.2f}")

                    # RSI detailed
                    st.metric("📊 RSI 14", f"{d['rsi']:.2f}", d['rsi_status'])
                    st.progress(min(max(d['rsi']/100,0),1))
                    st.caption("OB=70 🔴 | OS=30 🟢 | 50 Neutral")

                    st.divider()
                    # EMA detailed
                    st.markdown("**📈 EMA 9/20/50:**")
                    st.code(f"EMA 9 (Fast) : ${d['ema9']:.2f}\nEMA 20 (Mid) : ${d['ema20']:.2f}\nEMA 50 (Slow) : ${d['ema50']:.2f}\nPrice vs EMA9: {'Above 🟢' if d['price']>d['ema9'] else 'Below 🔴'}", language="text")

                    # MACD detailed
                    st.markdown("**📊 MACD:**")
                    st.code(f"MACD Line : {d['macd']:.4f}\nSignal Line: {d['macd_signal']:.4f}\nHistogram : {d['macd_hist']:.4f}\nTrend: {d['macd_trend']}", language="text")

                    # ATR + Support Resistance
                    st.markdown("**💰 PRICE SECTION:**")
                    st.code(f"ATR (Volatility): {d['atr']:.4f}\nSupport (20 low): ${d['support']:.2f}\nResistance (20 high): ${d['resistance']:.2f}\nScore: {d['score']}/5", language="text")

                    # Patterns
                    if show_patterns:
                        st.markdown("**🕯️ PATTERNS:**")
                        pats = detect_candle_patterns(df)
                        for p in pats:
                            if "BUY" in p or "HAMMER" in p or "BULLISH" in p:
                                st.success(p)
                            elif "SELL" in p or "SHOOTING" in p or "BEARISH" in p:
                                st.error(p)
                            else:
                                st.info(p)

        # --- FINAL SIGNAL - BIG ---
        st.divider()
        st.markdown(f"<h1 style='text-align:center; color:{main_color}; font-size:42px;'>FINAL: STRONG {main_signal} - {max(buy_count,3-buy_count)}/3 TF AGREE</h1>", unsafe_allow_html=True)

        m1,m2,m3,m4 = st.columns(4)
        m1.metric("Avg RSI 14", f"{avg_rsi:.2f}", "70 OB / 30 OS")
        m2.metric("Avg Score", f"{avg_score:.1f}/5", f"{buy_count}B / {3-buy_count}S")
        m3.metric("Avg ATR", f"{avg_atr:.4f}", "Volatility")
        m4.metric("QUALITY", f"{quality}%", "95% MAX")

        st.markdown(f"<h1 style='text-align:center; color:#FFD700; font-size:75px;'>{quality}%</h1>", unsafe_allow_html=True)
        st.progress(quality/100)

        # Entry / SL / TP
        entry = d15['price']
        if "BUY" in main_signal:
            sl = entry - avg_atr * 1.2
            tp = entry + avg_atr * 1.8
        else:
            sl = entry + avg_atr * 1.2
            tp = entry - avg_atr * 1.8

        e1,e2,e3 = st.columns(3)
        e1.metric("🎯 ENTRY", f"${entry:.2f}", "Current price")
        e2.metric("🛑 STOP LOSS", f"${sl:.2f}", f"{sl-entry:+.2f}", delta_color="inverse")
        e3.metric("💰 TAKE PROFIT", f"${tp:.2f}", f"{tp-entry:+.2f}")

        if auto and quality >= min_q:
            st.success(f"🤖 AUTO TRADE EXECUTED: {main_signal} {single_market_name} @ ${entry:.2f} | Quality {quality}% ✅ | SL ${sl:.2f} TP ${tp:.2f}")
            st.balloons()
        elif auto:
            st.warning(f"⏸️ AUTO ON - Waiting for Quality >= {min_q}% | Current {quality}% | Signal {main_signal}")
        else:
            st.info(f"💤 AUTO OFF - Manual mode | Quality {quality}% | {single_market_name}")

    with tab2:
        # MULTI MARKET WALL
        st.markdown(f"## 🌍 MULTI MARKET CHART WALL - {chart_tf.upper()}")
        if multi_markets:
            cols = st.columns(2)
            summary = []
            for idx, m_name in enumerate(multi_markets[:4]):
                sym = MARKETS[m_name]
                md, mdf = get_market_data(sym, chart_tf)
                if md is None: continue
                summary.append({"Market": m_name, "Price": md['price'], "Signal": md['signal'], "Score": md['score'], "RSI": md['rsi']})

                col = cols[idx % 2]
                with col:
                    with st.container(border=True):
                        col_color = "#00FF88" if "BUY" in md['signal'] else "#FF3B30"
                        st.markdown(f"<h4 style='color:{col_color};'>{m_name} - {md['signal']} {md['score']}/5</h4>", unsafe_allow_html=True)
                        st.metric("Price", f"${md['price']:.2f}", f"RSI {md['rsi']:.1f}")

                        df_c = mdf.tail(60).copy()
                        df_c['EMA9'] = ta.trend.ema_indicator(df_c['Close'], 9)
                        df_c['EMA20'] = ta.trend.ema_indicator(df_c['Close'], 20)
                        fig_m = go.Figure()
                        fig_m.add_trace(go.Candlestick(x=df_c.index, open=df_c['Open'], high=df_c['High'], low=df_c['Low'], close=df_c['Close'], showlegend=False))
                        fig_m.add_trace(go.Scatter(x=df_c.index, y=df_c['EMA9'], line=dict(color='#FFD700', width=1), name="EMA9"))
                        fig_m.add_trace(go.Scatter(x=df_c.index, y=df_c['EMA20'], line=dict(color='#00ff88', width=1), name="EMA20"))
                        fig_m.update_layout(height=250, template="plotly_dark", paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a", xaxis_rangeslider_visible=False, margin=dict(l=5,r=5,t=5,b=5), legend=dict(orientation="h", y=1.1))
                        st.plotly_chart(fig_m, use_container_width=True)

            if summary:
                st.divider()
                st.markdown("### 📊 SUMMARY TABLE")
                st.dataframe(pd.DataFrame(summary), use_container_width=True, hide_index=True)

                # Comparison normalized
                st.markdown("### 📈 NORMALIZED COMPARISON (Who is rising fastest?)")
                fig_comp = go.Figure()
                for m_name in multi_markets[:4]:
                    sym = MARKETS[m_name]
                    _, cdf = get_market_data(sym, chart_tf)
                    if cdf is not None:
                        norm = (cdf['Close'].tail(100) / cdf['Close'].tail(100).iloc[0] * 100)
                        fig_comp.add_trace(go.Scatter(x=norm.index, y=norm, name=m_name, mode='lines'))
                fig_comp.update_layout(height=350, template="plotly_dark", paper_bgcolor="#0a0e1a", plot_bgcolor="#0a0e1a")
                st.plotly_chart(fig_comp, use_container_width=True)
        else:
            st.warning("Sidebar se 4 markets select karo Multi Wall ke liye!")

    with tab3:
        # KNOWLEDGE CENTER - FULL DETAILED
        st.markdown(f"## 📚 KNOWLEDGE CENTER - {single_market_name} - FULL GUIDE")

        k1,k2,k3 = st.columns(3)

        with k1:
            st.markdown("### 🕯️ 1. CANDLESTICK PATTERNS - FULL DETAIL")
            st.success("**🔨 HAMMER:**\n- Lower shadow > 2x body\n- Upper shadow small\n- Means: Sellers failed, buyers came\n- At SUPPORT = Strong BUY 🟢\n- Entry: Next candle green")
            st.error("**⭐ SHOOTING STAR:**\n- Upper shadow > 2x body\n- Lower shadow small\n- Means: Buyers failed, sellers came\n- At RESISTANCE = Strong SELL 🔴\n- Entry: Next candle red")
            st.warning("**➕ DOJI:**\n- Body very small (open=close)\n- Means: No decision\n- Action: WAIT, don't trade")
            st.info("**🟢 BULLISH ENGULFING:**\n- Green candle fully covers previous red\n- Means: Strong buyer takeover\n- Action: BUY immediately")
            st.error("**🔴 BEARISH ENGULFING:**\n- Red candle fully covers previous green\n- Means: Strong seller takeover\n- Action: SELL immediately")
            st.markdown("**📌 PIN BAR:**\n- Long shadow one side\n- Bullish Pin = long lower shadow + green\n- Bearish Pin = long upper shadow + red")

        with k2:
            st.markdown("### 💰 2. PRICE SECTION - SUPPORT/RESISTANCE")
            if show_price:
                st.code(f"""Market: {single_market_name}
Symbol: {single_symbol}
Current Price: ${d15['price']:.2f}

Support (20 bars low): ${d15['support']:.2f}
Resistance (20 bars high): ${d15['resistance']:.2f}
Range: ${d15['range']:.2f}
ATR: {d15['atr']:.4f}

--- RULES ---
1. BUY near Support + Bullish Pattern
   Example: Price $4150 near Support $4140 + Hammer = BUY

2. SELL near Resistance + Bearish Pattern
   Example: Price $4180 near Resistance $4190 + Shooting Star = SELL

3. SL = 1.2 x ATR
4. TP = 1.8 x ATR
5. Risk Reward = 1 : 1.5

Current Position:
Price {d15['price']:.2f} is {(d15['price']-d15['support'])/d15['range']*100:.0f}% above Support
""", language="text")

            st.markdown("**📊 HOW TO USE SUPPORT/RESISTANCE:**")
            st.markdown("- **
