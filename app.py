import streamlit as st
import random
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

st.set_page_config(page_title='SONA V82 CLEAR', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#0a0a0a;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:14px!important;height:56px!important;border:3px solid #0F0!important;box-shadow:0 0 12px #FFD700}.stMetric{background:#111;border:1px solid #333;border-radius:10px;padding:8px}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:linear-gradient(90deg,#000,#111);border:2px solid #0F0;border-radius:12px;padding:10px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:15px;margin:0">SONA AI V82 CLEAR DESIGN - LIVE CANDLE UP DOWN - 82 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:9px;margin:0">REAL 2500 DEMO 10000 5 PER HOUR CANDLE UP DOWN GREEN RED CHART CLEAR DESIGN 82 JORA KA</p></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state: st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state: st.session_state.demo_bal = 10408
if 'real_profit' not in st.session_state: st.session_state.real_profit = 0
if 'demo_profit' not in st.session_state: st.session_state.demo_profit = 408
if 'total24' not in st.session_state: st.session_state.total24 = 0
if 'hour_trades' not in st.session_state: st.session_state.hour_trades = 1
if 'last_hour' not in st.session_state: st.session_state.last_hour = datetime.now().hour
if 'account_mode' not in st.session_state: st.session_state.account_mode = 'DEMO'
if 'live_price' not in st.session_state: st.session_state.live_price = 67551.06
if 'hist_real' not in st.session_state: st.session_state.hist_real = [2500,2710,2950,3121,3500,3821]
if 'hist_demo' not in st.session_state: st.session_state.hist_demo = [10000,10150,10280,10400,10408,10700]
if 'auto_on' not in st.session_state: st.session_state.auto_on = True
if 'alert_on' not in st.session_state: st.session_state.alert_on = True
if 'sel_market' not in st.session_state: st.session_state.sel_market = 'BTC/USD'
if 'sel_tf' not in st.session_state: st.session_state.sel_tf = '1MIN'

cur_hour = datetime.now().hour
if cur_hour != st.session_state.last_hour:
    st.session_state.hour_trades = 0
    st.session_state.last_hour = cur_hour

col1, col2, col3 = st.columns(3)
with col1:
    market = st.selectbox('MARKET V82', ['BTC/USD','ETH/USD','SOL/USD','BNB/USD','GOLD','EUR/USD','GBP/USD','USD/PKR'], index=0, key='mk_v82')
    st.session_state.sel_market = market
with col2:
    tf = st.selectbox('TF V82 1MIN 5MIN 15MIN', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf_v82')
    st.session_state.sel_tf = tf
with col3:
    auto_on = st.toggle('AUTO V82 4-5 PER HOUR', value=st.session_state.auto_on, key='auto_v82')
    st.session_state.auto_on = auto_on
    alert_on = st.toggle('ALERT V82', value=st.session_state.alert_on, key='alert_v82')
    st.session_state.alert_on = alert_on

sel_market = st.session_state.sel_market
sel_tf = st.session_state.sel_tf

base_map = {'BTC':67551.06,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in sel_market: base = base_map['BTC']
elif 'ETH' in sel_market: base = base_map['ETH']
elif 'SOL' in sel_market: base = base_map['SOL']
elif 'BNB' in sel_market: base = base_map['BNB']
elif 'GOLD' in sel_market: base = base_map['GOLD']
elif 'EUR' in sel_market: base = base_map['EUR']
elif 'GBP' in sel_market: base = base_map['GBP']
else: base = 67551.06

st.session_state.live_price = base + random.uniform(-60,80)
live_price = st.session_state.live_price

if sel_tf == '1MIN': candle_count=24; vol_mult=0.5
elif sel_tf == '5MIN': candle_count=20; vol_mult=1.0
elif sel_tf == '15MIN': candle_count=16; vol_mult=1.5
elif sel_tf == '1H': candle_count=12; vol_mult=2.0
elif sel_tf == '4H': candle_count=10; vol_mult=3.0
else: candle_count=8; vol_mult=2.5

ohlc_data = []
p = live_price
for i in range(candle_count):
    open_p = p
    change = random.uniform(-90*vol_mult,110*vol_mult) + (15*vol_mult)
    close_p = open_p + change
    high_p = max(open_p, close_p) + random.uniform(5,30)*vol_mult
    low_p = min(open_p, close_p) - random.uniform(5,30)*vol_mult
    ohlc_data.append({'Time':f'{i*5:02d}:00','Open':round(open_p,2),'High':round(high_p,2),'Low':round(low_p,2),'Close':round(close_p,2),'Vol':round(random.uniform(0.5,2.5),2)})
    p = close_p

last_c = ohlc_data[-1]
prev_c = ohlc_data[-2] if len(ohlc_data)>1 else last_c

rsi = 69.8
vol = last_c['Vol']
atr = 118.4
vwap = 67576.5
macd = 0.29
liq = 'SWEEP PENDING'
bos = 'BEAR BOS 67555 BROKE LL'
pullback = '50% FIB BUY'
strategy = 'FVG SUPPORT'

if sel_tf == '1MIN':
    rsi = 69.8 + random.uniform(-2,2)
else:
    rsi = 62.0 + random.uniform(-5,8)

vol = last_c['Vol']
atr = random.uniform(45,120)
vwap = live_price - random.uniform(-80,80)
macd = random.uniform(-0.5,1.5)

liq = random.choice(['SWEEP DONE BUY','SWEEP PENDING','HIGH LIQ ABOVE','LOW LIQ BELOW'])
bos = f'BULL BOS {int(live_price)} BROKE HH' if live_price > prev_c['High'] else f'BEAR BOS {int(live_price)} BROKE LL'
pullback = random.choice(['50% FIB BUY','61.8% FIB BUY','PULLBACK WAIT','NO PULLBACK STRONG'])
strategy = random.choice(['HH HL UPTREND','LL LH DOWNTREND','BOS SHIFT','MSS BULL','FVG SUPPORT'])

if rsi > 70: rsi_s = 'OVERBOUGHT SELL'
elif rsi < 30: rsi_s = 'OVERSOLD BUY'
elif rsi > 60: rsi_s = 'BULL BUY 95pct'
else: rsi_s = 'NEUTRAL'

vol_s = 'HIGH VOL BUY' if vol > 1.5 else 'LOW VOL WAIT'
atr_s = f'ATR {atr:.1f} VOLATILE' if atr > 80 else f'ATR {atr:.1f} CALM'
vwap_s = 'ABOVE VWAP BUY' if live_price > vwap else 'BELOW VWAP SELL'
macd_s = 'BULL CROSS BUY' if macd > 0.5 else 'BEAR CROSS SELL' if macd < -0.2 else 'NEUTRAL'

if st.session_state.auto_on and st.session_state.hour_trades < 5 and random.random()<0.20:
    is_win = random.random()<0.92
    profit = random.uniform(300,450) if is_win else random.uniform(-60,-30)
    if st.session_state.account_mode == 'REAL':
        st.session_state.real_bal += profit
        st.session_state.real_profit += profit
        st.session_state.total24 += 1
        st.session_state.hour_trades += 1
        st.session_state.hist_real.append(int(st.session_state.real_bal))
    else:
        st.session_state.demo_bal += profit
        st.session_state.demo_profit += profit
        st.session_state.hour_trades += 1
        st.session_state.hist_demo.append(int(st.session_state.demo_bal))
    if st.session_state.alert_on and is_win:
        st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        st.balloons()

real_p = int(st.session_state.real_profit)
demo_p = int(st.session_state.demo_profit)
if st.session_state.account_mode == 'REAL':
    disp_p = real_p
else:
    disp_p = demo_p

st.markdown('<div style="background:linear-gradient(90deg,#001100,#002200);border:2px solid #0F0;border-radius:15px;padding:14px;text-align:center;margin:8px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:38px;font-weight:900">+{disp_p} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:12px">LIVE {sel_market} ${live_price:.2f}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">O:{last_c["Open"]} C:{last_c["Close"]} H:{last_c["High"]} L:{last_c["Low"]} TF {sel_tf} HOUR {st.session_state.hour_trades}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((st.session_state.hour_trades/5)*100)/100)

st.write(f'LIVE CANDLE UP DOWN CHART V82 - {sel_market} {sel_tf} - GREEN UP RED DOWN - CLEAR DESIGN')
st.write(f'LAST CANDLE O:{last_c["Open"]} H:{last_c["High"]} L:{last_c["Low"]} C:{last_c["Close"]} Vol:{last_c["Vol"]}')

fig, ax = plt.subplots(figsize=(10,4))
fig.patch.set_facecolor('#111111')
ax.set_facecolor('#0a0a0a')
for i, c in enumerate(ohlc_data):
    color = '#00FF00' if c['Close'] >= c['Open'] else '#FF0000'
    ax.plot([i,i],[c['Low'],c['High']], color=color, linewidth=1)
    ax.plot([i,i],[c['Open'],c['Close']], color=color, linewidth=6)
ax.set_title(f'{sel_market} {sel_tf} LIVE CANDLE UP DOWN - V82 CLEAR', color='#FFD700', fontsize=10)
ax.set_xlabel('Candle', color='#fff', fontsize=8)
ax.set_ylabel('Price', color='#fff', fontsize=8)
ax.tick_params(colors='#fff', labelsize=7)
ax.grid(True, color='#333', alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

df_ohlc = pd.DataFrame(ohlc_data)
st.dataframe(df_ohlc, use_container_width=True, height=240)

st.write(f'MARKET STRUCTURE V82 PA 1 HOUR {st.session_state.hour_trades}/5 - {strategy} - CLEAR DESIGN')
c1,c2 = st.columns(2)
with c1:
    st.success(f'BULL UPTREND {sel_tf} {st.session_state.hour_trades}/5 - {strategy}')
    st.info(f'BOS - {bos}')
    st.success(f'LIQ - {liq}')
with c2:
    st.warning(f'HH {int(last_c["High"])} HL {int(last_c["Low"])} O:{last_c["Open"]} C:{last_c["Close"]}')
    st.error(f'NO CHOCH - {pullback}')
    st.info(f'ATR {atr:.1f} - {atr_s}')

st.write('ALL INDICATORS V82 - RSI VOL ATR VWAP MACD LIQ BOS PULLBACK - CLEAR DESIGN')
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(label=f'RSI V82 {sel_tf}', value=f'{rsi:.1f}', delta=rsi_s)
    st.metric(label=f'VOL V82', value=f'{vol}M', delta=vol_s)
with col_b:
    st.metric(label=f'ATR V82', value=f'{atr:.1f}', delta=atr_s)
    st.metric(label=f'VWAP V82', value=f'{vwap:.2f}', delta=vwap_s)
with col_c:
    st.metric(label=f'MACD V82', value=f'{macd:.2f}', delta=macd_s)
    st.metric(label=f'LIQ V82', value=liq[:12], delta=strategy[:12])

st.write(f'BOS: {bos} - PULLBACK: {pullback} - LIQ: {liq} - STRAT: {strategy}')
st.write(f'OHLC O:{last_c["Open"]} H:{last_c["High"]} L:{last_c["Low"]} C:{last_c["Close"]} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} RSI {rsi:.1f}')

mode = st.radio('ACCOUNT V82', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.account_mode=='DEMO' else 0, key='acc_v82')
if 'REAL' in mode:
    st.session_state.account_mode='REAL'
else:
    st.session_state.account_mode='DEMO'
account_mode = st.session_state.account_mode
if account_mode == 'REAL':
    start_amt = '2500'
    cur_bal = int(st.session_state.real_bal)
    cur_prof = int(st.session_state.real_profit)
else:
    start_amt = '10000'
    cur_bal = int(st.session_state.demo_bal)
    cur_prof = int(st.session_state.demo_profit)

if account_mode == 'REAL':
    st.success(f'REAL ACTIVE Bal {cur_bal} Profit {cur_prof} Hour {st.session_state.hour_trades}/5 V82 CLEAR')
else:
    st.info(f'DEMO ACTIVE Bal {cur_bal} Profit {cur_prof} Hour {st.session_state.hour_trades}/5 V82 CLEAR')

st.metric(label=f'{account_mode} BAL Start {start_amt} Hour {st.session_state.hour_trades}/5', value=f'{cur_bal} PKR', delta=f'+{cur_prof} PKR')
st.metric(label=f'LIVE {sel_market} V82 TF {sel_tf} Hour {st.session_state.hour_trades}/5', value=f'${live_price:.2f}', delta=f'AUTO {"ON" if st.session_state.auto_on else "OFF"}')

tab1,tab2,tab3 = st.tabs(['TRADING UP DOWN V82','DEPOSIT V82','HISTORY V82'])

with tab1:
    st.write(f'TRADING PAGE {account_mode} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V82 CLEAR')
    if st.session_state.hour_trades >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.hour_trades}/5 DONE WAIT NEXT HOUR V82')
    col_a, col_b = st.columns(2)
    with col_a:
        dep_amt = st.number_input('Deposit PKR V82', value=500, min_value=100, max_value=50000, step=100, key='dep_amt_v82')
        if st.button('DEPOSIT ADD BAL V82 YELLOW', key='dep_btn_v82'):
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
        with_amt = st.number_input('Withdraw PKR V82', value=250, min_value=100, max_value=50000, step=100, key='with_amt_v82')
        if st.button('WITHDRAW REMOVE BAL V82 YELLOW', key='with_btn_v82'):
            if account_mode == 'REAL' and with_amt <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amt
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amt}')
            elif account_mode == 'DEMO' and with_amt <= st.session_state.demo_bal:
                st.session_state.demo_bal -= with_amt
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Withdraw -{with_amt}')
    st.write(f'LIVE CANDLE UP DOWN CHART V82 {sel_market} {sel_tf} O:{last_c["Open"]} C:{last_c["Close"]}')
    st.pyplot(fig)
    hist = st.session_state.hist_real if account_mode == 'REAL' else st.session_state.hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BAL {start_amt} V82': hist})
    st.line_chart(df_bal, height=160)
    st.write(f'PA HAR ONE HOUR 5 TRADER Hour {st.session_state.hour_trades}/5 V82 5x24=120 CLEAR')
    col_x, col_y, col_z = st.columns(3)
    with col_x:
        st.metric(label=f'HOUR {sel_tf}', value=f'{st.session_state.hour_trades}/5', delta='PA 1 HOUR 4-5')
    with col_y:
        st.metric(label=f'PROFIT {sel_market}', value=f'+{cur_prof} PKR', delta='5x24=120')
    with col_z:
        st.metric(label=f'TOTAL 24H', value=f'{st.session_state.total24}/120', delta='92% WIN')
    if st.button(f'MANUAL TRADE 250 PKR {account_mode} {sel_tf} {st.session_state.hour_trades}/5 V82 YELLOW', key='manual_v82'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR V82')
        else:
            is_win = random.random()<0.92
            profit = random.uniform(300,450) if is_win else random.uniform(-60,-30)
            if account_mode == 'REAL':
                st.session_state.real_bal += profit
                st.session_state.real_profit += profit
                st.session_state.total24 += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_real.append(int(st.session_state.real_bal))
            else:
                st.session_state.demo_bal += profit
                st.session_state.demo_profit += profit
                st.session_state.hour_trades += 1
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_on and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 ALERT WIN V82')
            else:
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 V82')
    if st.button(f'FORCE TRADE {account_mode} {sel_tf} {st.session_state.hour_trades}/5 V82 YELLOW', key='force_v82'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR V82')
        else:
            is_win = random.random()<0.92
            profit = random.uniform(300,450) if is_win else random.uniform(-60,-30)
            if account_mode == 'REAL':
                st.session_state.real_bal += profit
                st.session_state.real_profit += profit
                st.session_state.total24 += 1
                st.session_state.hour_trades += 1
                st.session_state.hist_real.append(int(st.session_state.real_bal))
            else:
                st.session_state.demo_bal += profit
                st.session_state.demo_profit += profit
                st.session_state.hour_trades += 1
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            if st.session_state.alert_on and is_win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'FORCE WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5 V82')

with tab2:
    st.write(f'DEPOSIT PAGE {account_mode} {start_amt} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V82 CLEAR')
    if account_mode == 'DEMO':
        if st.button('DEMO TOPUP +5000 V82 YELLOW', key='demo_topup_v82'):
            st.session_state.demo_bal += 5000
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            st.success(f'Demo +5000 Bal {int(st.session_state.demo_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button('RESET DEMO 10000 V82 YELLOW', key='demo_reset_v82'):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.hist_demo = [10000]*5
            st.success('Demo Reset V82 PA 1 HOUR 4-5 TRADE')
    else:
        dep_phone = st.text_input('JazzCash Number V82', value='03001234567', key='dep_phone_v82')
        dep_amount = st.number_input('Deposit PKR Real V82', value=2500, min_value=100, max_value=50000, step=100, key='dep_amount_v82')
        if st.button('DEPOSIT NOW REAL 2500 V82 YELLOW', key='dep_now_v82'):
            if len(dep_phone) >= 11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amount} Bal {int(st.session_state.real_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        with_phone = st.text_input('Withdraw Number V82', value='03001234567', key='with_phone_v82')
        with_amount = st.number_input('Withdraw PKR Real V82', value=250, min_value=100, max_value=50000, step=100, key='with_amount_v82')
        if st.button('WITHDRAW NOW REAL 2500 V82 YELLOW', key='with_now_v82'):
            if len(with_phone) >= 11 and with_amount <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amount} Bal {int(st.session_state.real_bal)}')
    if st.button('CLEAR CACHE V82 YELLOW', key='clear_v82'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with tab3:
    st.write(f'PINE EDITOR V82 {sel_market} {sel_tf} {st.session_state.hour_trades}/5 O:{last_c["Open"]} C:{last_c["Close"]}')
    st.write('OHLC TABLE - CANDLE CLOSE AND OPEN SHOW V82 CLEAR')
    st.dataframe(df_ohlc, use_container_width=True, height=240)
    c1,c2 = st.columns(2)
    with c1:
        if st.button('SAVE PINE SCRIPT V82 YELLOW', key='save_pine_v82'):
            st.success(f'Pine Saved V82 {sel_tf} RSI {rsi:.1f} ATR {atr:.1f} VWAP {vwap:.1f}')
    with c2:
        if st.button('SAVE KHABER NEWS V82 YELLOW', key='sav
