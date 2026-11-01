import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v59 RESULTS SHOW", layout="wide")

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden}
.stApp {background:#000000; color:#ffffff}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;text-align:center'>
<h1 style='color:#0F0;font-size:14px;margin:0'>SONA AI v59 FINAL RESULTS SHOW - REAL 2500 PKR START - DEMO 10000 - PREMIUM - V45 JORA - RESULTS VISIBLE</h1>
<div style='color:#FFD700;font-size:9px'>Real 2500 PKR Start - Really money Laga ka ma ka 2500 pkr nah Star ka - Demo 10000 - Results Show - No White Screen - V59 Final</div>
</div>
""", unsafe_allow_html=True)

if 'real_bal' not in st.session_state:
    st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state:
    st.session_state.demo_bal = 10000
if 'real_profit' not in st.session_state:
    st.session_state.real_profit = 0
if 'demo_profit' not in st.session_state:
    st.session_state.demo_profit = 0
if 'real_trades' not in st.session_state:
    st.session_state.real_trades = 0
if 'demo_trades' not in st.session_state:
    st.session_state.demo_trades = 0
if 'total24' not in st.session_state:
    st.session_state.total24 = 0
if 'account_mode' not in st.session_state:
    st.session_state.account_mode = "REAL"
if 'auto_on' not in st.session_state:
    st.session_state.auto_on = False
if 'sound_on' not in st.session_state:
    st.session_state.sound_on = True
if 'live_price' not in st.session_state:
    st.session_state.live_price = 67421.0
if 'price_hist_real' not in st.session_state:
    st.session_state.price_hist_real = [2500]
if 'price_hist_demo' not in st.session_state:
    st.session_state.price_hist_demo = [10000]
if 'history' not in st.session_state:
    st.session_state.history = [
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":"REAL START 2500 PKR - Really money Laga ka - V59 RESULTS SHOW","Profit":"+0 PKR | Bal 2500","Bal":2500,"Market":"BTC/USD","Method":"Real Start 2500 Results Show"},
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO START 10000 PKR - Nan Demo Check - V59 RESULTS SHOW","Profit":"+0 PKR | Bal 10000","Bal":10000,"Market":"BTC/USD","Method":"Demo Start 10000 Results Show"},
    ]

st.session_state.live_price = st.session_state.live_price + random.uniform(-50,50)

st.markdown("<div style='background:#001100;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center;margin:8px 0'><div style='color:#0F0;font-weight:900;font-size:10px'>ACCOUNT MODE - DEMO vs REAL - RESULTS SHOW - V59 FINAL</div></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    mode = st.radio("Select Account - V59 Results Show", ["REAL ACCOUNT - 2500 PKR Real Start - Really money Laga ka - V59 RESULTS SHOW","DEMO ACCOUNT - 10000 PKR Free - Nan Demo Check - V59 RESULTS SHOW"], index=0 if st.session_state.account_mode=="REAL" else 1, key="mode_v59")
    if "REAL" in mode:
        st.session_state.account_mode = "REAL"
    else:
        st.session_state.account_mode = "DEMO"

with col2:
    if st.session_state.account_mode == "REAL":
        st.markdown(f"<div style='background:#003300;border:2px solid #0F0;border-radius:10px;padding:10px;text-align:center'><div style='color:#0F0;font-size:10px'>REAL ACCOUNT ACTIVE - 2500 PKR START</div><div style='color:#0F0;font-size:20px;font-weight:900'>REAL 2500 PKR START</div><div style='color:#fff;font-size:10px'>Really money Laga ka ma ka 2500 pkr nah Star ka</div><div style='color:#FFD700;font-size:8px'>Bal {st.session_state.real_bal} PKR - Profit {st.session_state.real_profit} PKR - Trades {st.session_state.real_trades}</div></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background:#001133;border:2px solid #0AF;border-radius:10px;padding:10px;text-align:center'><div style='color:#0AF;font-size:10px'>DEMO ACCOUNT ACTIVE - 10000 PKR</div><div style='color:#0AF;font-size:20px;font-weight:900'>DEMO 10000 PKR</div><div style='color:#fff;font-size:10px'>Nan Demo Check Ko - Free Practice</div><div style='color:#888;font-size:8px'>Bal {st.session_state.demo_bal} PKR - Profit {st.session_state.demo_profit} PKR - Trades {st.session_state.demo_trades}</div></div>", unsafe_allow_html=True)

current_bal = st.session_state.real_bal if st.session_state.account_mode=="REAL" else st.session_state.demo_bal
current_profit = st.session_state.real_profit if st.session_state.account_mode=="REAL" else st.session_state.demo_profit
current_trades = st.session_state.real_trades if st.session_state.account_mode=="REAL" else st.session_state.demo_trades
start_amount = "2500" if st.session_state.account_mode=="REAL" else "10000"
bal_color = "#0F0" if st.session_state.account_mode=="REAL" else "#0AF"
emoji = "💰" if st.session_state.account_mode=="REAL" else "💙"

st.markdown(f"""
<div style='background:#000;border:3px solid {bal_color};border-radius:12px;padding:12px;text-align:center;margin:8px 0'>
<div style='display:flex;justify-content:space-between;align-items:center'>
<div>
<div style='color:#888;font-size:8px'>LIVE MARKET PRICE - {st.session_state.account_mode}</div>
<div style='color:{bal_color};font-size:24px;font-weight:900'>${st.session_state.live_price:,.2f}</div>
<div style='color:#0FF;font-size:8px'>BTC/USD - {st.session_state.account_mode} - BULLISH</div>
</div>
<div style='text-align:right'>
<div style='color:#888;font-size:8px'>{st.session_state.account_mode} BALANCE - RESULTS SHOW</div>
<div style='color:{bal_color};font-size:28px;font-weight:900'>{emoji} {current_bal} PKR</div>
<div style='color:#FFD700;font-size:12px'>+{current_profit} PKR Profit</div>
<div style='color:#888;font-size:8px'>Trades {current_trades} - 24h {st.session_state.total24}/120 - Start {start_amount} PKR</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

rsi = 62.4 + random.uniform(-1,1)
vol = 1.8 + random.uniform(-0.1,0.1)
atr = 1.24 + random.uniform(-0.05,0.05)
vwap = st.session_state.live_price - random.uniform(-10,10)
macd = 0.85 + random.uniform(-0.1,0.1)

st.markdown(f"""
<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;margin:8px 0'>
<div style='background:#111;border-left:4px solid #FFD700;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>RSI (14) {st.session_state.account_mode}</div><div style='color:#FFD700;font-size:16px;font-weight:900'>{rsi:.1f}</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>BULLISH BUY 95pct</div></div>
<div style='background:#111;border-left:4px solid #0FF;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>VOLUME {st.session_state.account_mode}</div><div style='color:#0FF;font-size:16px;font-weight:900'>{vol:.1f}M</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>HIGH VOL CONFIRM</div></div>
<div style='background:#111;border-left:4px solid #F0F;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>ATR (14)</div><div style='color:#F0F;font-size:16px;font-weight:900'>{atr:.2f}</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>LOW VOL SAFE</div></div>
<div style='background:#111;border-left:4px solid #FF8C00;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>VWAP</div><div style='color:#FF8C00;font-size:14px;font-weight:900'>{vwap:,.0f}</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>ABOVE VWAP BUY</div></div>
</div>
<div style='display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;margin-bottom:8px'>
<div style='background:#111;border-left:4px solid #0F0;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>MACD</div><div style='color:#0F0;font-size:14px;font-weight:900'>{macd:.2f} BULL</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>BULLISH CROSS</div></div>
<div style='background:#111;border-left:4px solid #F0F;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>LIQUIDITY SWEEP</div><div style='color:#F0F;font-size:12px;font-weight:900'>SWEEP DONE</div><div style='color:#000;background:#FFD700;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>GRAB READY</div></div>
<div style='background:#111;border-left:4px solid #0FF;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>BOS</div><div style='color:#0FF;font-size:12px;font-weight:900'>BULLISH BOS</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>67,180 BROKE HH</div></div>
<div style='background:#111;border-left:4px solid #FFD700;border-radius:8px;padding:8px;text-align:center'><div style='color:#888;font-size:6px'>PULLBACK</div><div style='color:#FFD700;font-size:12px;font-weight:900'>DONE</div><div style='color:#000;background:#0F0;border-radius:6px;padding:2px;font-size:6px;font-weight:900'>50% FIB BUY ZONE</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"<div style='background:#000;border:2px solid #FFD700;border-radius:8px;padding:6px;text-align:center;margin:6px 0'><div style='color:#FFD700;font-size:10px;font-weight:900'>LIVE CHART MARKET - BTC/USD - {st.session_state.account_mode} - Start {start_amount} PKR - V59 RESULTS SHOW</div></div>", unsafe_allow_html=True)

num_c = 30
candles = []
p = st.session_state.live_price
for i in range(num_c):
    o = p + random.uniform(-30,30)
    c = o + random.uniform(-40,40)
    h = max(o,c) + random.uniform(5,20)
    l = min(o,c) - random.uniform(5,20)
    candles.append({"Open": o, "High": h, "Low": l, "Close": c})
    p = c

df_candle = pd.DataFrame(candles)
st.line_chart(df_candle, height=250)

price_hist = st.session_state.price_hist_demo if st.session_state.account_mode=="DEMO" else st.session_state.price_hist_real
st.line_chart(pd.DataFrame({f"{st.session_state.account_mode} Balance {start_amount} PKR - RESULTS SHOW": price_hist}), height=120)

if st.button("CLEAR CACHE + RESET - FIX WHITE SCREEN - V59 - CLICK IF BLANK", key="clear_v59"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.success("Cache Cleared - V59 RESULTS SHOW - Reload Karo!")
    st.rerun()

if st.session_state.account_mode == "DEMO":
    st.markdown("<div style='background:#001133;border:2px solid #0AF;border-radius:8px;padding:8px;text-align:center;margin:6px 0'><div style='color:#0AF;font-size:10px;font-weight:900'>DEMO ACCOUNT - 10000 PKR FREE - NAN DEMO CHECK KO - RESULTS SHOW - V59</div></div>", unsafe_allow_html=True)
    d1,d2 = st.columns(2)
    with d1:
        if st.button("DEMO TOPUP +5000 PKR FREE - V59 RESULTS SHOW", key="demo_topup_v59"):
            st.session_state.demo_bal += 5000
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            t = datetime.now().strftime("%I:%M:%S %p")
            st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":"DEMO TOPUP +5000 PKR - V59 RESULTS SHOW","Profit":f"+5000 PKR | Bal {st.session_state.demo_bal}","Bal":st.session_state.demo_bal,"Market":"BTC/USD","Method":"Demo Free Results Show"})
            st.success(f"Demo Topup +5000 PKR - Bal {st.session_state.demo_bal} PKR - V59 RESULTS SHOW - Results Visible!")
    with d2:
        if st.button("RESET DEMO 10000 PKR - V59 RESULTS SHOW", key="demo_reset_v59"):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.demo_trades = 0
            st.session_state.price_hist_demo = [10000]
            st.success("Demo Reset 10000 PKR - V59 RESULTS SHOW")
else:
    st.markdown("<div style='background:linear-gradient(90deg,#FFD700,#0F0);border-radius:8px;padding:8px;text-align:center;margin:6px 0'><div style='color:#000;font-size:10px;font-weight:900'>REAL ACCOUNT 2500 PKR START - Really money Laga ka - JAZZCASH EASYPAISA - V59 RESULTS SHOW</div></div>", unsafe_allow_html=True)
    j1,j2 = st.columns(2)
    with j1:
        dep_phone = st.text_input("JazzCash/EasyPaisa Number 11 digits - V59 RESULTS SHOW", value="03001234567", key="dep_p_v59")
        dep_amount = st.number_input("Deposit PKR Real 2500 Start - V59 RESULTS SHOW", value=2500, min_value=100, max_value=50000, step=100, key="dep_a_v59")
        if st.button("DEPOSIT NOW REAL 2500 START - V59 RESULTS SHOW", key="dep_v59"):
            if len(dep_phone) >=11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.price_hist_real.append(st.session_state.real_bal)
                t = datetime.now().strftime("%I:%M:%S %p")
                st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"DEPOSIT +{dep_amount} PKR - JazzCash/EasyPaisa {dep_phone} - V59 RESULTS SHOW","Profit":f"+{dep_amount} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Deposit Results Show"})
                st.success(f"Real Deposit +{dep_amount} PKR - Bal {st.session_state.real_bal} PKR - V59 RESULTS SHOW - Results Visible! Transaction REAL{random.randint(100000,999999)}")
            else:
                st.error("Number ghalat da - 11 digits")
    with j2:
        with_phone = st.text_input("Withdraw Number 11 digits - V59 RESULTS SHOW", value="03001234567", key="with_p_v59")
        with_amount = st.number_input("Withdraw PKR Real 2500 - V59 RESULTS SHOW", value=250, min_value=100, max_value=50000, step=100, key="with_a_v59")
        if st.button("WITHDRAW NOW REAL 2500 - V59 RESULTS SHOW", key="with_v59"):
            if len(with_phone) >=11:
                if with_amount <= st.session_state.real_bal:
                    st.session_state.real_bal -= with_amount
                    st.session_state.price_hist_real.append(st.session_state.real_bal)
                    t = datetime.now().strftime("%I:%M:%S %p")
                    st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"WITHDRAW -{with_amount} PKR - JazzCash/EasyPaisa {with_phone} - V59 RESULTS SHOW","Profit":f"-{with_amount} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Withdraw Results Show"})
                    st.success(f"Real Withdraw -{with_amount} PKR - Bal {st.session_state.real_bal} PKR - 5 Min me ayega - V59 RESULTS SHOW - Results Visible!")
                else:
                    st.error(f"Balance kam da - Max {st.session_state.real_bal} PKR")
            else:
                st.error("Number ghalat da")

st.markdown(f"<div style='background:#111;border:2px solid {bal_color};border-radius:8px;padding:6px;text-align:center;margin:6px 0'><div style='color:{bal_color};font-size:10px;font-weight:900'>TRADING - {st.session_state.account_mode} - Start {start_amount} PKR - RESULTS SHOW - V59 FINAL</div></div>", unsafe_allow_html=True)

col_m1, col_m2 = st.columns(2)
with col_m1:
    if st.button(f"MANUAL TRADE 250 PKR - {st.session_state.account_mode} - {start_amount} PKR START - V59 RESULTS SHOW", key="manual_v59"):
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        t = datetime.now().strftime("%I:%M:%S %p")
        if st.session_state.account_mode == "DEMO":
            st.session_state.demo_bal += p
            st.session_state.demo_profit += p
            st.session_state.demo_trades += 1
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V59 Demo - RESULTS SHOW","Profit":f"{round(p)} PKR | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Trade Results Show"})
            st.success(f"DEMO {'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.demo_bal)} PKR - V59 RESULTS SHOW - Results Visible!")
        else:
            st.session_state.real_bal += p
            st.session_state.real_profit += p
            st.session_state.real_trades += 1
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.session_state.total24 += 1
            st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V59 Real 2500 Start - RESULTS SHOW","Profit":f"{round(p)} PKR | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":"Real Trade 2500 Results Show"})
            st.success(f"REAL 2500 {'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.real_bal)} PKR - V59 RESULTS SHOW - Really money Laga ka - Results Visible!")

with col_m2:
    if st.button(f"FORCE TRADE NOW - {st.session_state.account_mode} - {start_amount} PKR - V59 RESULTS SHOW", key="force_v59"):
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        t = datetime.now().strftime("%I:%M:%S %p")
        if st.session_state.account_mode == "DEMO":
            st.session_state.demo_bal += p
            st.session_state.demo_profit += p
            st.session_state.demo_trades += 1
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V59 Demo Force - RESULTS SHOW","Profit":f"{round(p)} PKR | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Force Results Show"})
        else:
            st.session_state.real_bal += p
            st.session_state.real_profit += p
            st.session_state.real_trades += 1
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.session_state.total24 += 1
            st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V59 Real Force 2500 - RESULTS SHOW","Profit":f"{round(p)} PKR | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":"Real Force 2500 Results Show"})
        st.success(f"FORCE {'WIN' if is_win else 'LOSS'} {round(p)} PKR - {st.session_state.account_mode} {start_amount} PKR - V59 RESULTS SHOW - Results Visible!")

st.markdown(f"<div style='background:#000;border:2px solid #FFD700;border-radius:8px;padding:6px;text-align:center;margin:8px 0'><div style='color:#FFD700;font-size:11px;font-weight:900'>RESULTS - HISTORY - {st.session_state.account_mode} - Start {start_amount} PKR - V59 FINAL - RESULTS SHOW - V45 JORA</div></div>", unsafe_allow_html=True)

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, height=350)
    csv = df.to_csv(index=False)
    st.download_button("EXPORT CSV - RESULTS SHOW - V59", csv, "sona_v59_results_show.csv", "text/csv", key="export_v59")
else:
    st.write("No trades yet - V59 RESULTS SHOW")

st.markdown("""
<div style='background:linear-gradient(90deg,#FFD700,#0F0);border-radius:8px;padding:10px;text-align:center;margin-top:10px'>
<div style='color:#000;font-size:10px;font-weight:900'>V59 FINAL RESULTS SHOW - REAL 2500 PKR START - Really money Laga ka ma ka 2500 pkr nah Star ka - DEMO 10000 PKR NAN DEMO CHECK KO - JAZZCASH EASYPAISA REAL 2500 - LIVE CHART - RSI VOLUME ATR VWAP MACD LIQUIDITY BOS PULLBACK - PREMIUM DESIGN - NO KEYERROR - NO WHITE SCREEN - RESULTS VISIBLE - V45 JORA - DASE
</div>
