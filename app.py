import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Sona AI King V71", layout="wide")
st.markdown("<h1 style='color:gold; text-align:center;'>👑 SONA AI KING V71 - MULTI MARKET TERMINAL</h1>", unsafe_allow_html=True)

markets = {"Gold XAUUSD":"GC=F","Silver":"SI=F","BTC":"BTC-USD","ETH":"ETH-USD","EURUSD":"EURUSD=X","GBPUSD":"GBPUSD=X","US100":"^NDX"}

st.sidebar.header("⚙️ CONTROL")
market_name = st.sidebar.selectbox("📈 Active Market", list(markets.keys()))
timeframe = st.sidebar.selectbox("⏰ Timeframe", ["1m","5m","15m","30m","1h","4h","1d"])
sl_atr = st.sidebar.slider("SL ATR", 0.5, 3.0, 1.5)
tp_atr = st.sidebar.slider("TP ATR", 1.0, 5.0, 3.0)

tf_map = {"1m":("1m","1d"),"5m":("5m","5d"),"15m":("15m","5d"),"30m":("30m","1mo"),"1h":("60m","1mo"),"4h":("60m","3mo"),"1d":("1d","1y")}
interval, period = tf_map[timeframe]

@st.cache_data(ttl=60)
def load_data(sym, per, inter):
    df = yf.download(sym, period=per, interval=inter, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
    df.dropna(inplace=True)
    return df

def calc_signal(df):
    df['EMA9'] = df['Close'].ewm(9).mean()
    df['EMA21'] = df['Close'].ewm(21).mean()
    df['EMA200'] = df['Close'].ewm(200).mean()
    delta = df['Close'].diff()
    gain = delta.where(delta>0,0).rolling(14).mean()
    loss = -delta.where(delta<0,0).rolling(14).mean()
    df['RSI'] = 100 - (100/(1+gain/loss))
    df['MACD'] = df['Close'].ewm(12).mean() - df['Close'].ewm(26).mean()
    df['MACD_Sig'] = df['MACD'].ewm(9).mean()
    df['TP'] = (df['High']+df['Low']+df['Close'])/3
    df['VWAP'] = (df['TP']*df['Volume']).cumsum()/df['Volume'].cumsum()
    df['TR'] = pd.concat([df['High']-df['Low'], abs(df['High']-df['Close'].shift(1)), abs(df['Low']-df['Close'].shift(1))], axis=1).max(axis=1)
    df['ATR'] = df['TR'].rolling(14).mean()
    last = df.iloc[-1]
    price=float(last['Close']); ema9=float(last['EMA9']); ema21=float(last['EMA21']); ema200=float(last['EMA200']); rsi=float(last['RSI']); macd=float(last['MACD']); sig=float(last['MACD_Sig']); vwap=float(last['VWAP']); atr=float(last['ATR'])
    buy = (ema9>ema21) and (price>ema200) and (price>vwap) and (50<rsi<72) and (macd>sig)
    sell = (ema9<ema21) and (price<ema200) and (price<vwap) and (28<rsi<50) and (macd<sig)
    if buy: sig_text="🟢 BUY"; sl=price-atr*sl_atr; tp=price+atr*tp_atr
    elif sell: sig_text="🔴 SELL"; sl=price+atr*sl_atr; tp=price-atr*tp_atr
    else: sig_text="⚪ WAIT"; sl=price-atr*sl_atr; tp=price-atr*tp_atr
    return df, price, rsi, sig_text, sl, tp, ema9, ema21, ema200, macd, vwap, atr

# --- TOL MARKET OVERVIEW TABLE ---
st.subheader(f"🌍 Tol Market Overview - Timeframe: {timeframe}")
overview_data = []
for m_name, m_sym in markets.items():
    try:
        d = load_data(m_sym, period, interval)
        if len(d)>210:
            _, p, r, s, sl, tp, _, _, _, _, _, _ = calc_signal(d.copy())
            overview_data.append({"Market":m_name, "Price":round(p,2), "RSI":round(r,1), "Signal":s, "SL":round(sl,2), "TP":round(tp,2)})
    except: pass

if overview_data:
    st.dataframe(pd.DataFrame(overview_data), use_container_width=True, hide_index=True)

st.divider()

# --- ACTIVE MARKET DETAIL ---
df_main = load_data(markets[market_name], period, interval)
df_main, price, rsi, signal_text, sl, tp, ema9, ema21, ema200, macd, vwap, atr = calc_signal(df_main)

# Color signal
if "BUY" in signal_text: st.markdown(f"<div style='background:#00c853;color:white;padding:15px;border-radius:10px;text-align:center;font-size:22px;font-weight:bold;'>{signal_text} - {market_name} - {timeframe}</div>", unsafe_allow_html=True)
elif "SELL" in signal_text: st.markdown(f"<div style='background:#ff1744;color:white;padding:15px;border-radius:10px;text-align:center;font-size:22px;font-weight:bold;'>{signal_text} - {market_name} - {timeframe}</div>", unsafe_allow_html=True)
else: st.markdown(f"<div style='background:#333;color:white;padding:15px;border-radius:10px;text-align:center;font-size:20px;'>{signal_text} - {market_name}</div>", unsafe_allow_html=True)

c1,c2,c3,c4,c5 = st.columns(5)
c1.metric(market_name, f"{price:.2f}")
c2.metric("EMA9/21/200", f"{ema9:.1f}/{ema21:.1f}/{ema200:.1f}")
c3.metric("RSI14", f"{rsi:.1f}")
c4.metric("SL", f"{sl:.2f}")
c5.metric("TP", f"{tp:.2f}")

fig = go.Figure()
fig.add_trace(go.Candlestick(x=df_main.index, open=df_main['Open'], high=df_main['High'], low=df_main['Low'], close=df_main['Close'], name="Price"))
fig.add_trace(go.Scatter(x=df_main.index, y=df_main['EMA9'], line=dict(color='#00E5FF', width=1.5), name='EMA9'))
fig.add_trace(go.Scatter(x=df_main.index, y=df_main['EMA21'], line=dict(color='#FF9100', width=1.5), name='EMA21'))
fig.add_trace(go.Scatter(x=df_main.index, y=df_main['EMA200'], line=dict(color='#FF00FF', width=2.5), name='EMA200'))
fig.add_trace(go.Scatter(x=df_main.index, y=df_main['VWAP'], line=dict(color='yellow', dash='dot'), name='VWAP'))
fig.add_hline(y=sl, line_dash="dash", line_color="red", annotation_text=f"SL {sl:.2f}")
fig.add_hline(y=tp, line_dash="dash", line_color="green", annotation_text=f"TP {tp:.2f}")
fig.update_layout(height=600, xaxis_rangeslider_visible=False, template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

colA, colB = st.columns(2)
with colA:
    f1=go.Figure(); f1.add_trace(go.Scatter(x=df_main.index, y=df_main['RSI'], line=dict(color='yellow'), name='RSI')); f1.add_hline(y=70, line_dash="dash", line_color="red"); f1.add_hline(y=30, line_dash="dash", line_color="green"); f1.update_layout(height=250, template="plotly_dark", title=f"RSI14 - {market_name}"); st.plotly_chart(f1, use_container_width=True)
with colB:
    f2=go.Figure(); f2.add_trace(go.Scatter(x=df_main.index, y=df_main['MACD'], line=dict(color='blue'), name='MACD')); f2.add_trace(go.Scatter(x=df_main.index, y=df_main['MACD_Sig'], line=dict(color='orange'), name='Signal')); f2.add_trace(go.Bar(x=df_main.index, y=df_main['MACD']-df_main['MACD_Sig'], name='Hist')); f2.update_layout(height=250, template="plotly_dark", title=f"MACD - {market_name}"); st.plotly_chart(f2, use_container_width=True)

st.caption(f"King V71 | Active: {market_name} TF:{timeframe} | Price:{price} EMA9:{ema9:.1f} EMA21:{ema21:.1f} EMA200:{ema200:.1f} RSI:{rsi:.1f} VWAP:{vwap:.1f}")
