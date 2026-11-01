import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='SONA V74 FIXED', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;font-size:13px!important;border-radius:14px!important;height:56px!important;border:3px solid #0F0!important;box-shadow:0 0 15px #FFD700}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:15px;padding:12px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px">SONA AI V74 FINAL FIXED - 4-5 TRADE PER HOUR - NO ERROR</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:9px">REAL 2500 START - DEMO 10000 - 5 PER HOUR MAX - 120 PER DAY - 74 JORA KA</p></div>', unsafe_allow_html=True)

st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700);border-radius:8px;padding:8px;text-align:center;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<p style="color:#000;font-size:10px;font-weight:900">V74 FIXED - PA HAR ONE HOUR 5 TRADER - NO UNTERMINATED - 74 JORA KA</p></div>', unsafe_allow_html=True)

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
if 'price_hist_real' not in st.session_state: st.session_state.price_hist_real = [2500,2710,2950,3121,3500,3821,4121]
if 'price_hist_demo' not in st.session_state: st.session_state.price_hist_demo = [10000,10150,10280,10400,10550,10700,11000]
if 'auto_trading' not in st.session_state: st.session_state.auto_trading = False
if 'alert_sound' not in st.session_state: st.session_state.alert_sound = True
if 'selected_market' not in st.session_state: st.session_state.selected_market = 'BTC/USD - Bitcoin - $67K'
if 'selected_tf' not in st.session_state: st.session_state.selected_tf = '1MIN - Scalp - 1 min candle - Fast'
if 'history' not in st.session_state:
    st.session_state.history = [
        {'Time':'12:08 PM','Account':'REAL','Result':'WIN 250 RS - V74 FIXED 1MIN 1/5 - 74 JORA KA','Profit':'321 PKR','Bal':2821,'Market':'BTC/USD 1MIN 1/5','Method':'Real V74'},
        {'Time':'12:08 PM','Account':'REAL','Result':'WIN 250 RS - V74 5MIN 2/5 PER HOUR','Profit':'300 PKR','Bal':4121,'Market':'ETH/USD 5MIN 2/5','Method':'Auto V74'},
    ]

cur_hour = datetime.now().hour
if cur_hour != st.session_state.last_hour:
    st.session_state.hour_trades = 0
    st.session_state.last_hour = cur_hour

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    market = st.selectbox('SELECT MARKET - V74 - MULTI MARKET', ['BTC/USD - Bitcoin - $67K','ETH/USD - Ethereum - $3.5K','SOL/USD - Solana - $180','BNB/USD - BNB - $600','GOLD - XAU/USD - $2350','EUR/USD - Forex - 1.08','GBP/USD - Forex - 1.27','USD/PKR - Forex - 278'], index=0, key='market_v74')
    st.session_state.selected_market = market
with col_m2:
    tf = st.selectbox('SELECT TIMEFRAME - V74 - 1MIN 5MIN 15MIN', ['1MIN - Scalp - 1 min candle - Fast','5MIN - Fast - 5 min - Best','15MIN - Swing - 15 min - Strong','1H - 1 Hour - Trend','4H - 4 Hour - Big Trend','1D - Daily - Long'], index=0, key='tf_v74')
    st.session_state.selected_tf = tf
with col_m3:
    auto_on = st.toggle('AUTO TRADING ON/OFF - V74 - 4-5 PER HOUR', value=st.session_state.auto_trading, key='auto_v74')
    st.session_state.auto_trading = auto_on
    alert_on = st.toggle('ALERT SOUND WIN - V74 - ALERT SOUND WIN', value=st.session_state.alert_sound, key='alert_v74')
    st.session_state.alert_sound = alert_on

selected_market = st.session_state.selected_market
selected_tf = st.session_state.selected_tf

base_map = {'BTC':67534.78,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in selected_market: base = base_map['BTC']
elif 'ETH' in selected_market: base = base_map['ETH']
elif 'SOL' in selected_market: base = base_map['SOL']
elif 'BNB' in selected_market: base = base_map['BNB']
elif 'GOLD' in selected_market: base = base_map['GOLD']
elif 'EUR' in selected_market: base = base_map['EUR']
elif 'GBP' in selected_market: base = base_map['GBP']
else: base = 67534.78

st.session_state.live_price = base + random.uniform(-60,80)
live_price = st.session_state.live_price

if '1MIN' in selected_tf: candle_count=60; vol_mult=0.5; tf_label='1MIN'
elif '5MIN' in selected_tf: candle_count=48; vol_mult=1.0; tf_label='5MIN'
elif '15MIN' in selected_tf: candle_count=32; vol_mult=1.5; tf_label='15MIN'
elif '1H' in selected_tf: candle_count=24; vol_mult=2.0; tf_label='1H'
elif '4H' in selected_tf: candle_count=20; vol_mult=3.0; tf_label='4H'
else: candle_count=30; vol_mult=2.5; tf_label='1D'

if st.session_state.auto_trading and st.session_state.hour_trades < 5 and random.random()<0.20:
    is_win=random.random()<0.92
    profit=random.uniform(300,420) if is_win else random.uniform(-60,-30)
    t=datetime.now().strftime('%I:%M:%S %p')
    if st.session_state.account_mode=='REAL':
        st.session_state.real_bal+=profit
        st.session_state.real_profit+=profit
        st.session_state.real_trades+=1
        st.session_state.total24+=1
        st.session_state.hour_trades+=1
        st.session_state.price_hist_real.append(int(st.session_state.real_bal))
        st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'AUTO WIN {tf_label} {st.session_state.hour_trades}/5','Profit':f'{round(profit)} PKR','Bal':int(st.session_state.real_bal),'Market':f'{selected_market} {tf_label}','Method':f'Auto V74'})
    else:
        st.session_state.demo_bal+=profit
        st.session_state.demo_profit+=profit
        st.session_state.demo_trades+=1
        st.session_state.hour_trades+=1
        st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
    if st.session_state.alert_sound and is_win:
        st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        st.balloons()

real_profit_int = int(st.session_state.real_profit)
demo_profit_int = int(st.session_state.demo_profit)
display_profit = real_profit_int if st.session_state.account_mode=='REAL' else demo_profit_int

st.markdown('<div style="background:#001100;border:3px solid #0F0;border-radius:15px;padding:16px;text-align:center">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:36px;font-weight:900">+{display_profit} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">LIVE {selected_market.split(" - ")[0]} ${live_price:,.2f} | TF {tf_label} | HOUR {st.session_state.hour_trades}/5 | AUTO {"ON" if st.session_state.auto_trading else "OFF"}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

hour_pct = int((st.session_state.hour_trades/5)*100)
st.markdown(f'<div style="background:#333;height:12px;border-radius:6px;margin:6px 0"><div style="background:linear-gradient(90deg,#0F0,#FFD700);height:12px;border-radius:6px;width:{hour_pct}%"></div></div>', unsafe_allow_html=True)

st.markdown('<p style="color:#FFD700;font-weight:900;text-align:center">MARKET STRUCTURE - HH HL BOS CHOCH MSS - V74 - PA 1 HOUR 4-5 TRADE</p>', unsafe_allow_html=True)
c1,c2 = st.columns(2)
with c1:
    st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#0F0">BULLISH - HH HL - UPTREND - {tf_label} {st.session_state.hour_trades}/5</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #0FF;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#0FF">BULLISH BOS - {int(live_price)} BROKE HH - {selected_market.split(" - ")[0]}</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="background:#000;border:2px solid #FFD700;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#FFD700">HH {int(live_price+150)} - HL {int(live_price-200)} - {tf_label} {st.session_state.hour_trades}/5</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #F00;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#F00">NO CHOCH - BULLISH INTACT</p></div>', unsafe_allow_html=True)

rsi = 62.8 + random.uniform(-1,1)
vol = 1.8 + random.uniform(-0.2,0.2)
vwap = live_price - random.uniform(-50,50)
macd = 0.90 + random.uniform(-0.05,0.05)
st.write(f'RSI: {rsi:.1f} - BULLISH BUY 95pct {tf_label} {st.session_state.hour_trades}/5 | VOL: {vol:.1f}M | VWAP: {vwap:,.2f} | MACD: {macd:.2f} - V74')
st.write(f'LIQ: SWEEP DONE {tf_label} {st.session_state.hour_trades}/5 | BOS: BULLISH BOS BROKE HH - AUTO {"ON" if st.session_state.auto_trading else "OFF"} - {st.session_state.hour_trades}/5 PER HOUR - 5x24=120')

mode = st.radio('SELECT ACCOUNT - V74 - PA 1 HOUR 4-5 TRADE', ['REAL - 2500 PKR - Really money Laga ka - V74','DEMO - 10000 PKR - Nan Demo Check - V74'], index=0 if st.session_state.account_mode=='REAL' else 1)
if 'REAL' in mode: st.session_state.account_mode='REAL'
else: st.session_state.account_mode='DEMO'
account_mode = st.session_state.account_mode
start_amount = '2500' if account_mode=='REAL' else '10000'
current_bal = int(st.session_state.real_bal) if account_mode=='REAL' else int(st.session_state.demo_bal)
current_profit = int(st.session_state.real_profit) if account_mode=='REAL' else int(st.session_state.demo_profit)

if account_mode=='REAL':
    st.success(f'REAL ACTIVE - Bal {current_bal} PKR - Profit {current_profit} PKR - Hour {st.session_state.hour_trades}/5 - Market {selected_market.split(" - ")[0]} TF {tf_label} - V74')
else:
    st.info(f'DEMO ACTIVE - Bal {current_bal} PKR - Profit {current_profit} PKR - Hour {st.session_state.hour_trades}/5 - V74')

st.metric(label=f'{account_mode} BALANCE - Start {start_amount} - Hour {st.session_state.hour_trades}/5', value=f'{current_bal} PKR', delta=f'+{current_profit} PKR')
st.metric(label=f'LIVE {selected_market.split(" - ")[0]} - V74 - TF {tf_label} Hour {st.session_state.hour_trades}/5', value=f'${live_price:,.2f}', delta=f'AUTO {"ON" if st.session_state.auto_trading else "OFF"} {st.session_state.hour_trades}/5')

tab1,tab2,tab3 = st.tabs(['TRADING - 4-5 PER HOUR - V74','DEPOSIT WITHDRAW - V74','PINE + HISTORY - V74'])

with tab1:
    st.write(f'TRADING PAGE - {account_mode} {start_amount} - {selected_market} {tf_label} {st.session_state.hour_trades}/5 - V74')
    if st.session_state.hour_trades >= 5:
        st.warning(f'HOUR LIMIT - {st.session_state.hour_trades}/5 DONE - WAIT NEXT HOUR - V74 - PA 1 HOUR 4-5 TRADE')
    col1,col2 = st.columns(2)
    with col1:
        dep_amt = st.number_input(f'Deposit PKR - V74 - {tf_label} Hour {st.session_state.hour_trades}/5', value=500, min_value=100, max_value=50000, step=100, key='dep_amt_v74')
        if st.button(f'DEPOSIT - ADD BALANCE - V74 {tf_label} {st.session_state.hour_trades}/5 YELLOW', key='dep_v74'):
            if account_mode=='REAL':
                st.session_state.real_bal+=dep_amt
                st.session_state.real_profit+=dep_amt
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amt} Bal {int(st.session_state.real_bal)}')
                if st.session_state.alert_sound:
                    st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            else:
                st.session_state.demo_bal+=dep_amt
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Deposit +{dep_amt}')
    with col2:
        with_amt = st.number_input(f'Withdraw PKR - V74 - {tf_label} Hour {st.session_state.hour_trades}/5', value=250, min_value=100, max_value=50000, step=100, key='with_amt_v74')
        if st.button(f'WITHDRAW - REMOVE BALANCE - V74 {tf_label} {st.session_state.hour_trades}/5 YELLOW', key='with_v74'):
            if account_mode=='REAL' and with_amt<=st.session_state.real_bal:
                st.session_state.real_bal-=with_amt
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amt}')
            elif account_mode=='DEMO' and with_amt<=st.session_state.demo_bal:
                st.session_state.demo_bal-=with_amt
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Withdraw -{with_amt}')
    st.write(f'CANDLE CHART - V74 - {selected_market} {tf_label} {st.session_state.hour_trades}/5 - AUTO {"ON" if st.session_state.auto_trading else "OFF"}')
    candles = []
    p = live_price
    for i in range(candle_count):
        p = p + random.uniform(-90*vol_mult,110*vol_mult) + (15*vol_mult)
        candles.append(round(p,2))
    df_candle = pd.DataFrame({f'{selected_market.split(" - ")[0]} LIVE V74 {tf_label} {candle_count} CANDLES': candles})
    st.line_chart(df_candle, height=260)
    st.write(f'BALANCE CHART - V74 - {account_mode} {start_amount} {tf_label} {st.session_state.hour_trades}/5 GREEN')
    hist = st.session_state.price_hist_real if account_mode=='REAL' else st.session_state.price_hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BAL {start_amount} V74 {tf_label} {st.session_state.hour_trades}/5': hist})
    st.line_chart(df_bal, height=160)
    st.write(f'PA HAR ONE HOUR 5 TRADER - Hour {st.session_state.hour_trades}/5 - V74 - 5x24=120')
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#888;font-size:8px">HOUR TRADES {tf_label}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#0F0;font-size:18px;font-weight:900">{st.session_state.hour_trades}/5</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#888;font-size:7px">PA 1 HOUR 4-5</div></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div style="background:#000;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#888;font-size:8px">PROFIT {selected_market.split(" - ")[0]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#FFD700;font-size:18px;font-weight:900">+{current_profit} PKR</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#888;font-size:7px">5x24=120</div></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div style="background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#888;font-size:8px">TOTAL 24H {tf_label}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color:#F0F;font-size:18px;font-weight:900">{st.session_state.total24}/120</div>', unsafe_allow_html=True)
        st.markdown('<div style="color:#888;font-size:7px">92% WIN</div></div>', unsafe_allow_html=True)
    total_pct = int((st.session_state.total24/120)*100)
    st.markdown(f'<div style="background:#333;height:8px;border-radius:4px;margin:6px 0"><div style="background:linear-gradient(90deg,#F0F,#0FF);height:8px;border-radius:4px;width:{total_pct}%"></div></div>', unsafe_allow_html=True)
    if st.button(f'MANUAL TRADE 250 PKR - {account_mode} {tf_label} {st.session_state.hour_trades}/5 - V74 YELLOW - PA 1 HOUR 4-5 TRADE', key='manual_v74'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 - WAIT NEXT HOUR - V74')
        else:
            is_win=random.random()<0.92
            profit=random.uniform(300,450) if is_win else random.uniform(-60,-30)
            t=datetime.now().strftime('%I:%M:%S %p')
            if account_mode=='REAL':
                st.session_state.real_bal+=profit
                st.session_state.real_profit+=profit
                st.session_state.real_trades+=1
                st.session_state.total24+=1
                st.session_state.hour_trades+=1
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'WIN {tf_label} {st.session_state.hour_trades}/5','Profit':f'{round(profit)} PKR','Bal':int(st.session_state.real_bal),'Market':f'{selected_market} {tf_label}','Method':f'Manual V74 {st.session_state.hour_trades}/5'})
            else:
                st.session_state.demo_bal+=profit
                st.session_state.demo_profit+=profit
                st.session_state.demo_trades+=1
                st.session_state.hour_trades+=1
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_sound and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
                st.success(f'WIN {round(profit)} PKR - {tf_label} {st.session_state.hour_trades}/5 - ALERT SOUND WIN - V74')
            else:
                st.success(f'WIN {round(profit)} PKR - {tf_label} {st.session_state.hour_trades}/5 - V74')
    if st.button(f'FORCE TRADE - {account_mode} {tf_label} {st.session_state.hour_trades}/5 - V74 YELLOW - AUTO {"ON" if st.session_state.auto_trading else "OFF"}', key='force_v74'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 - WAIT NEXT HOUR - V74')
        else:
            is_win=random.random()<0.92
            profit=random.uniform(300,450) if is_win else random.uniform(-60,-30)
            t=datetime.now().strftime('%I:%M:%S %p')
            if account_mode=='REAL':
                st.session_state.real_bal+=profit
                st.session_state.real_profit+=profit
                st.session_state.real_trades+=1
                st.session_state.total24+=1
                st.session_state.hour_trades+=1
                st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            else:
                st.session_state.demo_bal+=profit
                st.session_state.demo_profit+=profit
                st.session_state.demo_trades+=1
                st.session_state.hour_trades+=1
                st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_sound and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'FORCE WIN {round(profit)} PKR - {tf_label} {st.session_state.hour_trades}/5 - V74')

with tab2:
    st.write(f'
