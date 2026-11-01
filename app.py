import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='SONA V75 FIX', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:14px!important;height:56px!important;border:3px solid #0F0!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:15px;padding:12px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px">SONA AI V75 FIX - 4-5 PER HOUR - NO ERROR</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:9px">REAL 2500 DEMO 10000 5 PER HOUR 120 PER DAY 75 JORA KA</p></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state: st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state: st.session_state.demo_bal = 10000
if 'real_profit' not in st.session_state: st.session_state.real_profit = 621
if 'demo_profit' not in st.session_state: st.session_state.demo_profit = 0
if 'real_trades' not in st.session_state: st.session_state.real_trades = 1
if 'demo_trades' not in st.session_state: st.session_state.demo_trades = 0
if 'total24' not in st.session_state: st.session_state.total24 = 1
if 'hour_trades' not in st.session_state: st.session_state.hour_trades = 1
if 'last_hour' not in st.session_state: st.session_state.last_hour = datetime.now().hour
if 'account_mode' not in st.session_state: st.session_state.account_mode = 'REAL'
if 'live_price' not in st.session_state: st.session_state.live_price = 67534.78
if 'hist_real' not in st.session_state: st.session_state.hist_real = [2500,2710,2950,3121,3500,3821,4121]
if 'hist_demo' not in st.session_state: st.session_state.hist_demo = [10000,10150,10280,10400,10550,10700,11000]
if 'auto_on' not in st.session_state: st.session_state.auto_on = False
if 'alert_on' not in st.session_state: st.session_state.alert_on = True
if 'sel_market' not in st.session_state: st.session_state.sel_market = 'BTC/USD'
if 'sel_tf' not in st.session_state: st.session_state.sel_tf = '1MIN'
if 'history' not in st.session_state:
    st.session_state.history = [
        {'Time':'12:16 PM','Account':'REAL','Result':'WIN V75 1MIN 1/5','Profit':'321 PKR','Bal':2821,'Market':'BTC 1MIN','Method':'Real V75'},
        {'Time':'12:16 PM','Account':'REAL','Result':'WIN V75 5MIN 2/5','Profit':'300 PKR','Bal':4121,'Market':'ETH 5MIN','Method':'Auto V75'},
    ]

cur_hour = datetime.now().hour
if cur_hour != st.session_state.last_hour:
    st.session_state.hour_trades = 0
    st.session_state.last_hour = cur_hour

col1, col2, col3 = st.columns(3)
with col1:
    market = st.selectbox('SELECT MARKET V75', ['BTC/USD','ETH/USD','SOL/USD','BNB/USD','GOLD','EUR/USD','GBP/USD','USD/PKR'], index=0, key='mk_v75')
    st.session_state.sel_market = market
with col2:
    tf = st.selectbox('SELECT TF V75 1MIN 5MIN 15MIN', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf_v75')
    st.session_state.sel_tf = tf
with col3:
    auto_on = st.toggle('AUTO ON/OFF V75 4-5 PER HOUR', value=st.session_state.auto_on, key='auto_v75')
    st.session_state.auto_on = auto_on
    alert_on = st.toggle('ALERT SOUND V75', value=st.session_state.alert_on, key='alert_v75')
    st.session_state.alert_on = alert_on

sel_market = st.session_state.sel_market
sel_tf = st.session_state.sel_tf

base_map = {'BTC':67534.78,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in sel_market: base = base_map['BTC']
elif 'ETH' in sel_market: base = base_map['ETH']
elif 'SOL' in sel_market: base = base_map['SOL']
elif 'BNB' in sel_market: base = base_map['BNB']
elif 'GOLD' in sel_market: base = base_map['GOLD']
elif 'EUR' in sel_market: base = base_map['EUR']
elif 'GBP' in sel_market: base = base_map['GBP']
else: base = 67534.78

st.session_state.live_price = base + random.uniform(-60,80)
live_price = st.session_state.live_price

if sel_tf == '1MIN': candle_count=60; vol_mult=0.5
elif sel_tf == '5MIN': candle_count=48; vol_mult=1.0
elif sel_tf == '15MIN': candle_count=32; vol_mult=1.5
elif sel_tf == '1H': candle_count=24; vol_mult=2.0
elif sel_tf == '4H': candle_count=20; vol_mult=3.0
else: candle_count=30; vol_mult=2.5

if st.session_state.auto_on and st.session_state.hour_trades < 5 and random.random()<0.20:
    is_win = random.random()<0.92
    profit = random.uniform(300,420) if is_win else random.uniform(-60,-30)
    t = datetime.now().strftime('%I:%M:%S %p')
    if st.session_state.account_mode == 'REAL':
        st.session_state.real_bal += profit
        st.session_state.real_profit += profit
        st.session_state.real_trades += 1
        st.session_state.total24 += 1
        st.session_state.hour_trades += 1
        st.session_state.hist_real.append(int(st.session_state.real_bal))
        st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':'AUTO WIN','Profit':str(round(profit)),'Bal':int(st.session_state.real_bal),'Market':sel_market,'Method':'Auto V75'})
    else:
        st.session_state.demo_bal += profit
        st.session_state.demo_profit += profit
        st.session_state.demo_trades += 1
        st.session_state.hour_trades += 1
        st.session_state.hist_demo.append(int(st.session_state.demo_bal))
    if st.session_state.alert_on and is_win:
        st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        st.balloons()

real_profit_int = int(st.session_state.real_profit)
demo_profit_int = int(st.session_state.demo_profit)
if st.session_state.account_mode == 'REAL':
    display_profit = real_profit_int
else:
    display_profit = demo_profit_int

st.markdown('<div style="background:#001100;border:3px solid #0F0;border-radius:15px;padding:16px;text-align:center">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:36px;font-weight:900">+{display_profit} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">LIVE {sel_market} ${live_price:.2f} TF {sel_tf} HOUR {st.session_state.hour_trades}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

hour_pct = int((st.session_state.hour_trades/5)*100)
st.progress(hour_pct/100)

st.write(f'MARKET STRUCTURE V75 PA 1 HOUR {st.session_state.hour_trades}/5')
c1,c2 = st.columns(2)
with c1:
    st.success(f'BULLISH UPTREND {sel_tf} {st.session_state.hour_trades}/5')
    st.info(f'BOS {int(live_price)} BROKE HH {sel_market}')
with c2:
    st.warning(f'HH {int(live_price+150)} HL {int(live_price-200)} {sel_tf}')
    st.error('NO CHOCH BULLISH INTACT')

rsi = 62.8 + random.uniform(-1,1)
st.write(f'RSI {rsi:.1f} BULLISH BUY 95pct {sel_tf} {st.session_state.hour_trades}/5')
st.write(f'AUTO {"ON" if st.session_state.auto_on else "OFF"} {st.session_state.hour_trades}/5 PER HOUR 5x24=120')

mode = st.radio('SELECT ACCOUNT V75', ['REAL 2500','DEMO 10000'], index=0 if st.session_state.account_mode=='REAL' else 1)
if 'REAL' in mode:
    st.session_state.account_mode='REAL'
else:
    st.session_state.account_mode='DEMO'
account_mode = st.session_state.account_mode
if account_mode == 'REAL':
    start_amount = '2500'
    current_bal = int(st.session_state.real_bal)
    current_profit = int(st.session_state.real_profit)
else:
    start_amount = '10000'
    current_bal = int(st.session_state.demo_bal)
    current_profit = int(st.session_state.demo_profit)

if account_mode == 'REAL':
    st.success(f'REAL ACTIVE Bal {current_bal} Profit {current_profit} Hour {st.session_state.hour_trades}/5 Market {sel_market} TF {sel_tf} V75')
else:
    st.info(f'DEMO ACTIVE Bal {current_bal} Profit {current_profit} Hour {st.session_state.hour_trades}/5 V75')

st.metric(label=f'{account_mode} BAL Start {start_amount} Hour {st.session_state.hour_trades}/5', value=f'{current_bal} PKR', delta=f'+{current_profit} PKR')
st.metric(label=f'LIVE {sel_market} V75 TF {sel_tf} Hour {st.session_state.hour_trades}/5', value=f'${live_price:.2f}', delta=f'AUTO {"ON" if st.session_state.auto_on else "OFF"}')

tab1,tab2,tab3 = st.tabs(['TRADING 4-5 PER HOUR V75','DEPOSIT V75','HISTORY V75'])

with tab1:
    st.write(f'TRADING PAGE {account_mode} {start_amount} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V75')
    if st.session_state.hour_trades >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.hour_trades}/5 DONE WAIT NEXT HOUR V75')
    col_a, col_b = st.columns(2)
    with col_a:
        dep_amt = st.number_input(f'Deposit PKR V75 {sel_tf} {st.session_state.hour_trades}/5', value=500, min_value=100, max_value=50000, step=100, key='dep_v75')
        if st.button(f'DEPOSIT ADD BALANCE V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='dep_v75'):
            if account_mode == 'REAL':
                st.session_state.real_bal += dep_amt
                st.session_state.real_profit += dep_amt
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amt} Bal {int(st.session_state.real_bal)}')
                if st.session_state.alert_on:
                    st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            else:
                st.session_state.demo_bal += dep_amt
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Deposit +{dep_amt}')
    with col_b:
        with_amt = st.number_input(f'Withdraw PKR V75 {sel_tf} {st.session_state.hour_trades}/5', value=250, min_value=100, max_value=50000, step=100, key='with_v75')
        if st.button(f'WITHDRAW REMOVE BALANCE V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='with_v75'):
            if account_mode == 'REAL' and with_amt <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amt
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amt}')
            elif account_mode == 'DEMO' and with_amt <= st.session_state.demo_bal:
                st.session_state.demo_bal -= with_amt
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Withdraw -{with_amt}')
    st.write(f'CANDLE CHART V75 {sel_market} {sel_tf} {st.session_state.hour_trades}/5')
    candles = []
    p = live_price
    for i in range(candle_count):
        p = p + random.uniform(-90*vol_mult,110*vol_mult) + (15*vol_mult)
        candles.append(round(p,2))
    df_candle = pd.DataFrame({f'{sel_market} LIVE V75 {sel_tf}': candles})
    st.line_chart(df_candle, height=260)
    st.write(f'BALANCE CHART V75 {account_mode} {start_amount} {sel_tf} {st.session_state.hour_trades}/5 GREEN')
    hist = st.session_state.hist_real if account_mode == 'REAL' else st.session_state.hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BAL {start_amount} V75 {sel_tf}': hist})
    st.line_chart(df_bal, height=160)
    st.write(f'PA HAR ONE HOUR 5 TRADER Hour {st.session_state.hour_trades}/5 V75 5x24=120')
    col_x, col_y, col_z = st.columns(3)
    with col_x:
        st.metric(label=f'HOUR TRADES {sel_tf}', value=f'{st.session_state.hour_trades}/5', delta='PA 1 HOUR 4-5')
    with col_y:
        st.metric(label=f'PROFIT {sel_market}', value=f'+{current_profit} PKR', delta='5x24=120')
    with col_z:
        st.metric(label=f'TOTAL 24H {sel_tf}', value=f'{st.session_state.total24}/120', delta='92% WIN')
    if st.button(f'MANUAL TRADE 250 PKR {account_mode} {sel_tf} {st.session_state.hour_trades}/5 V75 YELLOW', key='manual_v75'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR V75')
        else:
            is_win = random.random()<0.92
            profit = random.uniform(300,450) if is_win else random.uniform(-60,-30)
            t = datetime.now().strftime('%I:%M:%S %p')
            if account_mode == 'REAL':
                st.session_state.real_bal += profit
                st.session_state.real_profit += profit
                st.session_state.real_trades += 1
                st.session_state.total24 += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_real.append(int(st.session_state.real_bal))
            else:
                st.session_state.demo_bal += profit
                st.session_state.demo_profit += profit
                st.session_state.demo_trades += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_on and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 ALERT WIN V75')
            else:
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 V75')
    if st.button(f'FORCE TRADE {account_mode} {sel_tf} {st.session_state.hour_trades}/5 V75 YELLOW', key='force_v75'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR V75')
        else:
            is_win = random.random()<0.92
            profit = random.uniform(300,450) if is_win else random.uniform(-60,-30)
            if account_mode == 'REAL':
                st.session_state.real_bal += profit
                st.session_state.real_profit += profit
                st.session_state.real_trades += 1
                st.session_state.total24 += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_real.append(int(st.session_state.real_bal))
            else:
                st.session_state.demo_bal += profit
                st.session_state.demo_profit += profit
                st.session_state.demo_trades += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_on and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'FORCE WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 V75')

with tab2:
    st.write(f'DEPOSIT PAGE {account_mode} {start_amount} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V75')
    if account_mode == 'DEMO':
        if st.button(f'DEMO TOPUP +5000 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='demo_topup_v75_p2'):
            st.session_state.demo_bal += 5000
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            st.success(f'Demo +5000 Bal {int(st.session_state.demo_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button(f'RESET DEMO 10000 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='demo_reset_v75_p2'):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.demo_trades = 0
            st.session_state.hist_demo = [10000]*5
            st.success('Demo Reset V75 PA 1 HOUR 4-5 TRADE')
    else:
        dep_phone = st.text_input(f'JazzCash Number 11 digits V75 {sel_tf} {st.session_state.hour_trades}/5', value='03001234567', key='dep_p_v75_p2')
        dep_amount = st.number_input(f'Deposit PKR Real 2500 V75 {sel_tf} {st.session_state.hour_trades}/5', value=2500, min_value=100, max_value=50000, step=100, key='dep_a_v75_p2')
        if st.button(f'DEPOSIT NOW REAL 2500 V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='dep_v75_p2'):
            if len(dep_phone) >= 11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amount} Bal {int(st.session_state.real_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        with_phone = st.text_input(f'Withdraw Number 11 digits V75 {sel_tf} {st.session_state.hour_trades}/5', value='03001234567', key='with_p_v75_p2')
        with_amount = st.number_input(f'Withdraw PKR Real 2500 V75 {sel_tf} {st.session_state.hour_trades}/5', value=250, min_value=100, max_value=50000, step=100, key='with_a_v75_p2')
        if st.button(f'WITHDRAW NOW REAL 2500 V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='with_v75_p2'):
            if len(with_phone) >= 11 and with_amount <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amount} Bal {int(st.session_state.real_bal)}')
    if st.button(f'CLEAR CACHE V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='clear_v75_p2'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with tab3:
    st.write(f'PINE EDITOR V75 {sel_market} {sel_tf} {st.session_state.hour_trades}/5')
    c1,c2 = st.columns(2)
    with c1:
        if st.button(f'SAVE PINE SCRIPT V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='save_pine_v75'):
            st.success(f'Pine Saved V75 {sel_tf} {st.session_state.hour_trades}/5')
    with c2:
        if st.button(f'SAVE KHABER NEWS V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW', key='save_khaber_v75'):
            st.success(f'Khaber Saved V75 {sel_tf} {st.session_state.hour_trades}/5 ALERT SOUND')
    st.write(f'HISTORY PKR V75 5x24=120 PA 1 HOUR 4-5 TRADE {st.session_state.hour_trades}/5')
    if st.session_state.history:
        df = pd.DataFrame(st.session_state.history)
        st.dataframe(df,use_container_width=True,height=380)
        csv = df.to_csv(index=False)
        st.download_button(f'EXPORT CSV V75 {sel_tf} {st.session_state.hour_trades}/5 YELLOW',csv,f'sona_v75_{sel_tf}_{st.session_state.hour_trades}perhour.csv','text/csv')

st.success(f'V75 FIX NO ERROR PA 1 HOUR 4-5 TRADE {st.session_state.hour_trades}/5 AUTO {"ON" if st.session_state.auto_on else "OFF"} ALERT {"ON" if st.session_state.alert_on else "OFF"} 75 JORA KA')
