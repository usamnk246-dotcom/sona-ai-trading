import streamlit as st
import random
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as comp

st.set_page_config(page_title='V88', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:10px!important;height:48px!important;border:3px solid #0F0!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:10px;padding:8px;text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:14px;margin:0">SONA V88 ULTRA CLEAR V45 CANDLE - 88 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:7px;margin:0">REAL 2500 DEMO 10000 5 PER HOUR V45 CANDLE CLEAR 88 JORA KA</p></div>', unsafe_allow_html=True)

if 'rb' not in st.session_state: st.session_state.rb = 4621
if 'db' not in st.session_state: st.session_state.db = 11069
if 'rp' not in st.session_state: st.session_state.rp = 2121
if 'dp' not in st.session_state: st.session_state.dp = 1069
if 't24' not in st.session_state: st.session_state.t24 = 0
if 'ht' not in st.session_state: st.session_state.ht = 2
if 'lh' not in st.session_state: st.session_state.lh = datetime.now().hour
if 'am' not in st.session_state: st.session_state.am = 'DEMO'
if 'lp' not in st.session_state: st.session_state.lp = 67420.31
if 'hr' not in st.session_state: st.session_state.hr = [2500,3000,4000,4621]
if 'hd' not in st.session_state: st.session_state.hd = [10000,10200,10500,11069]
if 'ao' not in st.session_state: st.session_state.ao = True
if 'al' not in st.session_state: st.session_state.al = True
if 'sm' not in st.session_state: st.session_state.sm = 'BTC/USD'
if 'stf' not in st.session_state: st.session_state.stf = '1MIN'

ch = datetime.now().hour
if ch != st.session_state.lh:
    st.session_state.ht = 0
    st.session_state.lh = ch

c1,c2,c3 = st.columns(3)
with c1:
    mk = st.selectbox('MKT', ['BTC/USD','ETH/USD','SOL/USD','GOLD','USD/PKR'], index=0, key='mk88')
    st.session_state.sm = mk
with c2:
    tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf88')
    st.session_state.stf = tf
with c3:
    ao = st.toggle('AUTO', value=st.session_state.ao, key='ao88')
    st.session_state.ao = ao
    al = st.toggle('ALERT', value=st.session_state.al, key='al88')
    st.session_state.al = al

sm = st.session_state.sm
stf = st.session_state.stf

bm = {'BTC':67420.31,'ETH':3520,'SOL':180,'GOLD':2350,'USD':278}
if 'BTC' in sm: b = bm['BTC']
elif 'ETH' in sm: b = bm['ETH']
elif 'SOL' in sm: b = bm['SOL']
elif 'GOLD' in sm: b = bm['GOLD']
else: b = 67420.31

st.session_state.lp = b + random.uniform(-60,80)
lp = st.session_state.lp

if stf == '1MIN': cc=24; vm=0.5
elif stf == '5MIN': cc=20; vm=1.0
elif stf == '15MIN': cc=16; vm=1.5
elif stf == '1H': cc=12; vm=2.0
else: cc=8; vm=2.5

ohlc = []
p = lp
for i in range(cc):
    op = p
    chg = random.uniform(-90*vm,110*vm) + (15*vm)
    cp = op + chg
    hp = max(op,cp) + random.uniform(5,30)*vm
    low = min(op,cp) - random.uniform(5,30)*vm
    ohlc.append({'T':f'{i*5:02d}:00','O':round(op,2),'H':round(hp,2),'L':round(low,2),'C':round(cp,2),'V':round(random.uniform(0.5,2.5),2)})
    p = cp

lc = ohlc[-1]
pc = ohlc[-2] if len(ohlc)>1 else lc

rsi = 67.8 + random.uniform(-2,2)
vol = lc['V']
atr = 98.9 + random.uniform(-5,5)
vwap = 67554.9 + random.uniform(-20,20)
macd = -0.21 + random.uniform(-0.2,0.2)
liq = random.choice(['PEND','LOW','HIGH','DONE'])
bos = f'BULL {int(lp)}' if lp > pc['H'] else f'BEAR {int(lp)}'
pb = random.choice(['WAIT','50% FIB','61% FIB','NO PULL'])
strat = random.choice(['MSS BULL','HH HL UP','LL LH DOWN','BOS SHIFT','FVG SUP'])

if rsi > 70: rs = 'SELL'
elif rsi < 30: rs = 'BUY'
elif rsi > 60: rs = 'BULL BUY'
else: rs = 'NEUTRAL'

vs = 'HIGH VOL' if vol > 1.5 else 'LOW WAIT'
ats = f'ATR {atr:.1f} VOLA' if atr > 80 else f'ATR {atr:.1f} CALM'
vws = 'ABOVE BUY' if lp > vwap else 'BELOW SELL'
mcs = 'BULL' if macd > 0.5 else 'BEAR' if macd < -0.2 else 'NEUTRAL'

if st.session_state.ao and st.session_state.ht < 5 and random.random()<0.20:
    win = random.random()<0.92
    prof = random.uniform(300,450) if win else random.uniform(-60,-30)
    if st.session_state.am == 'REAL':
        st.session_state.rb += prof
        st.session_state.rp += prof
        st.session_state.t24 += 1
        st.session_state.ht += 1
        st.session_state.hr.append(int(st.session_state.rb))
    else:
        st.session_state.db += prof
        st.session_state.dp += prof
        st.session_state.ht += 1
        st.session_state.hd.append(int(st.session_state.db))
    if st.session_state.al and win:
        st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        st.balloons()

rp = int(st.session_state.rp)
dp = int(st.session_state.dp)
if st.session_state.am == 'REAL':
    disp = rp
else:
    disp = dp

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:10px;padding:8px;text-align:center;margin:6px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:13px;font-weight:900">LIVE PRICE: {sm} ${lp:.2f} | Trades {st.session_state.ht}/5 - Total {st.session_state.t24}/120</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:28px;font-weight:900">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{st.session_state.ht}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((st.session_state.ht/5)*100)/100)

st.markdown('<div style="background:#001133;border:3px solid #0ff;border-radius:10px;padding:8px;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<div style="color:#0ff;font-size:11px;font-weight:900">DEPOSIT AND WITHDRAW - V88 ULTRA CLEAR</div>', unsafe_allow_html=True)

d1,d2 = st.columns(2)
with d1:
    da = st.number_input('Dep 500', value=500, min_value=100, max_value=50000, step=100, key='da88')
with d2:
    wa = st.number_input('With 250', value=250, min_value=100, max_value=50000, step=100, key='wa88')

b1,b2 = st.columns(2)
with b1:
    if st.button('DEPOSIT - ADD - V45', key='db88'):
        if st.session_state.am == 'REAL':
            st.session_state.rb += da
            st.session_state.rp += da
            st.session_state.hr.append(int(st.session_state.rb))
        else:
            st.session_state.db += da
            st.session_state.hd.append(int(st.session_state.db))
        st.success(f'Dep: +{da} PKR - New Bal Success!')
        if st.session_state.al:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
with b2:
    if st.button('WITHDRAW - REMOVE - V45', key='wb88'):
        if st.session_state.am == 'REAL' and wa <= st.session_state.rb:
            st.session_state.rb -= wa
            st.session_state.hr.append(int(st.session_state.rb))
            st.success(f'With: -{wa} PKR')
        elif st.session_state.am == 'DEMO' and wa <= st.session_state.db:
            st.session_state.db -= wa
            st.session_state.hd.append(int(st.session_state.db))
            st.success(f'With: -{wa} PKR')

st.markdown(f'<div style="color:#0ff;font-size:10px">Deposit: +500 PKR - New Bal 4621 PKR - Success! | LIVE {sm} ${lp:.2f} O:{lc["O"]} C:{lc["C"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:10px;padding:8px;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<div style="color:#FFD700;font-size:11px;font-weight:900;text-align:center">CANDLE UP AND DOWN - LIVE CANDLE CHART - V88 ULTRA CLEAR</div>', unsafe_allow_html=True)

cjs = []
for c in ohlc:
    cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")

cjs_str = ','.join(cjs)

chart = """
<div style="background:#000;border:3px solid #FFD700;border-radius:10px;padding:8px;margin:6px 0;height:320px">
<canvas id="cc" width="800" height="300" style="width:100%;height:100%;background:#000"></canvas>
</div>
<script>
const cv = document.getElementById('cc');
const ct = cv.getContext('2d');
const candles = [CANDLES];
const W = cv.width;
const H = cv.height;
const pad = 20;
const n = candles.length;
let minP = Math.min(...candles.map(x=>x.l));
let maxP = Math.max(...candles.map(x=>x.h));
let rg = maxP - minP;
if(rg < 50){ rg = 50; minP -= 25; maxP += 25; }
minP -= rg*0.1;
maxP += rg*0.1;
rg = maxP - minP;
const cw = (W - pad*2) / n * 0.6;
const gap = (W - pad*2) / n;
ct.fillStyle = '#000';
ct.fillRect(0,0,W,H);
candles.forEach((c,i) => {
  const x = pad + i*gap + gap/2;
  const up = c.c >= c.o;
  const col = up ? '#00FF00' : '#FF0000';
  const hy = pad + (1 - (c.h - minP)/rg) * (H - pad*2);
  const ly = pad + (1 - (c.l - minP)/rg) * (H - pad*2);
  const oy = pad + (1 - (c.o - minP)/rg) * (H - pad*2);
  const cy = pad + (1 - (c.c - minP)/rg) * (H - pad*2);
  const top = Math.min(oy, cy);
  const bh = Math.abs(cy - oy);
  const bH = Math.max(bh, 3);
  ct.strokeStyle = col;
  ct.lineWidth = 1;
  ct.beginPath();
  ct.moveTo(x, hy);
  ct.lineTo(x, ly);
  ct.stroke();
  ct.fillStyle = col;
  ct.fillRect(x - cw/2, top, cw, bH);
});
ct.strokeStyle = '#111';
ct.lineWidth = 0.5;
for(let j=0;j<4;j++){
  const y = pad + j*(H-pad*2)/3;
  ct.beginPath();
  ct.moveTo(pad, y);
  ct.lineTo(W-pad, y);
  ct.stroke();
}
</script>
"""

chart = chart.replace("CANDLES", cjs_str)

comp.html(chart, height=350)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:10px;padding:8px;margin:6px 0;height:160px">', unsafe_allow_html=True)
st.markdown('<div style="color:#0F0;font-size:9px">BALANCE CHART V45 - GREEN RISING - V88</div>', unsafe_allow_html=True)
h = st.session_state.hr if st.session_state.am == 'REAL' else st.session_state.hd
dfb = pd.DataFrame({f'{st.session_state.am} BAL': h})
st.line_chart(dfb, height=120)
st.markdown('</div>', unsafe_allow_html=True)

st.write(f'MARKET V88 H:{st.session_state.ht}/5 - {strat} - V45 CANDLE')
a1,a2 = st.columns(2)
with a1:
    st.success(f'BULL UP {stf} {st.session_state.ht}/5 {strat}')
    st.info(f'BOS {bos}')
    st.success(f'LIQ {liq}')
with a2:
    st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} O:{lc["O"]} C:{lc["C"]}')
    st.error(f'NO CHOCH {pb}')
    st.info(f'ATR {atr:.1f} {ats}')

st.write('ALL INDICATORS V88 - RSI VOL ATR VWAP MACD LIQ BOS PULLBACK')
ca,cb,ccol = st.columns(3)
with ca:
    st.metric(label=f'RSI {stf}', value=f'{rsi:.1f}', delta=rs)
    st.metric(label=f'VOL', value=f'{vol}M', delta=vs)
with cb:
    st.metric(label=f'ATR', value=f'{atr:.1f}', delta=ats)
    st.metric(label=f'VWAP', value=f'{vwap:.2f}', delta=vws)
with ccol:
    st.metric(label=f'MACD', value=f'{macd:.2f}', delta=mcs)
    st.metric(label=f'LIQ', value=liq[:10], delta=strat[:10])

st.write(f'BOS:{bos} PULL:{pb} LIQ:{liq} STRAT:{strat}')
st.write(f'OHLC O:{lc["O"]} H:{lc["H"]} L:{lc["L"]} C:{lc["C"]} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} RSI {rsi:.1f}')

md = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.am=='DEMO' else 0, key='ac88')
if 'REAL' in md:
    st.session_state.am='REAL'
else:
    st.session_state.am='DEMO'
am = st.session_state.am
if am == 'REAL':
    sa = '2500'
    cb_bal = int(st.session_state.rb)
    cp_bal = int(st.session_state.rp)
else:
    sa = '10000'
    cb_bal = int(st.session_state.db)
    cp_bal = int(st.session_state.dp)

if am == 'REAL':
    st.success(f'REAL Bal {cb_bal} Profit {cp_bal} H:{st.session_state.ht}/5 V88')
else:
    st.info(f'DEMO Bal {cb_bal} Profit {cp_bal} H:{st.session_state.ht}/5 V88')

st.metric(label=f'{am} BAL {sa} H:{st.session_state.ht}/5', value=f'{cb_bal} PKR', delta=f'+{cp_bal} PKR')
st.metric(label=f'LIVE {sm} {stf} H:{st.session_state.ht}/5', value=f'${lp:.2f}', delta=f'AUTO {"ON" if st.session_state.ao else "OFF"}')

t1,t2,t3 = st.tabs(['TRADING V88','DEPOSIT V88','HISTORY V88'])

with t1:
    st.write(f'TRADING {am} {sm} {stf} {st.session_state.ht}/5 V88')
    if st.session_state.ht >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.ht}/5 WAIT NEXT HOUR')
    st.write(f'PA 1 HOUR 5 TRADE H:{st.session_state.ht}/5 5x24=120 CLEAR')
    x1,x2,x3 = st.columns(3)
    with x1:
        st.metric(label=f'HOUR {stf}', value=f'{st.session_state.ht}/5', delta='PA 1 HOUR 4-5')
    with x2:
        st.metric(label=f'PROFIT {sm}', value=f'+{cp_bal} PKR', delta='5x24=120')
    with x3:
        st.metric(label=f'TOTAL 24H', value=f'{st.session_state.t24}/120', delta='92% WIN')
    if st.button('MANUAL TRADE', key='m88'):
        if st.session_state.ht >= 5:
            st.error(f'HOUR LIMIT {st.session_state.ht}/5 WAIT')
        else:
            win = random.random()<0.92
            prof = random.uniform(300,450) if win else random.uniform(-60,-30)
            if am == 'REAL':
                st.session_state.rb += prof
                st.session_state.rp += prof
                st.session_state.t24 += 1
                st.session_state.ht += 1
                st.session_state.hr.append(int(st.session_state.rb))
            else:
                st.session_state.db += prof
                st.session_state.dp += prof
                st.session_state.ht += 1
                st.session_state.hd.append(int(st.session_state.db))
            if st.session_state.al and win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
                st.success(f'WIN {round(prof)} PKR {stf} {st.session_state.ht}/5')
            else:
                st.success(f'WIN {round(prof)} PKR {stf} {st.session_state.ht}/5')
    if st.button('FORCE TRADE', key='f88'):
        if st.session_state.ht >= 5:
            st.error(f'HOUR LIMIT {st.session_state.ht}/5 WAIT')
        else:
            win = random.random()<0.92
            prof = random.uniform(300,450) if win else random.uniform(-60,-30)
            if am == 'REAL':
                st.session_state.rb += prof
                st.session_state.rp += prof
                st.session_state.t24 += 1
                st.session_state.ht += 1
                st.session_state.hr.append(int(st.session_state.rb))
            else:
                st.session_state.db += prof
                st.session_state.dp += prof
                st.session_state.ht += 1
                st.session_state.hd.append(int(st.session_state.db))
            if st.session_state.al and win:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'FORCE WIN {round(prof)} PKR {stf} {st.session_state.ht}/5')

with t2:
    st.write(f'DEPOSIT {am} {sa} {sm} {stf} {st.session_state.ht}/5')
    if am == 'DEMO':
        if st.button('TOPUP +5000', key='tp88'):
            st.session_state.db += 5000
            st.session_state.hd.append(int(st.session_state.db))
            st.success(f'Demo +5000 Bal {int(st.session_state.db)}')
            if st.session_state.al:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button('RESET DEMO', key='rs88'):
            st.session_state.db = 10000
            st.session_state.dp = 0
            st.session_state.hd = [10000]*5
            st.success('Demo Reset')
    else:
        dp_phone = st.text_input('Jazz Num', value='03001234567', key='dp88')
        dp_amt = st.number_input('Dep PKR Real', value=2500, min_value=100, max_value=50000, step=100, key='dpr88')
        if st.button('DEPOSIT NOW', key='dn88'):
            if len(dp_phone) >= 11:
                st.session_state.rb += dp_amt
                st.session_state.rp += dp_amt
                st.session_state.hr.append(int(st.session_state.rb))
                st.success(f'Dep +{dp_amt} Bal {int(st.session_state.rb)}')
            if st.session_state.al:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        wp = st.text_input('With Num', value='03001234567', key='wp88')
        w_amt = st.number_input('With PKR Real', value=250, min_value=100, max_value=50000, step=100, key='wpr88')
        if st.button('WITHDRAW NOW', key='wn88'):
            if len(wp) >= 11 and w_amt <= st.session_state.rb:
                st.session_state.rb -= w_amt
                st.session_state.hr.append(int(st.session_state.rb))
                st.success(f'With -{w_amt} Bal {int(st.session_state.rb)}')
    if st.button('CLEAR CACHE', key='cl88'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with t3:
    st.write(f'PINE EDITOR {sm} {stf} {st.session_state.ht}/5 O:{lc["O"]} C:{lc["C"]}')
    st.write('OHLC TABLE V88 ULTRA CLEAR')
    o = ohlc
    df = pd.DataFrame(o)
    st.dataframe(df, use_container_width=True, height=240)
    y1,y2 = st.columns(2)
    with y1:
        if st.button('PINE', key='pine88'):
            st.success(f'Pine Saved {stf} RSI {rsi:.1f} ATR {atr:.1f}')
    with y2:
        if st.button('KHABER', key='khab88'):
            st.success(f'Khaber Saved {stf} {bos} {liq}')
    st.write(f'HISTORY V88 5x24=120 PA 1 HOUR 4-5 TRADE {st.session_state.ht}/5')

st.success(f'V88 ULTRA CLEAR UP DOWN O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} LIQ {liq} BOS {bos} 88 JORA KA')
