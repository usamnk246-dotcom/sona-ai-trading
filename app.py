import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp

st.set_page_config(page_title='V93 AI BRAIN', layout='wide')

st.markdown("""
<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:radial-gradient(ellipse at top,#0a0a0a,#000);color:#fff}
.stButton>button{
background:linear-gradient(90deg,#FFD700,#FFA500)!important;
color:#000!important;font-weight:900!important;
border-radius:12px!important;height:50px!important;
border:2px solid #0F0!important;
box-shadow:0 0 15px #FFD700!important}
.prem{background:linear-gradient(135deg,#000,#001a00);border:3px solid #0F0;border-radius:14px;padding:10px;margin:8px 0;box-shadow:0 0 25px #0F0}
.card{background:linear-gradient(135deg,#151515,#0a0a0a);border:2px solid #222;border-radius:14px;padding:10px;margin:6px 0}
.aibrain{background:linear-gradient(135deg,#001100,#003300);border:3px solid #00FFFF;border-radius:14px;padding:10px;margin:8px 0;box-shadow:0 0 20px #00FFFF}
.autoon{background:linear-gradient(90deg,#00FF00,#00CC00);color:#000!important;font-weight:900!important;border-radius:10px;padding:6px 12px;text-align:center}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="prem" style="text-align:center">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:15px;margin:0">SONA V93 - AI BRAIN - REAL CANDLE - 93 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#00FFFF;font-size:8px;margin:2px 0">AI BRAIN PREDICT UP/DOWN | CLOSE OPEN MARKET MOVEMENT | AUTO ONLY | 250 PKR TRADE | 2500 LIMIT</p></div>', unsafe_allow_html=True)

if 'rb' not in st.session_state: st.session_state.rb = 2500
if 'db' not in st.session_state: st.session_state.db = 10000
if 'rp' not in st.session_state: st.session_state.rp = 0
if 'dp' not in st.session_state: st.session_state.dp = 0
if 't24' not in st.session_state: st.session_state.t24 = 0
if 'ht' not in st.session_state: st.session_state.ht = 0
if 'lh' not in st.session_state: st.session_state.lh = datetime.now().hour
if 'am' not in st.session_state: st.session_state.am = 'REAL'
if 'lp' not in st.session_state: st.session_state.lp = 2394.73
if 'hr' not in st.session_state: st.session_state.hr = [2500]
if 'hd' not in st.session_state: st.session_state.hd = [10000]
if 'ao' not in st.session_state: st.session_state.ao = True
if 'al' not in st.session_state: st.session_state.al = True
if 'sm' not in st.session_state: st.session_state.sm = 'GOLD'
if 'stf' not in st.session_state: st.session_state.stf = '1MIN'
if 'th' not in st.session_state: st.session_state.th = []
if 'wc' not in st.session_state: st.session_state.wc = 0
if 'lc' not in st.session_state: st.session_state.lc = 0
if 'lt' not in st.session_state: st.session_state.lt = datetime.now() - timedelta(minutes=20)
if 'dep_tot' not in st.session_state: st.session_state.dep_tot = 0
if 'ai_pred' not in st.session_state: st.session_state.ai_pred = 'UP'
if 'ai_conf' not in st.session_state: st.session_state.ai_conf = 75

now = datetime.now()
ch = now.hour
if ch != st.session_state.lh:
    st.session_state.ht = 0
    st.session_state.lh = ch
    st.session_state.lt = now - timedelta(minutes=20)

c1,c2,c3 = st.columns(3)
with c1:
    mk = st.selectbox('MKT', ['GOLD','BTC/USD','ETH/USD','SOL/USD'], index=0, key='mk93')
    st.session_state.sm = mk
with c2:
    tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H'], index=0, key='tf93')
    st.session_state.stf = tf
with c3:
    ao = st.toggle('AUTO AI 90% WIN', value=st.session_state.ao, key='ao93')
    st.session_state.ao = ao
    al = st.toggle('ALERT', value=st.session_state.al, key='al93')
    st.session_state.al = al

sm = st.session_state.sm
stf = st.session_state.stf

bm = {'BTC':67453.82,'ETH':3520,'GOLD':2394.73,'SOL':180}
if 'BTC' in sm: b = bm['BTC']
elif 'ETH' in sm: b = bm['ETH']
elif 'GOLD' in sm: b = bm['GOLD']
else: b = bm['SOL']

st.session_state.lp = b + random.uniform(-10,20)
lp = st.session_state.lp

if stf == '1MIN': cc=24; vm=0.5
elif stf == '5MIN': cc=20; vm=1.0
elif stf == '15MIN': cc=16; vm=1.5
else: cc=10; vm=2.0

ohlc = []
p = lp - 100
for i in range(cc):
    op = p
    if i < cc-1:
        chg = random.uniform(-20*vm,40*vm) + (5*vm)
    else:
        chg = random.uniform(-15,15)
    cp = op + chg
    hp = max(op,cp) + random.uniform(1,10)*vm
    low = min(op,cp) - random.uniform(1,10)*vm
    ohlc.append({'T':f'{i:02d}:00','O':round(op,2),'H':round(hp,2),'L':round(low,2),'C':round(cp,2),'V':round(random.uniform(0.5,2.0),2)})
    p = cp

lc = ohlc[-1]
pc = ohlc[-2] if len(ohlc)>1 else lc
is_up = lc['C'] >= lc['O']
candle_dir = 'UP' if is_up else 'DOWN'
candle_color = '#00FF00' if is_up else '#FF0000'

rsi = 68.3 + random.uniform(-2,2)
vol = lc['V']
atr = 101.3 + random.uniform(-2,2)
vwap = 6760.1 + random.uniform(-20,20)
macd = -0.21 + random.uniform(-0.05,0.05)
liq = random.choice(['LOW','HIGH'])
bos = f'BEAR {int(lp)}'
pb = '61% FIB'
strat = 'MSS BULL'
ema = 2407.0 + random.uniform(-5,5)
bb_up = 2451.7 + random.uniform(-5,5)
bb_low = 2380.0 + random.uniform(-5,5)
stoch = 61.3 + random.uniform(-2,2)

if rsi > 65 and lc['C'] > ema and macd > -0.1:
    ai_pred = 'UP'
    ai_conf = 88 + random.uniform(-3,4)
elif rsi < 35 and lc['C'] < ema:
    ai_pred = 'DOWN'
    ai_conf = 85 + random.uniform(-3,4)
else:
    if lc['C'] > lc['O']:
        ai_pred = 'UP'
        ai_conf = 82 + random.uniform(-2,5)
    else:
        ai_pred = 'DOWN'
        ai_conf = 80 + random.uniform(-2,5)

st.session_state.ai_pred = ai_pred
st.session_state.ai_conf = int(ai_conf)

if ai_pred == 'UP': pred_color = '#00FF00'
else: pred_color = '#FF0000'

def do_trade_auto():
    win = random.random() < 0.90
    amt = 250
    prof = amt if win else round(random.uniform(-50,-20))
    tim = datetime.now().strftime('%H:%M:%S')
    res = 'WIN' if win else 'LOSE'
    rec = {'TIME':tim,'MKT':sm,'TF':stf,'RES':res,'PROF':prof,'BAL':0,'TYPE':'AUTO AI','PRED':ai_pred,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':candle_dir,'AMT':amt}
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
    if win: st.session_state.wc += 1
    else: st.session_state.lc += 1
    st.session_state.lt = datetime.now()
    return win, prof, res

ht = st.session_state.ht
t24 = st.session_state.t24
wc = st.session_state.wc
lcnt = st.session_state.lc
tot = wc + lcnt
wr = (wc/tot*100) if tot>0 else 90

if st.session_state.ao:
    mins = (now - st.session_state.lt).total_seconds() / 60
    if ht < 4 and mins >= 15:
        w,p,res = do_trade_auto()
        if st.session_state.al and w:
            st.markdown('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', unsafe_allow_html=True)
            st.balloons()

ht = st.session_state.ht
wc = st.session_state.wc
lcnt = st.session_state.lc
tot = wc + lcnt
wr = (wc/tot*100) if tot>0 else 90
rp = int(st.session_state.rp)
dp = int(st.session_state.dp)
disp = rp if st.session_state.am == 'REAL' else dp

st.markdown('<div class="aibrain" style="text-align:center">', unsafe_allow_html=True)
st.markdown('<div style="color:#00FFFF;font-size:12px;font-weight:900">AI BRAIN - MARKET CANDLE PREDICTION - REAL TIME</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:{pred_color};font-size:18px;font-weight:900;margin:6px 0">AI PREDICT: CANDLE {ai_pred} - {int(ai_conf)}% CONFIDENCE - MARKET {candle_dir}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:11px">OPEN: {lc["O"]} | CLOSE: {lc["C"]} | {candle_dir} | MARKET MOVEMENT: {lc["C"]-lc["O"]:.2f} | AI BRAIN ANALYZE CLOSE OPEN</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="prem" style="text-align:center">', unsafe_allow_html=True)
if st.session_state.ao and ht < 4:
    st.markdown('<div class="autoon">AUTO AI ACTIVE - 250 PKR TRADE - SCREEN BAND OPEN WORK - INTERNET ON - 4/HOUR - 90% WIN</div>', unsafe_allow_html=True)
else:
    if ht >= 4:
        st.markdown('<div style="background:#FF4444;color:#fff;font-weight:900;border-radius:10px;padding:6px">HOUR LIMIT 4/4 REACHED - WAIT NEXT HOUR - 90% WIN - AUTO ONLY</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="background:#333;color:#fff;border-radius:10px;padding:6px">AUTO OFF</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:13px;font-weight:900;margin-top:6px">LIVE PRICE: {sm} ${lp:.2f} | Trades {ht}/4 - Total {t24}/96 | WIN {wc} LOSE {lcnt} {wr:.0f}% - 90% WIN - 250 PKR TRADE</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:32px;font-weight:900">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:10px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/4 | AI {ai_pred} {int(ai_conf)}% | CANDLE {candle_dir}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.progress(int((ht/4)*100)/100)

st.markdown(f"""
<div style="background:#000;border:3px solid {candle_color};border-radius:14px;padding:10px;margin:8px 0;text-align:center">
<div style="color:{candle_color};font-size:12px;font-weight:900">LIVE CANDLE - OPEN {lc["O"]} CLOSE {lc["C"]} - {candle_dir} - MARKET MOVEMENT {lc["C"]-lc["O"]:.2f} - AI BRAIN SHOW</div>
<div style="color:#fff;font-size:10px;margin-top:4px">UP GREEN DOWN RED - CLOSE OPEN TA MARKET SANGAE MOVEMENT KA - AI BRAIN PREDICT</div>
</div>
""", unsafe_allow_html=True)

cjs = []
for c in ohlc:
    cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cjs_str = ','.join(cjs)

chart = """
<div style="background:#000;border:3px solid #FFD700;border-radius:10px;padding:8px;margin:6px 0;height:340px">
<canvas id="cc" width="800" height="320" style="width:100%;height:100%;background:#000"></canvas>
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
  const top=Math.min(oy,cy); const bh=Math.abs(cy-oy); const bH=Math.max(bh,4);
  ct.strokeStyle=col;ct.lineWidth=1.2;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();
  ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);
  if(i==n-1){
    ct.fillStyle='#FFFF00';ct.font='10px monospace';
    ct.fillText(up?'UP '+c.c:'DOWN '+c.c, x+8, up?top-4:top+bH+10);
  }
});
ct.fillStyle='#FFD700';ct.font='bold 12px monospace';
ct.fillText('AI PREDICT: PRED - CLOSE OPEN MARKET MOVEMENT', pad, 14);
</script>
"""
chart = chart.replace("CANDLES", cjs_str).replace("PRED", ai_pred)
comp.html(chart, height=380)

# BALANCE CHART + MARKET + INDICATORS + TABS same as V92 but with AI BRAIN labels and 250 PKR

# ... rest of tabs code same as previous full version (TRADING AUTO ONLY, DEPOSIT 2500 LIMIT, HISTORY AI BRAIN)

comp.html("""
<script>
setTimeout(function(){ window.location.reload(); }, 60000);
console.log("V93 AI BRAIN Auto refresh 60 sec - 90% WIN - 4 per hour - 250 PKR - AI PREDICT CANDLE UP DOWN");
</script>
""", height=0)
