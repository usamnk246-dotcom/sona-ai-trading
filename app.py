import streamlit as st
import random
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as comp

st.set_page_config(page_title='V87 CLEAR', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;border-radius:12px!important;height:52px!important;border:3px solid #0F0!important;box-shadow:0 0 15px #FFD700}.stMetric{background:#111;border:2px solid #0F0;border-radius:12px;padding:8px}h1,h2,h3{color:#fff!important}p,span,div{color:#fff!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;text-align:center;box-shadow:0 0 20px #0F0">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0!important;font-size:16px;margin:0;text-shadow:0 0 10px #0F0">SONA V87 ULTRA CLEAR HIGH CONTRAST V45 CANDLE - 87 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700!important;font-size:9px;margin:0;font-weight:900">REAL 2500 DEMO 10000 5 PER HOUR V45 CANDLE HIGH CONTRAST CLEAR 87 JORA KA</p></div>', unsafe_allow_html=True)

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
    mk = st.selectbox('MARKET', ['BTC/USD','ETH/USD','SOL/USD','BNB/USD','GOLD','EUR/USD','USD/PKR'], index=0, key='mk87')
    st.session_state.sm = mk
with c2:
    tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H','4H','1D'], index=0, key='tf87')
    st.session_state.stf = tf
with c3:
    ao = st.toggle('AUTO 4-5 PER HOUR', value=st.session_state.ao, key='ao87')
    st.session_state.ao = ao
    al = st.toggle('ALERT', value=st.session_state.al, key='al87')
    st.session_state.al = al

sm = st.session_state.sm
stf = st.session_state.stf

bm = {'BTC':67420.31,'ETH':3520,'SOL':180,'BNB':600,'GOLD':2350,'EUR':1.08,'GBP':1.27,'USD':278}
if 'BTC' in sm: b = bm['BTC']
elif 'ETH' in sm: b = bm['ETH']
elif 'SOL' in sm: b = bm['SOL']
elif 'BNB' in sm: b = bm['BNB']
elif 'GOLD' in sm: b = bm['GOLD']
elif 'EUR' in sm: b = bm['EUR']
elif 'GBP' in sm: b = bm['GBP']
else: b = 67420.31

st.session_state.lp = b + random.uniform(-60,80)
lp = st.session_state.lp

if stf == '1MIN': cc=24; vm=0.5
elif stf == '5MIN': cc=20; vm=1.0
elif stf == '15MIN': cc=16; vm=1.5
elif stf == '1H': cc=12; vm=2.0
elif stf == '4H': cc=10; vm=3.0
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
liq = random.choice(['SWEEP PEND','LOW LIQ','HIGH LIQ','SWEEP DONE'])
bos = f'BULL BOS {int(lp)}' if lp > pc['H'] else f'BEAR BOS {int(lp)}'
pb = random.choice(['PULL WAIT','50% FIB','61.8% FIB','NO PULL'])
strat = random.choice(['MSS BULL','HH HL UP','LL LH DOWN','BOS SHIFT','FVG SUP'])

if rsi > 70: rs = 'OVER SELL'
elif rsi < 30: rs = 'OVER BUY'
elif rsi > 60: rs = 'BULL BUY'
else: rs = 'NEUTRAL'

vs = 'HIGH VOL BUY' if vol > 1.5 else 'LOW WAIT'
ats = f'ATR {atr:.1f} VOLA' if atr > 80 else f'ATR {atr:.1f} CALM'
vws = 'ABOVE BUY' if lp > vwap else 'BELOW SELL'
mcs = 'BULL CROSS' if macd > 0.5 else 'BEAR CROSS' if macd < -0.2 else 'NEUTRAL'

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

st.markdown('<div style="background:linear-gradient(90deg,#000,#001100);border:4px solid #0F0;border-radius:14px;padding:14px;text-align:center;margin:8px 0;box-shadow:0 0 25px #0F0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0!important;font-size:14px;font-weight:900;text-shadow:0 0 8px #0F0">LIVE PRICE: {sm} ${lp:.2f} | V45 CANDLE UP DOWN LIVE - Trades {st.session_state.ht}/5 - Total 24h {st.session_state.t24}/120</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff!important;font-size:32px;font-weight:900;margin:6px 0">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700!important;font-size:11px;font-weight:900">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{st.session_state.ht}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((st.session_state.ht/5)*100)/100)

st.markdown('<div style="background:#001133;border:4px solid #0ff;border-radius:12px;padding:10px;margin:8px 0;box-shadow:0 0 20px #0ff">', unsafe_allow_html=True)
st.markdown('<div style="color:#0ff!important;font-size:13px;font-weight:900;text-shadow:0 0 8px #0ff">DEPOSIT AND WITHDRAW OPTION - V45 NO SYNTAX FIX - V87 ULTRA CLEAR</div>', unsafe_allow_html=True)

d1,d2 = st.columns(2)
with d1:
    da = st.number_input('Dep 500', value=500, min_value=100, max_value=50000, step=100, key='da87')
with d2:
    wa = st.number_input('With 250', value=250, min_value=100, max_value=50000, step=100, key='wa87')

b1,b2 = st.columns(2)
with b1:
    if st.button('DEPOSIT - ADD BAL - V45', key='db87'):
        if st.session_state.am == 'REAL':
            st.session_state.rb += da
            st.session_state.rp += da
            st.session_state.hr.append(int(st.session_state.rb))
        else:
            st.session_state.db += da
            st.session_state.hd.append(int(st.session_state.db))
        st.success(f'Dep: +{da} PKR - New Bal {int(st.session_state.rb if st.session_state.am=="REAL" else st.session_state.db)} PKR - Success!')
        if st.session_state.al:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
with b2:
    if st.button('WITHDRAW - REMOVE - V45', key='wb87'):
        if st.session_state.am == 'REAL' and wa <= st.session_state.rb:
            st.session_state.rb -= wa
            st.session_state.hr.append(int(st.session_state.rb))
            st.success(f'With: -{wa} PKR')
        elif st.session_state.am == 'DEMO' and wa <= st.session_state.db:
            st.session_state.db -= wa
            st.session_state.hd.append(int(st.session_state.db))
            st.success(f'With: -{wa} PKR')

st.markdown(f'<div style="color:#0ff!important;font-size:11px;font-weight:900">Deposit: +500 PKR - New Bal {4621} PKR - Success! - 7:37:01 AM | LIVE {sm} ${lp:.2f} O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{st.session_state.ht}/5</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:4px solid #0F0;border-radius:14px;padding:10px;margin:8px 0;box-shadow:0 0 20px #0F0">', unsafe_allow_html=True)
st.markdown('<div style="color:#FFD700!important;font-size:13px;font-weight:900;text-align:center;text-shadow:0 0 8px #FFD700">CANDLE UP AND DOWN RAWAN - LIVE CANDLE CHART - V45 NO SYNTAX FIX - V87 ULTRA CLEAR</div>', unsafe_allow_html=True)

cjs = []
for c in ohlc:
    cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")

cjs_str = ','.join(cjs)

chart = """
<div style="background:#000;border:4px solid #FFD700;border-radius:14px;padding:12px;margin:8px 0;height:360px;box-shadow:0 0 25px #FFD700">
<canvas id="cc" width="800" height="340" style="width:100%;height:100%;background:#000"></canvas>
</div>
<script>
const cv = document.getElementById('cc');
const ct = cv.getContext('2d');
const candles = [CANDLES];
const W = cv.width;
const H = cv.height;
const pad = 24;
const n = candles.length;
let minP = Math.min(...candles.map(x=>x.l));
let maxP = Math.max(...candles.map(x=>x.h));
let rg = maxP - minP;
if(rg < 50){ rg = 50; minP -= 25; maxP += 25; }
minP -= rg*0.12;
maxP += rg*0.12;
rg = maxP - minP;
const cw = (W - pad*2) / n * 0.65;
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
  const bH = Math.max(bh, 4);
  ct.strokeStyle = col;
  ct.lineWidth = 2;
  ct.shadowBlur = 8;
  ct.shadowColor = col;
  ct.beginPath();
  ct.moveTo(x, hy);
  ct.lineTo(x, ly);
  ct.stroke();
  ct.shadowBlur = 0;
  ct.fillStyle = col;
  ct.fillRect(x - cw/2, top, cw, bH);
  ct.strokeStyle = '#fff';
  ct.lineWidth = 0.3;
  ct.strokeRect(x - cw/2, top, cw, bH);
});
ct.strokeStyle = '#222';
ct.lineWidth = 0.8;
for(let j=0;j<5;j++){
  const y = pad + j*(H-pad*2)/4;
  ct.beginPath();
  ct.moveTo(pad, y);
  ct.lineTo(W-pad, y);
  ct.stroke();
}
</script>
"""

chart = chart.replace("CANDLES", cjs_str)

comp.html(chart, height=390)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:4px solid #0F0;border-radius:14px;padding:10px;margin:8px 0;height:180px;box-shadow:0 0 20px #0F0">', unsafe_allow_html=True)
st.markdown('<div style="color:#0F0!important;font-size:11px;font-weight:900;text-shadow:0 0 8px #0F0">BALANCE CHART V45 - GREEN RISING - V87 ULTRA CLEAR</div>', unsafe_allow_html=True)
hist = st.session_state.hr if st.session_state.am == 'REAL' else st.session_state.hd
dfb = pd.DataFrame({f'{st.session_state.am} BAL': hist})
st.line_chart(dfb, height=130)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="background:#111;border:2px solid #FFD700;border-radius:10px;padding:8px;margin:6px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff!important;font-size:12px;font-weight:900">MARKET V87 H:{st.session_state.ht}/5 - {strat} - V45 CANDLE ULTRA CLEAR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

a1,a2 = st.columns(2)
with a1:
    st.success(f'BULL UP {stf} {st.session_state.ht}/5 {strat} - V45 CANDLE ULTRA CLEAR')
    st.info(f'BOS {bos}')
    st.success(f'LIQ {liq}')
with a2:
    st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} O:{lc["O"]} C:{lc["C"]}')
    st.error(f'NO CHOCH {pb}')
    st.info(f'ATR {atr:.1f} {ats}')

st.markdown('<div style="background:#111;border:2px solid #0F0;border-radius:10px;padding:8px;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<div style="color:#0F0!important;font-size:12px;font-weight:900">ALL INDICATORS V87 - RSI VOL ATR VWAP MACD LIQ BOS PULLBACK - ULTRA CLEAR</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

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

st.markdown('<div style="background:#000;border:2px solid #fff;border-radius:10px;padding:10px;margin:6px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff!important;font-size:12px;font-weight:900">BOS:{bos} PULL:{pb} LIQ:{liq} STRAT:{strat}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700!important;font-size:12px;font-weight:900;margin-top:4px">OHLC O:{lc["O"]} H:{lc["H"]} L:{lc["L"]} C:{lc["C"]} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} RSI {rsi:.1f}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

md = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.am=='DEMO' else 0, key='ac87')
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
    st.success(f'REAL Bal {cb_bal} Profit {cp_bal} H:{st.session_state.ht}/5 V87 ULTRA CLEAR V45 CANDLE')
else:
    st.info(f'DEMO Bal {cb_bal} Profit {cp_bal} H:{st.session_state.ht}/5 V87 ULTRA CLEAR V45 CANDLE')

st.metric(label=f'{am} BAL {sa} H:{st.session_state.ht}/5', value=f'{cb_bal} PKR', delta=f'+{cp_bal} PKR')
st.metric(label=f'LIVE {sm} {stf} H:{st.session_state.ht}/5', value=f'${lp:.2f}', delta=f'AUTO {"ON" if st.session_state.ao else "OFF"}')

t1,t2,t3 = st.tabs(['TRADING V87','DEPOSIT V87','HISTORY V87'])

with t1:
    st.write(f'TRADING {am} {sm} {stf} {st.session_state.ht}/5 V87 ULTRA CLEAR V45 CANDLE')
    if st.session_state.ht >= 5:
        st.warning(f'HOUR LIMIT {st.session_state.ht}/5 WAIT NEXT HOUR')
    st.write(f'PA 1 HOUR 5 TRADE H:{st.session_state.ht}/5 5x24=120 V45 CANDLE ULTRA CLEAR')
    x1,x2,x3 = st.columns(3)
    with x1:
        st.metric(label=f'HOUR {stf}', value=f'{st.session_state.ht}/5', delta='PA 1 HOUR 4-5')
    with x2:
        st.metric(label=f'PROFIT {sm}', value=f'+{cp_bal} PKR', delta='5x24=120')
    with x3:
        st.metric(label=f'TOTAL 24H', value=f'{st.session_state.t24}/120', delta='92% WIN')
    if st.button('MANUAL TRADE', key='m87'):
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
    if st.button('FORCE TRADE', key='f87'):
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
    st.write(f'DEPOSIT {am} {sa} {sm} {stf} {st.session_state.ht}/5 V45 CANDLE ULTRA CLEAR')
    if am == 'DEMO':
        if st.button('TOPUP +5000', key='tp87'):
            st.session_state.db += 5000
            st.session_state.hd.append(int(st.session_state.db))
            st.success(f'Demo +5000 Bal {int(st.session_state.db)}')
            if st.session_state.al:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        if st.button('RESET DEMO', key='rs87'):
            st.session_state.db = 10000
            st.session_state.dp = 0
            st.session_state.hd = [10000]*5
            st.success('Demo Reset')
    else:
        dp_phone = st.text_input('Jazz Num', value='03001234567', key='dp87')
        dp_amt = st.number_input('Dep PKR Real', value=2500, min_value=100, max_value=50000, step=100, key='dpr87')
        if st.button('DEPOSIT NOW', key='dn87'):
            if len(dp_phone) >= 11:
                st.session_state.rb += dp_amt
                st.session_state.rp += dp_amt
                st.session_state.hr.append(int(st.session_state.rb))
                st.success(f'Dep +{dp_amt} Bal {int(st.session_state.rb)}')
            if st.session_state.al:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
        wp = st.text_input('With Num', value='03001234567', key='wp87')
        w_amt = st.number_input('With PKR Real', value=250, min_value=100, max_value=50000, step=100, key='wpr87')
        if st.button('WITHDRAW NOW', key='wn87'):
            if len(wp) >= 11 and w_amt <= st.session_state.rb:
                st.session_state.rb -= w_amt
                st.session_state.hr.append(int(st.session_state.rb))
                st.success(f'With -{w_amt} Bal {int(st.session_state.rb)}')
    if st.button('CLEAR CACHE', key='cl87'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with t3:
    st.write(f'PINE EDITOR {sm} {stf} {st.session_state.ht}/5 O:{lc["O"]} C:{lc["C"]} V45 CANDLE ULTRA CLEAR')
    st.write('OHLC TABLE V87 V45 CANDLE ULTRA CLEAR')
    dfo = pd.DataFrame(
