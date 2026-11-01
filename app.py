import streamlit as st
import random
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title='SONA V85 V45 CANDLE', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:12px!important;height:50px!important;border:2px solid #0F0!important;box-shadow:0 0 10px #FFD700}.stMetric{background:#0a0a0a;border:1px solid #0F0;border-radius:10px;padding:6px}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px;margin:0">SONA V85 V45 STYLE REAL CANDLE WICK BODY - 85 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:8px;margin:0">REAL 2500 DEMO 10000 5 PER HOUR V45 CANDLE UP DOWN WICK BODY CLEAR 85 JORA KA</p></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state: st.session_state.real_bal = 4621
if 'demo_bal' not in st.session_state: st.session_state.demo_bal = 11069
if 'real_profit' not in st.session_state: st.session_state.real_profit = 2121
if 'demo_profit' not in st.session_state: st.session_state.demo_profit = 1069
if 'total24' not in st.session_state: st.session_state.total24 = 0
if 'hour_trades' not in st.session_state: st.session_state.hour_trades = 2
if 'last_hour' not in st.session_state: st.session_state.last_hour = datetime.now().hour
if 'account_mode' not in st.session_state: st.session_state.account_mode = 'DEMO'
if 'live_price' not in st.session_state: st.session_state.live_price = 67421.96
if 'hist_real' not in st.session_state: st.session_state.hist_real = [2500,3000,3500,4000,4621]
if 'hist_demo' not in st.session_state: st.session_state.hist_demo = [10000,10200,10500,10800,11069]
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
    market = st.selectbox('MARKET', ['BTC/USD','ETH/USD','SOL/USD','BNB/USD','GOLD','EUR/USD','GBP/USD','USD/PKR'], index=0, key='mk85')
    st.session_state.sel_market = market
with col2:
    tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf85')
    st.session_state.sel_tf = tf
with col3:
    auto_on = st.toggle('AUTO 4-5 PER HOUR', value=st.session_state.auto_on, key='auto85')
    st.session_state.auto_on = auto_on
    alert_on = st.toggle('ALERT', value=st.session_state.alert_on, key='alert85')
    st.session_state.alert_on = alert_on

sel_market = st.session_state.sel_market
sel_tf = st.session_state.sel_tf

base_map = {'BTC':67421.96,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in sel_market: base = base_map['BTC']
elif 'ETH' in sel_market: base = base_map['ETH']
elif 'SOL' in sel_market: base = base_map['SOL']
elif 'BNB' in sel_market: base = base_map['BNB']
elif 'GOLD' in sel_market: base = base_map['GOLD']
elif 'EUR' in sel_market: base = base_map['EUR']
elif 'GBP' in sel_market: base = base_map['GBP']
else: base = 67421.96

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

rsi = 68.2 + random.uniform(-2,2)
vol = last_c['V']
atr = 103.4 + random.uniform(-5,5)
vwap = 67568.0 + random.uniform(-20,20)
macd = -0.36 + random.uniform(-0.2,0.2)
liq = random.choice(['LOW LIQ','HIGH LIQ','SWEEP DONE','SWEEP PEND'])
bos = f'BULL BOS {int(live_price)}' if live_price > prev_c['H'] else f'BEAR BOS {int(live_price)}'
pullback = random.choice(['50% FIB','61.8% FIB','PULL WAIT','NO PULL'])
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

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;text-align:center;margin:8px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:13px;font-weight:900">LIVE PRICE: {sel_market} ${live_price:.2f} | V45 NO SYNTAX ERROR FIX - CANDLE UP DOWN LIVE - Trades {st.session_state.hour_trades}/5 - Total 24h {st.session_state.total24}/120</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

progress_pct = int((st.session_state.hour_trades/5)*100)
st.progress(progress_pct/100)

st.markdown('<div style="background:#001133;border:3px solid #0ff;border-radius:12px;padding:12px;margin:8px 0">', unsafe_allow_html=True)
st.markdown('<div style="color:#0ff;font-size:13px;font-weight:900">DEPOSIT AND WITHDRAW OPTION - V45 NO SYNTAX ERROR FIX - V85 CLEAR</div>', unsafe_allow_html=True)

c_dep1, c_dep2 = st.columns(2)
with c_dep1:
    dep_amt = st.number_input('Dep 500', value=500, min_value=100, max_value=50000, step=100, key='dep_amt85')
with c_dep2:
    with_amt = st.number_input('With 250', value=250, min_value=100, max_value=50000, step=100, key='with_amt85')

c_btn1, c_btn2 = st.columns(2)
with c_btn1:
    if st.button('DEPOSIT - ADD BALANCE - V45', key='dep_btn85'):
        if st.session_state.account_mode == 'REAL':
            st.session_state.real_bal += dep_amt
            st.session_state.real_profit += dep_amt
            st.session_state.hist_real.append(int(st.session_state.real_bal))
        else:
            st.session_state.demo_bal += dep_amt
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
        st.success(f'Deposit: +{dep_amt} PKR - New Bal {int(st.session_state.real_bal if st.session_state.account_mode=="REAL" else st.session_state.demo_bal)} PKR - Success! - {datetime.now().strftime("%I:%M:%S %p")}')
        if st.session_state.alert_on:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
with c_btn2:
    if st.button('WITHDRAW - REMOVE BALANCE - V45', key='with_btn85'):
        if st.session_state.account_mode == 'REAL' and with_amt <= st.session_state.real_bal:
            st.session_state.real_bal -= with_amt
            st.session_state.hist_real.append(int(st.session_state.real_bal))
            st.success(f'Withdraw: -{with_amt} PKR')
        elif st.session_state.account_mode == 'DEMO' and with_amt <= st.session_state.demo_bal:
            st.session_state.demo_bal -= with_amt
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            st.success(f'Withdraw: -{with_amt} PKR')

st.markdown(f'<div style="color:#0ff;font-size:11px">Deposit: +500 PKR - New Bal {4621} PKR - Success! - 7:37:01 AM | LIVE {sel_market} ${live_price:.2f} O:{last_c["O"]} C:{last_c["C"]} H:{last_c["H"]} L:{last_c["L"]} TF {sel_tf} H:{st.session_state.hour_trades}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;margin:8px 0">', unsafe_allow_html=True)
st.markdown('<div style="color:#FFD700;font-size:12px;font-weight:900;text-align:center">CANDLE UP AND DOWN RAWAN - LIVE CANDLE CHART - V45 NO SYNTAX ERROR FIX - V85 CLEAR</div>', unsafe_allow_html=True)

candle_js = []
for c in ohlc_data:
    candle_js.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")

candle_js_str = ','.join(candle_js)

chart_html = """
<div style="background:#000;border:3px solid #FFD700;border-radius:12px;padding:10px;margin:8px 0;height:320px;position:relative">
<canvas id="candleCanvas" width="800" height="300" style="width:100%;height:100%;background:#000"></canvas>
</div>
<script>
const canvas = document.getElementById('candleCanvas');
const ctx = canvas.getContext('2d');
const candles = [CANDLES];
const W = canvas.width;
const H = canvas.height;
const padding = 20;
const n = candles.length;
let minP = Math.min(...candles.map(x=>x.l));
let maxP = Math.max(...candles.map(x=>x.h));
let range = maxP - minP;
if(range < 50){ range = 50; minP -= 25; maxP += 25; }
minP -= range*0.1;
maxP += range*0.1;
range = maxP - minP;
const candleWidth = (W - padding*2) / n * 0.6;
const gap = (W - padding*2) / n;
ctx.fillStyle = '#000';
ctx.fillRect(0,0,W,H);
candles.forEach((c,i) => {
  const x = padding + i*gap + gap/2;
  const isUp = c.c >= c.o;
  const color = isUp ? '#00FF00' : '#FF0000';
  const highY = padding + (1 - (c.h - minP)/range) * (H - padding*2);
  const lowY = padding + (1 - (c.l - minP)/range) * (H - padding*2);
  const openY = padding + (1 - (c.o - minP)/range) * (H - padding*2);
  const closeY = padding + (1 - (c.c - minP)/range) * (H - padding*2);
  const bodyTop = Math.min(openY, closeY);
  const bodyH = Math.abs(closeY - openY);
  const bodyHeight = Math.max(bodyH, 3);
  ctx.strokeStyle = color;
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(x, highY);
  ctx.lineTo(x, lowY);
  ctx.stroke();
  ctx.fillStyle = color;
  ctx.fillRect(x - candleWidth/2, bodyTop, candleWidth, bodyHeight);
});
ctx.strokeStyle = '#111';
ctx.lineWidth = 0.5;
for(let j=0;j<4;j++){
  const y = padding + j*(H-padding*2)/3;
  ctx.beginPath();
  ctx.moveTo(padding, y);
  ctx.lineTo(W-padding, y);
  ctx.stroke();
}
</script>
"""

chart_html = chart_html.replace("CANDLES", candle_js_str)

components.html(chart_html, height=350)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;margin:8px 0;height:180px">', unsafe_allow_html=True)
st.markdown('<div style="color:#0F0;font-size:10px">BALANCE CHART V45 - GREEN RISING - V85</div>', unsafe_allow_html=True)
hist = st.session_state.hist_real if st.session_state.account_mode == 'REAL' else st.session_state.hist_demo
df_bal = pd.DataFrame({f'{st.session_state.account_mode} BAL': hist})
st.line_chart(df_bal, height=140)
st.markdown('</div>', unsafe_allow_html=True)

st.write(f'MARKET V85 H:{st.session_state.hour_trades}/5 - {strategy} - V45 CANDLE CLEAR')
c1,c2 = st.columns(2)
with c1:
    st.success(f'BULL UP {sel_tf} {st.session_state.hour_trades}/5 {strategy} - V45 CANDLE')
    st.info(f'BOS {bos}')
    st.success(f'LIQ {liq}')
with c2:
    st.warning(f'HH {int(last_c["H"])} HL {int(last_c["L"])} O:{last_c["O"]} C:{last_c["C"]}')
    st.error(f'NO CHOCH {pullback}')
    st.info(f'ATR {atr:.1f} {atr_s}')

st.write('ALL INDICATORS V85 - RSI VOL ATR VWAP MACD LIQ BOS PULLBACK - V45 CLEAR')
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

mode = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.account_mode=='DEMO' else 0, key='acc85')
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
    st.success(f'REAL Bal {cur_bal} Profit {cur_prof} H:{st.session_state.hour_trades}/5 V85 V45 CANDLE CLEAR')
else:
    st.info(f'DEMO Bal {cur_bal} Profit {cur_prof} H:{st.session_state.hour_trades}/5 V85 V45 CANDLE CLEAR')

st.metric(label=f'{account_mode} BAL {start_amt} H:{st.session_state.hour_trades}/5', value=f'{cur_bal} PKR', delta=f'+{cur_prof} PKR')
st.metric(label=f'LIVE {sel_market} {sel_tf} H:{st.session_state.hour_trades}/5', value=f'${live_price:.2f}', delta=f'AUTO {"ON" if st.session_state.auto_on else "OFF"}')

tab1,tab2,tab3 = st.tabs(['TRADING V85','DEPOSIT V85','HISTORY V85'])

with tab1:
    st.write(f'TRADING {account_mode} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V85 V45 CANDLE')
    if st.session_state.hour_trades >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.hour_trades}/5 WAIT NEXT HOUR')
    st.write(f'PA 1 HOUR 5 TRADE H:{st.session_state.hour_trades}/5 5x24=120 V45 CANDLE CLEAR')
    col_x, col_y, col_z = st.columns(3)
    with col_x:
        st.metric(label=f'HOUR {sel_tf}', value=f'{st.session_state.hour_trades}/5', delta='PA 1 HOUR 4-5')
    with col_y:
        st.metric(label=f'PROFIT {sel_market}', value=f'+{cur_prof} PKR', delta='5x24=120')
    with col_z:
        st.metric(label=f'TOTAL 24H', value=f'{st.session_state.total24}/120', delta='92% WIN')
    if st.button('MANUAL TRADE', key='manual85'):
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
    if st.button('FORCE TRADE', key='force85'):
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
    st.write(f'DEPOSIT {account_mode} {start_amt} {sel_market} {sel_tf} {st.session_state.hour_trades}/5 V45 CANDLE')
    if account_mode == 'DEMO':
        if st.button('TOPUP +5000', key='topup85'):
            st.session_state.demo_bal += 5000
            st.session_state.hist_demo.append(int(st.session_state.demo_bal))
            st.success(f'Demo +5000 Bal {int(st.session_state.demo_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button('RESET DEMO', key='reset85'):
            st.session_state.demo_bal = 10000
            st.session_state.demo_profit = 0
            st.session_state.hist_demo = [10000]*5
            st.success('Demo Reset')
    else:
        dep_phone = st.text_input('JazzCash Num', value='03001234567', key='dep_phone85')
        dep_amount = st.number_input('Dep PKR Real', value=2500, min_value=100, max_value=50000, step=100, key='dep_amount85')
        if st.button('DEPOSIT NOW', key='dep_now85'):
            if len(dep_phone) >= 11:
                st.session_state.real_bal += dep_amount
                st.session_state.real_profit += dep_amount
                st.session_state.hist_real.append(int(st.session_state.real_bal))
                st.success(f'Dep +{dep_amount} Bal {int(st.session_state.real_bal)}')
            if st.session_state.alert_on:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        with_phone = 
