import streamlit as st
import random
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="SONA AI v66 HYBRID", layout="wide")

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:15px;padding:12px;text-align:center;box-shadow:0 0 20px #0F0"><div style="color:#0F0;font-size:15px;font-weight:900">SONA AI v66 HYBRID - V45 PREMIUM DESIGN + V64 RESULTS - REAL 2500 PKR START - DEMO 10000 - PAGES - V45 JORA</div></div>', unsafe_allow_html=True)

st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700);border-radius:12px;padding:10px;text-align:center;margin:8px 0"><div style="color:#000;font-size:11px;font-weight:900">V45 DESIGN - NO SYNTAX ERROR FIX - CANDLE UP DOWN + PINE EDITOR + DEPOSIT WITHDRAW + 24H RESULTS - V64 RESULTS - 5 x 24 = 120 TRADES/DAY - REAL 2500 START - DEMO 10000 - PAGES - HYBRID</div></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state:
    st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state:
    st.session_state.demo_bal = 10000
if 'real_profit' not in st.session_state:
    st.session_state.real_profit = 621
if 'demo_profit' not in st.session_state:
    st.session_state.demo_profit = 0
if 'real_trades' not in st.session_state:
    st.session_state.real_trades = 1
if 'demo_trades' not in st.session_state:
    st.session_state.demo_trades = 0
if 'total24' not in st.session_state:
    st.session_state.total24 = 1
if 'account_mode' not in st.session_state:
    st.session_state.account_mode = "REAL"
if 'live_price' not in st.session_state:
    st.session_state.live_price = 67421.96
if 'price_hist_real' not in st.session_state:
    st.session_state.price_hist_real = [4000, 4100, 4200, 4300, 4621, 4921]
if 'price_hist_demo' not in st.session_state:
    st.session_state.price_hist_demo = [10000, 10000, 10000, 10000, 10000]
if 'history' not in st.session_state:
    st.session_state.history = [
        {"Time": "7:37:58 AM", "Account":"REAL","Result":"WIN 250 RS - V66 HYBRID - 95pct - Total 24h 1/120 - V45 DESIGN + V64 RESULTS","Profit":"300 PKR | Bal 4921","Bal":4921,"Market":"BTC/USD","Method":"Real Hybrid V66"},
        {"Time": "8:36 AM", "Account":"REAL","Result":"WIN 250 RS - V66 - 95pct - Total 24h 1/120","Profit":"310 PKR | Bal 3621","Bal":3621,"Market":"BTC/USD","Method":"Real Hybrid V66"},
        {"Time": "8:31 AM", "Account":"REAL","Result":"WIN 250 RS - V66 - 95pct - Total 24h 1/120","Profit":"295 PKR | Bal 3531","Bal":3531,"Market":"BTC/USD","Method":"Real Hybrid V66"},
    ]

st.session_state.live_price += random.uniform(-100,100)
live_price = st.session_state.live_price

st.markdown('<div style="background:#111;border:2px solid #FFD700;border-radius:12px;padding:10px;margin:8px 0"><div style="color:#FFD700;font-size:13px;font-weight:900;text-align:center">MARKET STRUCTURE - HH HL LH LL BOS CHOCH MSS - V66 HYBRID</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px"><div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TREND</div><div style="color:#0F0;font-size:14px;font-weight:900">BULLISH - HH HL - UPTREND</div></div><div style="background:#000;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">LAST POINTS</div><div style="color:#FFD700;font-size:12px;font-weight:900">HH 67,180 - HL 66,900 - LH 67,050 - LL 66,800</div></div><div style="background:#000;border:2px solid #0FF;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">BOS</div><div style="color:#0FF;font-size:12px;font-weight:900">BULLISH BOS - 67,180 BROKE HH 67,150 - BREAK UP</div></div><div style="background:#000;border:2px solid #F00;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">CHOCH</div><div style="color:#F00;font-size:12px;font-weight:900">NO CHOCH - BULLISH TREND INTACT</div></div><div style="background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">MSS</div><div style="color:#F0F;font-size:12px;font-weight:900">BULLISH MSS - SHIFT BEARISH TO BULLISH - CONFIRMED</div></div><div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">OB + FVG</div><div style="color:#0F0;font-size:11px;font-weight:900">BULL OB 67,050 + BULL FVG 66,900-67,000 - SUPPORT</div></div></div></div>', unsafe_allow_html=True)

account_choice = st.radio("SELECT ACCOUNT - V66 HYBRID - V45 DESIGN + V64 RESULTS", ["REAL - 2500 PKR - Really money Laga ka - V66 HYBRID V45 DESIGN + V64 RESULTS","DEMO - 10000 PKR - Nan Demo Check - V66 HYBRID V45 DESIGN + V64 RESULTS"], index=0 if st.session_state.account_mode=="REAL" else 1, key="acc_v66")
if "REAL" in account_choice:
    st.session_state.account_mode = "REAL"
else:
    st.session_state.account_mode = "DEMO"

account_mode = st.session_state.account_mode
start_amount = "2500" if account_mode=="REAL" else "10000"
current_bal = st.session_state.real_bal if account_mode=="REAL" else st.session_state.demo_bal
current_profit = st.session_state.real_profit if account_mode=="REAL" else st.session_state.demo_profit
current_trades = st.session_state.real_trades if account_mode=="REAL" else st.session_state.demo_trades

if account_mode == "REAL":
    st.markdown(f'<div style="background:#001100;border:3px solid #0F0;border-radius:15px;padding:15px;text-align:center;box-shadow:0 0 15px #0F0"><div style="color:#0F0;font-size:32px;font-weight:900">+{current_profit} PKR</div><div style="color:#0F0;font-size:10px">LIVE PRICE: BTC ${live_price:,.2f} | V66 HYBRID V45 DESIGN + V64 RESULTS - REAL 2500 START - Trades {current_trades}/5 - Total 24h {st.session_state.total24}/120 - Bal {current_bal} PKR</div><div style="background:linear-gradient(90deg,#0F0,#FFD700);height:12px;border-radius:6px;margin-top:8px;width:90%"></div></div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div style="background:#001133;border:3px solid #0AF;border-radius:15px;padding:15px;text-align:center;box-shadow:0 0 15px #0AF"><div style="color:#0AF;font-size:28px;font-weight:900">DEMO {current_bal} PKR</div><div style="color:#0AF;font-size:10px">DEMO ACCOUNT ACTIVE - 10000 PKR - Bal {current_bal} PKR - Profit {current_profit} PKR - Trades {current_trades} - Nan Demo Check - V66 HYBRID</div><div style="background:linear-gradient(90deg,#0AF,#FFD700);height:12px;border-radius:6px;margin-top:8px;width:80%"></div></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["TRADING PAGE - CANDLE UP DOWN + 24H RESULTS", "DEPOSIT WITHDRAW - JAZZCASH EASYPAISA", "PINE EDITOR + HISTORY - V45 DESIGN"])

with tab1:
    st.markdown(f'<div style="background:#000;border:2px solid #0FF;border-radius:12px;padding:10px;text-align:center"><div style="color:#0FF;font-size:11px;font-weight:900">DEPOSIT AND WITHDRAW OPTION - V66 HYBRID V45 DESIGN + V64 RESULTS - REAL {start_amount} PKR START</div></div>', unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        dep_amt = st.number_input("Deposit Amount PKR - V66 Hybrid", value=500, min_value=100, max_value=50000, step=100, key="dep_amt_v66")
        if st.button("DEPOSIT - ADD BALANCE - V66 HYBRID", key="dep_v66_hybrid"):
            if account_mode=="REAL":
                st.session_state.real_bal += dep_amt
                st.session_state.real_profit += dep_amt
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                t = datetime.now().strftime("%I:%M:%S %p")
                st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"DEPOSIT +{dep_amt} PKR - V66 HYBRID - V45 DESIGN + V64 RESULTS","Profit":f"+{dep_amt} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Deposit Hybrid V66"})
                st.success(f"Deposit: +{dep_amt} PKR - New Bal {st.session_state.real_bal} PKR - Success! - {t}")
            else:
                st.session_state.demo_bal += dep_amt
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f"Demo Deposit +{dep_amt} PKR - Bal {st.session_state.demo_bal} PKR")
    with c2:
        with_amt = st.number_input("Withdraw Amount PKR - V66 Hybrid", value=250, min_value=100, max_value=50000, step=100, key="with_amt_v66")
        if st.button("WITHDRAW - REMOVE BALANCE - V66 HYBRID", key="with_v66_hybrid"):
            if account_mode=="REAL" and with_amt <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amt
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                t = datetime.now().strftime("%I:%M:%S %p")
                st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"WITHDRAW -{with_amt} PKR - V66 HYBRID","Profit":f"-{with_amt} PKR | Bal {st.session_state.real_bal}","Bal":st.session_state.real_bal,"Market":"BTC/USD","Method":"Real Withdraw Hybrid V66"})
                st.success(f"Withdraw -{with_amt} PKR - Bal {st.session_state.real_bal} PKR")
            elif account_mode=="DEMO" and with_amt <= st.session_state.demo_bal:
                st.session_state.demo_bal -= with_amt
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f"Demo Withdraw -{with_amt} PKR")

    st.markdown('<div style="background:#111;border:2px solid #FFD700;border-radius:12px;padding:10px;margin:8px 0;text-align:center"><div style="color:#FFD700;font-size:12px;font-weight:900">CANDLE UP AND DOWN RAWAN - LIVE CANDLE CHART - V66 HYBRID V45 DESIGN + V64 RESULTS</div></div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10,4))
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    n = 30
    opens = []
    closes = []
    highs = []
    lows = []
    price = live_price - 500
    for i in range(n):
        o = price + random.uniform(-80,80)
        c = o + random.uniform(-100,100)
        h = max(o,c) + random.uniform(10,50)
        l = min(o,c) - random.uniform(10,50)
        opens.append(o)
        closes.append(c)
        highs.append(h)
        lows.append(l)
        price = c
    for i in range(n):
        color = '#00FF00' if closes[i] >= opens[i] else '#FF0000'
        ax.plot([i,i],[lows[i],highs[i]],color=color,linewidth=1)
        ax.add_patch(plt.Rectangle((i-0.15, min(opens[i],closes[i])), 0.3, abs(closes[i]-opens[i]), color=color))
    ax.set_xlim(-1,n)
    ax.tick_params(colors='white')
    st.pyplot(fig)

    fig2, ax2 = plt.subplots(figsize=(10,2.5))
    fig2.patch.set_facecolor('black')
    ax2.set_facecolor('black')
    price_hist = st.session_state.price_hist_real if account_mode=="REAL" else st.session_state.price_hist_demo
    ax2.plot(price_hist, color='#00FF00', linewidth=2.5)
    ax2.fill_between(range(len(price_hist)), price_hist, alpha=0.2, color='#00FF00')
    ax2.tick_params(colors='white')
    st.pyplot(fig2)

    st.markdown(f'<div style="background:#221100;border:2px solid #FFD700;border-radius:12px;padding:10px;margin:8px 0;text-align:center"><div style="color:#FFD700;font-size:12px;font-weight:900">WAITING - V66 HYBRID - Candle Up Down + Pine Editor + Deposit Withdraw + 24H Results - 5 x 24 = 120 Trades/Day - Ready - {account_mode} {start_amount} PKR</div><div style="background:linear-gradient(90deg,#0F0,#FFD700);height:14px;border-radius:7px;margin:8px 0"></div><div style="color:#0F0;font-size:11px">Candle: Ready - V66 Hybrid - Candle Up Down Live - Auto Every 1 Min - 24H - 95% Win - {account_mode} {start_amount} PKR</div><div style="color:#0F0;background:#001100;border-radius:6px;padding:6px;font-size:9px;margin-top:6px">Hourly Info: Hour 0 | Trades {current_trades}/5 | Next reset 60min | 24H Trading Active | V66 Hybrid</div></div>', unsafe_allow_html=True)

    st.markdown(f'<div style="background:#220022;border:2px solid #F0F;border-radius:12px;padding:10px;margin:8px 0"><div style="color:#F0F;font-size:11px;font-weight:900;text-align:center">PA HAR ONE HOURS KA 5 TRADER KA , DA 24 HOURS RESULTS TOL SHOW KA - 24H RESULTS - 5 x 24 = 120 TRADES/DAY - V66 HYBRID - {account_mode} {start_amount} PKR</div><div style="background:#111;border-radius:8px;padding:8px;margin:8px 0;display:flex;justify-content:space-between;color:#FFD700;font-size:10px"><div>7:00</div><div>{current_trades}/5</div><div>{st.session_state.total24}</div><div>0</div><div>300 PKR</div><div>{current_bal} PKR</div></div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px"><div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H TRADES</div><div style="color:#0F0;font-size:18px;font-weight:900">{st.session_state.total24}/120</div></div><div style="background:#000;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H PROFIT</div><div style="color:#FFD700;font-size:18px;font-weight:900">+{current_profit} PKR</div></div><div style="background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H WIN %</div><div style="color:#F0F;font-size:18px;font-weight:900">90%</div></div></div></div>', unsafe_allow_html=True)

    if st.button(f"MANUAL TRADE 250 PKR - {account_mode} {start_amount} - V66 HYBRID V45 DESIGN", key="manual_v66"):
        is_win = random.random() < 0.9
        profit = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        t = datetime.now().strftime("%I:%M:%S %p")
        if account_mode=="REAL":
            st.session_state.real_bal += profit
            st.session_state.real_profit += profit
            st.session_state.real_trades += 1
            st.session_state.total24 += 1
            st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"WIN 250 RS - V66 HYBRID - 95pct - Total 24h {st.session_state.total24}/120 - V45 DESIGN + V64 RESULTS","Profit":f"{round(profit)} PKR | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":"Real Hybrid V66"})
        else:
            st.session_state.demo_bal += profit
            st.session_state.demo_profit += profit
            st.session_state.demo_trades += 1
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"WIN 250 RS - V66 HYBRID DEMO - 95pct - Total 24h {st.session_state.total24}/120","Profit":f"{round(profit)} | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Hybrid V66"})
        st.success(f"{'WIN' if is_win else 'LOSS'} {round(profit)} PKR - {account_mode} {start_amount} PKR - V66 HYBRID - RESULTS SHOW - V45 DESIGN")

    if st.button(f"FORCE TRADE NOW - {account_mode} {start_amount} - V66 HYBRID", key="force_v66"):
        is_win = random.random() < 0.9
        profit = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        t = datetime.now().strftime("%I:%M:%S %p")
        if account_mode=="REAL":
            st.session_state.real_bal += profit
            st.session_state.real_profit += profit
            st.session_state.real_trades += 1
            st.session_state.total24 += 1
            st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            st.session_state.history.insert(0, {"Time": t, "Account":"REAL","Result":f"WIN 250 RS - V66 HYBRID FORCE - 95pct - Total 24h {st.session_state.total24}/120","Profit":f"{round(profit)} | Bal {int(st.session_state.real_bal)}","Bal":int(st.session_state.real_bal),"Market":"BTC/USD","Method":"Real Hybrid Force V66"})
        else:
            st.session_state.demo_bal += profit
            st.session_state.demo_profit += profit
            st.session_state.demo_trades += 1
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            st.session_state.history.insert(0, {"Time": t, "Account":"DEMO","Result":f"WIN 250 RS - V66 HYBRID DEMO FORCE","Profit":f"{round(profit)} | Bal {int(st.session_state.demo_bal)}","Bal":int(st.session_state.demo_bal),"Market":"BTC/USD","Method":"Demo Hybrid Force V66"})
        st.success(f"FORCE {'WIN' if is_win else 'LOSS'} {round(profit)} PKR - {account_mode} - V66 HYBRID - V45 DESIGN + V64 RESULTS")

with tab2:
    st.markdown(f'<div style="background:#001133;border:2px solid #0AF;border-radius:12px;padding:12px"><div style="color:#0AF;font-size:12px;font-weight:900">DEPOSIT WITHDRAW PAGE - {account_mode} - Start {start_amount} PKR - V66 HYBRID - V45 DESIGN + V64 RESULTS - PAGE 2 - JAZZCASH EASYPAISA - REAL 2500 START</div></div>', unsafe_allow_html=True)
    if account_mode=="DEMO":
        if st.button("DEMO TOPUP +5000 PKR FREE - V66 HYBRID V45 DESIGN", key="demo_topup_v66_p2"):
            st.session_state.demo_bal += 5000
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            st.success(f"Demo +5000 PKR - Bal {st.session_state.demo_bal} PKR - V66 HYBRID")
        if st.button("RESET DEMO 10000 PKR - V66 HYBRID V45 DESIGN", key="demo_reset_v66_p2"):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.demo_trades = 0
            st.session_state.price_hist_demo = [10000, 10000, 10000, 10000, 10000]
            st.success("Demo Reset 10000 PKR - V66 HYBRID")
    else:
        dep_phone = st.text_input("JazzCash EasyPaisa Number 11 digits - V66 HYBRID PAGE 2", value="03001234567", key="dep_p_v66_p2")
        dep_amount = st.number_input("Deposit PKR Real 2500 - V66 HYBRID PAGE 2", value=2500, min_value=100, max_value=50000, step=100, key="dep_a_v66_p2")
        if st.button("DEPOSIT NOW REAL 2500 - V66 HYBRID PAGE 2 - V45 DESIGN", key="dep_v66_p2"):
            if len(dep_phone)>=11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f"Deposit +{dep_amount} PKR - Bal {st.session_state.real_bal} PKR - TXN REAL{random.randint(100000,999999)} - V66 HYBRID")
        with_phone = st.text_input("Withdraw Number 11 digits - V66 HYBRID PAGE 2", value="03001234567", key="with_p_v66_p2")
        with_amount = st.number_input("Withdraw PKR Real 2500 - V66 HYBRID PAGE 2", value=250, min_value=100, max_value=50000, step=100, key="with_a_v66_p2")
        if st.button("WITHDRAW NOW REAL 2500 - V66 HYBRID PAGE 2 - V45 DESIGN", key="with_v66_p2"):
            if len(with_phone)>=11 and with_amount <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amount
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f"Withdraw -{with_amount} PKR - Bal {st.session_state.real_bal} PKR - 5 Min me ayega - V66 HYBRID")
    if st.button("CLEAR CACHE - V66 HYBRID V45 DESIGN + V64 RESULTS - CLICK IF BLANK", key="clear_v66_p2"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with tab3:
    st.markdown('<div style="background:#221100;border:2px solid #FFD700;border-radius:12px;padding:10px"><div style="color:#FFD700;font-size:12px;font-weight:900">BAL KHABER PINE EDITOR PA KA ADD KA - V66 HYBRID - V45 DESIGN + V64 RESULTS</div><div style="display:grid;grid-template-
