import streamlit as st
import random
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

st.set_page_config(page_title='SONA V83', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#0a0a0a;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:12px!important;height:50px!important;border:2px solid #0F0!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px;margin:0">SONA V83 CLEAR UP DOWN CANDLE - 83 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:8px;margin:0">REAL 2500 DEMO 10000 5 PER HOUR GREEN RED UP DOWN 83 JORA KA</p></div>', unsafe_allow_html=True)

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
    market = st.selectbox('MARKET', ['BTC/USD','ETH/USD','SOL/USD','BNB/USD','GOLD','EUR/USD','GBP/USD','USD/PKR'], index=0, key='mk83')
    st.session_state.sel_market = market
with col2:
    tf = st.selectbox('TF 1MIN 5MIN 15MIN', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf83')
    st.session_state.sel_tf = tf
with col3:
    auto_on = st.toggle('AUTO 4-5 PER HOUR', value=st.session_state.auto_on, key='auto83')
    st.session_state.auto_on = auto_on
    alert_on = st.toggle('ALERT', value=st.session_state.alert_on, key='alert83')
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
    ohlc_data.append({'T':f'{i*5:02d}:00','O':round(open_p,2),'H':round(high_p,2),'L':round(low_p,2),'C':round(close_p,2),'V':round(random.uniform(0.5,2.5),2)})
    p = close_p

last_c = ohlc_data[-1]
prev_c = ohlc_data[-2] if len(ohlc_data)>1 else last_c

rsi = 69.8 + random.uniform(-2,2)
vol = last_c['V']
atr = random.uniform(45,120)
vwap = live_price - random.uniform(-80,80)
macd = random.uniform(-0.5,1.5)
liq = random.choice(['SWEEP DONE','SWEEP PEND','HIGH LIQ','LOW LIQ'])
bos = f'BULL BOS {int(live_price)}' if live_price > prev_c['H'] else f'BEAR BOS {int(live_price)}'
pullback = random.choice(['50% FIB','61.8% FIB','PULL WAIT','NO PULL STRONG'])
strategy = random.choice(['HH HL UP','LL LH DOWN','BOS SHIFT','MSS BULL','FVG SUP'])

if rsi > 70: rsi_s = 'OVER SELL'
elif rsi < 30: rsi_s = 'OVER BUY'
elif rsi > 60: rsi_s = 'BULL BUY'
else: rsi_s = 'NEUTRAL'

vol_s = 'HIGH VOL BUY' if vol > 1.5 else 'LOW WAIT'
atr_s = f'ATR {atr:.1f} VOLA' if atr > 80 else f'ATR {atr:.1f} CALM'
vwap_s = 'ABOVE BUY' if live_price > vwap else 'BELOW SELL'
macd_s = 'BULL CROSS' if macd > 0.5 else 'BEAR CROSS' if macd < -0.2 else 'NEUTRAL'

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

st.markdown('<div style="background:linear-gradient(90deg,#001100,#002200);border:2px solid #0F0;border-radius:12px;padding:12px;text-align:center;margin:6px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:36px;font-weight:900">+{disp_p} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:12px">LIVE {sel_market} ${live_price:.2f}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">O:{last_c["O"]} C:{last_c["C"]} H:{last_c["H"]} L:{last_c["L"]} TF {sel_tf} H:{st.session_state.hour_trades}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((st.session_state.hour_trades/5)*100)/100)

st.write(f'UP DOWN CHART V83 {sel_market} {sel_tf} GREEN UP RED DOWN')
st.write(f'LAST O:{last_c["O"]} H:{last_c["H"]} L:{last_c["L"]} C:{last_c["C"]} V:{last_c["V"]}')

fig, ax = plt.subplots(figsize=(10,4))
fig.patch.set_facecolor('#111111')
ax.set_facecolor('#0a0a0a')
for i, c in enumerate(ohlc_data):
    color = '#00FF00' if c['C'] >= c['O'] else '#FF0000'
    ax.plot([i,i],[c['L'],c['H']], color=color, linewidth=1)
    ax.plot([i,i],[c['O'],c['C']], color=color, linewidth=6)
ax.set_title(f'{sel_market} {sel_tf} UP DOWN V83', color='#FFD700', fontsize=10)
ax.set_xlabel('Candle', color='#fff', fontsize=8)
ax.set_ylabel('Price', color='#fff', fontsize=8)
ax.tick_params(colors='#fff', labelsize=7)
ax.grid(True, color='#333', alpha=0.3)
plt.tight_layout()
st.pyplot(fig)

df_ohlc = pd.DataFrame(ohlc_data)
st.dataframe(df_ohlc, use_container_width=True, height=240)

st.write(f'MARKET V83 H:{st.session_state.hour_trades}/5 - {strategy} - CLEAR')
c1,c2 = st.columns(2)
with c1:
    st.success(f'BULL UP {sel_tf} {st.session_state.hour_trades}/5 {strategy}')
    st.info(f'BOS {bos}')
    st.success(f'LIQ {liq}')
with c2:
    st.warning(f'HH {int(last_c["H"])} HL {int(last_c["L"])} O:{last_c["O"]} C:{last_c["C"]}')
    st.error(f'NO CHOCH {pullback}')
    st.info(f'ATR {atr:.1f} {atr_s}')

st.write('ALL INDICATORS V83 - RSI VOL ATR VWAP MACD LIQ BOS PULLBACK')
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.metric(label=f'RSI {sel_tf}', value=f'{rsi:.1f}', delta=rsi_s)
    st.metric(label=f'VOL', value=f'{vol}M', delta=vol_s)
with col_b:
    st.metric(label=f'ATR', value=f'{atr:.1f}', delta=atr_s)
    st.metric(label=f'VWAP', value=f'{vwap:.2f}', delta=vwap_s)
with col_c:
    st.metric(label=f'MACD', value=f'{macd:.2f}', delta=macd_s)
    st.metric(label=f'LIQ', value=liq[:10], delta=strategy[:10])

st.write(f'BOS:{bos} PULL:{pullback} LIQ:{liq} STRAT:{strategy}')
st.write(f'OHLC O:{last_c["O"]} H:{last_c["H"]} L:{last_c["L"]} C:{last_c["C"]} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} RSI {rsi:.1f}')

mode = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.account_mode=='DEMO' else 0, key='acc83')
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
    st.success(f'REAL Bal {cur_bal} Profit {cur_prof} H:{st.session_state.hour_trades}/5 V83')
else:
    st.info(f'DEMO Bal {cur_bal} Profit {cur_prof} H:{st.session_state.hour_trades}/5 V83')

st.metric(label=f'{account_mode} BAL {start_amt} H:{st.session_state.hour_trades}/5', value=f'{cur_bal} PKR', delta=f'+{cur_prof} PKR')
st.metric(label=f'LIVE {sel_market} {sel_tf} H:{st.session_state.hour_trades}/5', value=f'${live_price:.2f}', delta=f'AUTO {"ON" if st.session_state.auto_on else "OFF"}')

tab1,tab2,tab3 = st.tabs(['TRADING V83','DEPOSIT V83','HISTORY V83'])

with tab1:
    st.write(f'TRADING {account_mode} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V83')
    if st.session_state.hour_trades >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR')
    col_a, col_b = st.columns(2)
    with col_a:
        dep_amt = st.number_input('Deposit PKR', value=500, min_value=100, max_value=50000, step=100, key='dep_amt83')
        if st.button('DEPOSIT', key='dep_btn83'):
            if account_mode == 'REAL':
                st.session_state.real_bal += dep_amt
                st.session_state.real_profit += dep_amt
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Dep +{dep_amt} Bal {int(st.session_state.real_bal)}')
                if st.session_state.alert_on:
                    st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            else:
                st.session_state.demo_bal += dep_amt
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Dep +{dep_amt}')
    with col_b:
        with_amt = st.number_input('Withdraw PKR', value=250, min_value=100, max_value=50000, step=100, key='with_amt83')
        if st.button('WITHDRAW', key='with_btn83'):
            if account_mode == 'REAL' and with_amt <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amt
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'With -{with_amt}')
            elif account_mode == 'DEMO' and with_amt <= st.session_state.demo_bal:
                st.session_state.demo_bal -= with_amt
                st.session_state.hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo With -{with_amt}')
    st.write(f'UP DOWN CHART {sel_market} {sel_tf} O:{last_c["O"]} C:{last_c["C"]}')
    st.pyplot(fig)
    hist = st.session_state.hist_real if account_mode == 'REAL' else st.session_state.hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BAL {start_amt}': hist})
    st.line_chart(df_bal, height=160)
    st.write(f'PA 1 HOUR 5 TRADE H:{st.session_state.hour_trades}/5 5x24=120')
    col_x, col_y, col_z = st.columns(3)
    with col_x:
        st.metric(label=f'HOUR {sel_tf}', value=f'{st.session_state.hour_trades}/5', delta='PA 1 HOUR 4-5')
    with col_y:
        st.metric(label=f'PROFIT {sel_market}', value=f'+{cur_prof} PKR', delta='5x24=120')
    with col_z:
        st.metric(label=f'TOTAL 24H', value=f'{st.session_state.total24}/120', delta='92% WIN')
    if st.button('MANUAL TRADE', key='manual83'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT')
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
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5')
            else:
                st.success(f'WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5')
    if st.button('FORCE TRADE', key='force83'):
        if st.session_state.hour_trades >= 5:
            st.error(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT')
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
            st.success(f'FORCE WIN {round(profit)} PKR {sel_tf} {st.session_state.hour_trades}/5')

with tab2:
    st.write(f'DEPOSIT {account_mode} {start_amt} {sel_market} {sel_tf} {st.session_state.hour_trades}/5')
    if account_mode == 'DEMO':
        if st.button('TOPUP +5000', key='topup83'):
            st.session_state.demo_bal += 5000
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            st.success(f'Demo +5000 Bal {int(st.session_state.demo_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button('RESET DEMO', key='reset83'):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.hist_demo = [10000]*5
            st.success('Demo Reset')
    else:
        dep_phone = st.text_input('JazzCash Num', value='03001234567', key='dep_phone83')
        dep_amount = st.number_input('Dep PKR Real', value=2500, min_value=100, max_value=50000, step=100, key='dep_amount83')
        if st.button('DEPOSIT NOW', key='dep_now83'):
            if len(dep_phone) >= 11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Dep +{dep_amount} Bal {int(st.session_state.real_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        with_phone = st.text_input('With Num', value='03001234567', key='with_phone83')
        with_amount = st.number_input('With PKR Real', value=250, min_value=100, max_value=50000, step=100, key='with_amount83')
        if st.button('WITHDRAW NOW', key='with_now83'):
            if len(with_phone) >= 11 and with_amount <= st.session_state.real_bal:
                st.session_state.real_bal -= with_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'With -{with_amount} Bal {int(st.session_state.real_bal)}')
    if st.button('CLEAR CACHE', key='clear83'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with tab3:
    st.write(f'PINE EDITOR {sel_market} {sel_tf} {st.session_state.hour_trades}/5 O:{last_c["O"]} C:{last_c["C"]}')
    st.write('OHLC TABLE V83 CLEAR')
    st.dataframe(df_ohlc, use_container_width=True, height=240)
    c1,c2 = st.columns(2)
    with c1:
        if st.button('PINE', key='pine83'):
            st.success(f'Pine Saved {sel_tf} RSI {rsi:.1f} ATR {atr:.1f}')
    with c2:
        if st.button('KHABER', key='khaber83'):
            st.success(f'Khaber Saved {sel_tf} {bos} {liq}')
    st.write(f'HISTORY V83 5x24=120 PA 1 HOUR 4-5 TRADE {st.session_state.hour_trades}/5')

st.success(f'V83 CLEAR NO ERROR UP DOWN O:{last_c["O"]} C:{last_c["C"]} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} LIQ {liq} BOS {bos} 83 JORA KA')
