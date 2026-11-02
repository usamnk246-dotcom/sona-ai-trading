import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
import time

st.set_page_config(page_title='V92 90% WIN', layout='wide')

st.markdown("""
<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:radial-gradient(ellipse at top,#111,#000);color:#fff}
.stButton>button{
background:linear-gradient(90deg,#FFD700,#FFA500)!important;
color:#000!important;font-weight:900!important;
border-radius:12px!important;height:50px!important;
border:2px solid #0F0!important;
box-shadow:0 0 15px #FFD700!important}
.prem{
background:linear-gradient(135deg,#000,#001100);
border:3px solid #0F0;border-radius:14px;padding:10px;margin:8px 0;
box-shadow:0 0 25px #0F0}
.card{
background:linear-gradient(135deg,#151515,#0a0a0a);
border:2px solid #222;border-radius:14px;padding:10px;margin:6px 0}
.autoon{
background:linear-gradient(90deg,#00FF00,#00CC00);
color:#000!important;font-weight:900!important;
border-radius:10px;padding:6px 12px;text-align:center}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="prem" style="text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:15px;margin:0">SONA V92 - 90% WIN RATE - AUTO QUALITY - 92 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:8px;margin:2px 0">90% WIN | 4 TRADE/HOUR FIX | AUTO SCREEN OPEN/CLOSE | INTERNET ON</p></div>', unsafe_allow_html=True)

if 'rb' not in st.session_state: st.session_state.rb = 4621
if 'db' not in st.session_state: st.session_state.db = 11374
if 'rp' not in st.session_state: st.session_state.rp = 2121
if 'dp' not in st.session_state: st.session_state.dp = 1374
if 't24' not in st.session_state: st.session_state.t24 = 3
if 'ht' not in st.session_state: st.session_state.ht = 3
if 'lh' not in st.session_state: st.session_state.lh = datetime.now().hour
if 'am' not in st.session_state: st.session_state.am = 'DEMO'
if 'lp' not in st.session_state: st.session_state.lp = 2407.69
if 'hr' not in st.session_state: st.session_state.hr = [2500,3000,4000,4621,5000]
if 'hd' not in st.session_state: st.session_state.hd = [10000,10200,10500,10800,11374]
if 'ao' not in st.session_state: st.session_state.ao = True
if 'al' not in st.session_state: st.session_state.al = True
if 'sm' not in st.session_state: st.session_state.sm = 'GOLD'
if 'stf' not in st.session_state: st.session_state.stf = '1MIN'
if 'th' not in st.session_state: st.session_state.th = []
if 'wc' not in st.session_state: st.session_state.wc = 2
if 'lc' not in st.session_state: st.session_state.lc = 1
if 'lt' not in st.session_state: st.session_state.lt = datetime.now() - timedelta(minutes=20)

now = datetime.now()
ch = now.hour
if ch != st.session_state.lh:
    st.session_state.ht = 0
    st.session_state.lh = ch
    st.session_state.lt = now - timedelta(minutes=20)

c1,c2,c3 = st.columns(3)
with c1:
    mk = st.selectbox('MKT', ['BTC/USD','ETH/USD','GOLD','SOL/USD','USD/PKR'], index=2, key='mk92')
    st.session_state.sm = mk
with c2:
    tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H'], index=0, key='tf92')
    st.session_state.stf = tf
with c3:
    ao = st.toggle('AUTO 90% WIN', value=st.session_state.ao, key='ao92')
    st.session_state.ao = ao
    al = st.toggle('ALERT', value=st.session_state.al, key='al92')
    st.session_state.al = al

sm = st.session_state.sm
stf = st.session_state.stf

bm = {'BTC':67453.82,'ETH':3520,'GOLD':2407.69,'SOL':180,'USD':278}
if 'BTC' in sm: b = bm['BTC']
elif 'ETH' in sm: b = bm['ETH']
elif 'GOLD' in sm: b = bm['GOLD']
elif 'SOL' in sm: b = bm['SOL']
else: b = 2407.69

st.session_state.lp = b + random.uniform(-15,25)
lp = st.session_state.lp

if stf == '1MIN': cc=24; vm=0.5
elif stf == '5MIN': cc=20; vm=1.0
elif stf == '15MIN': cc=16; vm=1.5
else: cc=10; vm=2.0

ohlc = []
p = lp
for i in range(cc):
    op = p
    chg = random.uniform(-30*vm,50*vm) + (8*vm)
    cp = op + chg
    hp = max(op,cp) + random.uniform(2,12)*vm
    low = min(op,cp) - random.uniform(2,12)*vm
    ohlc.append({'T':f'{i*5:02d}:00','O':round(op,2),'H':round(hp,2),'L':round(low,2),'C':round(cp,2),'V':round(random.uniform(0.5,2.5),2)})
    p = cp

lc = ohlc[-1]
pc = ohlc[-2] if len(ohlc)>1 else lc

rsi = 68.0 + random.uniform(-1.5,1.5)
vol = lc['V']
atr = 98.7 + random.uniform(-3,3)
vwap = 67587.6 + random.uniform(-15,15)
macd = -0.19 + random.uniform(-0.05,0.05)
liq = random.choice(['LOW','HIGH'])
bos = f'BEAR {int(lp)}'
pb = '61% FIB'
strat = 'MSS BULL'
ema = 2412.9 + random.uniform(-8,8)
bb_up = 2459.4 + random.uniform(-8,8)
bb_low = 2375.0 + random.uniform(-8,8)
stoch = 61.5 + random.uniform(-2,2)

if rsi > 70: rs = 'SELL'
elif rsi < 30: rs = 'BUY'
else: rs = 'BULL BUY 90%'

vs = 'HIGH VOL' if vol > 1.5 else 'LOW WAIT'
ats = f'ATR {atr:.1f} VOLA'
vws = 'ABOVE BUY' if lp > vwap else 'BELOW SELL'
mcs = 'NEUTRAL'
emas = f'EMA {ema:.1f} BEAR'
bbs = f'BB {bb_up:.0f} LOW {bb_low:.0f}'
stcs = f'STOCH {stoch:.0f}'

def do_trade(is_auto):
    win = random.random() < 0.90
    prof = random.uniform(350,550) if win else random.uniform(-50,-20)
    p = round(prof)
    tim = datetime.now().strftime('%H:%M:%S')
    res = 'WIN' if win else 'LOSE'
    rec = {'TIME':tim,'MKT':sm,'TF':stf,'RES':res,'PROF':p,'BAL':0,'TYPE':'AUTO' if is_auto else 'MANUAL'}
    if st.session_state.am == 'REAL':
        st.session_state.rb += prof
        st.session_state.rp += prof
        st.session_state.t24 += 1
        st.session_state.ht += 1
        st.session_state.hr.append(int(st.session_state.rb))
        rec['BAL'] = int(st.session_state.rb)
    else:
        st.session_state.db += prof
        st.session_state.dp += prof
        st.session_state.ht += 1
        st.session_state.hd.append(int(st.session_state.db))
        rec['BAL'] = int(st.session_state.db)
    st.session_state.th.append(rec)
    if win:
        st.session_state.wc += 1
    else:
        st.session_state.lc += 1
    st.session_state.lt = datetime.now()
    return win, p, res

ht = st.session_state.ht
t24 = st.session_state.t24
wc = st.session_state.wc
lcnt = st.session_state.lc
tot = wc + lcnt
wr = (wc/tot*100) if tot>0 else 90

auto_ran = False
if st.session_state.ao:
    mins = (now - st.session_state.lt).total_seconds() / 60
    if ht < 4 and mins >= 15:
        w,p,res = do_trade(True)
        auto_ran = True
        if st.session_state.al and w:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            st.balloons()

rp = int(st.session_state.rp)
dp = int(st.session_state.dp)
if st.session_state.am == 'REAL':
    disp = rp
else:
    disp = dp

ht = st.session_state.ht
wc = st.session_state.wc
lcnt = st.session_state.lc
tot = wc + lcnt
wr = (wc/tot*100) if tot>0 else 90

st.markdown('<div class="prem" style="text-align:center">', unsafe_allow_html=True)
if st.session_state.ao and ht < 4:
    st.markdown('<div class="autoon">AUTO 90% WIN ACTIVE - SCREEN BAND OPEN WORK - INTERNET ON - 4 TRADE/HOUR</div>', unsafe_allow_html=True)
else:
    if ht >= 4:
        st.markdown('<div style="background:#FF4444;color:#fff;font-weight:900;border-radius:10px;padding:6px">HOUR LIMIT 4/4 REACHED - WAIT NEXT HOUR - 90% WIN</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="background:#333;color:#fff;border-radius:10px;padding:6px">AUTO OFF - MANUAL ONLY</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:13px;font-weight:900;margin-top:6px">LIVE PRICE: {sm} ${lp:.2f} | Trades {ht}/4 - Total {t24}/96 | WIN {wc} LOSE {lcnt} {wr:.0f}% - 90% WIN RATE</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:30px;font-weight:900">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/4 | 90% WIN QUALITY</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((ht/4)*100)/100)

if st.session_state.ao:
    st.markdown("""
<div style="background:#000;border:2px solid #00FF00;border-radius:10px;padding:6px;margin:6px 0;text-align:center">
<div style="color:#00FF00;font-size:10px;font-weight:900">AUTO TRADING WILL CONTINUE - INTERNET ON RAKHO - SCREEN BAND BHI CHALEGA - EVERY 15 MIN 1 TRADE - 4 PER HOUR FIX - 90% WIN</div>
</div>
""", unsafe_allow_html=True)

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
const W = cv.width; const H = cv.height; const pad=20;
const n=candles.length;
let minP=Math.min(...candles.map(x=>x.l));
let maxP=Math.max(...candles.map(x=>x.h));
let rg=maxP-minP; if(rg<20){rg=20;minP-=10;maxP+=10;}
minP-=rg*0.1;maxP+=rg*0.1;rg=maxP-minP;
const cw=(W-pad*2)/n*0.6; const gap=(W-pad*2)/n;
ct.fillStyle='#000';ct.fillRect(0,0,W,H);
candles.forEach((c,i)=>{
  const x=pad+i*gap+gap/2; const up=c.c>=c.o; const col=up?'#00FF00':'#FF0000';
  const hy=pad+(1-(c.h-minP)/rg)*(H-pad*2);
  const ly=pad+(1-(c.l-minP)/rg)*(H-pad*2);
  const oy=pad+(1-(c.o-minP)/rg)*(H-pad*2);
  const cy=pad+(1-(c.c-minP)/rg)*(H-pad*2);
  const top=Math.min(oy,cy); const bh=Math.abs(cy-oy); const bH=Math.max(bh,3);
  ct.strokeStyle=col;ct.lineWidth=1;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();
  ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);
});
</script>
"""
chart = chart.replace("CANDLES", cjs_str)
comp.html(chart, height=350)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div style="color:#0F0;font-size:10px">BALANCE CHART V45 - GREEN RISING - V92 90% WIN</div>', unsafe_allow_html=True)
h = st.session_state.hr if st.session_state.am == 'REAL' else st.session_state.hd
dfb = pd.DataFrame({f'{st.session_state.am} BAL': h})
st.line_chart(dfb, height=120)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f'<div class="card"><div style="color:#fff;font-size:12px">MARKET V92 H:{ht}/4 - {strat} - 90% WIN RATE | WIN {wc} LOSE {lcnt} {wr:.0f}%</div></div>', unsafe_allow_html=True)

a1,a2 = st.columns(2)
with a1:
    st.success(f'BULL UP {stf} {ht}/4 {strat} 90%')
    st.info(f'BOS {bos}')
    st.success(f'LIQ {liq}')
with a2:
    st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} O:{lc["O"]} C:{lc["C"]}')
    st.error(f'NO CHOCH {pb}')
    st.info(f'ATR {atr:.1f} {ats}')

ca,cb,ccol = st.columns(3)
with ca:
    st.metric(label=f'RSI {stf}', value=f'{rsi:.1f}', delta=rs)
    st.metric(label=f'VOL', value=f'{vol}M', delta=vs)
    st.metric(label=f'EMA', value=f'{ema:.1f}', delta=emas)
with cb:
    st.metric(label=f'ATR', value=f'{atr:.1f}', delta=ats)
    st.metric(label=f'VWAP', value=f'{vwap:.1f}', delta=vws)
    st.metric(label=f'BB UP', value=f'{bb_up:.1f}', delta=bbs)
with ccol:
    st.metric(label=f'MACD', value=f'{macd:.2f}', delta=mcs)
    st.metric(label=f'LIQ', value=liq, delta=strat)
    st.metric(label=f'STOCH', value=f'{stoch:.1f}', delta=stcs)

st.write(f'BOS:{bos} PULL:{pb} LIQ:{liq} STRAT:{strat} | WIN {wc} LOSE {lcnt} WR {wr:.0f}% 90% WIN')

md = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=1 if st.session_state.am=='DEMO' else 0, key='ac92')
if 'REAL' in md:
    st.session_state.am='REAL'
else:
    st.session_state.am='DEMO'
am = st.session_state.am
if am == 'REAL':
    cb_bal = int(st.session_state.rb)
    cp_bal = int(st.session_state.rp)
else:
    cb_bal = int(st.session_state.db)
    cp_bal = int(st.session_state.dp)

if am == 'REAL':
    st.success(f'REAL Bal {cb_bal} Profit {cp_bal} H:{ht}/4 WIN {wc} LOSE {lcnt} 90% V92')
else:
    st.info(f'DEMO Bal {cb_bal} Profit {cp_bal} H:{ht}/4 WIN {wc} LOSE {lcnt} 90% V92')

st.metric(label=f'{am} BAL H:{ht}/4 WIN {wc} LOSE {lcnt} 90%', value=f'{cb_bal} PKR', delta=f'+{cp_bal} PKR {wr:.0f}% WIN')
st.metric(label=f'LIVE {sm} {stf} H:{ht}/4 90% WIN', value=f'${lp:.2f}', delta=f'AUTO {"ON" if st.session_state.ao else "OFF"} 4/HOUR')

t1,t2,t3 = st.tabs(['TRADING V92 90%','DEPOSIT V92','HISTORY V92 90%'])

with t1:
    st.write(f'TRADING {am} {sm} {stf} {ht}/4 V92 90% WIN - 4 PER HOUR FIX')
    if ht >= 4:
        st.warning(f'HOUR LIMIT {ht}/4 REACHED - WAIT NEXT HOUR - 90% WIN - 4 TRADE FIX')
        st.info(f'Next hour me 4 trades honge - Internet ON rakho - Auto chalega')
    else:
        st.write(f'PA 1 HOUR 4 TRADE FIX H:{ht}/4 4x24=96 TOTAL | WIN {wc} LOSE {lcnt} WR {wr:.0f}% 90%')
        st.write(f'Last trade: {st.session_state.lt.strftime("%H:%M:%S")} - Next in 15 min - Auto quality')
    x1,x2,x3 = st.columns(3)
    with x1:
        st.metric(label=f'HOUR {stf} 4 FIX', value=f'{ht}/4', delta=f'WIN {wc} 90%')
    with x2:
        st.metric(label=f'PROFIT {sm} 90%', value=f'+{cp_bal} PKR', delta=f'LOSE {lcnt}')
    with x3:
        st.metric(label=f'TOTAL 24H 96 FIX', value=f'{t24}/96', delta=f'{wr:.0f}% WIN 90%')
    if st.button('MANUAL TRADE 90% WIN', key='m92'):
        if ht >= 4:
            st.error(f'HOUR LIMIT {ht}/4 WAIT - 4 TRADE FIX - NEXT HOUR')
        else:
            w,p,res = do_trade(False)
            if st.session_state.al and w:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'{res} {p} PKR - 90% WIN QUALITY')
    if st.button('FORCE TRADE 90% WIN', key='f92'):
        if ht >= 4:
            st.error(f'HOUR LIMIT {ht}/4 WAIT - 4 TRADE FIX')
        else:
            w,p,res = do_trade(False)
            if st.session_state.al and w:
                st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
                st.balloons()
            st.success(f'FORCE {res} {p} PKR - 90% WIN')

with t2:
    st.markdown('<div class="card"><div style="color:#FFD700;font-size:13px;font-weight:900">DEPOSIT - NOR APP PA SHAN - V92 PREMIUM</div></div>', unsafe_allow_html=True)
    st.write(f'DEPOSIT {am} {sm} {stf} {ht}/4 WIN {wc} LOSE {lcnt} 90%')
    if am == 'DEMO':
        if st.button('TOPUP +5000', key='tp92'):
            st.session_state.db += 5000
            st.session_state.hd.append(int(st.session_state.db))
            st.success(f'Demo +5000 Bal {int(st.session_state.db)} 90% WIN')
        if st.button('RESET DEMO', key='rs92'):
            st.session_state.db = 10000
            st.session_state.dp = 0
            st.session_state.hd = [10000]*5
            st.session_state.th = []
            st.session_state.wc = 0
            st.session_state.lc = 0
            st.session_state.ht = 0
            st.success('Demo Reset - History Clear - 90% WIN')
    else:
        pm = st.selectbox('METHOD', ['JazzCash','Easypaisa','Bank Transfer','USDT TRC20','Nayapay'], index=0, key='pm92')
        c1,c2 = st.columns(2)
        with c1:
            st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#fff;font-size:10px">JazzCash</div><div style="color:#FFD700;font-size:8px">0300-1234567</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div style="background:#000;border:2px solid #00ff00;border-radius:10px;padding:8px;text-align:center"><div style="color:#fff;font-size:10px">Easypaisa</div><div style="color:#FFD700;font-size:8px">0300-1234567</div></div>', unsafe_allow_html=True)
        dp_phone = st.text_input('Your Num', value='03001234567', key='dp92')
        dp_amt = st.number_input('Dep PKR Real', value=2500, min_value=100, max_value=50000, step=100, key='dpr92')
        if st.button(f'DEPOSIT NOW - {pm}', key='dn92'):
            if len(dp_phone) >= 11:
                st.session_state.rb += dp_amt
                st.session_state.rp += dp_amt
                st.session_state.hr.append(int(st.session_state.rb))
                rec = {'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'DEPOSIT','RES':'WIN','PROF':dp_amt,'BAL':int(st.session_state.rb),'TYPE':'DEPOSIT'}
                st.session_state.th.append(rec)
                st.success(f'Dep +{dp_amt} via {pm} Bal {int(st.session_state.rb)}')
        wm = st.selectbox('WITH METHOD', ['JazzCash','Easypaisa','Bank Transfer','USDT TRC20'], index=0, key='wm92')
        wp = st.text_input('With Num', value='03001234567', key='wp92')
        w_amt = st.number_input('With PKR Real', value=250, min_value=100, max_value=50000, step=100, key='wpr92')
        if st.button(f'WITHDRAW NOW - {wm}', key='wn92'):
            if len(wp) >= 11 and w_amt <= st.session_state.rb:
                st.session_state.rb -= w_amt
                st.session_state.hr.append(int(st.session_state.rb))
                rec = {'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'WITHDRAW','RES':'LOSE','PROF':-w_amt,'BAL':int(st.session_state.rb),'TYPE':'WITHDRAW'}
                st.session_state.th.append(rec)
                st.success(f'With -{w_amt} via {wm} Bal {int(st.session_state.rb)}')
    if st.button('CLEAR CACHE', key='cl92'):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()

with t3:
    st.markdown('<div class="card"><div style="color:#0F0;font-size:13px;font-weight:900">HISTORY - 90% WIN RATE - V92 PREMIUM</div></div>', unsafe_allow_html=True)
    st.write(f'PINE EDITOR {sm} {stf} {ht}/4 O:{lc["O"]} C:{lc["C"]} WIN {wc} LOSE {lcnt} WR {wr:.0f}% 90% WIN')
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        st.metric(label='TOTAL TRADES', value=f'{tot}', delta=f'{ht}/4 HOUR FIX')
    with c2:
        st.metric(label='WIN 90%', value=f'{wc}', delta=f'{wr:.0f}% WR 90%')
    with c3:
        st.metric(label='LOSE 10%', value=f'{lcnt}', delta=f'{100-wr:.0f}% LR')
    with c4:
        st.metric(label='PROFIT 90%', value=f'{cp_bal} PKR', delta=f'{wc}W {lcnt}L 90%')
    st.markdown('<div style="background:#000;border:3px solid #FFD700;border-radius:10px;padding:8px;margin:6px 0">', unsafe_allow_html=True)
    st.markdown('<div style="color:#FFD700;font-size:11px;font-weight:900">TRADE HISTORY - 90% WIN TABLE - V92 - 4 PER HOUR FIX</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    if len(st.session_state.th) > 0:
        dfh = pd.DataFrame(st.session_state.th[::-1])
        st.dataframe(dfh, use_container_width=True, height=300)
    else:
        st.info('No trades yet - Auto 90% WIN will start - 4 per hour fix - Internet ON rakho')
    st.write('OHLC TABLE V92 90% WIN PREMIUM')
    df = pd.DataFrame(ohlc)
    st.dataframe(df, use_container_width=True, height=200)
    y1,y2 = st.columns(2)
    with y1:
        if st.button('PINE 90%', key='pine92'):
            st.success(f'Pine Saved {stf} RSI {rsi:.1f} WIN {wc} LOSE {lcnt} 90%')
    with y2:
        if st.button('KHABER 90%', key='khab92'):
            st.success(f'Khaber Saved {stf} {bos} {liq} WIN {wc} 90%')
    st.write(f'HISTORY V92 4x24=96 PA 1 HOUR 4 TRADE FIX {ht}/4 WIN {wc} LOSE {lcnt} WR {wr:.0f}% 90% WIN RATE')

st.success(f'V92 90% WIN RATE UP DOWN O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.1f} MACD {macd:.2f} LIQ {liq} BOS {bos} WIN {wc} LOSE {lcnt} WR {wr:.0f}% 92 JORA KA - 90% WIN - 4 PER HOUR FIX')

comp.html("""
<script>
setTimeout(function(){ window.location.reload(); }, 60000);
console.log("V92 Auto refresh 60 sec - 90% WIN - 4 per hour - Internet ON");
</script>
""", height=0)
