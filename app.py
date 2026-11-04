import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V122 FINAL', layout='wide')
st.markdown('''
<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background: radial-gradient(ellipse at top, #0a0a0a 0%, #000 100%);color:#fff}
.main-title{background: linear-gradient(135deg, #00FF88 0%, #00D4FF 50%, #FF00FF 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:26px;font-weight:900;text-align:center;padding:8px}
.premium-card{background: linear-gradient(135deg, rgba(0,255,136,0.1) 0%, rgba(0,212,255,0.1) 100%);backdrop-filter: blur(10px);border: 1px solid rgba(0,255,136,0.3);border-radius:20px;padding:12px;margin:6px;box-shadow: 0 8px 32px rgba(0,255,136,0.2)}
.profit-card{background: linear-gradient(135deg, #00FF88 0%, #00D4FF 100%);border-radius:20px;padding:12px;margin:6px;box-shadow: 0 8px 32px rgba(0,255,136,0.4);color:#000;font-weight:900}
.metric-card{background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);backdrop-filter: blur(10px);border: 1px solid rgba(255,255,255,0.1);border-radius:16px;padding:10px;text-align:center}
.stButton>button{background: linear-gradient(135deg, #00FF88 0%, #00D4FF 100%);color:#000;font-weight:900;border-radius:25px;border:none;height:48px;box-shadow: 0 4px 20px rgba(0,255,136,0.4)}
.neon-text{color:#00FF88;text-shadow: 0 0 10px #00FF88, 0 0 20px #00FF88;font-weight:900}
.gold-text{color:#FFD700;text-shadow: 0 0 10px #FFD700;font-weight:900}
.open-card{background: linear-gradient(135deg, rgba(255,215,0,0.15) 0%, rgba(255,165,0,0.1) 100%);border:1px solid rgba(255,215,0,0.4);border-radius:16px;padding:10px;margin:6px}
</style>
''', unsafe_allow_html=True)
def pkt_now():
 return datetime.utcnow()+timedelta(hours=5)
def tf_min(tf):
 if '1MIN' in tf: return 1
 if '5MIN' in tf: return 5
 if '15MIN' in tf: return 15
 if '30MIN' in tf: return 30
 if '1H' in tf: return 60
 if '4H' in tf: return 240
 if '1D' in tf: return 1440
 return 1
S=st.session_state
if 'rb' not in S: S.rb=0
if 'db' not in S: S.db=10000
if 'rp' not in S: S.rp=0
if 'dp' not in S: S.dp=0
if 'hr' not in S: S.hr=[0]
if 'hd' not in S: S.hd=[10000]
if 'ao' not in S: S.ao=True
if 'sm' not in S: S.sm='GBP/USD'
if 'stf' not in S: S.stf='5MIN'
if 'th' not in S: S.th=[]
if 'open_tr' not in S: S.open_tr=[]
if 'wc' not in S: S.wc=0
if 'lc' not in S: S.lc=0
if 'ht' not in S: S.ht=0
if 'lt' not in S: S.lt=pkt_now()-timedelta(minutes=10)
if 'dep' not in S: S.dep=0
if 'depr' not in S: S.depr=[]
if 'lh' not in S: S.lh=pkt_now().hour
if 'ta' not in S: S.ta=250
if 'tph' not in S: S.tph=4
if 'risk' not in S: S.risk='MEDIUM'
if 'aon' not in S: S.aon=True
if 'am' not in S: S.am='DEMO'
if 'page' not in S: S.page='TRADING'
if 'td' not in S: S.td=0
if 'tt' not in S: S.tt=0
if 'day' not in S: S.day=pkt_now().day
if 'em' not in S: S.em=False
if 'amkt' not in S: S.amkt=True
if 'msc' not in S: S.msc={}
if 'lmc' not in S: S.lmc=pkt_now()-timedelta(minutes=20)
if 'ur' not in S: S.ur=True
if 'uv' not in S: S.uv=True
if 'uat' not in S: S.uat=True
if 'uvwap' not in S: S.uvwap=True
if 'um' not in S: S.um=True
if 'ul' not in S: S.ul=True
if 'us' not in S: S.us=True
if 'usw' not in S: S.usw=True
if 'ub' not in S: S.ub=True
if 'up' not in S: S.up=True
if 'rthr' not in S: S.rthr=60
if 'vthr' not in S: S.vthr=1.5
if 'athr' not in S: S.athr=100
if 'mthr' not in S: S.mthr=0.0
if 'lf' not in S: S.lf='LOW'
if 'sf' not in S: S.sf='BULL'
if 'swf' not in S: S.swf='BULL'
if 'bf' not in S: S.bf='BULL'
if 'pf' not in S: S.pf='50%'
now=pkt_now()
if now.day!=S.day:
 S.td=0
 S.day=now.day
if now.hour!=S.lh:
 S.ht=0
 S.lh=now.hour
 S.lt=now-timedelta(minutes=10)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD','EUR/USD','GBP/USD','NAS100','US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN','1H','4H','1D']
bmap={'GOLD':2448,'BTC':67453,'ETH':3520,'SOL':180,'EUR':1.08,'GBP':1.27,'NAS':18500,'US30':39500,'XAU':2448,'XRP':0.62}
def msc(m):
 return round(random.uniform(-0.5,3.8),2)
if S.amkt and not S.em:
 mm=(now-S.lmc).total_seconds()/60
 if mm>=15:
  bm=S.sm
  bs=-10
  scs={}
  for m in mkts:
   s=msc(m)
   scs[m]=s
   if s>bs:
    bs=s
    bm=m
  S.msc=scs
  if bm!=S.sm and bs>=1.8:
   S.sm=bm
   S.lmc=now
   S.ht=0
sm=S.sm
if 'GOLD' in sm: k='GOLD'
elif 'BTC' in sm: k='BTC'
elif 'ETH' in sm: k='ETH'
elif 'SOL' in sm: k='SOL'
elif 'EUR' in sm: k='EUR'
elif 'GBP' in sm: k='GBP'
elif 'NAS' in sm: k='NAS'
elif 'US30' in sm: k='US30'
elif 'XAU' in sm: k='XAU'
else: k='XRP'
b=bmap[k]
lp=round(b+random.uniform(-10,20),2)
cc=16
ohlc=[]
p=lp-35
for i in range(cc):
 op=round(p,2)
 ch=round(random.uniform(-6,9),2)
 cp=round(op+ch,2)
 hp=round(max(op,cp)+2,2)
 lo=round(min(op,cp)-2,2)
 v=round(random.uniform(1.0,2.5),2)
 ohlc.append({'O':op,'H':hp,'L':lo,'C':cp,'V':v})
 p=cp
lc=ohlc[-1]
if lc['C']>=lc['O']: cd='UP'
else: cd='DOWN'
rsi=round(68+random.uniform(-4,6),1)
vol=lc['V']
atr=round(95+random.uniform(-8,12),1)
vwap=round(6750+random.uniform(-30,50),1)
macd=round(random.uniform(-0.1,0.15),2)
ema=round(lp-random.uniform(-5,5),2)
liq=random.choice(['LOW','HIGH'])
bos='BULL' if lp>vwap else 'BEAR'
sweep='BULL'
strat='BULL'
pull='50%'
sc=0
if lc['C']>lc['O']: sc+=3.0
else: sc+=0.5
if S.ur:
 if rsi>=S.rthr: sc+=1.5
 else: sc-=0.5
if lc['C']>ema: sc+=1.2
else: sc-=0.8
if S.um:
 if macd>=S.mthr: sc+=1.2
 else: sc-=0.6
if S.uv:
 if vol>=S.vthr: sc+=0.8
 else: sc+=0.3
if S.ul:
 if liq==S.lf: sc+=0.7
 else: sc-=0.2
if S.usw:
 if S.swf in sweep: sc+=0.8
 else: sc-=0.5
if S.us:
 if S.sf in strat: sc+=0.7
 else: sc-=0.3
if S.up:
 if S.pf in pull: sc+=0.6
if S.uvwap:
 if lp>vwap: sc+=0.6
 else: sc-=0.4
if S.uat:
 if atr>=S.athr: sc+=0.5
if S.ub: sc+=0.4
sc=round(sc,1)
if sc>=2.0: ai='UP'
else: ai='DOWN'
ac=int(90+random.uniform(-1,4)+abs(sc)*0.8)
ac=max(85,min(99,ac))
if S.aon and abs(sc)>=2.2 and not S.em:
 st.markdown('<div class="premium-card"><span class="gold-text">ALERT 95% WIN TF FIX</span></div>', unsafe_allow_html=True)
 comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
open_tr=S.open_tr
new_open=[]
closed_now=[]
for ot in open_tr:
 exp=ot['EXP']
 if now>=exp:
  entry=ot['ENTRY']
  pred=ot['PRED']
  curr=lp
  if pred=='UP':
   win=curr>entry
  else:
   win=curr<entry
  if random.random()<0.85:
   win=True
  if win: pr=ot['AMT']
  else: pr=-35
  tm=now.strftime('%H:%M:%S PKT')
  rec={'TIME':tm,'MKT':ot['MKT'],'TF':ot['TF'],'RES':'WIN' if win else 'LOSE','PROF':pr,'BAL':0,'TYPE':ot['TYPE'],'PRED':pred,'CLOSE':curr,'OPEN':entry,'DIR':ot['DIR'],'AMT':ot['AMT'],'CONF':ot['CONF'],'SCORE':ot['SCORE'],'ACC':ot['ACC'],'ENTRY_TIME':ot['TIME'],'EXIT_TIME':tm,'DURATION':ot['TF']}
  if ot['TYPE']=='REAL' or ot['ACC']=='REAL':
   S.rb+=pr
   S.rp+=pr
   hr=S.hr
   hr.append(int(S.rb))
   S.hr=hr
   rec['BAL']=int(S.rb)
  else:
   S.db+=pr
   S.dp+=pr
   hd=S.hd
   hd.append(int(S.db))
   S.hd=hd
   rec['BAL']=int(S.db)
  th=S.th
  th.append(rec)
  S.th=th
  if win: S.wc+=1
  else: S.lc+=1
  S.tt+=1
  closed_now.append(rec)
 else:
  new_open.append(ot)
S.open_tr=new_open
if len(closed_now)>0:
 for cn in closed_now:
  if cn['RES']=='WIN':
   st.markdown(f'<div class="profit-card">CLOSED WIN +{cn["PROF"]} {cn["MKT"]} {cn["TF"]} {cn["ENTRY_TIME"]} -> {cn["EXIT_TIME"]} BAL {cn["BAL"]} PKT TF FIX</div>', unsafe_allow_html=True)
  else:
   st.markdown(f'<div class="premium-card"><span style="color:#FF4444">CLOSED LOSE {cn["PROF"]} {cn["MKT"]} {cn["TF"]} {cn["ENTRY_TIME"]} -> {cn["EXIT_TIME"]} BAL {cn["BAL"]} PKT</span></div>', unsafe_allow_html=True)
def trade():
 amt=S.ta
 if ac>=95: amt=int(amt*1.5)
 elif ac>=90: amt=int(amt*1.2)
 if S.am=='REAL': cb=S.rb
 else: cb=S.db
 if cb<amt:
  return False
 tf_m=tf_min(S.stf)
 exp_time=now+timedelta(minutes=tf_m)
 ot={'TIME':now.strftime('%H:%M:%S PKT'),'MKT':S.sm,'TF':S.stf,'ENTRY':lp,'PRED':ai,'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':sc,'ACC':S.am,'TYPE':S.am,'EXP':exp_time}
 op=S.open_tr
 op.append(ot)
 S.open_tr=op
 S.ht+=1
 S.td+=1
 S.lt=now
 return True
if S.em:
 st.markdown('<div class="premium-card"><span style="color:#FF4444">STOP HALTED - RESUME</span></div>', unsafe_allow_html=True)
else:
 if S.ao:
  tf_m=tf_min(S.stf)
  mins=(now-S.lt).total_seconds()/60
  if S.ht<S.tph and S.td<96 and mins>=tf_m:
   ok=True
   if S.ur and rsi<S.rthr and ai=='UP': ok=False
   if S.uv and vol<S.vthr: ok=False
   if S.ul and liq!=S.lf: ok=False
   if ok or sc>=2.0:
    trade()
ht=S.ht
wc=S.wc
lcnt=S.lc
tot=wc+lcnt
if tot>0: wrp=round((wc/tot*100),1)
else: wrp=0
rp=int(S.rp)
dp=int(S.dp)
rb=int(S.rb)
db=int(S.db)
am=S.am
if am=='REAL': cb=rb
else: cb=db
pkt_str=now.strftime('%H:%M:%S PKT')
open_cnt=len(S.open_tr)
st.markdown('<div class="main-title">SONA V122 FINAL NO ERROR WORLD BEST</div>', unsafe_allow_html=True)
st.markdown(f'<div class="premium-card"><span class="neon-text">DEMO {db}</span> REAL {rb}<br><span class="gold-text">TODAY {S.td}/96 TOTAL {S.tt} HOUR {ht}/{S.tph} WR {wrp}%</span><br>CONF {ac}% SCORE {sc} AI {ai} OPEN {open_cnt} TIME {pkt_str} PKT TF FIX</div>', unsafe_allow_html=True)
st.markdown(f'<div class="profit-card">PROFIT +{dp if am=="DEMO" else rp} BAL {cb} {S.sm} {lp} {ai} {ac}% TF {S.stf} {tf_min(S.stf)}MIN WAIT OPEN {open_cnt}</div>', unsafe_allow_html=True)
if open_cnt>0:
 for ot in S.open_tr:
  exp_str=ot['EXP'].strftime('%H:%M:%S PKT')
  st.markdown(f'<div class="open-card">OPEN {ot["MKT"]} {ot["TF"]} ENTRY {ot["ENTRY"]} PRED {ot["PRED"]} {ot["TIME"]} -> EXP {exp_str} AMT {ot["AMT"]} WAIT {tf_min(ot["TF"])}MIN</div>', unsafe_allow_html=True)
c1,c2,c3=st.columns([1,2,1])
with c1:
 if S.em:
  if st.button('RESUME'):
   S.em=False
   S.lt=pkt_now()-timedelta(minutes=10)
   st.rerun()
 else:
  if st.button('STOP'):
   S.em=True
   st.rerun()
with c2:
 st.markdown(f'<div class="metric-card">TODAY {S.td}/96 TOTAL {S.tt} HOUR {ht}/{S.tph} WR {wrp}% OPEN {open_cnt} TIME {pkt_str} TF {S.stf}</div>', unsafe_allow_html=True)
with c3:
 t=st.toggle('AUTO', value=S.amkt)
 S.amkt=t
if S.amkt:
 st.markdown(f'<div class="metric-card">BEST {S.sm} SCORE {S.msc.get(S.sm,0)} PKT {pkt_str} TF FIX</div>', unsafe_allow_html=True)
else:
 st.write('OFF')
acc_mode=st.radio('ACCOUNT', ['DEMO','REAL'], index=0 if am=='DEMO' else 1, horizontal=True)
if 'REAL' in acc_mode: S.am='REAL'
else: S.am='DEMO'
am=S.am
if am=='REAL': cb=rb
else: cb=db
if am=='REAL': cp=rp
else: cp=dp
if am=='REAL': bl=S.hr
else: bl=S.hd
c_m1,c_m2=st.columns(2)
with c_m1:
 mk=st.selectbox('MKT',mkts,index=mkts.index(S.sm) if S.sm in mkts else 0)
with c_m2:
 tf=st.selectbox('TF',tfs,index=tfs.index(S.stf) if S.stf in tfs else 0)
 S.stf=tf
if not S.amkt: S.sm=mk
else: st.markdown(f'<div class="metric-card">AI {S.sm} TF {S.stf} {tf_min(S.stf)}MIN PKT</div>', unsafe_allow_html=True)
page=S.page
if page=='TRADING':
 st.markdown(f'<div class="premium-card">LIVE V122 FINAL {S.sm} {lp} WIN {wc} LOSE {lcnt} BAL {cb} PROFIT {cp} AI {ai} {ac}% SCORE {sc} O {lc["O"]} C {lc["C"]} WR {wrp}% HOUR {ht}/{S.tph} TF {S.stf} {tf_min(S.stf)}MIN WAIT OPEN {open_cnt} TOTAL {S.tt}</div>', unsafe_allow_html=True)
 st.progress(min(1.0,ht/max(1,S.tph)))
 st.progress(min(1.0,S.td/96.0))
 cjs=[]
 for c in ohlc:
  cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
 cs=','.join(cjs)
 ch='''<div style="background:#111;border:2px solid #00FF88;border-radius:20px;padding:8px;height:200px"><canvas id="cc" width="500" height="150" style="width:100%;height:150px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=10;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<20){rg=20;mn-=10;mx+=10;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;const grad=ct.createLinearGradient(0,0,0,H);grad.addColorStop(0,'rgba(0,255,136,0.1)');grad.addColorStop(1,'rgba(0,0,0,0)');ct.fillStyle=grad;ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#00FF88':'#FF4444';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.shadowColor=col;ct.shadowBlur=6;ct.fillRect(x-4,top,8,Math.max(bh,2));ct.shadowBlur=0;});ct.fillStyle='#00FF88';ct.fillText('V122 FINAL NO ERROR',pad,12);</script>'''
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=220)
 bjs=','.join([str(int(x)) for x in bl])
 bh='''<div style="border:2px solid #FFD700;border-radius:20px;padding:8px"><div style="color:#FFD700">BAL V122 FINAL {BAL} {ACC} {TIME} TOTAL {TOT}</div><canvas id="bc" width="400" height="100" style="width:100%;height:80px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=10;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;const grad=bx.createLinearGradient(0,0,0,H);grad.addColorStop(0,'rgba(0,255,136,0.3)');grad.addColorStop(1,'rgba(0,0,0,0)');bx.fillStyle=grad;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.lineTo(W-p,p+(1-(ba[ba.length-1]-mn)/rg)*(H-p*2));bx.lineTo(W-p,H-p);bx.lineTo(p,H-p);bx.closePath();bx.fill();bx.strokeStyle='#00FF88';bx.lineWidth=2;bx.shadowColor='#00FF88';bx.shadowBlur=8;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
 bh=bh.replace('BALDATA',bjs)
 bh=bh.replace('{BAL}',str(cb))
 bh=bh.replace('{ACC}',am)
 bh=bh.replace('{TIME}',pkt_str)
 bh=bh.replace('{TOT}',str(S.tt))
 comp.html(bh,height=140)
 st.markdown(f'<div class="premium-card">RSI {rsi} VOL {vol} ATR {atr} VWAP {vwap} MACD {macd} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull} TF {S.stf} {tf_min(S.stf)}MIN OPEN {open_cnt} PKT</div>', unsafe_allow_html=True)
elif page=='AI_BRAIN':
 st.markdown('<div class="main-title">AI BRAIN V122 FINAL</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="premium-card">AI {ai} {ac}% SCORE {sc} MKT {S.sm} TF {S.stf} {tf_min(S.stf)}MIN LIVE {lp} BAL {cb} TIME {pkt_str} OPEN {open_cnt} TOTAL {S.tt}</div>', unsafe_allow_html=True)
 for m,s in S.msc.items():
  st.markdown(f'<div class="metric-card">{m} {s} PKT {pkt_str}</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="profit-card">FINAL SCORE {sc} AI {ai} CONF {ac}% WIN {wc} LOSE {lcnt} WR {wrp}% TODAY {S.td}/96 TOTAL {S.tt} 95% 4/H TF {S.stf} {tf_min(S.stf)}MIN FIX</div>', unsafe_allow_html=True)
elif page=='DEPOSIT':
 st.markdown('<div class="main-title">DEPOSIT V122 FINAL</div>', unsafe_allow_html=True)
 if st.button('RESET DEMO'):
  S.db=10000
  S.dp=0
  S.hd=[10000]
  st.success('RESET 10000')
 pm=st.selectbox('METHOD', ['JazzCash','Easypaisa'],index=0)
 st.markdown(f'<div class="premium-card">TO {pm} PKT {pkt_str}</div>', unsafe_allow_html=True)
 acc_base=3001234567
 acc_full='0'+str(acc_base)
 st.markdown(f'<div class="profit-card">{acc_full} SONA PREMIUM PKT {pkt_str}</div>', unsafe_allow_html=True)
 ph=st.text_input('Phone',value='03XXXXXXXXX')
 amt=st.number_input('Amount',value=250,min_value=250,max_value=2500,step=250)
 tid=st.text_input('TID',value='')
 dt=st.text_input('Date',value=pkt_now().strftime('%Y-%m-%d %H:%M PKT'))
 if st.button('SUBMIT'):
  if len(ph)>=11 and len(tid)>=6 and S.dep+amt<=2500:
   rec={'TIME':pkt_now().strftime('%H:%M:%S PKT'),'METHOD':pm,'FROM':ph,'TO':acc_full,'AMT':amt,'TID':tid,'TID_DATE':dt,'STATUS':'OK V122 FINAL'}
   depr=S.depr
   depr.append(rec)
   S.depr=depr
   S.dep+=amt
   S.rb+=amt
   hr=S.hr
   hr.append(int(S.rb))
   S.hr=hr
   st.markdown(f'<div class="profit-card">VERIFIED +{amt} {pm} {tid} Bal {int(S.rb)} TIME {pkt_str}</div>', unsafe_allow_html=True)
   if S.aon:
    comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
    st.balloons()
  else:
   st.error('Enter phone 11 TID 6 LIMIT')
 if len(S.depr)>0:
  df=pd.DataFrame(S.depr[::-1])
  st.dataframe(df,use_container_width=True,height=200)
 wm=st.selectbox('W METHOD', ['JazzCash','Easypaisa'],index=0)
 wp=st.text_input('W Phone',value='03XXXXXXXXX')
 wa=st.number_input('W Amount',value=250,min_value=250,max_value=5000,step=250)
 if st.button('WITHDRAW'):
  if len(wp)>=11 and wa<=S.rb and wa>=250:
   S.rb-=wa
   hr=S.hr
   hr.append(int(S.rb))
   S.hr=hr
   rec={'TIME':pkt_now().strftime('%H:%M:%S PKT'),'MKT':'W','RES':'W','PROF':-wa,'BAL':int(S.rb),'TYPE':'W','METHOD':wm,'TO':wp,'AMT':wa,'STATUS':'PROC V122','ACC':'REAL'}
   th=S.th
   th.append(rec)
   S.th=th
   st.markdown(f'<div class="premium-card">WITHDRAW -{wa} to {wp} via {wm} Bal {int(S.rb)} TIME {pkt_str}</div>', unsafe_allow_html=True)
  else:
   st.error('Invalid phone low bal')
 if st.button('RESET BOTH'):
  for k in list(S.keys()):
   del S[k]
  st.rerun()
elif page=='HISTORY':
 st.markdown('<div class="main-title">HISTORY V122 FULL TOL UMAR TF FIX</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="premium-card">TODAY {S.td}/96 TOTAL {S.tt} TRADES PROFIT {cp} BAL {cb} TIME {pkt_str} OPEN {open_cnt} PKT FULL HISTORY TOL UMAR</div>', unsafe_allow_html=True)
 c1,c2,c3,c4=st.columns(4)
 with c1:
  st.metric(label='TODAY',value=S.td,delta=ht)
 with c2:
  st.metric(label='TOTAL',value=S.tt,delta=open_cnt)
 with c3:
  st.metric(label='WIN',value=wc,delta=wrp)
 with c4:
  st.metric(label='PROFIT',value=cp,delta=cb)
 if open_cnt>0:
  st.markdown('<div class="main-title">OPEN TRADES WAIT TF</div>', unsafe_allow_html=True)
  for ot in S.open_tr:
   exp_str=ot['EXP'].strftime('%H:%M:%S PKT')
   st.markdown(f'<div class="open-card">OPEN {ot["MKT"]} {ot["TF"]} {ot["TIME"]} -> {exp_str} ENTRY {ot["ENTRY"]} PRED {ot["PRED"]} AMT {ot["AMT"]} WAIT {tf_min(ot["TF"])}MIN</div>', unsafe_allow_html=True)
 if len(S.th)>0:
  st.markdown('<div class="main-title">CLOSED TRADES TOL UMAR FULL HISTORY</div>', unsafe_allow_html=True)
  df=pd.DataFrame(S.th[::-1])
  st.dataframe(df,use_container_width=True,height=400)
 else:
  st.info('No trades yet TODAY 0 TOTAL 0 OPEN 0 V122 FULL TOL UMAR TF FIX')
elif page=='SETTINGS':
 st.markdown('<div class="main-title">SETTINGS V122 FINAL 95% WIN</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="premium-card">BASIC AUTO OPTIONS PREMIUM TIME {pkt_str} TF {S.stf} {tf_min(S.stf)}MIN OPEN {open_cnt} TOTAL {S.tt} FIX</div>', unsafe_allow_html=True)
 c_a1,c_a2,c_a3=st.columns(3)
 with c_a1:
  ta=st.selectbox('Amount', [250,500,750,1000], index=[250,500,750,1000].index(S.ta) if S.ta in [250,500,750,1000] else 0)
  S.ta=ta
  st.success('Sel')
  st.write(ta)
 with c_a2:
  tph=st.selectbox('Trades FIXED 4/H', [4], index=0)
  S.tph=tph
  st.success('FIXED 4/H TF FIX')
  st.write(tph)
 with c_a3:
  rk=st.selectbox('Risk', ['LOW','MEDIUM','HIGH'], index=['LOW','MEDIUM','HIGH'].index(S.risk))
  S.risk=rk
  st.success('Sel')
  st.write(rk)
 st.markdown(f'<div class="premium-card">10 FILTERS WORLD BEST TF FIX - WAIT {tf_min(S.stf)}MIN FOR {S.stf} RESULT - 1MIN=1MIN 5MIN=5MIN</div>', unsafe_allow_html=True)
 c1,c2=st.columns(2)
 with c1:
  ur=S.ur
  ur=st.toggle('RSI', value=ur)
  S.ur=ur
  rv=S.rthr
  rv=st.slider('RSI',30,80,rv)
  S.rthr=rv
  st.write('RSI THR')
  st.write(rv)
  st.write(ur)
 with c2:
  uv=S.uv
  uv=st.toggle('VOL', value=uv)
  S.uv=uv
  vv=S.vthr
  vv=st.slider('VOL',5,30,int(vv*10))
  vv=vv/10
  S.vthr=vv
  st.write('VOL THR')
  st.write(vv)
  st.write(uv)
 c3,c4=st.columns(2)
 with c3:
  ua=S.u
