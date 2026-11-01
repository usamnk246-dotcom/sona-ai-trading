import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='SONA V72 PRO - 1MIN 5MIN 15MIN', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;font-size:13px!important;border-radius:14px!important;height:56px!important;border:3px solid #0F0!important;box-shadow:0 0 15px #FFD700}.stNumberInput input{background:#111!important;color:#0F0!important;border:2px solid #0F0!important}.stTextInput input{background:#111!important;color:#FFD700!important;border:2px solid #FFD700!important}.stSelectbox>div>div{background:#111!important;color:#0F0!important;border:2px solid #0FF!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:15px;padding:12px;text-align:center;box-shadow:0 0 22px #0F0">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px">SONA AI V72 PRO - 1MIN 5MIN 15MIN CHART + AUTO TRADING + ALERT SOUND - 72 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:9px">REAL 2500 START - DEMO 10000 - MULTI MARKET MULTI TIMEFRAME - AUTO ON/OFF - ALERT SOUND - 72 JORA KA</p></div>', unsafe_allow_html=True)

st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700,#0FF);border-radius:8px;padding:8px;text-align:center;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<p style="color:#000;font-size:10px;font-weight:900">V72 PRO - 1MIN 5MIN 15MIN - AUTO TRADING ON/OFF - ALERT SOUND WIN - MULTI MARKET - 72 JORA KA</p></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state: st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state: st.session_state.demo_bal = 10000
if 'real_profit' not in st.session_state: st.session_state.real_profit = 621
if 'demo_profit' not in st.session_state: st.session_state.demo_profit = 0
if 'real_trades' not in st.session_state: st.session_state.real_trades = 1
if 'demo_trades' not in st.session_state: st.session_state.demo_trades = 0
if 'total24' not in st.session_state: st.session_state.total24 = 1
if 'account_mode' not in st.session_state: st.session_state.account_mode = 'REAL'
if 'live_price' not in st.session_state: st.session_state.live_price = 67534.78
if 'price_hist_real' not in st.session_state: st.session_state.price_hist_real = [2500,2710,2950,3121,3500,3821,4121]
if 'price_hist_demo' not in st.session_state: st.session_state.price_hist_demo = [10000,10150,10280,10400,10550,10700,11000]
if 'auto_trading' not in st.session_state: st.session_state.auto_trading = False
if 'alert_sound' not in st.session_state: st.session_state.alert_sound = True
if 'selected_market' not in st.session_state: st.session_state.selected_market = 'BTC/USD - Bitcoin'
if 'selected_tf' not in st.session_state: st.session_state.selected_tf = '1MIN - Scalp - 1 min candle'
if 'history' not in st.session_state:
    st.session_state.history = [
        {'Time':'11:53 AM','Account':'REAL','Result':'WIN 250 RS - V72 PRO 1MIN 95pct 1/120 - 72 JORA KA','Profit':'321 PKR | Bal 2821','Bal':2821,'Market':'BTC/USD 1MIN','Method':'Real V72 1MIN'},
        {'Time':'11:54 AM','Account':'REAL','Result':'WIN 250 RS - V72 AUTO ON 5MIN 95pct','Profit':'300 PKR | Bal 4121','Bal':4121,'Market':'ETH/USD 5MIN','Method':'Auto V72'},
        {'Time':'11:54 AM','Account':'DEMO','Result':'WIN 250 RS - V72 DEMO 15MIN 95pct - ALERT SOUND','Profit':'0 PKR | Bal 10000','Bal':10000,'Market':'SOL/USD 15MIN','Method':'Demo V72'},
    ]

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    market = st.selectbox('SELECT MARKET - V72 PRO - DIFFERENT MARKET PAKA ADD KA', ['BTC/USD - Bitcoin - $67K','ETH/USD - Ethereum - $3.5K','SOL/USD - Solana - $180','BNB/USD - BNB - $600','GOLD - XAU/USD - $2350','EUR/USD - Forex - 1.08','GBP/USD - Forex - 1.27','USD/PKR - Forex - 278'], index=0, key='market_v72')
    st.session_state.selected_market = market
with col_m2:
    tf = st.selectbox('SELECT TIMEFRAME - V72 PRO - 1MIN 5MIN 15MIN CHART PAKA ADD KA', ['1MIN - Scalp - 1 min candle - Fast','5MIN - Fast - 5 min - Best','15MIN - Swing - 15 min - Strong','1H - 1 Hour - Trend','4H - 4 Hour - Big Trend','1D - Daily - Long'], index=0, key='tf_v72')
    st.session_state.selected_tf = tf
with col_m3:
    auto_on = st.toggle('AUTO TRADING ON/OFF - V72 PRO - AUTO TRADING ON OFF', value=st.session_state.auto_trading, key='auto_v72')
    st.session_state.auto_trading = auto_on
    alert_on = st.toggle('ALERT SOUND WIN - V72 PRO - ALERT SOUND KALA SAH TRADE WIN SHA', value=st.session_state.alert_sound, key='alert_v72')
    st.session_state.alert_sound = alert_on

selected_market = st.session_state.selected_market
selected_tf = st.session_state.selected_tf

base_prices = {'BTC':67534.78,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in selected_market: base = base_prices['BTC']
elif 'ETH' in selected_market: base = base_prices['ETH']
elif 'SOL' in selected_market: base = base_prices['SOL']
elif 'BNB' in selected_market: base = base_prices['BNB']
elif 'GOLD' in selected_market: base = base_prices['GOLD']
elif 'EUR' in selected_market: base = base_prices['EUR']
elif 'GBP' in selected_market: base = base_prices['GBP']
else: base = 67534.78

st.session_state.live_price = base + random.uniform(-60,80)
live_price = st.session_state.live_price

if '1MIN' in selected_tf: candle_count=60; vol_mult=0.5; tf_label='1MIN'
elif '5MIN' in selected_tf: candle_count=48; vol_mult=1.0; tf_label='5MIN'
elif '15MIN' in selected_tf: candle_count=32; vol_mult=1.5; tf_label='15MIN'
elif '1H' in selected_tf: candle_count=24; vol_mult=2.0; tf_label='1H'
elif '4H' in selected_tf: candle_count=20; vol_mult=3.0; tf_label='4H'
else: candle_count=30; vol_mult=2.5; tf_label='1D'

if st.session_state.auto_trading and random.random()<0.35:
    is_win=random.random()<0.92; profit=random.uniform(300,420) if is_win else random.uniform(-60,-30); t=datetime.now().strftime('%I:%M:%S %p')
    if st.session_state.account_mode=='REAL':
        st.session_state.real_bal+=profit; st.session_state.real_profit+=profit; st.session_state.real_trades+=1; st.session_state.total24+=1
        st.session_state.price_hist_real.append(int(st.session_state.real_bal))
        st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'AUTO WIN 250 RS - V72 {tf_label} AUTO ON {st.session_state.total24}/120','Profit':f'{round(profit)} PKR | Bal {int(st.session_state.real_bal)}','Bal':int(st.session_state.real_bal),'Market':f'{selected_market} {tf_label}','Method':f'Auto V72 {tf_label}'})
    else:
        st.session_state.demo_bal+=profit; st.session_state.demo_profit+=profit; st.session_state.demo_trades+=1
        st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
    if st.session_state.alert_sound and is_win:
        st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        st.balloons()

st.markdown(f'<div style="background:#001100;border:3px solid #0F0;border-radius:15px;padding:16px;text-align:center;box-shadow:0 0 18px #0F0;margin:8px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:36px;font-weight:900">+{st.session_state.real_profit if st.session_state.account_mode=="REAL" else st.session_state.demo_profit} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">LIVE {selected_market.split(" - ")[0]} ${live_price:,.2f} | TF {tf_label} | AUTO {"ON" if st.session_state.auto_trading else "OFF"} | ALERT {"ON" if st.session_state.alert_sound else "OFF"} | V72 PRO - REAL 2500 - Trades {st.session_state.real_trades}/5 - Total 24h {st.session_state.total24}/120</div>', unsafe_allow_html=True)
st.markdown(f'<div style="background:linear-gradient(90deg,#0F0,#FFD700);height:14px;border-radius:7px;margin-top:10px;width:{int((st.session_state.total24/120)*100)}%"></div></div>', unsafe_allow_html=True)

st.markdown('<p style="color:#FFD700;font-weight:900;text-align:center">MARKET STRUCTURE - HH HL BOS CHOCH MSS - V72 PRO - 72 JORA KA - MULTI MARKET MULTI TIMEFRAME</p>', unsafe_allow_html=True)
c1,c2 = st.columns(2)
with c1:
    st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#0F0">BULLISH - HH HL - UPTREND - {tf_label}</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #0FF;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#0FF">BULLISH BOS - {int(live_price)} BROKE HH - {selected_market.split(" - ")[0]}</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #F0F;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#F0F">BULLISH MSS - SHIFT BULLISH</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="background:#000;border:2px solid #FFD700;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#FFD700">HH {int(live_price+150)} - HL {int(live_price-200)} - LH {int(live_price-50)} - {tf_label}</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #F00;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#F00">NO CHOCH - BULLISH INTACT</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#0F0">BULL OB + FVG SUPPORT - AUTO ' + ('ON' if st.session_state.auto_trading else 'OFF') + '</p></div>', unsafe_allow_html=True)

rsi = 62.8 + random.uniform(-1,1)
vol = 1.8 + random.uniform(-0.2,0.2)
vwap = live_price - random.uniform(-50,50)
macd = 0.90 + random.uniform(-0.05,0.05)
st.markdown(f'<p style="color:#0F0;font-size:11px">RSI: {rsi:.1f} - BULLISH BUY 95pct {tf_label} | VOL: {vol:.1f}M - HIGH VOL {selected_market.split(" - ")[0]} | VWAP: {vwap:,.2f} - ABOVE VWAP BUY | MACD: {macd:.2f} BULL - V72 {tf_label}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#FFD700;font-size:11px">LIQ: SWEEP DONE {tf_label} | PULLBACK: DONE 50% FIB BUY ZONE | BOS: BULLISH BOS BROKE HH - V72 PRO - AUTO { "ON - TRADING" if st.session_state.auto_trading else "OFF - MANUAL"} - ALERT SOUND { "ON" if st.session_state.alert_sound else "OFF"}</p>', unsafe_allow_html=True)

mode = st.radio('SELECT ACCOUNT - V72 PRO 72 JORA KA', ['REAL - 2500 PKR - Really money Laga ka - V72 PRO','DEMO - 10000 PKR - Nan Demo Check - V72 PRO'], index=0 if st.session_state.account_mode=='REAL' else 1)
if 'REAL' in mode: st.session_state.account_mode='REAL'
else: st.session_state.account_mode='DEMO'
account_mode = st.session_state.account_mode
start_amount = '2500' if account_mode=='REAL' else '10000'
current_bal = st.session_state.real_bal if account_mode=='REAL' else st.session_state.demo_bal
current_profit = st.session_state.real_profit if account_mode=='REAL' else st.session_state.demo_profit
current_trades = st.session_state.real_trades if account_mode=='REAL' else st.session_state.demo_trades

if account_mode=='REAL':
    st.success(f'REAL ACTIVE - 2500 START - Bal {current_bal} PKR - Profit {current_profit} PKR - Trades {current_trades} - Market {selected_market.split(" - ")[0]} TF {tf_label} - AUTO {"ON" if st.session_state.auto_trading else "OFF"} - V72 PRO 72 JORA KA')
else:
    st.info(f'DEMO ACTIVE - 10000 PKR - Bal {current_bal} PKR - Profit {current_profit} PKR - Trades {current_trades} - Market {selected_market.split(" - ")[0]} TF {tf_label} - V72 PRO 72 JORA KA')

st.metric(label=f'{account_mode} BALANCE - Start {start_amount} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO', value=f'{current_bal} PKR', delta=f'+{current_profit} PKR - 72 JORA KA')
st.metric(label=f'LIVE {selected_market.split(" - ")[0]} - V72 PRO - TF {tf_label}', value=f'${live_price:,.2f}', delta=f'BULLISH BUY ZONE - AUTO {"ON" if st.session_state.auto_trading else "OFF"} - V72')

tab1,tab2,tab3 = st.tabs(['TRADING - 1MIN 5MIN 15MIN - V72 PRO','DEPOSIT WITHDRAW - V72 PRO','PINE + HISTORY - V72 PRO'])

with tab1:
    st.write(f'TRADING PAGE - {account_mode} {start_amount} PKR - {selected_market} - {tf_label} - V72 PRO - 72 JORA KA - AUTO {"ON" if st.session_state.auto_trading else "OFF"}')
    col1,col2 = st.columns(2)
    with col1:
        dep_amt = st.number_input(f'Deposit PKR - V72 PRO - {selected_market.split(" - ")[0]} {tf_label}', value=500, min_value=100, max_value=50000, step=100, key='dep_amt_v72')
        if st.button(f'DEPOSIT - ADD BALANCE - V72 PRO {selected_market.split(" - ")[0]} {tf_label} YELLOW 72 JORA KA', key='dep_v72'):
            if account_mode=='REAL':
                st.session_state.real_bal+=dep_amt; st.session_state.real_profit+=dep_amt; st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amt} - Bal {st.session_state.real_bal} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO')
                if st.session_state.alert_sound:
                    st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            else:
                st.session_state.demo_bal+=dep_amt; st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Deposit +{dep_amt} - V72 PRO')
    with col2:
        with_amt = st.number_input(f'Withdraw PKR - V72 PRO - {selected_market.split(" - ")[0]} {tf_label}', value=250, min_value=100, max_value=50000, step=100, key='with_amt_v72')
        if st.button(f'WITHDRAW - REMOVE BALANCE - V72 PRO {selected_market.split(" - ")[0]} {tf_label} YELLOW 72 JORA KA', key='with_v72'):
            if account_mode=='REAL' and with_amt<=st.session_state.real_bal:
                st.session_state.real_bal-=with_amt; st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amt} - V72 PRO')
            elif account_mode=='DEMO' and with_amt<=st.session_state.demo_bal:
                st.session_state.demo_bal-=with_amt; st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Withdraw -{with_amt} - V72 PRO')
    st.write(f'CANDLE UP AND DOWN - LIVE CANDLE CHART - V72 PRO - {selected_market} - {tf_label} CHART PAKA ADD KA - FIXED BULLISH UPTREND - AUTO {"ON" if st.session_state.auto_trading else "OFF"}')
    candles = []
    p = live_price
    for i in range(candle_count):
        p = p + random.uniform(-90*vol_mult,110*vol_mult) + (15*vol_mult)
        candles.append(round(p,2))
    df_candle = pd.DataFrame({f'{selected_market.split(" - ")[0]} LIVE - V72 PRO {tf_label} {candle_count} CANDLES - AUTO {"ON" if st.session_state.auto_trading else "OFF"}': candles})
    st.line_chart(df_candle, height=260)
    st.write(f'BALANCE CHART - GREEN LINE - V72 PRO - {account_mode} {start_amount} - {selected_market.split(" - ")[0]} {tf_label} - GREEN RISING - 72 JORA KA')
    hist = st.session_state.price_hist_real if account_mode=='REAL' else st.session_state.price_hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BALANCE {start_amount} PKR - V72 PRO {selected_market.split(" - ")[0]} {tf_label} GREEN': hist})
    st.line_chart(df_bal, height=160)
    st.write(f'WAITING - V72 PRO - {selected_market} - {tf_label} - Candle Up Down + Pine + Deposit + 24H - 5x24=120 Trades - AUTO {"ON" if st.session_state.auto_trading else "OFF"} - ALERT SOUND {"ON" if st.session_state.alert_sound else "OFF"} - 72 JORA KA')
    st.write(f'PA HAR ONE HOUR 5 TRADER - 24H RESULTS - {account_mode} {start_amount} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO - 72 JORA KA - AUTO {"ON" if st.session_state.auto_trading else "OFF"}')
    st.markdown(f'<div style="background:#220022;border:2px solid #F0F;border-radius:12px;padding:10px;margin:8px 0"><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px"><div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H TRADES {tf_label}</div><div style="color:#0F0;font-size:18px;font-weight:900">{st.session_state.total24}/120</div></div><div style="background:#000;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H PROFIT {selected_market.split(" - ")[0]}</div><div style="color:#FFD700;font-size:18px;font-weight:900">+{current_profit} PKR</div></div><div style="background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H WIN % {tf_label} AUTO</div><div style="color:#F0F;font-size:18px;font-weight:900">92%</div></div></div><div style="margin-top:8px"><div style="background:#333;height:10px;border-radius:5px"><div style="background:linear-gradient(90deg,#0F0,#FFD700);height:10px;border-radius:5px;width:{int((st.session_state.total24/120)*100)}%"></div></div></div></div>', unsafe_allow_html=True)
    if st.button(f'MANUAL TRADE 250 PKR - {account_mode} {start_amount} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO YELLOW 72 JORA KA - ALERT SOUND', key='manual_v72'):
        is_win=random.random()<0.92; profit=random.uniform(300,450) if is_win else random.uniform(-60,-30); t=datetime.now().strftime('%I:%M:%S %p')
        if account_mode=='REAL':
            st.session_state.real_bal+=profit; st.session_state.real_profit+=profit; st.session_state.real_trades+=1; st.session_state.total24+=1
            st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'WIN 250 RS - V72 PRO MANUAL {tf_label} 72 JORA KA {st.session_state.total24}/120','Profit':f'{round(profit)} PKR | Bal {int(st.session_state.real_bal)}','Bal':int(st.session_state.real_bal),'Market':f'{selected_market} {tf_label}','Method':f'Manual V72 {tf_label}'})
        else:
            st.session_state.demo_bal+=profit; st.session_state.demo_profit+=profit; st.session_state.demo_trades+=1
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            st.session_state.history.insert(0,{'Time':t,'Account':'DEMO','Result':f'WIN 250 RS - V72 PRO DEMO {tf_label} 72 JORA KA','Profit':f'{round(profit)} | Bal {int(st.session_state.demo_bal)}','Bal':int(st.session_state.demo_bal),'Market':f'{selected_market} {tf_label}','Method':f'Demo V72 {tf_label}'})
        if st.session_state.alert_sound and is_win:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            st.balloons()
            st.success(f'WIN {round(profit)} PKR - {account_mode} - {selected_market.split(" - ")[0]} {tf_label} - ALERT SOUND KALA SAH TRADE WIN SHA - V72 PRO 72 JORA KA')
        else:
            st.success(f'WIN {round(profit)} PKR - {account_mode} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO 72 JORA KA - YELLOW VISIBLE')
    if st.button(f'FORCE TRADE - {account_mode} - {selected_market.split(" - ")[0]} {tf_label} - V72 PRO YELLOW 72 JORA KA - AUTO {"ON" if st.session_state.auto_trading else "OFF"}', key='force_v72'):
        is_win=random.random()<0.92; profit=random.uniform(300,450) if is_win else random.uniform(-60,-30); t=datetime.now().strftime('%I:%M:%S %p')
        if account_mode=='REAL':
            st.session_state.real_bal
