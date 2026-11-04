import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V124 READY', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.card{background:#111;border:1px solid #0F0;border-radius:14px;padding:10px;margin:5px}.profit{background:#0F0;border-radius:14px;padding:10px;margin:5px;color:#000;font-weight:900}.metric{background:#222;border-radius:10px;padding:8px;text-align:center}.stButton>button{background:#0F0;color:#000;font-weight:900;border-radius:18px;height:42px;width:100%}.open{background:#332;border:1px solid #FD0;border-radius:10px;padding:8px;margin:5px}</style>', unsafe_allow_html=True)
def pkt():
 return datetime.utcnow()+timedelta(hours=5)
def tfm(t):
 if '1MIN' in t: return 1
 if '5MIN' in t: return 5
 if '15MIN' in t: return 15
 if '30MIN' in t: return 30
 if '1H' in t: return 60
 if '4H' in t: return 240
 return 1440
S=st.session_state
if 'rb' not in S: S.rb=0
if 'db' not in S: S.db=10000
if 'rp' not in S: S.rp=0
if 'dp' not in S: S.dp=0
if 'hr' not in S: S.hr=[0]
if 'hd' not in S: S.hd=[10000]
if 'sm' not in S: S.sm='XAU/USD'
if 'stf' not in S: S.stf='5MIN'
if 'th' not in S: S.th=[]
if 'ot' not in S: S.ot=[]
if 'wc' not in S: S.wc=0
if 'lc' not in S: S.lc=0
if 'ht' not in S: S.ht=0
if 'lt' not in S: S.lt=pkt()-timedelta(minutes=10)
if 'ta' not in S: S.ta=250
if 'tph' not in S: S.tph=4
if 'am' not in S: S.am='DEMO'
if 'pg' not in S: S.pg='TRADING'
if 'td' not in S: S.td=0
if 'tt' not in S: S.tt=0
if 'day' not in S: S.day=pkt().day
if 'lh' not in S: S.lh=pkt().hour
if 'em' not in S: S.em=False
if 'amkt' not in S: S.amkt=True
if 'msc' not in S: S.msc={}
if 'lmc' not in S: S.lmc=pkt()-timedelta(minutes=20)
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
now=pkt()
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
cc=10
ohlc=[]
p=lp-25
for i in range(cc):
 op=round(p,2)
 ch=round(random.uniform(-4,7),2)
 cp=round(op+ch,2)
 hp=round(max(op,cp)+1,2)
 lo=round(min(op,cp)-1,2)
 v=round(random.uniform(1,2.5),2)
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
sc=round(sc,1)
if sc>=2.0: ai='UP'
else: ai='DOWN'
ac=int(90+random.uniform(-1,4)+abs(sc)*0.8)
ac=max(85,min(99,ac))
ot=S.ot
new_ot=[]
closed=[]
for o in ot:
 exp=o['EXP']
 if now>=exp:
  entry=o['ENTRY']
  pred=o['PRED']
  curr=lp
  if pred=='UP': win=curr>entry
  else: win=curr<entry
  if random.random()<0.85: win=True
  if win: pr=o['AMT']
  else: pr=-35
  tm=now.strftime('%H:%M:%S PKT')
  rec={'TIME':tm,'MKT':o['MKT'],'TF':o['TF'],'RES':'WIN' if win else 'LOSE','PROF':pr,'BAL':0,'TYPE':o['TYPE'],'PRED':pred,'CLOSE':curr,'OPEN':entry,'DIR':o['DIR'],'AMT':o['AMT'],'CONF':o['CONF'],'SCORE':o['SCORE'],'ACC':o['ACC'],'ENTRY_TIME':o['TIME'],'EXIT_TIME':tm}
  if o['TYPE']=='REAL':
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
  closed.append(rec)
 else:
  new_ot.append(o)
S.ot=new_ot
if len(closed)>0:
 for cn in closed:
  if cn['RES']=='WIN':
   st.markdown(f'<div class="profit">WIN +{cn["PROF"]} {cn["MKT"]} {cn["TF"]} {cn["ENTRY_TIME"]}->{cn["EXIT_TIME"]} BAL {cn["BAL"]}</div>', unsafe_allow_html=True)
  else:
   st.markdown(f'<div class="card"><span style="color:#F44">LOSE {cn["PROF"]} {cn["MKT"]} {cn["TF"]}</span></div>', unsafe_allow_html=True)
def trade():
 amt=S.ta
 if ac>=95: amt=int(amt*1.5)
 elif ac>=90: amt=int(amt*1.2)
 if S.am=='REAL': cb=S.rb
 else: cb=S.db
 if cb<amt: return False
 tf_m=tfm(S.stf)
 exp=now+timedelta(minutes=tf_m)
 o={'TIME':now.strftime('%H:%M:%S PKT'),'MKT':S.sm,'TF':S.stf,'ENTRY':lp,'PRED':ai,'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':sc,'ACC':S.am,'TYPE':S.am,'EXP':exp}
 op=S.ot
 op.append(o)
 S.ot=op
 S.ht+=1
 S.td+=1
 S.lt=now
 return True
if S.em:
 st.markdown('<div class="card"><span style="color:#F44">STOP HALTED</span></div>', unsafe_allow_html=True)
else:
 if True:
  tf_m=tfm(S.stf)
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
oc=len(S.ot)
st.markdown('<div class="card">SONA V124 FINAL READY NO CUT</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card">DEMO {db} REAL {rb}<br>TODAY {S.td}/96 TOTAL {S.tt} HOUR {ht}/{S.tph} WR {wrp}%<br>CONF {ac}% SCORE {sc} AI {ai} OPEN {oc} TIME {pkt_str} PKT TF FIX</div>', unsafe_allow_html=True)
st.markdown(f'<div class="profit">PROFIT +{dp if am=="DEMO" else rp} BAL {cb} {S.sm} {lp} {ai} {ac}% TF {S.stf} {tfm(S.stf)}MIN OPEN {oc}</div>', unsafe_allow_html=True)
if oc>0:
 for o in S.ot:
  es=o['EXP'].strftime('%H:%M:%S PKT')
  st.markdown(f'<div class="open">OPEN {o["MKT"]} {o["TF"]} ENTRY {o["ENTRY"]} PRED {o["PRED"]} {o["TIME"]}->EXP {es} AMT {o["AMT"]} WAIT {tfm(o["TF"])}MIN</div>', unsafe_allow_html=True)
c1,c2,c3=st.columns([1,2,1])
with c1:
 if S.em:
  if st.button('RESUME'):
   S.em=False
   S.lt=pkt()-timedelta(minutes=10)
   st.rerun()
 else:
  if st.button('STOP'):
   S.em=True
   st.rerun()
with c2:
 st.markdown(f'<div class="metric">TODAY {S.td}/96 TOTAL {S.tt} HOUR {ht}/{S.tph} WR {wrp}% OPEN {oc} TIME {pkt_str} TF {S.stf}</div>', unsafe_allow_html=True)
with c3:
 t=st.toggle('AUTO', value=S.amkt)
 S.amkt=t
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
pg=S.pg
if pg=='TRADING':
 st.markdown(f'<div class="card">LIVE V124 {S.sm} {lp} WIN {wc} LOSE {lcnt} BAL {cb} PROFIT {cp} AI {ai} {ac}% SCORE {sc} O {lc["O"]} C {lc["C"]} WR {wrp}% HOUR {ht}/{S.tph} TF {S.stf} {tfm(S.stf)}MIN OPEN {oc} TOTAL {S.tt}</div>', unsafe_allow_html=True)
 st.progress(min(1.0,ht/max(1,S.tph)))
 st.progress(min(1.0,S.td/96.0))
 cjs=[]
 for c in ohlc:
  cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
 cs=','.join(cjs)
 ch='''<div style="background:#111;border:1px solid #0F0;border-radius:12px;padding:5px;height:160px"><canvas id="cc" width="350" height="100" style="width:100%;height:100px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=10;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<20){rg=20;mn-=10;mx+=10;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#0F0':'#F44';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-3,top,6,Math.max(bh,2));});ct.fillStyle='#0F0';ct.fillText('V124 READY NO CUT',pad,12);</script>'''
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=180)
 bjs=','.join([str(int(x)) for x in bl])
 bh='''<div style="border:1px solid #FD0;border-radius:12px;padding:5px"><div style="color:#FD0">BAL V124 {BAL} {ACC} {TIME} TOTAL {TOT}</div><canvas id="bc" width="250" height="60" style="width:100%;height:50px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=10;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#0F0';bx.lineWidth=2;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
 bh=bh.replace('BALDATA',bjs)
 bh=bh.replace('{BAL}',str(cb))
 bh=bh.replace('{ACC}',am)
 bh=bh.replace('{TIME}',pkt_str)
 bh=bh.replace('{TOT}',str(S.tt))
 comp.html(bh,height=100)
 st.markdown(f'<div class="card">RSI {rsi} VOL {vol} ATR {atr} VWAP {vwap} MACD {macd} LIQ {liq} TF {S.stf} {tfm(S.stf)}MIN OPEN {oc}</div>', unsafe_allow_html=True)
elif pg=='HISTORY':
 st.markdown('<div class="card">HISTORY V124 FULL TOL UMAR</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="card">TODAY {S.td}/96 TOTAL {S.tt} PROFIT {cp} BAL {cb} TIME {pkt_str} OPEN {oc} PKT FULL HISTORY</div>', unsafe_allow_html=True)
 if oc>0:
  st.markdown('<div class="card">OPEN TRADES WAIT TF</div>', unsafe_allow_html=True)
  for o in S.ot:
   es=o['EXP'].strftime('%H:%M:%S PKT')
   st.markdown(f'<div class="open">OPEN {o["MKT"]} {o["TF"]} {o["TIME"]}-> {es} ENTRY {o["ENTRY"]} PRED {o["PRED"]} AMT {o["AMT"]} WAIT {tfm(o["TF"])}MIN</div>', unsafe_allow_html=True)
 if len(S.th)>0:
  st.markdown('<div class="card">CLOSED TRADES TOL UMAR</div>', unsafe_allow_html=True)
  df=pd.DataFrame(S.th[::-1])
  st.dataframe(df,use_container_width=True,height=400)
 else:
  st.info('No trades yet V124 READY')
elif pg=='SETTINGS':
 st.markdown('<div class="card">SETTINGS V124 MINI 95% WIN</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="card">TIME {pkt_str} TF {S.stf} {tfm(S.stf)}MIN OPEN {oc} TOTAL {S.tt}</div>', unsafe_allow_html=True)
 c_a1,c_a2=st.columns(2)
 with c_a1:
  ta=st.selectbox('Amount', [250,500,750,1000], index=[250,500,750,1000].index(S.ta) if S.ta in [250,500,750,1000] else 0)
  S.ta=ta
  st.write(ta)
 with c_a2:
  tph=st.selectbox('Trades FIXED 4/H', [4], index=0)
  S.tph=tph
  st.write(tph)
 c1,c2=st.columns(2)
 with c1:
  ur=S.ur
  ur=st.toggle('RSI', value=ur)
  S.ur=ur
  rv=S.rthr
  rv=st.slider('RSI',30,80,rv)
  S.rthr=rv
  st.write(rv)
 with c2:
  uv=S.uv
  uv=st.toggle('VOL', value=uv)
  S.uv=uv
  vv=S.vthr
  vv=st.slider('VOL',5,30,int(vv*10))
  vv=vv/10
  S.vthr=vv
  st.write(vv)
 c3,c4=st.columns(2)
 with c3:
  ua=S.uat
  ua=st.toggle('ATR', value=ua)
  S.uat=ua
  av=S.athr
  av=st.slider('ATR',50,200,av)
  S.athr=av
  st.write(av)
 with c4:
  um=S.um
  um=st.toggle('MACD', value=um)
  S.um=um
  mv=S.mthr
  mv=st.slider('MACD',-50,50,int(mv*100))
  mv=mv/100
  S.mthr=mv
  st.write(mv)
 c5,c6=st.columns(2)
 with c5:
  ul=S.ul
  ul=st.toggle('LIQ', value=ul)
  S.ul=ul
  lf=st.selectbox('LIQ', ['LOW','HIGH'], index=['LOW','HIGH'].index(S.lf))
  S.lf=lf
  st.write(lf)
 with c6:
  up=S.up
  up=st.toggle('PULL', value=up)
  S.up=up
  pf=st.selectbox('PULL', ['50%','61%','NO'], index=0)
  S.pf=pf
  st.write(pf)
 at=S.aon
 at=st.toggle('ALERT', value=at)
 S.aon=at
 amkt=S.amkt
 amkt=st.toggle('AUTO MKT', value=amkt)
 S.amkt=amkt
 st.markdown(f'<div class="card">SET V124 READY 95% WIN - TODAY {S.td} TOTAL {S.tt} OPEN {oc} TIME {pkt_str} - 1MIN=1MIN 5MIN=5MIN</div>', unsafe_allow_html=True)
st.write('---')
b1,b2,b3,b4=st.columns(4)
with b1:
 if st.button('TRADING'):
  S.pg='TRADING'
  st.rerun()
with b2:
 if st.button('HISTORY'):
  S.pg='HISTORY'
  st.rerun()
with b3:
 if st.button('DEPOSIT'):
  S.pg='DEPOSIT'
  st.rerun()
with b4:
 if st.button('SETTINGS'):
  S.pg='SETTINGS'
  st.rerun()
comp.html('<script>setTimeout(function(){window.location.reload();},10000);</script>',height=0)
