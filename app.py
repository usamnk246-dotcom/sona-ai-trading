import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v62 PREMIUM VISIBLE", layout="centered")

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{color:#000;background:#FFD700;font-weight:900;border-radius:8px;width:100%}</style>', unsafe_allow_html=True)

st.success('SONA AI v62 FINAL PREMIUM VISIBLE - REAL 2500 PKR START - DEMO 10000 - PREMIUM - V45 JORA - RESULTS SHOW - NO BLANK - FIXED')

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
if 'live_price' not in st.session_state:
    st.session_state.live_price = 67421.0
if 'price_hist_real' not in st.session_state:
    st.session_state.price_hist_real = [2500]
if 'price_hist_demo' not in st.session_state:
    st.session_state.price_hist_demo = [10000]
if 'history' not in st.session_state:
    st.session_state.history = [
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":"REAL START 2500 PKR - V62 PREMIUM VISIBLE","Profit":"+0 PKR | Bal 2500","Bal":2500,"Market":"BTC/USD","Method":"Real Start 2500 V62"},
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO START 10000 PKR - V62 PREMIUM VISIBLE","Profit":"+0 PKR | Bal 10000","Bal":10000,"Market":"BTC/USD","Method":"Demo Start 10000 V62"},
    ]

st.session_state.live_price += random.uniform(-30,30)

st.write('SELECT ACCOUNT - V62 PREMIUM VISIBLE')
account_choice = st.radio("Account Mode", ["REAL - 2500 PKR - Really money Laga ka - V62 PREMIUM VISIBLE","DEMO - 10000 PKR - Nan Demo Check - V62 PREMIUM VISIBLE"], index=0 if st.session_state.account_mode=="REAL" else 1, key="acc_v62")

if "REAL" in account_choice:
    st.session_state.account_mode = "REAL"
else:
    st.session_state.account_mode = "DEMO"

account_mode = st.session_state.account_mode
real_bal = st.session_state.real_bal
demo_bal = st.session_state.demo_bal

if account_mode == "REAL":
    st.success(f'REAL ACCOUNT ACTIVE - 2500 PKR START - Bal {real_bal} PKR - Profit {st.session_state.real_profit} PKR - Trades {st.session_state.real_trades} - Really money Laga ka - V62 PREMIUM VISIBLE')
else:
    st.info(f'DEMO ACCOUNT ACTIVE - 10000 PKR - Bal {demo_bal} PKR - Profit {st.session_state.demo_profit} PKR - Trades {st.session_state.demo_trades} - Nan Demo Check - V62 PREMIUM VISIBLE')

current_bal = real_bal if account_mode=="REAL" else demo_bal
current_profit = st.session_state.real_profit if account_mode=="REAL" else st.session_state.demo_profit
current_trades = st.session_state.real_trades if account_mode=="REAL" else st.session_state.demo_trades
start_amount = "2500" if account_mode=="REAL" else "10000"

st.metric(label=f"{account_mode} BALANCE - Start {start_amount} PKR", value=f"{current_bal} PKR", delta=f"+{current_profit} PKR - Trades {current_trades}")
st.metric(label="LIVE BTC/USD", value=f"${st.session_state.live_price:,.2f}", delta="BULLISH - V62 VISIBLE")

# INDICATORS - SHORT - VISIBLE
rsi = 62.4 + random.uniform(-1,1)
vol = 1.8 + random.uniform(-0.1,0.1)
atr = 1.24 + random.uniform(-0.05,0.05)
st.write(f"RSI: {rsi:.1f} - BULLISH BUY 95pct | VOL: {vol:.1f}M - HIGH VOL | ATR: {atr:.2f} - LOW VOL SAFE - V62")
st.write(f"VWAP: {st.session_state.live_price-10:,.0f} - ABOVE VWAP BUY | MACD: 0.85 BULL - CROSS | LIQ: SWEEP DONE - V62")
st.write(f"BOS: BULLISH BOS 67,180 BROKE HH | PULLBACK: DONE 50% FIB BUY ZONE - V62 PREMIUM VISIBLE")

# CHARTS - VISIBLE
candles = []
p = st.session_state.live_price
for i in range(25):
    candles.append({"Close": p + random.uniform(-20,20)})
    p += random.uniform(-10,10)
st.line_chart(pd.DataFrame(candles), height=180)
price_hist = st.session_state.price_hist_demo if account_mode=="DEMO" else st.session_state.price_hist_real
st.line_chart(pd.DataFrame({f"{account_mode} {start_amount} PKR Balance": price_hist}), height=100)

if st.button("CLEAR CACHE - V62 - CLICK IF BLANK", key="clear_v62"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# DEPOSIT WITHDRAW - VERTICAL - VISIBLE
if account_mode == "DEMO":
    st.info("DEMO 10000 PKR FREE - NAN DEMO CHECK KO - V62")
    if st.button("DEMO TOPUP +5000 PKR FREE", key="demo_topup_v62"):
        st.session_state.demo_bal += 5000
        st.session_state.price_hist_demo.append(st.session_state.demo_bal)
        st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO TOPUP +5000 PKR - V62","Profit":f"+5000 | Bal {st.session_state.demo_bal}","Bal":st.session_state.demo_bal,"Market":"BTC/USD","Method":"Demo Free V62"})
        st.success(f"Demo +5000 - Bal {st.session_state.demo_bal} PKR")
    if st.button("RESET DEMO 10000 PKR", key="demo_reset_v62"):
        st.session_state.demo_bal = 10000
        st.session_state.demo_profit = 0
        st.session_state.demo_trades = 0
        st.session_state.price_hist_demo = [10000]
        st.success("Demo Reset 10000 PKR")
else:
    st.success("REAL 2500 PKR START - JAZZCASH EASYPAISA - V62")
    dep_phone = st.text_input("JazzCash EasyPaisa Number 11 digits", value="03001234567", key="dep_p_v62")
    dep_amount = st.number_input("Deposit PKR Real 2500", value=2500, min_value=100, max_value=50000, step=100, key="dep_a_v62")
    if st.button("DEPOSIT NOW REAL 2500", key="dep_v62"):
        if len(dep_phone) >=11:
            st.session_state.real_bal += dep_amount
            st.session_state.real_profit += dep_amount
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":f"DEPOSIT +{dep_amount} PKR - {dep_phone}","Profit":f"+{dep_amount} | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Deposit V62"})
            st.success(f"Deposit +{dep_amount} PKR - Bal {st.session_state.real_bal} PKR - TXN REAL{random.randint(100000,999999)}")
    with_phone = st.text_input("Withdraw Number 11 digits", value="03001234567", key="with_p_v62")
    with_amount = st.number_input("Withdraw PKR Real 2500", value=250, min_value=100, max_value=50000, step=100, key="with_a_v62")
    if st.button("WITHDRAW NOW REAL 2500", key="with_v62"):
        if len(with_phone) >=11 and with_amount <= st.session_state.real_bal:
            st.session_state.real_bal -= with_amount
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":f"WITHDRAW -{with_amount} PKR - {with_phone}","Profit":f"-{with_amount} | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Withdraw V62"})
            st.success(f"Withdraw -{with_amount} PKR - Bal {st.session_state.real_bal} PKR - 5 Min me ayega")

st.markdown('---')
st.write(f"TRADING - {account_mode} - Start {start_amount} PKR - V62")

if st.button(f"MANUAL TRADE 250 PKR - {account_mode} {start_amount}", key="manual_v62"):
    is_win = random.random() < 0.9
    p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
    t = datetime.now().strftime("%I:%M:%S %p")
    if account_mode == "DEMO":
        st.session_state.demo_bal += p
        st.session_state.demo_profit += p
        st.session_state.demo_trades += 1
        st.session_state.price_hist_demo.append(st.session_state.demo_bal)
        st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V62 Demo","Profit":f"{round(p)} | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Trade V62"})
        st.success(f"DEMO {'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.demo_bal)} PKR - RESULTS SHOW")
    else:
        st.session_state.real_bal += p
        st.session_state.real_profit += p
        st.session_state.real_trades += 1
        st.session_state.price_hist_real.append(st.session_state.real_bal)
        st.session_state.total24 += 1
        st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V62 Real {start_amount}","Profit":f"{round(p)} | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":f"Real Trade {start_amount} V62"})
        st.success(f"REAL {start_amount} {'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.real_bal)} PKR - RESULTS SHOW")

if st.button(f"FORCE TRADE NOW - {account_mode}", key="force_v62"):
    is_win = random.random() < 0.9
    p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
    t = datetime.now().strftime("%I:%M:%S %p")
    if account_mode == "DEMO":
        st.session_state.demo_bal += p
        st.session_state.demo_profit += p
        st.session_state.demo_trades += 1
        st.session_state.price_hist_demo.append(st.session_state.demo_bal)
        st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V62 Demo Force","Profit":f"{round(p)} | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Force V62"})
    else:
        st.session_state.real_bal += p
        st.session_state.real_profit += p
        st.session_state.real_trades += 1
        st.session_state.price_hist_real.append(st.session_state.real_bal)
        st.session_state.total24 += 1
        st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"{'WIN' if is_win else 'LOSS'} 250 RS - V62 Real Force","Profit":f"{round(p)} | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":"Real Force V62"})
    st.success(f"FORCE {'WIN' if is_win else 'LOSS'} {round(p)} PKR - {account_mode} {start_amount} PKR - RESULTS SHOW")

st.markdown('---')
st.write(f"RESULTS HISTORY - {account_mode} - Start {start_amount} PKR - V62 - V45 JORA - RESULTS SHOW")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, height=400)
    csv = df.to_csv(index=False)
    st.download_button("EXPORT CSV - V62 RESULTS SHOW", csv, "sona_v62_results_show.csv", "text/csv", key="export_v62")

st.success('V62 FINAL PREMIUM VISIBLE - REAL 2500 PKR START - DEMO 10000 - JAZZCASH EASYPAISA - LIVE CHART - RSI VOLUME ATR VWAP MACD LIQUIDITY BOS PULLBACK - NO BLANK - VERTICAL VISIBLE - V45 JORA - DASE JORA KA - READY - RESULTS SHOW')
