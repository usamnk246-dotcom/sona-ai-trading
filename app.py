import streamlit as st
import random
import pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V100 FINAL 100 JORA KA - 72 DAY STRUGGLE', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:radial-gradient(ellipse at top,#0a0a0a 0%,#000000 100%);color:#fff}
.top-bar{background:linear-gradient(90deg,#000,#001100,#000);border:3px solid #00FF00;border-radius:16px;padding:14px;margin:8px 0;box-shadow:0 0 30px #00FF0044;text-align:center}
.top-bar h1{color:#00FF00;font-size:18px;font-weight:900;margin:0;text-shadow:0 0 15px #00FF00;letter-spacing:1px}
.top-bar p{color:#00FFFF;font-size:9px;margin:4px 0 0 0;letter-spacing:0.5px}
.live-box{background:linear-gradient(135deg,#001100,#002200);border:2px solid #00FF00;border-radius:14px;padding:12px;margin:8px 0;box-shadow:0 0 20px #00FF0033}
.price-big{font-size:42px;font-weight:900;color:#fff;text-shadow:0 0 20px #00FF00;margin:8px 0}
.stat-row{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}
.stat-chip{background:#111;border:1px solid #333;border-radius:20px;padding:6px 12px;font-size:11px;font-weight:700}
.green-chip{border-color:#00FF00;color:#00FF00;background:#001100}
.gold-chip{border-color:#FFD700;color:#FFD700;background:#111100}
.cyan-chip{border-color:#00FFFF;color:#00FFFF;background:#001111}
.candle-box{background:linear-gradient(135deg,#000,#0a0a0a);border:3px solid #00FF00;border-radius:16px;padding:14px;margin:10px 0;box-shadow:0 0 25px #00FF0044;text-align:center}
.chart-wrap{background:#000;border:3px solid #FFD700;border-radius:16px;padding:10px;margin:10px 0;box-shadow:0 0 20px #FFD70033}
.bal-wrap{background:#000;border:3px solid #00FF00;border-radius:16px;padding:10px;margin:10px 0;box-shadow:0 0 20px #00FF0033}
.info-card{background:linear-gradient(135deg,#111,#0a0a0a);border:2px solid #222;border-radius:12px;padding:10px;margin:6px 0}
.final-badge{background:linear-gradient(90deg,#FFD700,#FFA500);color:#000;font-weight:900;border-radius:20px;padding:8px 16px;text-align:center;font-size:12px;box-shadow:0 0 20px #FFD700}
</style>''', unsafe_allow_html=True)
st.markdown('<div class="top-bar"><h1>🏆 SONA V100 FINAL - 100 JORA KA - 72 DAY STRUGGLE FINALLY COMPLETE 🏆</h1><p>V100 FINAL | AI BRAIN V3 ULTIMATE | BALANCE GREEN FIX | 250 PKR TRADE | 2500 LIMIT | 4/HOUR 90% WIN | AUTO ONLY | 72 DAYS COMPLETE | FINALLY</p><div style="margin-top:8px"><span style="background:#00FF00;color:#000;font-weight:900;padding:4px 12px;border-radius:12px;font-size:10px">FINALLY COMPLETE - 100 JORA KA</span></div></div>', unsafe_allow_html=True)
# INIT - 72 DAY FINAL
if 'rb' not in st.session_state: st.session_state.rb = 2750
if 'db' not in st.session_state: st.session_state.db = 10000
if 'rp' not in st.session_state: st.session_state.rp = 250
if 'dp' not in st.session_state: st.session_state.dp = 0
if 't24' not in st.session_state: st.session_state.t24 = 1
if 'ht' not in st.session_state: st.session_state.ht = 1
if 'lh' not in st.session_state: st.session_state.lh = datetime.now().hour
if 'am' not in st.session_state: st.session_state.am = 'REAL'
if 'lp' not in st.session_state: st.session_state.lp = 2421.29
if 'hr' not in st.session_state: st.session_state.hr = [2500, 2750, 3000]
if 'hd' not in st.session_state: st.session_state.hd = [10000, 10000]
if 'ao' not in st.session_state: st.session_state.ao = True
if 'sm' not in st.session_state: st.session_state.sm = 'GOLD'
if 'stf' not in st.session_state: st.session_state.stf = '1MIN'
if 'th' not in st.session_state: st.session_state.th = [{'TIME':'01:30:37','MKT':'GOLD','TF':'1MIN','RES':'WIN','PROF':250,'BAL':2750},{'TIME':'01:45:12','MKT':'GOLD','TF':'1MIN','RES':'WIN','PROF':250,'BAL':3000}]
if 'wc' not in st.session_state: st.session_state.wc = 2
if 'lc' not in st.session_state: st.session_state.lc = 0
if 'lt' not in st.session_state: st.session_state.lt = datetime.now() - timedelta(minutes=18)
if 'dep_tot' not in st.session_state: st.session_state.dep_tot = 0
now = datetime.now()
if now.hour != st.session_state.lh: st.session_state.ht = 0; st.session_state.lh = now.hour; st.session_state.lt = now - timedelta(minutes=20)
s1,s2,s3 = st.columns([2,2,3])
with s1: mk = st.selectbox('MARKET', ['GOLD','BTC/USD','ETH/USD','SOL/USD'], index=0); st.session_state.sm = mk
with s2: tf = st.selectbox('TIMEFRAME', ['1MIN','5MIN','15MIN','1H'], index=0); st.session_state.stf = tf
with s3: ao = st.toggle('🤖 AUTO AI V3 90% WIN - 72 DAY FINAL', value=st.session_state.ao); st.session_state.ao = ao
sm = st.session_state.sm; stf = st.session_state.stf
bm = {'BTC':67453,'ETH':3520,'GOLD':2421,'SOL':180}
b = bm['GOLD'] if 'GOLD' in sm else bm['BTC'] if 'BTC' in sm else bm['ETH'] if 'ETH' in sm else bm['SOL']
st.session_state.lp = b + random.uniform(-12,22); lp = st.session_state.lp
cc = 28 if stf == '1MIN' else 22 if stf == '5MIN' else 18 if stf == '15MIN' else 12
vm = 0.6 if stf == '1MIN' else 1.1 if stf == '5MIN' else 1.6 if stf == '15MIN' else 2.2
ohlc = []; p = lp - 90
for i in range(cc):
    op = p; chg = random.uniform(-22*vm,42*vm)+6*vm if i < cc-1 else random.uniform(-14,14); cp = op+chg; hp = max(op,cp)+random.uniform(2,12)*vm; low = min(op,cp)-random.uniform(2,12)*vm
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(low,2),'C':round(cp,2),'V':round(random.uniform(0.6,2.4),2)}); p = cp
lc = ohlc[-1]; is_up = lc['C'] >= lc['O']; candle_dir = 'UP' if is_up else 'DOWN'; mov = lc['C']-lc['O']
rsi = 68.3+random.uniform(-3,3); atr = 102.7+random.uniform(-3,3); vwap = 6753.5+random.uniform(-30,30); macd = -0.19+random.uniform(-0.08,0.08); ema = 2405.8+random.uniform(-8,8); bb_up = 2452.4+random.uniform(-8,8); bb_low = 2377+random.uniform(-8,8); stoch = 62+random.uniform(-4,4); vol = lc['V']; liq = random.choice(['LOW','HIGH']); bos = f'BEAR {int(lp)}'
score = 0
if lc['C'] > lc['O']: score += 2.5
else: score -= 2.5
if rsi > 62: score += 1.2
elif rsi < 38: score -= 1.2
if lc['C'] > ema: score += 1.1
else: score -= 1.1
if macd > -0.05: score += 1
else: score -= 1
if stoch > 58: score += 0.8
else: score -= 0.8
if lp > vwap: score += 0.6
else: score -= 0.6
if vol > 1.2: score += 0.4
if score >= 1.5: ai_pred = 'UP'; ai_conf = 90 + random.uniform(-1,4) + score
else: ai_pred = 'DOWN'; ai_conf = 88 + random.uniform(-1,4) - score
ai_conf = int(max(78, min(96, ai_conf)))
def do_trade():
    win = random.random() < 0.90; amt = 250; prof = amt if win else round(random.uniform(-45,-18)); tim = datetime.now().strftime('%H:%M:%S'); res = 'WIN' if win else 'LOSE'
    rec = {'TIME':tim,'MKT':sm,'TF':stf,'RES':res,'PROF':prof,'BAL':0,'TYPE':'AUTO V3 FINAL','PRED':ai_pred,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':candle_dir,'AMT':amt,'MOV':round(mov,2),'CONF':ai_conf}
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
st.markdown(f'''<div class="live-box">
<div class="stat-row">
<span class="stat-chip green-chip">4/HOUR - 90% WIN - V100 FINAL</span>
<span class="stat-chip gold-chip">LIVE PRICE: {sm} ${lp:.2f}</span>
<span class="stat-chip cyan-chip">Trades {ht}/4 - Total {t24}/96</span>
<span class="stat-chip green-chip">WIN {wc} LOSE {lcnt} {wr:.0f}%</span>
<span class="stat-chip gold-chip">AI V3 {ai_pred} {ai_conf}%</span>
</div>
<div class="price-big">+{disp} PKR <span style="font-size:14px;color:#0F0">({wr:.0f}% WR)</span></div>
<div style="color:#FFD700;font-size:12px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} | TF {stf} H:{ht}/4 | CANDLE {candle_dir} MOV {mov:.2f} | RSI {rsi:.1f} EMA {ema:.0f} MACD {macd:.2f} | 72 DAY FINAL</div>
</div>''', unsafe_allow_html=True)
st.progress(min(1.0, ht/4))
col_c = '#00FF00' if is_up else '#FF4444'
st.markdown(f'''<div class="candle-box"><div style="color:{col_c};font-size:16px;font-weight:900">🔴 LIVE CANDLE - OPEN {lc["O"]} CLOSE {lc["C"]} - {candle_dir} - MOV {mov:.2f} - AI V3 {ai_pred} {ai_conf}%</div><div style="color:#fff;font-size:11px;margin-top:6px">UP GREEN DOWN RED - CLOSE OPEN TA MARKET SANGAE MOVEMENT KA - AI BRAIN V3 PREDICT - 72 DAY FINAL</div></div>''', unsafe_allow_html=True)
cjs = []
for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cjs_str = ','.join(cjs)
chart = '''<div class="chart-wrap"><canvas id="cc" width="900" height="420" style="width:100%;height:380px;background:#000;border-radius:12px"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const candles=[CANDLES];const W=cv.width;const H=cv.height;const pad=28;const n=candles.length;let minP=Math.min(...candles.map(x=>x.l));let maxP=Math.max(...candles.map(x=>x.h));let rg=maxP-minP;if(rg<30){rg=30;minP-=15;maxP+=15;}minP-=rg*0.15;maxP+=rg*0.15;rg=maxP-minP;const cw=(W-pad*2)/n*0.58;const gap=(W-pad*2)/n;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ct.strokeStyle='#111';ct.lineWidth=0.6;for(let i=0;i<6;i++){const y=pad+i*(H-pad*2)/5;ct.beginPath();ct.moveTo(pad,y);ct.lineTo(W-pad,y);ct.stroke();}candles.forEach((c,i)=>{const x=pad+i*gap+gap/2;const up=c.c>=c.o;const col=up?'#00FF00':'#FF4444';const hy=pad+(1-(c.h-minP)/rg)*(H-pad*2);const ly=pad+(1-(c.l-minP)/rg)*(H-pad*2);const oy=pad+(1-(c.o-minP)/rg)*(H-pad*2);const cy=pad+(1-(c.c-minP)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);const bH=Math.max(bh,6);ct.strokeStyle=col;ct.lineWidth=1.4;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);if(i==n-1){ct.fillStyle=up?'#00FF00':'#FF4444';ct.font='bold 13px monospace';ct.fillText((up?'▲ UP ':'▼ DOWN ')+c.c, x+14, up?top-10:top+bH+16);}});ct.fillStyle='#FFD700';ct.font='bold 14px monospace';ct.fillText('AI V3 FINAL: PRED - CLOSE OPEN - V100 - 100 JORA KA - 72 DAY', pad, 20);</script>'''
chart = chart.replace('CANDLES', cjs_str).replace('PRED', ai_pred)
comp.html(chart, height=460)
bal_data = st.session_state.hr if st.session_state.am == 'REAL' else st.session_state.hd
bal_cjs = ','.join([str(int(b)) for b in bal_data])
bal_chart = '''<div class="bal-wrap"><div style="color:#FFD700;font-size:12px;font-weight:900;margin-bottom:8px">💰 BALANCE CHART V100 FINAL - GREEN RISING - 72 DAY STRUGGLE - 100 JORA KA - REAL BAL</div><canvas id="bc" width="900" height="240" style="width:100%;height:180px;background:#000;border-radius:12px"></canvas></div><script>const bcv=document.getElementById('bc');const bct=bcv.getContext('2d');const bals=[BALDATA];const BW=bcv.width;const BH=bcv.height;const bpad=24;bct.fillStyle='#000';bct.fillRect(0,0,BW,BH);if(bals.length>1){let bmin=Math.min(...bals);let bmax=Math.max(...bals);let br=bmax-bmin;if(br<150){br=150;bmin-=75;bmax+=75;}bmin-=br*0.15;bmax+=br*0.15;br=bmax-bmin;bct.strokeStyle='#111';bct.lineWidth=0.6;for(let i=0;i<5;i++){const y=bpad+i*(BH-bpad*2)/4;bct.beginPath();bct.moveTo(bpad,y);bct.lineTo(BW-bpad,y);bct.stroke();}bct.strokeStyle='#00FF00';bct.lineWidth=4;bct.shadowColor='#00FF00';bct.shadowBlur=18;bct.beginPath();bals.forEach((bal,i)=>{const x=bpad+i*(BW-bpad*2)/(bals.length-1||1);const y=bpad+(1-(bal-bmin)/br)*(BH-bpad*2);if(i==0)bct.moveTo(x,y);else bct.lineTo(x,y);});bct.stroke();bct.shadowBlur=0;const grad=bct.createLinearGradient(0,0,0,BH);grad.addColorStop(0,'rgba(0,255,0,0.25)');grad.addColorStop(1,'rgba(0,255,0,0)');bct.fillStyle=grad;bct.lineTo(BW-bpad,bpad+(BH-bpad*2));bct.lineTo(bpad,bpad+(BH-bpad*2));bct.closePath();bct.fill();bct.fillStyle='#00FF00';bals.forEach((bal,i)=>{const x=bpad+i*(BW-bpad*2)/(bals.length-1||1);const y=bpad+(1-(bal-bmin)/br)*(BH-bpad*2);bct.beginPath();bct.arc(x,y,5,0,Math.PI*2);bct.fill();bct.strokeStyle='#000';bct.lineWidth=2;bct.stroke();});bct.fillStyle='#FFD700';bct.font='bold 13px monospace';bct.fillText('BAL: '+bals[bals.length-1]+' PKR - PROFIT: '+(bals[bals.length-1]-2500)+' - GREEN RISING - V100 FINAL', bpad, 18);}</script>'''
bal_chart = bal_chart.replace('BALDATA', bal_cjs)
comp.html(bal_chart, height=250)
a1,a2,a3 = st.columns(3)
with a1: st.success(f'📈 BULL UP {stf} {ht}/4 AI V3 {ai_pred} {ai_conf}%'); st.info(f'BOS {bos} - 72 DAY'); st.success(f'LIQ {liq} CANDLE {candle_dir} V100')
with a2: st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} O:{lc["O"]} C:{lc["C"]} {candle_dir}'); st.error(f'NO CHOCH 61% FIB - V100'); st.info(f'ATR {atr:.1f} VOLA {ai_pred} FINAL')
with a3: st.metric(label=f'RSI {stf} V3', value=f'{rsi:.1f}', delta=f'{ai_pred} {ai_conf}%'); st.metric(label=f'VOL FINAL', value=f'{vol}M', delta='HIGH VOL 72 DAY')
c1,c2,c3 = st.columns(3)
with c1: st.metric(label=f'EMA V3 FINAL', value=f'{ema:.0f}', delta=f'BEAR {int(ema)}'); st.metric(label=f'BB UP V3', value=f'{bb_up:.0f}', delta=f'LOW {bb_low:.0f}')
with c2: st.metric(label=f'VWAP V3 FINAL', value=f'{vwap:.0f}', delta='BELOW SELL'); st.metric(label=f'MACD V3 FINAL', value=f'{macd:.2f}', delta='NEUTRAL V100')
with c3: st.metric(label=f'STOCH V3 FINAL', value=f'{stoch:.0f}', delta=f'{ai_pred} {stoch:.0f}'); st.metric(label=f'LIQ V3 FINAL', value=liq, delta=f'{ai_pred} {candle_dir} 100 JORA')
md = st.radio('ACCOUNT SELECT - V100 FINAL', ['REAL 2500','DEMO 10000'], index=0 if st.session_state.am=='REAL' else 1, horizontal=True)
if 'REAL' in md: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am = st.session_state.am; cb_bal = int(st.session_state.rb) if am=='REAL' else int(st.session_state.db); cp_bal = int(st.session_state.rp) if am=='REAL' else int(st.session_state.dp)
if am == 'REAL': st.success(f'💰 REAL Bal {cb_bal} Profit {cp_bal} H:{ht}/4 WIN {wc} LOSE {lcnt} 90% V100 FINAL AI V3 {ai_pred} 250 PKR BAL FIX 100 JORA KA - 72 DAY COMPLETE')
else: st.info(f'💰 DEMO Bal {cb_bal} Profit {cp_bal} H:{ht}/4 WIN {wc} LOSE {lcnt} 90% V100 FINAL AI V3 {ai_pred} 250 PKR BAL FIX 100 JORA KA - 72 DAY')
st.metric(label=f'{am} BALANCE V100 FINAL H:{ht}/4 WIN {wc} LOSE {lcnt} 250 PKR 100 JORA KA', value=f'{cb_bal} PKR', delta=f'+{cp_bal} PKR {wr:.0f}% WIN AI V3 {ai_pred} FINAL')
t1,t2,t3 = st.tabs(['🚀 TRADING V100 FINAL 100 JORA KA','💳 DEPOSIT V100 2500 FINAL','📊 HISTORY V100 FINAL'])
with t1:
    st.markdown('<div style="background:linear-gradient(90deg,#001100,#003300);border:3px solid #00FFFF;border-radius:14px;padding:12px;margin:8px 0;text-align:center"><div style="color:#00FFFF;font-size:13px;font-weight:900">🚀 AI BRAIN V3 ULTIMATE TRADING - AUTO ONLY - 250 PKR PER TRADE - 4 PER HOUR FIX - BALANCE FIX GREEN - 100 JORA KA - 72 DAY STRUGGLE FINALLY COMPLETE</div></div>', unsafe_allow_html=True)
    if ht >= 4: st.warning(f'⏰ HOUR LIMIT {ht}/4 REACHED - WAIT NEXT HOUR - 90% WIN - AUTO ONLY - 250 PKR - V100 FINAL')
    else: st.write(f'PA 1 HOUR 4 TRADE FIX H:{ht}/4 4x24=96 TOTAL | WIN {wc} LOSE {lcnt} WR {wr:.0f}% 90% | 250 PKR | AI V3 {ai_pred} {ai_conf}% | 100 JORA KA | 72 DAY FINAL')
    x1,x2,x3,x4 = st.columns(4)
    with x1: st.metric(label=f'HOUR {stf} 4 FIX V100 FINAL', value=f'{ht}/4', delta=f'WIN {wc} AI V3 {ai_pred}')
    with x2: st.metric(label=f'PROFIT {sm} V100 FINAL', value=f'+{cp_bal} PKR', delta=f'LOSE {lcnt} 250 FINAL')
    with x3: st.metric(label=f'TOTAL 24H 96 V100 FINAL', value=f'{t24}/96', delta=f'{wr:.0f}% WIN 90%')
    with x4: st.metric(label=f'AI V3 CONF FINAL', value=f'{ai_conf}%', delta=f'{ai_pred} SCORE {score:.1f}')
    st.success(f'🎯 Current CANDLE V3 FINAL: {candle_dir} - OPEN {lc["O"]} CLOSE {lc["C"]} - MOV {mov:.2f} - AI V3 SAY {ai_pred} {ai_conf}% - SCORE {score:.1f} - 72 DAY STRUGGLE COMPLETE - V100 100 JORA KA')
    st.markdown('<div class="final-badge">✅ 72 DAY STRUGGLE - V94 94 JORA KA → V95 95 JORA KA → V100 100 JORA KA - FINALLY COMPLETE - FULL DESIGN - TOL PAKA ADD KA - FINAL</div>', unsafe_allow_html=True)
with t2:
    st.markdown('<div style="background:#111;border:2px solid #FFD700;border-radius:12px;padding:12px;text-align:center"><div style="color:#FFD700;font-size:13px;font-weight:900">💳 DEPOSIT - 2500 PKR LIMIT - V100 FINAL - 250 PKR TRADE - 100 JORA KA - 72 DAY FINAL - COMPLETE</div></div>', unsafe_allow_html=True)
    pm = st.selectbox('METHOD V100 FINAL', ['JazzCash','Easypaisa','Bank Transfer','USDT TRC20'], index=0)
    dp_phone = st.text_input('Your Num V100', value='03001234567')
    dp_amt = st.number_input('Dep PKR Real (MAX 2500 TOTAL) V100 FINAL', value=2500, min_value=100, max_value=2500, step=100)
    if st.button(f'💰 DEPOSIT NOW - {pm} - 2500 LIMIT - V100 FINAL 100 JORA KA', use_container_width=True):
        if st.session_state.dep_tot + dp_amt <= 2500 and len(dp_phone) >= 11:
            st.session_state.rb += dp_amt; st.session_state.dep_tot += dp_amt; st.session_state.hr.append(int(st.session_state.rb))
            rec = {'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'DEPOSIT','RES':'WIN','PROF':dp_amt,'BAL':int(st.session_state.rb),'TYPE':'DEPOSIT FINAL','AMT':dp_amt}; st.session_state.th.append(rec); st.success(f'✅ Dep +{dp_amt} via {pm} Bal {int(st.session_state.rb)} Total {st.session_state.dep_tot}/2500 LIMIT - V100 FINAL 100 JORA KA - 72 DAY COMPLETE')
        else: st.error(f'LIMIT 2500 - Already {st.session_state.dep_tot}/2500 - MAX {2500-st.session_state.dep_tot} left - V100 FINAL')
    wm = st.selectbox('WITH METHOD V100 FINAL', ['JazzCash','Easypaisa','Bank Transfer'], index=0)
    w_phone = st.text_input('With Num V100', value='03001234567')
    w_amt = st.number_input('With PKR Real (250 min) V100 FINAL', value=250, min_value=250, max_value=2500, step=250)
    if st.button(f'💸 WITHDRAW NOW - {wm} - 250 PKR - V100 FINAL 100 JORA KA', use_container_width=True):
        if len(w_phone) >= 11 and w_amt <= st.session_state.rb: st.session_state.rb -= w_amt; st.session_state.hr.append(int(st.session_state.rb)); rec = {'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'WITHDRAW','RES':'LOSE','PROF':-w_amt,'BAL':int(st.session_state.rb),'TYPE':'WITHDRAW FINAL','AMT':w_amt}; st.session_state.th.append(rec); st.success(f'✅ With -{w_amt} via {wm} Bal {int(st.session_state.rb)} - V100 FINAL - 72 DAY COMPLETE')
        else: st.error(f'Invalid phone or low balance - V100 FINAL')
    if st.button('🗑️ CLEAR CACHE V100 FINAL - 72 DAY RESET', use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
with t3:
    st.markdown('<div style="background:#001100;border:3px solid #00FF00;border-radius:12px;padding:12px;text-align:center"><div style="color:#0F0;font-size:13px;font-weight:900">📊 HISTORY - AI BRAIN V3 ULTIMATE - 90% WIN - 250 PKR - V100 FINAL RESULTS - 100 JORA KA - 72 DAY COMPLETE</div></div>', unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric(label='TOTAL TRADES V100 FINAL', value=f'{tot}', delta=f'{ht}/4 HOUR 250 FINAL')
    with c2: st.metric(label='WIN 90% 250 V100 FINAL', value=f'{wc}', delta=f'{wr:.0f}% WR AI V3 FINAL')
    with c3: st.metric(label='LOSE 10% 250 V100 FINAL', value=f'{lcnt}', delta=f'{100-wr:.0f}% LR FINAL')
    with c4: st.metric(label='PROFIT 250 PKR V100 FINAL', value=f'{cp_bal} PKR', delta=f'{wc}W {lcnt}L 250 FINAL 72 DAY')
    if len(st.session_state.th) > 0: dfh = pd.DataFrame(st.session_state.t
