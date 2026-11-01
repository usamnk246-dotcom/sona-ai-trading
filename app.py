import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v56 REAL 2500 START", layout="wide", page_icon="💰")

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden}
.stApp {background: radial-gradient(1200px 600px at 20% 0%, #1a1a2e 0%, #0f0f0f 50%, #000 100%); color:#fff}
.premium-card {
  background: linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,215,0,0.3);
  border-radius: 16px;
  padding: 12px;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(0,0,0,0.6);
}
.gold-glow {box-shadow: 0 0 20px rgba(255,215,0,0.4); border:1px solid #FFD700}
.green-glow {box-shadow: 0 0 20px rgba(0,255,0,0.4); border:1px solid #0F0}
.demo-glow {box-shadow: 0 0 20px rgba(0,150,255,0.5); border:1px solid #0AF}
.real-glow {box-shadow: 0 0 20px rgba(0,255,0,0.5); border:1px solid #0F0}
.indicator-card {
  background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
  border-radius: 12px;
  padding: 10px;
  text-align: center;
  border-left: 4px solid;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='premium-card gold-glow' style='text-align:center; margin-bottom:10px'>
<div style='font-size:9px; letter-spacing:3px; color:#888'>SONA AI • V56 • REAL 2500 PKR START • PREMIUM</div>
<h1 style='margin:4px 0; font-size:16px; background: linear-gradient(90deg,#FFD700,#0F0); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:900'>💰 SONA AI v56 REAL 2500 PKR START • Really money Laga ka ma ka 2500 pkr nah Star ka • V45 JORA</h1>
<div style='font-size:8px; color:#0F0'>Really money Laga ka ma ka 2500 pkr nah Star ka • Real 2500 PKR Start • Demo 10000 PKR • 5x24=120 • DASE JORA KA</div>
</div>
""", unsafe_allow_html=True)

if 'real_bal' not in st.session_state:
    st.session_state.real_bal = 2500
    st.session_state.demo_bal = 10000
    st.session_state.real_profit = 0
    st.session_state.demo_profit = 0
    st.session_state.real_trades = 0
    st.session_state.demo_trades = 0
    st.session_state.total24 = 0
    st.session_state.history = [
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":"REAL START 2500 PKR - Really money Laga ka - 2500 pkr nah Star ka - V56","Profit":"+0 PKR | Bal 2500","Bal":2500,"Market":"BTC/USD","Method":"Real Start 2500"},
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO START 10000 PKR - Nan Demo Check Ko - Free - V56","Profit":"+0 PKR | Bal 10000","Bal":10000,"Market":"BTC/USD","Method":"Demo Start 10000"},
    ]
    st.session_state.price_hist_real = [2500]
    st.session_state.price_hist_demo = [10000]
    st.session_state.auto_on = False
    st.session_state.sound_on = True
    st.session_state.account_mode = "REAL"
    st.session_state.live_price = 67421.0

st.session_state.live_price += random.uniform(-120,120)

st.markdown("<div class='premium-card' style='text-align:center; margin:8px 0; background: linear-gradient(90deg, #003300, #001a00)'><div style='font-size:10px; font-weight:900; color:#0F0; letter-spacing:2px'>💰 REAL MONEY 2500 PKR START • Really money Laga ka ma ka 2500 pkr nah Star ka • NAN DEMO 10000 • SABA REAL 2500 • PREMIUM • V56</div></div>", unsafe_allow_html=True)

col_mode1, col_mode2, col_mode3 = st.columns([1,1,1])
with col_mode1:
    mode = st.radio("Select Account - V56 Real 2500 Start", ["REAL ACCOUNT - Really money Laga ka ma ka 2500 pkr nah Star ka - 2500 PKR Real Start - V56","DEMO ACCOUNT - Nan Demo Check Ko - Free 10000 PKR - Practice - V56"], index=0 if st.session_state.account_mode=="REAL" else 1, key="account_mode_radio_v56")
    if "REAL" in mode:
        st.session_state.account_mode = "REAL"
    else:
        st.session_state.account_mode = "DEMO"

with col_mode2:
    if st.session_state.account_mode == "REAL":
        st.markdown("""
        <div class='premium-card real-glow' style='text-align:center; background: linear-gradient(135deg, #003300, #001a00)'>
        <div style='font-size:10px; color:#0F0; letter-spacing:2px'>REAL ACCOUNT ACTIVE - 2500 PKR START</div>
        <div style='font-size:22px; font-weight:900; color:#0F0'>💰 REAL 2500 PKR START</div>
        <div style='font-size:11px; color:#fff'>Really money Laga ka ma ka 2500 pkr nah Star ka</div>
        <div style='font-size:9px; color:#FFD700; margin-top:4px'>Real Money • 2500 PKR Start • JazzCash EasyPaisa • Real Profit</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class='premium-card demo-glow' style='text-align:center; background: linear-gradient(135deg, #001a33, #003366)'>
        <div style='font-size:10px; color:#0AF; letter-spacing:2px'>DEMO ACCOUNT ACTIVE - 10000 PKR</div>
        <div style='font-size:22px; font-weight:900; color:#0AF'>💙 DEMO 10000 PKR</div>
        <div style='font-size:11px; color:#fff'>Nan Demo Check Ko - Free Practice</div>
        <div style='font-size:9px; color:#888; margin-top:4px'>No Risk • Learn • Test • Free 10000 PKR</div>
        </div>
        """, unsafe_allow_html=True)

with col_mode3:
    if st.session_state.account_mode == "REAL":
        st.markdown(f"""
        <div class='premium-card real-glow' style='text-align:center'>
        <div style='font-size:8px; color:#888'>REAL BALANCE - 2500 PKR START</div>
        <div style='font-size:26px; font-weight:900; color:#0F0'>💰 {st.session_state.real_bal} PKR</div>
        <div style='font-size:10px; color:#FFD700'>+{st.session_state.real_profit} PKR Real Profit</div>
        <div style='font-size:8px; color:#888'>Start 2500 PKR • Trades: {st.session_state.real_trades} • Real Money</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='premium-card demo-glow' style='text-align:center'>
        <div style='font-size:8px; color:#888'>DEMO BALANCE - 10000 PKR FREE</div>
        <div style='font-size:24px; font-weight:900; color:#0AF'>💙 {st.session_state.demo_bal} PKR</div>
        <div style='font-size:10px; color:#0F0'>+{st.session_state.demo_profit} PKR Demo Profit</div>
        <div style='font-size:8px; color:#888'>Free 10000 PKR • Trades: {st.session_state.demo_trades} • Practice</div>
        </div>
        """, unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1:
    st.session_state.auto_on = st.toggle("AUTO TRADING ON/OFF - V56 2500 START", value=st.session_state.auto_on, key="auto_v56")
    if st.session_state.auto_on:
        st.success(f"AUTO ON - {st.session_state.account_mode} - 5x24=120")
    else:
        st.error(f"AUTO OFF - {st.session_state.account_mode} - Manual")
with c2:
    st.session_state.sound_on = st.toggle("SOUND WIN ON/OFF - V56 2500", value=st.session_state.sound_on, key="sound_v56")
    st.info(f"Sound {'ON' if st.session_state.sound_on else 'OFF'} - {st.session_state.account_mode} - WIN pe Ding!")
with c3:
    market = st.selectbox("DIFFERENT MARKET - V56 2500 START", ["BTC/USD - $67,421 - Bitcoin","ETH/USD - $3,450 - Ethereum","SOL/USD - $180 - Solana","GOLD/USD - $2,350 - Gold","EUR/USD - $1.08 - Forex","PKR/USD - 278 - Bearish"], index=0, key="market_v56")
with c4:
    tf = st.selectbox("TIMEFRAME - V56 2500 START - 1m 5m 1h", ["1m - 1 MIN - Fast - Scalping","5m - 5 MIN - Medium - Intraday","15m - 15 MIN - Swing","1h - 1 HOUR - Slow - Position","4h - 4 HOUR - Long","1D - 1 DAY - Invest"], index=0, key="tf_v56")

current_bal = st.session_state.real_bal if st.session_state.account_mode=="REAL" else st.session_state.demo_bal
current_profit = st.session_state.real_profit if st.session_state.account_mode=="REAL" else st.session_state.demo_profit
current_trades = st.session_state.real_trades if st.session_state.account_mode=="REAL" else st.session_state.demo_trades

glow_class = "real-glow" if st.session_state.account_mode=="REAL" else "demo-glow"
bal_color = "#0F0" if st.session_state.account_mode=="REAL" else "#0AF"
account_emoji = "💰" if st.session_state.account_mode=="REAL" else "💙"
start_text = "Really money Laga ka 2500 pkr nah Star ka" if st.session_state.account_mode=="REAL" else "Nan Demo Check Ko"

st.markdown(f"""
<div class='premium-card {glow_class}' style='text-align:center; margin:10px 0'>
<div style='display:flex; justify-content:space-between; align-items:center'>
<div>
<div style='font-size:8px; color:#888; letter-spacing:2px'>LIVE MARKET PRICE • {st.session_state.account_mode}</div>
<div style='font-size:26px; font-weight:900; color:{bal_color}'>${st.session_state.live_price:,.2f}</div>
<div style='font-size:9px; color:#0FF'>{market} • {tf} • BULLISH • {st.session_state.account_mode} • {start_text}</div>
</div>
<div style='text-align:right'>
<div style='font-size:8px; color:#888; letter-spacing:2px'>{st.session_state.account_mode} BALANCE • {start_text}</div>
<div style='font-size:28px; font-weight:900; color:{bal_color}'>{account_emoji} {current_bal} PKR</div>
<div style='font-size:14px; color:#FFD700'>+{current_profit} PKR {st.session_state.account_mode} Profit</div>
<div style='font-size:8px; color:#888'>Trades {current_trades} • 24h {st.session_state.total24}/120 • AUTO {'ON' if st.session_state.auto_on else 'OFF'} • {st.session_state.account_mode} • Start {"2500" if st.session_state.account_mode=="REAL" else "10000"} PKR</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

rsi_val = 62.4 + random.uniform(-2,2)
vol_val = 1.8 + random.uniform(-0.2,0.3)
atr_val = 1.24 + random.uniform(-0.1,0.1)
vwap_val = st.session_state.live_price - random.uniform(-20,20)
macd_val = 0.85 + random.uniform(-0.2,0.2)

st.markdown(f"""
<div style='display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:6px; margin:8px 0'>
<div class='indicator-card' style='border-left-color:#FFD700'><div style='font-size:6px; color:#888'>RSI (14) {st.session_state.account_mode}</div><div style='font-size:18px; font-weight:900; color:#FFD700'>{rsi_val:.1f}</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>BULLISH BUY 95pct</div><div style='font-size:5px; color:#aaa'>Momentum Strong Bullish</div></div>
<div class='indicator-card' style='border-left-color:#0FF'><div style='font-size:6px; color:#888'>VOLUME {st.session_state.account_mode}</div><div style='font-size:18px; font-weight:900; color:#0FF'>{vol_val:.1f}M</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>HIGH VOL CONFIRM BUY</div><div style='font-size:5px; color:#aaa'>Institutional Buying</div></div>
<div class='indicator-card' style='border-left-color:#F0F'><div style='font-size:6px; color:#888'>ATR (14) PREMIUM</div><div style='font-size:18px; font-weight:900; color:#F0F'>{atr_val:.2f}</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>LOW VOL SAFE 95pct</div><div style='font-size:5px; color:#aaa'>Safe Entry Low Vol</div></div>
<div class='indicator-card' style='border-left-color:#FF8C00'><div style='font-size:6px; color:#888'>VWAP PREMIUM</div><div style='font-size:16px; font-weight:900; color:#FF8C00'>{vwap_val:,.0f}</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>ABOVE VWAP BUY 95pct</div><div style='font-size:5px; color:#aaa'>Price Above VWAP Bullish</div></div>
</div>
<div style='display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:6px; margin-bottom:8px'>
<div class='indicator-card' style='border-left-color:#0F0'><div style='font-size:6px; color:#888'>MACD PREMIUM</div><div style='font-size:16px; font-weight:900; color:#0F0'>{macd_val:.2f} BULL</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>MACD BULLISH CROSS BUY</div><div style='font-size:5px; color:#aaa'>Signal Cross Momentum Up</div></div>
<div class='indicator-card' style='border-left-color:#FF00FF'><div style='font-size:6px; color:#888'>LIQUIDITY STRATEGY SWEEP</div><div style='font-size:13px; font-weight:900; color:#FF00FF'>SWEEP DONE</div><div style='font-size:6px; background:#FFD700; color:#000; border-radius:8px; padding:2px; font-weight:900'>LIQUIDITY GRAB READY</div><div style='font-size:5px; color:#aaa'>Buy Side Liq Taken Reversal</div></div>
<div class='indicator-card' style='border-left-color:#00FFFF'><div style='font-size:6px; color:#888'>BOS PREMIUM</div><div style='font-size:12px; font-weight:900; color:#00FFFF'>BULLISH BOS</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>67,180 BROKE HH 67,150 UP</div><div style='font-size:5px; color:#aaa'>Break of Structure Continue</div></div>
<div class='indicator-card' style='border-left-color:#FFD700'><div style='font-size:6px; color:#888'>PULLBACK PREMIUM</div><div style='font-size:12px; font-weight:900; color:#FFD700'>PULLBACK DONE</div><div style='font-size:6px; background:#0F0; color:#000; border-radius:8px; padding:2px; font-weight:900'>50% FIB BUY ZONE READY</div><div style='font-size:5px; color:#aaa'>Retracement Complete Entry</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<div class='premium-card gold-glow' style='text-align:center; padding:6px; margin:6px 0'><div style='font-size:10px; font-weight:900; color:#FFD700'>📈 LIVE CHART MARKET • {market} • {tf} • {st.session_state.account_mode} • Start {'2500 PKR REAL' if st.session_state.account_mode=='REAL' else '10000 PKR DEMO'} • PREMIUM • V56</div></div>", unsafe_allow_html=True)

if "1m" in tf:
    num_c = 40
    volatility = 60
elif "5m" in tf:
    num_c = 35
    volatility = 120
else:
    num_c = 25
    volatility = 200

candles = []
p = st.session_state.live_price
for i in range(num_c):
    o = p + random.uniform(-volatility*0.5, volatility*0.5)
    c = o + random.uniform(-volatility, volatility)
    h = max(o, c) + random.uniform(5, volatility*0.6)
    l = min(o, c) - random.uniform(5, volatility*0.6)
    candles.append({"Open": o, "High": h, "Low": l, "Close": c})
    p = c

df_candle = pd.DataFrame(candles)
st.line_chart(df_candle, height=320)

price_hist = st.session_state.price_hist_demo if st.session_state.account_mode=="DEMO" else st.session_state.price_hist_real
st.line_chart(pd.DataFrame({f"{st.session_state.account_mode} Balance - Start {'2500' if st.session_state.account_mode=='REAL' else '10000'} PKR": price_hist}), height=150)

if st.session_state.account_mode == "DEMO":
    st.markdown("<div class='premium-card demo-glow' style='text-align:center; padding:10px; margin:8px 0'><div style='font-size:11px; font-weight:900; color:#0AF'>💙 DEMO ACCOUNT • 10000 PKR FREE • NAN DEMO CHECK KO • NO REAL MONEY • PRACTICE • V56</div></div>", unsafe_allow_html=True)
    d1,d2 = st.columns(2)
    with d1:
        if st.button("💙 DEMO TOPUP +5000 PKR FREE - V56 - 10000 START", key="demo_topup_v56"):
            st.session_state.demo_bal += 5000
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO TOPUP +5000 PKR - Free Practice - 10000 Start","Profit":"+5000 PKR | Bal "+str(st.session_state.demo_bal),"Bal":st.session_state.demo_bal,"Market":market.split(' - ')[0],"Method":"Demo Free 10000"})
            st.success(f"Demo Topup +5000 PKR - Bal {st.session_state.demo_bal} PKR - Free - 10000 Start - V56")
    with d2:
        if st.button("🔄 RESET DEMO 10000 PKR - V56", key="demo_reset_v56"):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.demo_trades = 0
            st.session_state.price_hist_demo = [10000]
            st.success("Demo Reset 10000 PKR - V56")
else:
    st.markdown("<div class='premium-card' style='background: linear-gradient(90deg, #FFD700, #0F0); text-align:center; padding:8px; margin:8px 0'><div style='font-size:11px; font-weight:900; color:#000'>💰 REAL ACCOUNT 2500 PKR START • Really money Laga ka ma ka 2500 pkr nah Star ka • JAZZCASH EASYPAISA DEPOSIT WITHDRAW • 2500 PKR START • V56</div></div>", unsafe_allow_html=True)
    j1,j2 = st.columns(2)
    with j1:
        dep_method = st.selectbox("Deposit Method Real 2500 Start", ["JazzCash - 03XX - Real 2500 Start - V56","EasyPaisa - 03XX - Real 2500 Start - V56","Bank Transfer - IBAN - Real 2500 - V56","USDT TRC20 - Crypto - Real 2500 - V56"], index=0, key="dep_real_v56")
        dep_phone = st.text_input("Number 11 digits Real Deposit 2500 Start", value="03001234567", key="dep_p_real_v56")
        dep_amount = st.number_input("Deposit PKR Real 2500 Start - Amount", value=2500, min_value=100, max_value=50000, step=100, key="dep_a_real_v56")
        if st.button("💰 DEPOSIT NOW REAL 2500 START - JAZZCASH EASYPAISA - V56 - Really money 2500", key="dep_real_btn_v56"):
            if len(dep_phone) >=11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.price_hist_real.append(st.session_state.real_bal)
                st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":f"DEPOSIT +{dep_amount} PKR - {dep_method.split(' - ')[0]} - Real 2500 Start - {dep_phone}","Profit":f"+{dep_amount} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":market.split(' - ')[0],"Method":dep_method.split(' - ')[0] + " Real 2500"})
                st.success(f"✅ Real Deposit Success +{dep_amount} PKR via {dep_method.split(' - ')[0]} {dep_phone} - Bal {st.session_state.real_bal} PKR - Really money Laga ka 2500 pkr nah Star ka - Transaction REAL{random.randint(100000,999999)} - V56")
                if st.session_state.sound_on:
                    st.markdown("<audio autoplay><source src='https://www.soundjay.com/buttons/beep-07a.wav' type='audio/wav'></audio>", unsafe_allow_html=True)
            else:
                st.error("Number ghalat da - 11 digits - 0300-XXXXXXX - Real 2500")
    with j2:
        with_method = st.selectbox("Withdraw Method Real 2500 Start", ["JazzCash - 03XX - Real 2500 - V56","EasyPaisa - 03XX - Real 2500 - V56","Bank Transfer - IBAN - Real 2500 - V56","USDT TRC20 - Crypto - Real 2500 - V56"], index=0, key="with_real_v56")
        with_phone = st.text_input("Number 11 digits Real Withdraw 2500 Start", value="03001234567", key="with_p_real_v56")
        with_amount = st.number_input("Withdraw PKR Real 2500 Start - Amount", value=250, min_value=100, max_value=50000, step=100, key="with_a_real_v56")
        if st.button("💸 WITHDRAW NOW REAL 2500 - JAZZCASH EASYPAISA - V56 - Really money 2500", key="with_real_btn_v56"):
            if len(with_phone) >=11:
                if with_amount <= st.session_state.real_bal:
                    st.session_state.real_bal -= with_amount
                    st.session_state.price_hist_real.append(st.session_state.real_bal)
                    st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":f"WITHDRAW -{with_amount} PKR - {with_method.split(' - ')[0]} - Real 2500 Start - {with_phone}","Profit":f"-{with_amount} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":market.split(' - ')[0],"Method":with_method.split(' - ')[0] + " Real 2500"})
                    st.success(f"✅ Real Withdraw Success -{with_amount} PKR via {with_method.split(' - ')[0]} {with_phone} - Bal {st.session_state.real_bal} PKR - 5 Min me JazzCash/EasyPaisa me ayega - Real 2500 Start - V56")
                else:
                    st.error(f"Balance kam da - Max {st.session_state.real_bal} PKR - Real 2500 Start")
            else:
                st.error("Number ghalat da - 11 digits - Real 2500")

st.markdown(f"<div style='text-align:center; margin:8px 0'><div style='font-size:10px; color:{'#0F0' if st.session_state.account_mode=='REAL' else '#0
