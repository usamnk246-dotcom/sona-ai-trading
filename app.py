import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v63 PAGES", layout="centered")

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{color:#000;background:#FFD700;font-weight:900;border-radius:8px;width:100%}.stTabs [data-baseweb="tab-list"]{gap:8px}.stTabs [data-baseweb="tab"]{background:#111;border:2px solid #0F0;border-radius:8px;padding:8px;color:#0F0;font-weight:900}</style>', unsafe_allow_html=True)

st.success('SONA AI v63 PAGES - REAL 2500 PKR START - DEMO 10000 - 3 PAGES - TRADING | DEPOSIT | RESULTS - PAGE CHANGE - V45 JORA')

# SAFE INIT - ALL KEYS
if 'real_bal' not in st.session_state:
    st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state:
    st.session_state.demo_bal = 10000
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
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"REAL","Result":"REAL START 2500 PKR - V63 PAGES","Profit":"+0 PKR | Bal 2500","Bal":2500,"Market":"BTC/USD","Method":"Real Start 2500 V63"},
        {"Time": datetime.now().strftime("%I:%M:%S %p"), "Account":"DEMO","Result":"DEMO START 10000 PKR - V63 PAGES","Profit":"+0 PKR | Bal 10000","Bal":10000,"Market":"BTC/USD","Method":"Demo Start 10000 V63"},
    ]

st.session_state.live_price += random.uniform(-30,30)

# ACCOUNT SELECT - TOP - VISIBLE
account_choice = st.radio("Account Mode V63", ["REAL - 2500 PKR - Really money Laga ka - V63 PAGES","DEMO - 10000 PKR - Nan Demo Check - V63 PAGES"], index=0 if st.session_state.account_mode=="REAL" else 1)
if "REAL" in account_choice:
    st.session_state.account_mode = "REAL"
else:
    st.session_state.account_mode = "DEMO"

account_mode = st.session_state.account_mode
start_amount = "2500" if account_mode=="REAL" else "10000"
st.metric(label=f"{account_mode} BALANCE - Start {start_amount} PKR - V63", value=f"{st.session_state.real_bal if account_mode=='REAL' else st.session_state.demo_bal} PKR")
st.metric(label="LIVE BTC/USD - V63", value=f"${st.session_state.live_price:,.2f}", delta="BULLISH")

# 3 TABS - PAGE CHANGE PA SHAN O KA
tab1, tab2, tab3 = st.tabs(["TRADING PAGE - LIVE CHART + TRADE", "DEPOSIT WITHDRAW PAGE - JAZZCASH EASYPAISA", "RESULTS HISTORY PAGE - EXPORT"])

with tab1:
    st.write(f"TRADING PAGE - {account_mode} - Start {start_amount} PKR - V63 - PAGE 1")
    rsi = 62.4 + random.uniform(-1,1)
    vol = 1.8 + random.uniform(-0.1,0.1)
    st.write(f"RSI: {rsi:.1f} - BULLISH BUY 95pct | VOL: {vol:.1f}M - HIGH VOL - V63")
    st.write(f"VWAP: {st.session_state.live_price-10:,.0f} - ABOVE VWAP BUY | MACD: 0.85 BULL - CROSS | BOS: BULLISH BOS - V63")
    # FIXED CHART - NO FLAT 60k LINE - PROPER CLOSE
    candles = []
    p = st.session_state.live_price
    for i in range(30):
        p = p + random.uniform(-80,80)
        candles.append({"Close": p})
    st.line_chart(pd.DataFrame(candles), height=220)
    price_hist = st.session_state.price_hist_demo if account_mode=="DEMO" else st.session_state.price_hist_real
    st.line_chart(pd.DataFrame({f"{account_mode} Balance {start_amount} PKR": price_hist}), height=130)
    if st.button(f"MANUAL TRADE 250 PKR - {account_mode} {start_amount} - V63 PAGE 1"):
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        if account_mode=="REAL":
            st.session_state.real_bal += p
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.success(f"REAL WIN {round(p)} PKR - Bal {int(st.session_state.real_bal)} - V63 PAGE CHANGE")
        else:
            st.session_state.demo_bal += p
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            st.success(f"DEMO WIN {round(p)} PKR - Bal {int(st.session_state.demo_bal)} - V63 PAGE CHANGE")
    if st.button(f"FORCE TRADE NOW - {account_mode} - V63 PAGE 1"):
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        if account_mode=="REAL":
            st.session_state.real_bal += p
            st.session_state.price_hist_real.append(st.session_state.real_bal)
        else:
            st.session_state.demo_bal += p
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
        st.success(f"FORCE {'WIN' if is_win else 'LOSS'} {round(p)} PKR - V63 PAGE CHANGE")

with tab2:
    st.write(f"DEPOSIT WITHDRAW PAGE - {account_mode} - V63 PAGE 2")
    if account_mode=="DEMO":
        if st.button("DEMO TOPUP +5000 PKR FREE - V63 PAGE 2"):
            st.session_state.demo_bal += 5000
            st.session_state.price_hist_demo.append(st.session_state.demo_bal)
            st.success(f"Demo +5000 - Bal {st.session_state.demo_bal} PKR - V63 PAGE 2")
    else:
        dep_phone = st.text_input("JazzCash EasyPaisa Number 11 digits - V63 PAGE 2", value="03001234567")
        dep_amount = st.number_input("Deposit PKR Real 2500 - V63 PAGE 2", value=2500, min_value=100, max_value=50000, step=100)
        if st.button("DEPOSIT NOW REAL 2500 - V63 PAGE 2"):
            st.session_state.real_bal += dep_amount
            st.session_state.price_hist_real.append(st.session_state.real_bal)
            st.success(f"Deposit +{dep_amount} PKR - Bal {st.session_state.real_bal} PKR - V63 PAGE 2 - TXN REAL{random.randint(100000,999999)}")
        with_phone = st.text_input("Withdraw Number 11 digits - V63 PAGE 2", value="03001234567")
        with_amount = st.number_input("Withdraw PKR Real 2500 - V63 PAGE 2", value=250, min_value=100, max_value=50000, step=100)
        if st.button("WITHDRAW NOW REAL 2500 - V63 PAGE 2"):
            if with_amount <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amount
                st.session_state.price_hist_real.append(st.session_state.real_bal)
                st.success(f"Withdraw -{with_amount} PKR - Bal {st.session_state.real_bal} PKR - V63 PAGE 2")

with tab3:
    st.write(f"RESULTS HISTORY PAGE - {account_mode} - Start {start_amount} PKR - V63 PAGE 3")
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df, use_container_width=True, height=450)
        csv = df.to_csv(index=False)
        st.download_button("EXPORT CSV - V63 RESULTS HISTORY PAGE", csv, "sona_v63_pages_results.csv", "text/csv")
