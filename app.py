import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="SONA AI + KING 103 WAR - FINAL", page_icon="👑", layout="wide")

st.markdown("""<div style="background: linear-gradient(90deg, #000, #FFD700); padding:15px; border-radius:15px; text-align:center;">
<h2>👑 SONA AI + KING 103 WAR + SONI MORNING STRATEGY 👑</h2>
<p>EMA 9/21/50/200 | RSI14 | MACD | VWAP | ATR14 | Volume | BOS | Liquidity Sweep | Pullback</p>
</div>""", unsafe_allow_html=True)

@st.cache_data(ttl=60)
def get_data(tf):
    try:
        period_map = {"15m": "5d", "5m": "2d", "1m": "1d"}
        df = yf.download("GC=F", period=period_map.get(tf,"5d"), interval=tf, progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df.dropna()
        if len(df) < 50: return None
        
        # EMA - Tumhara Sara
        df['EMA9'] = df['Close'].ewm(span=9).mean()
        df['EMA21'] = df['Close'].ewm(span=21).mean()
        df['EMA50'] = df['Close'].ewm(span=50).mean()
        df['EMA200'] = df['Close'].ewm(span=200).mean()
        
        # RSI 14
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # MACD
        exp1 = df['Close'].ewm(span=12).mean()
        exp2 = df['Close'].ewm(span=26).mean()
        df['MACD'] = exp1 - exp2
        df['MACD_SIGNAL'] = df['MACD'].ewm(span=9).mean()
        
        # VWAP - Volume Weighted
        typical = (df['High'] + df['Low'] + df['Close'])/3
        df['VWAP'] = (typical * df['Volume']).cumsum() / df['Volume'].cumsum()
        
        # ATR 14
        df['ATR'] = (df['High'] - df['Low']).rolling(14).mean()
        
        # BOS - Break of Structure
        df['SwingHigh'] = df['High'].rolling(20).max()
        df['SwingLow'] = df['Low'].rolling(20).min()
        df['BOS_Bull'] = df['Close'] > df['SwingHigh'].shift(1)
        df['BOS_Bear'] = df['Close'] < df['SwingLow'].shift(1)
        
        # Liquidity Sweep
        df['Liq_Sweep_Buy'] = (df['Low'] < df['SwingLow'].shift(1)) & (df['Close'] > df['SwingLow'].shift(1))
        df['Liq_Sweep_Sell'] = (df['High'] > df['SwingHigh'].shift(1)) & (df['Close'] < df['SwingHigh'].shift(1))
        
        # Pullback
        df['Pullback_Buy'] = (df['Close'] <= df['EMA21']) & (df['Close'] >= df['EMA50'])
        df['Pullback_Sell'] = (df['Close'] >= df['EMA21']) & (df['Close'] <= df['EMA50'])
        
        return df.tail(100)
    except:
        return None

tf_list = ["15m", "5m", "1m"]
all_data = {}
cols = st.columns(3)

for i, tf in enumerate(tf_list):
    df = get_data(tf)
    if df is not None:
        last = df.iloc[-1]
        price = float(last['Close'])
        ema9 = float(last['EMA9']); ema21 = float(last['EMA21'])
        ema50 = float(last['EMA50']); ema200 = float(last['EMA200'])
        rsi = float(last['RSI']); macd = float(last['MACD'])
        macd_sig = float(last['MACD_SIGNAL']); vwap = float(last['VWAP'])
        atr = float(last['ATR']); vol = float(last['Volume'])
        avg_vol = float(df['Volume'].tail(20).mean())
        
        bos_bull = bool(last['BOS_Bull']); bos_bear = bool(last['BOS_Bear'])
        liq_buy = bool(last['Liq_Sweep_Buy']); liq_sell = bool(last['Liq_Sweep_Sell'])
        pull_buy = bool(last['Pullback_Buy']); pull_sell = bool(last['Pullback_Sell'])
        
        # KING 103 + SONI SCORING - Da Tol Pa Ka
        score = 0
        reason = []
        # EMA 9/21 cross
        if ema9 > ema21: score+=1; reason.append("EMA9>21")
        if price > ema50: score+=1; reason.append("Price>50")
        if price > ema200: score+=1; reason.append("Price>200")
        # RSI
        if 50 < rsi < 70: score+=1; reason.append(f"RSI {rsi:.0f}")
        # MACD
        if macd > macd_sig: score+=1; reason.append("MACD Bull")
        # VWAP
        if price > vwap: score+=1; reason.append("VWAP>")
        # Volume
        if vol > avg_vol: score+=1; reason.append("Vol High")
        # BOS
        if bos_bull: score+=1; reason.append("BOS Bull")
        # Liquidity Sweep + Pullback
        if liq_buy or pull_buy: score+=1; reason.append("LiqSweep/Pullback")
        
        # Final Signal
        signal = "BUY" if score >= 5 else "SELL" if score <= 3 else "NEUTRAL"
        if liq_buy and bos_bull and score>=4: signal = "STRONG BUY"
        if liq_sell and bos_bear: signal = "STRONG SELL"
        
        all_data[tf] = {"price":price, "score":score, "signal":signal, "rsi":rsi, "reason":",".join(reason), "atr":atr, "bos":bos_bull, "liq":liq_buy}
        
        with cols[i]:
            st.subheader(f"⏰ {tf} - Score {score}/9")
            st.metric("Price", f"{price:.2f}", f"RSI {rsi:.0f}")
            st.write(f"EMA 9/21/50/200: {ema9:.1f}/{ema21:.1f}/{ema50:.1f}/{ema200:.1f}")
            st.write(f"VWAP: {vwap:.1f} | ATR: {atr:.2f}")
            st.write(f"BOS: {'✅' if bos_bull else '❌'} | Liq Sweep: {'✅' if liq_buy else '❌'} | Pullback: {'✅' if pull_buy else '❌'}")
            if "BUY" in signal: st.success(f"▲ {signal} - {','.join(reason)}")
            elif "SELL" in signal: st.error(f"▼ {signal}")
            else: st.warning(signal)

# FINAL DECISION - SONI + KING 103 WAR
if len(all_data)==3:
    buy_count = sum(1 for v in all_data.values() if "BUY" in v["signal"])
    sell_count = sum(1 for v in all_data.values() if "SELL" in v["signal"])
    avg_score = np.mean([v["score"] for v in all_data.values()])
    curr_price = all_data["5m"]["price"]; curr_atr = all_data["5m"]["atr"]
    quality = min((buy_count*30 + int(avg_score*10)), 95) if buy_count>=sell_count else min((sell_count*30 + int((9-avg_score)*10)),95)
    
    st.divider()
    st.header("🎯 FINAL DECISION - SONA + KING 103 WAR + LIQUIDITY")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Avg Score", f"{avg_score:.1f}/9"); c2.metric("BUY TFs", f"{buy_count}/3")
    c3.metric("SELL TFs", f"{sell_count}/3"); c4.metric("Quality", f"{quality:.0f}%")
    st.progress(quality/100)
    
    sl = curr_price - curr_atr*1.2 if buy_count>=2 else curr_price + curr_atr*1.2
    tp = curr_price + curr_atr*1.5 if buy_count>=2 else curr_price - curr_atr*1.5
    
    st.subheader("🔔 KHAPEL ALERT - King 103 + Soni War")
    alert_on = st.toggle("🔔 Alert ON - Liquidity + BOS + Pullback", value=False)
    
    if buy_count==3 and quality>=80:
        st.success(f"✅ STRONG BUY CONFIRMED - KING 103 WAR - {curr_price:.2f} Q {quality:.0f}%")
        st.write(f"Entry {curr_price:.2f} SL {sl:.2f} TP {tp:.2f} - EMA50/200 + RSI + MACD + VWAP + BOS + Liq Sweep OK")
        if alert_on: st.balloons(); st.components.v1.html(f"""<script>new Notification('👑 KING 103 BUY!',{{body:'{curr_price:.2f} Q{quality:.0f}%'}})</script><audio autoplay><source src="https://www.soundjay.com/buttons/beep-07a.wav"></audio>""", height=80)
    elif buy_count>=2:
        st.success(f"✅ BUY SIGNAL - {buy_count}/3 TFs - {curr_price:.2f}")
        if alert_on: st.toast("BUY Alert Baja!")
    elif sell_count==3:
        st.error(f"▼ STRONG SELL CONFIRMED - {curr_price:.2f} Q {quality:.0f}%")
        if alert_on: st.components.v1.html(f"""<script>new Notification('KING 103 SELL!',{{body:'{curr_price:.2f}'}})</script><audio autoplay><source src="https://www.soundjay.com/buttons/beep-07a.wav"></audio>""", height=80)
    else:
        st.info(f"⏸️ WAIT - No BOS/Liquidity Setup Yet - Score {avg_score:.1f}")
        if alert_on: 
            st.info("60 sec me auto check..."); time.sleep(60); st.rerun()

    st.write(f"**Entry:** {curr_price:.2f} | **SL:** {sl:.2f} | **TP:** {tp:.2f}")
    with st.expander("📊 Full Soni + King 103 Details - VWAP/BOS/Liquidity"): st.json(all_data)

st.button("🔄 Refresh War Mode")
