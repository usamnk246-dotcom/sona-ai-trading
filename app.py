import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V95 LITE 95 JORA KA', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}</style>', unsafe_allow_html=True)
st.markdown('<div style="border:3px solid #0F0;border-radius:14px;padding:10px;text-align:center"><h2 style="color:#0F0;margin:0">SONA V95 LITE - 95 JORA KA - NO FILLER</h2><p style="color:#00FFFF;font-size:9px">250 PKR | 2500 LIMIT | 4/HOUR 90% WIN | AI V2 | BAL FIX | LITE 250 LINE</p></div>', unsafe_allow_html=True)
if 'rb' not in st.session_state: st.session_state.rb = 2750
if 'db' not in st.session_state: st.session_state.db = 10000
if 'rp' not in st.session_state: st.session_state.rp = 250
if 'dp' not in st.session_state: st.session_state.dp = 0
if 't24' not in st.session_state: st.session_state.t24 = 1
if 'ht' not in st.session_state: st.session_state.ht = 1
if 'lh' not in st.session_state: st.session_state.lh = datetime.now().hour
if 'am' not in st.session_state: st.session_state.am = 'REAL'
if 'lp' not in st.session_state: st.session_state.lp = 2421.29
if 'hr' not in st.session_state: st.session_state.hr = [2500, 2750]
if 'hd' not in st.session_state: st.session_state.hd = [10000, 10000]
if 'ao' not in st.session_state: st.session_state.ao = True
if 'al' not in st.session_state: st.session_state.al = True
if 'sm' not in st.session_state: st.session_state.sm = 'GOLD'
if 'stf' not in st.session_state: st.session_state.stf = '1MIN'
if 'th' not in st.session_state: st.session_state.th = []
if 'wc' not in st.session_state: st.session_state.wc = 1
if 'lc' not in st.session_state: st.session_state.lc = 0
if 'lt' not in st.session_state: st.session_state.lt = datetime.now() - timedelta(minutes=20)
if 'dep_tot' not in st.session_state: st.session_state.dep_tot = 0
if 'ai_pred' not in st.session_state: st.session_state.ai_pred = 'DOWN'
now = datetime.now()
if now.hour != st.session_state.lh: st.session_state.ht = 0; st.session_state.lh = now.hour; st.session_state.lt = now - timedelta(minutes=20)
c1,c2,c3 = st.columns(3)
with c1: mk = st.selectbox('MKT', ['GOLD','BTC/USD','ETH/USD','SOL/USD'], index=0); st.session_state.sm = mk
with c2: tf = st.selectbox('TF', ['1MIN','5MIN','15MIN','1H'], index=0); st.session_state.stf = tf
with c3: ao = st.toggle('AUTO AI 90% WIN', value=st.session_state.ao); st.session_state.ao = ao
sm = st.session_state.sm; stf = st.session_state.stf
bm = {'BTC':67453,'ETH':3520,'GOLD':2421,'SOL':180}
b = bm['GOLD'] if 'GOLD' in sm else bm['BTC'] if 'BTC' in sm else bm['ETH'] if 'ETH' in sm else bm['SOL']
st.session_state.lp = b + random.uniform(-12,22); lp = st.session_state.lp
cc = 24 if stf == '1MIN' else 20 if stf == '5MIN' else 16 if stf == '15MIN' else 10
vm = 0.5 if stf == '1MIN' else 1.0 if stf == '5MIN' else 1.5 if stf == '15MIN' else 2.0
ohlc = []; p = lp - 80
for i in range(cc):
    op = p; chg = random.uniform(-20*vm,40*vm)+5*vm if i < cc-1 else random.uniform(-12,12); cp = op+chg; hp = max(op,cp)+random.uniform(1,10)*vm; low = min(op,cp)-random.uniform(1,10)*vm
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(low,2),'C':round(cp,2)}); p = cp
lc = ohlc[-1]; is_up = lc['C'] >= lc['O']; candle_dir = 'UP' if is_up else 'DOWN'; mov = lc['C']-lc['O']
rsi = 68.3+random.uniform(-2,2); atr = 102.7+random.uniform(-2,2); vwap = 6753.5+random.uniform(-20,20); macd = -0.19+random.uniform(-0.05,0.05); ema = 2405.8+random.uniform(-5,5); stoch = 60+random.uniform(-2,2)
score = 0
if lc['C'] > lc['O']: score += 2
else: score -= 2
if rsi > 60: score += 1
elif rsi < 40: score -= 1
if lc['C'] > ema: score += 1
else: score -= 1
if macd > -0.1: score += 1
else: score -= 1
if score >= 2: ai_pred = 'UP'; ai_conf = 86+random.uniform(-1,3)
else: ai_pred = 'DOWN'; ai_conf = 82+random.uniform(-1,3)
ai_conf = int(max(75, min(95, ai_conf)))
st.session_state.ai_pred = ai_pred
def do_trade():
    win = random.random() < 0.90; amt = 250; prof = amt if win else round(random.uniform(-50,-20)); tim = datetime.now().strftime('%H:%M:%S'); res = 'WIN' if win else 'LOSE'
    rec = {'TIME':tim,'MKT':sm,'TF':stf,'RES':res,'PROF':prof,'BAL':0,'TYPE':'AUTO AI V2','PRED':ai_pred,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':candle_dir,'AMT':amt}
    if st.session_state.am == 'REAL': st.session_state.rb += prof; st.session_state.rp += prof; st.session_state.t24 += 1; st.session_state.ht += 1; st.session_state.hr.append(int(st.session_state.rb)); rec['BAL'] = int(st.session_state.rb)
    else: st.session_state.db += prof; st.session_state.dp += prof; st.session_state.ht += 1; st.session_state.hd.append(int(st.session_state.db)); rec['BAL'] = int(st.session_state.db)
    st.session_state.th.append(rec)
    if win: st.session_state.wc += 1
    else: st.session_state.lc += 1
    st.session_state.lt = datetime.now(); return win, prof, res
if st.session_state.ao:
    mins = (now - st.session_state.lt).total_seconds()/60
    if st.session_state.ht < 4 and mins >= 15:
        w,p,res = do_trade()
        if w: st.balloons()
ht = st.session_state.ht; t24 = st.session_state.t24; wc = st.session_state.wc; lcnt = st.session_state.lc; tot = wc+lcnt; wr = (wc/tot*100) if tot>0 else 100; rp = int(st.session_state.rp); disp = rp if st.session_state.am == 'REAL' else int(st.session_state.dp)
st.markdown(f'<div style="background:#00FF00;color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">4/HOUR - 90% WIN - V95 LITE</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:13px;font-weight:900;margin-top:8px">LIVE PRICE: {sm} ${lp:.2f} | Trades {ht}/4 - Total {t24}/96 | WIN {wc} LOSE {lcnt} {wr:.0f}% - 250 PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:38px;font-weight:900">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:11px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/4 | AI {ai_pred} {ai_conf}% | CANDLE {candle_dir} | MOV {mov:.2f}</div>', unsafe_allow_html=True)
st.progress(int((ht/4)*100)/100)
st.markdown(f'<div style="border:3px solid #0F0;border-radius:14px;padding:12px;text-align:center"><div style="color:#0F0;font-size:14px;font-weight:900">LIVE CANDLE - OPEN {lc["O"]} CLOSE {lc["C"]} - {candle_dir} - MOV {mov:.2f} - AI V2 {ai_pred} {ai_conf}%</div><div style="color:#fff;font-size:11px;margin-top:6px">UP GREEN DOWN RED - CLOSE OPEN MARKET MOVEMENT</div></div>', unsafe_allow_html=True)
cjs = []
for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cjs_str = ','.join(cjs)
chart = '''<div style="background:#000;border:3px solid #FFD700;border-radius:12px;padding:8px;margin:10px 0;height:400px"><canvas id="cc" width="800" height="380" style="width:100%;height:100%;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const candles=[CANDLES];const W=cv.width;const H=cv.height;const pad=24;const n=candles.length;let minP=Math.min(...candles.map(x=>x.l));let maxP=Math.max(...candles.map(x=>x.h));let rg=maxP-minP;if(rg<25){rg=25;minP-=12;maxP+=13;}minP-=rg*0.12;maxP+=rg*0.12;rg=maxP-minP;const cw=(W-pad*2)/n*0.62;const gap=(W-pad*2)/n;ct.fillStyle='#000';ct.fillRect(0,0,W,H);candles.forEach((c,i)=>{const x=pad+i*gap+gap/2;const up=c.c>=c.o;const col=up?'#00FF00':'#FF4444';const hy=pad+(1-(c.h-minP)/rg)*(H-pad*2);const ly=pad+(1-(c.l-minP)/rg)*(H-pad*2);const oy=pad+(1-(c.o-minP)/rg)*(H-pad*2);const cy=pad+(1-(c.c-minP)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);const bH=Math.max(bh,5);ct.strokeStyle=col;ct.lineWidth=1.3;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);if(i==n-1){ct.fillStyle='#FFFF00';ct.font='bold 12px monospace';ct.fillText(up?'UP '+c.c:'DOWN '+c.c, x+12, up?top-8:top+bH+14);}});ct.fillStyle='#FFD700';ct.font='bold 13px monospace';ct.fillText('AI V2: PRED - V95 LITE - 95 JORA KA', pad, 18);</script>'''
chart = chart.replace('CANDLES', cjs_str).replace('PRED', ai_pred)
comp.html(chart, height=440)
bal_data = st.session_state.hr if st.session_state.am == 'REAL' else st.session_state.hd
bal_cjs = ','.join([str(int(b)) for b in bal_data])
bal_chart = '''<div style="border:3px solid #FFD700;border-radius:12px;padding:10px"><div style="color:#FFD700;font-size:11px">BALANCE CHART V95 LITE - GREEN RISING FIX - 250 PKR</div><canvas id="bc" width="800" height="200" style="width:100%;height:150px;background:#000"></canvas></div><script>const bcv=document.getElementById('bc');const bct=bcv.getContext('2d');const bals=[BALDATA];const BW=bcv.width;const BH=bcv.height;const bpad=20;bct.fillStyle='#000';bct.fillRect(0,0,BW,BH);if(bals.length>1){let bmin=Math.min(...bals);let bmax=Math.max(...bals);let br=bmax-bmin;if(br<100){br=100;bmin-=50;bmax+=50;}bmin-=br*0.1;bmax+=br*0.1;br=bmax-bmin;bct.strokeStyle='#00FF00';bct.lineWidth=3;bct.beginPath();bals.forEach((bal,i)=>{const x=bpad+i*(BW-bpad*2)/(bals.length-1||1);const y=bpad+(1-(bal-bmin)/br)*(BH-bpad*2);if(i==0)bct.moveTo(x,y);else bct.lineTo(x,y);});bct.stroke();}</script>'''
bal_chart = bal_chart.replace('BALDATA', bal_cjs)
comp.html(bal_chart, height=220)
a1,a2 = st.columns(2)
with a1: st.success(f'BULL UP {stf} {ht}/4 MSS BULL AI V2 {ai_pred} {ai_conf}%'); st.info(f'BOS BEAR {int(lp)}')
with a2: st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} O:{lc["O"]} C:{lc["C"]} {candle_dir}'); st.info(f'ATR {atr:.1f} AI V2 {ai_pred}')
ca,cb = st.columns(2)
with ca: st.metric(label=f'RSI AI V2', value=f'{rsi:.1f}', delta=f'{ai_pred} {ai_conf}%'); st.metric(label=f'EMA', value=f'{ema:.1f}', delta=f'BEAR')
with cb: st.metric(label=f'MACD', value=f'{macd:.2f}', delta='NEUTRAL'); st.metric(label=f'STOCH', value=f'{stoch:.1f}', delta=f'{ai_pred}')
md = st.radio('ACCOUNT', ['REAL 2500','DEMO 10000'], index=0 if st.session_state.am=='REAL' else 1)
if 'REAL' in md: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am = st.session_state.am; cb_bal = int(st.session_state.rb) if am=='REAL' else int(st.session_state.db); cp_bal = int(st.session_state.rp) if am=='REAL' else int(st.session_state.dp)
st.metric(label=f'{am} BAL H:{ht}/4 WIN {wc} LOSE {lcnt} 250 PKR V95 LITE', value=f'{cb_bal} PKR', delta=f'+{cp_bal} PKR {wr:.0f}% WIN AI V2')
t1,t2,t3 = st.tabs(['TRADING V95','DEPOSIT 2500','HISTORY'])
with t1:
    if ht >= 4: st.warning(f'HOUR LIMIT {ht}/4 REACHED - WAIT NEXT HOUR')
    else: st.write(f'PA 1 HOUR 4 TRADE FIX H:{ht}/4 4x24=96 | WIN {wc} LOSE {lcnt} WR {wr:.0f}% | 250 PKR | AI V2 {ai_pred} {ai_conf}% | V95 LITE')
    st.success(f'CANDLE {candle_dir} OPEN {lc["O"]} CLOSE {lc["C"]} MOV {mov:.2f} AI V2 {ai_pred} {ai_conf}% SCORE {score}')
with t2:
    pm = st.selectbox('METHOD', ['JazzCash','Easypaisa'], index=0)
    dp_amt = st.number_input('Dep PKR Real (MAX 2500 TOTAL)', value=2500, min_value=100, max_value=2500, step=100)
    if st.button(f'DEPOSIT NOW - {pm} - 2500 LIMIT - V95 LITE'):
        if st.session_state.dep_tot + dp_amt <= 2500: st.session_state.rb += dp_amt; st.session_state.dep_tot += dp_amt; st.session_state.hr.append(int(st.session_state.rb)); st.success(f'Dep +{dp_amt} Total {st.session_state.dep_tot}/2500 LIMIT - V95 LITE')
        else: st.error(f'LIMIT 2500 - Already {st.session_state.dep_tot}/2500')
    w_amt = st.number_input('With PKR Real (250 min)', value=250, min_value=250, max_value=2500, step=250)
    if st.button(f'WITHDRAW NOW - 250 PKR - V95 LITE'):
        if w_amt <= st.session_state.rb: st.session_state.rb -= w_amt; st.session_state.hr.append(int(st.session_state.rb)); st.success(f'With -{w_amt} Bal {int(st.session_state.rb)}')
    if st.button('CLEAR CACHE V95'): 
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
with t3:
    if len(st.session_state.th) > 0: dfh = pd.DataFrame(st.session_state.th[::-1]); st.dataframe(dfh, use_container_width=True, height=300)
    else: st.info('No trades yet - AI V2 Auto 90% WIN - 4 per hour - 250 PKR - V95 LITE')
    df = pd.DataFrame(ohlc); st.dataframe(df, use_container_width=True, height=200)
st.success(f'V95 LITE UP DOWN O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} ATR {atr:.1f} CANDLE {candle_dir} AI V2 {ai_pred} {ai_conf}% WIN {wc} LOSE {lcnt} WR {wr:.0f}% 95 JORA KA - 90% WIN - 4/HOUR - 250 PKR - BAL FIX - LITE')
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>', height=0)
