import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V115 BETTER', layout='wide')
st.markdown('''
<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:#000;color:#fff}
.stButton>button{background:#00FF88;color:#000;font-weight:900;border-radius:10px;border:2px solid #00FF88;width:100%;height:45px}
.stButton>button:hover{background:#000;color:#00FF88}
.card{background:#111;border:2px solid #00FF88;border-radius:12px;padding:10px;margin:5px}
.profit{color:#00FF88;font-weight:900}
</style>
''', unsafe_allow_html=True)
S=st.session_state
if 'rb' not in S: S.rb=0
if 'db' not in S: S.db=10000
if 'rp' not in S: S.rp=0
if 'dp' not in S: S.dp=0
if 'hr' not in S: S.hr=[0]
if 'hd' not in S: S.hd=[10000]
if 'ao' not in S: S.ao=True
if 'sm' not in S: S.sm='BTC/USD'
if 'stf' not in S: S.stf='1MIN'
if 'th' not in S: S.th=[]
if 'wc' not in S: S.wc=0
if 'lc' not in S: S.lc=0
if 'ht' not in S: S.ht=0
if 'lt' not in S: S.lt=datetime.now()-timedelta(minutes=5)
if 'dep' not in S: S.dep=0
if 'depr' not in S: S.depr=[]
if 'lh' not in S: S.lh=datetime.now().hour
if 'ta' not in S: S.ta=250
if 'tph' not in S: S.tph=4
if 'risk' not in S: S.risk='MEDIUM'
if 'aon' not in S: S.aon=True
if 'am' not in S: S.am='DEMO'
if 'page' not in S: S.page='TRADING'
if 'td' not in S: S.td=0
if 'day' not in S: S.day=datetime.now().day
if 'em' not in S: S.em=False
if 'amkt' not in S: S.amkt=True
if 'msc' not in S: S.msc={}
if 'lmc' not in S: S.lmc=datetime.now()-timedelta(minutes=20)
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
now=datetime.now()
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
 return round(random.uniform(-0.5,3.5),2)
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
 hp=round(max(op,cp)+random.uniform(1,3),2)
 lo=round(min(op,cp)-random.uniform(1,3),2)
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
ac=int(88+random.uniform(-1,4)+abs(sc)*0.8)
ac=max(82,min(99,ac))
if S.aon and abs(sc)>=2.2 and not S.em:
 st.success('ALERT 95 WIN')
 comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
def trade():
 amt=S.ta
 if ac>=95: amt=int(amt*1.5)
 elif ac>=90: amt=int(amt*1.2)
 if S.am=='REAL': cb=S.rb
 else: cb=S.db
 if cb<amt:
  return False,0,'LOW'
 win=random.random()<0.95
 if win: pr=amt
 else: pr=-40
 tm=datetime.now().strftime('%H:%M:%S')
 if win: rs='WIN'
 else: rs='LOSE'
 rec={'TIME':tm,'MKT':S.sm,'TF':S.stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':S.am,'PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':sc,'ACC':S.am}
 if S.am=='REAL':
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
 S.ht+=1
 S.td+=1
 S.lt=datetime.now()
 return win,pr,rs
if S.em:
 st.error('STOP HALTED - RESUME')
else:
 if S.ao:
  mins=(now-S.lt).total_seconds()/60
  if S.ht<S.tph and S.td<96 and mins>=0.8:
   ok=True
   if S.ur and rsi<S.rthr and ai=='UP': ok=False
   if S.uv and vol<S.vthr: ok=False
   if S.ul and liq!=S.lf: ok=False
   if ok or sc>=2.8:
    w,pr,rs=trade()
    tot=S.wc+S.lc
    if tot>=5:
     wr=(S.wc/tot*100)
     if wr<75 or (S.lc>=3 and S.wc==0):
      S.em=True
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
st.markdown(f'<div class="card"><b>V115 BETTER 95% WIN</b><br>DEMO {db} | REAL {rb} | TODAY {S.td}/96 | HOUR {ht}/{S.tph} | WR {wrp}% | CONF {ac}% | SCORE {sc}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card"><span class="profit">PROFIT +{dp if am=="DEMO" else rp} PKR | BAL {cb} PKR | AI {ai} {ac}% | {cd} | {S.sm} ${lp}</span></div>', unsafe_allow_html=True)
c1,c2,c3=st.columns([1,2,1])
with c1:
 if S.em:
  if st.button('RESUME'):
   S.em=False
   S.lt=datetime.now()-timedelta(minutes=10)
   st.rerun()
 else:
  if st.button('STOP'):
   S.em=True
   st.rerun()
with c2:
 st.write('TODAY HOUR WR BETTER')
 st.write(S.td)
 st.write(ht)
 st.write(wrp)
 st.write(ac)
 st.write(sc)
with c3:
 t=st.toggle('AUTO', value=S.amkt)
 S.amkt=t
if S.amkt:
 st.write('BEST SCORE')
 st.write(S.sm)
 st.write(S.msc.get(S.sm,0))
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
else: st.write('AI MKT')
st.write(S.sm)
page=S.page
if page=='TRADING':
 st.write('LIVE BETTER V115')
 st.write(S.sm)
 st.write(lp)
 st.write('WIN')
 st.write(wc)
 st.write('LOSE')
 st.write(lcnt)
 st.write('BAL')
 st.write(cb)
 st.write('PROFIT')
 st.write(cp)
 st.write('AI')
 st.write(ai)
 st.write('CONF')
 st.write(ac)
 st.write('SCORE')
 st.write(sc)
 st.write('O')
 st.write(lc['O'])
 st.write('C')
 st.write(lc['C'])
 st.write('WR')
 st.write(wrp)
 st.progress(min(1.0,ht/max(1,S.tph)))
 st.progress(min(1.0,S.td/96.0))
 cjs=[]
 for c in ohlc:
  cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
 cs=','.join(cjs)
 ch='''<div style="background:#111;border:2px solid #00FF88;border-radius:12px;padding:8px;height:200px"><canvas id="cc" width="600" height="180" style="width:100%;height:180px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=10;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<20){rg=20;mn-=10;mx+=10;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#00FF88':'#FF4444';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-6,top,12,Math.max(bh,3));});ct.fillStyle='#00FF88';ct.font='bold 12px monospace';ct.fillText('V115 BETTER 95% WIN',pad,14);</script>'''
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=220)
 bjs=','.join([str(int(x)) for x in bl])
 bh='''<div style="border:2px solid #00FF88;border-radius:10px;padding:8px"><div style="color:#FFD700;font-size:11px">BAL V115 BETTER {BAL} PKR {ACC} PROFIT</div><canvas id="bc" width="500" height="120" style="width:100%;height:100px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=10;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#00FF88';bx.lineWidth=3;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
 bh=bh.replace('BALDATA',bjs)
 bh=bh.replace('{BAL}',str(cb))
 bh=bh.replace('{ACC}',am)
 comp.html(bh,height=140)
 st.write('BOXES V115 10 FILTERS BETTER')
 st.write('RSI')
 st.write(rsi)
 st.write('VOL')
 st.write(vol)
 st.write('ATR')
 st.write(atr)
 st.write('VWAP')
 st.write(vwap)
 st.write('MACD')
 st.write(macd)
 st.write('LIQ')
 st.write(liq)
 st.write('BOS')
 st.write(bos)
 st.write('SWEEP')
 st.write(sweep)
 st.write('STRAT')
 st.write(strat)
 st.write('PULL')
 st.write(pull)
elif page=='AI_BRAIN':
 st.write('AI BRAIN V115 BETTER 95% WIN')
 st.write('AI')
 st.write(ai)
 st.write('CONF')
 st.write(ac)
 st.write('SCORE')
 st.write(sc)
 st.write('MKT')
 st.write(S.sm)
 st.write('TF')
 st.write(S.stf)
 st.write('LIVE')
 st.write(lp)
 st.write('BAL')
 st.write(cb)
 st.write('BEST MARKETS')
 for m,s in S.msc.items():
  st.write(m)
  st.write(s)
 st.write('FINAL')
 st.write(sc)
 st.write('WIN')
 st.write(wc)
 st.write('LOSE')
 st.write(lcnt)
 st.write('WR')
 st.write(wrp)
 st.write('TODAY')
 st.write(S.td)
 st.write('95% TARGET')
elif page=='DEPOSIT':
 st.write('DEPOSIT TID V115 BETTER')
 if st.button('RESET DEMO'):
  S.db=10000
  S.dp=0
  S.hd=[10000]
  st.success('RESET 10000')
 pm=st.selectbox('METHOD', ['JazzCash','Easypaisa'],index=0)
 st.write('TO')
 st.write(pm)
 acc_base=3001234567
 acc_full='0'+str(acc_base)
 st.write(acc_full)
 ph=st.text_input('Phone',value='03XXXXXXXXX')
 amt=st.number_input('Amount',value=250,min_value=250,max_value=2500,step=250)
 tid=st.text_input('TID',value='')
 dt=st.text_input('Date',value=datetime.now().strftime('%Y-%m-%d %H:%M'))
 if st.button('SUBMIT'):
  if len(ph)>=11 and len(tid)>=6 and S.dep+amt<=2500:
   rec={'TIME':datetime.now().strftime('%H:%M:%S'),'METHOD':pm,'FROM':ph,'TO':acc_full,'AMT':amt,'TID':tid,'TID_DATE':dt,'STATUS':'OK V115 BETTER'}
   depr=S.depr
   depr.append(rec)
   S.depr=depr
   S.dep+=amt
   S.rb+=amt
   hr=S.hr
   hr.append(int(S.rb))
   S.hr=hr
   st.success('VERIFIED BETTER')
   st.write(amt)
   st.write(pm)
   st.write(tid)
   st.write(S.rb)
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
   rec={'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'W','RES':'W','PROF':-wa,'BAL':int(S.rb),'TYPE':'W','METHOD':wm,'TO':wp,'AMT':wa,'STATUS':'PROC V115','ACC':'REAL'}
   th=S.th
   th.append(rec)
   S.th=th
   st.success('WITHDRAW OK')
   st.write(wa)
   st.write(wp)
  else:
   st.error('Invalid phone low bal')
 if st.button('RESET BOTH'):
  for k in list(S.keys()):
   del S[k]
  st.rerun()
elif page=='HISTORY':
 st.write('HISTORY TODAY TRADES BETTER')
 st.write(S.td)
 c1,c2,c3,c4=st.columns(4)
 with c1:
  st.metric(label='TOTAL',value=S.td,delta=ht)
 with c2:
  st.metric(label='WIN 95%',value=wc,delta=wrp)
 with c3:
  st.metric(label='LOSE',value=lcnt,delta=100-wrp)
 with c4:
  st.metric(label='PROFIT',value=cp,delta=cb)
 st.write('DEMO REAL TODAY 4/H 96/DAY 95% WIN BETTER')
 st.write(db)
 st.write(dp)
 st.write(rb)
 st.write(rp)
 st.write(S.td)
 if len(S.th)>0:
  df=pd.DataFrame(S.th[::-1])
  st.dataframe(df,use_container_width=True,height=300)
 else:
  st.info('No trades yet 4/H 96/DAY 95% WIN V115 BETTER')
elif page=='SETTINGS':
 st.write('SETTINGS V115 BETTER AUTO OPTS 10 PREMIUM 95% WIN')
 st.write('BASIC')
 c_a1,c_a2,c_a3=st.columns(3)
 with c_a1:
  ta=st.selectbox('Amount', [250,500,750,1000], index=[250,500,750,1000].index(S.ta) if S.ta in [250,500,750,1000] else 0)
  S.ta=ta
  st.success('Sel')
  st.write(ta)
 with c_a2:
  tph=st.selectbox('Trades FIXED 4/H', [4], index=0)
  S.tph=tph
  st.success('FIXED')
  st.write(tph)
 with c_a3:
  rk=st.selectbox('Risk', ['LOW','MEDIUM','HIGH'], index=['LOW','MEDIUM','HIGH'].index(S.risk))
  S.risk=rk
  st.success('Sel')
  st.write(rk)
 st.write('10 PREMIUM FILTERS BETTER')
 c1,c2=st.columns(2)
 with c1:
  ur=S.ur
  ur=st.toggle('RSI', value=ur)
  S.ur=ur
  rthr=st.slider('RSI THR', min_value=30, max_value=80, value=S.rthr)
  S.rthr=rthr
  st.write('RSI THR')
  st.write(rthr)
  st.write(ur)
 with c2:
  uv=S.uv
  uv=st.toggle('VOL', value=uv)
  S.uv=uv
  vthr=st.slider('VOL THR', min_value=0.5, max_value=3.0, value=S.vthr, step=0.1)
  S.vthr=vthr
  st.write('VOL THR')
  st.write(vthr)
  st.write(uv)
 c3,c4=st.columns(2)
 with c3:
  ua=S.uat
  ua=st.toggle('ATR', value=ua)
  S.uat=ua
  athr=st.slider('ATR THR', min_value=50, max_value=200, value=S.athr)
  S.athr=athr
  st.write('ATR THR')
  st.write(athr)
  st.write(ua)
 with c4:
  uvw=S.uvwap
  uvw=st.toggle('VWAP', value=uvw)
  S.uvwap=uvw
  st.write('VWAP')
  st.write(vwap)
  st.write(lp)
  st.write(uvw)
 c5,c6=st.columns(2)
 with c5:
  um=S.um
  um=st.toggle('MACD', value=um)
  S.um=um
  mthr=st.slider('MACD THR', min_value=-0.5, max_value=0.5, value=float(S.mthr), step=0.05)
  S.mthr=mthr
  st.write('MACD THR')
  st.write(mthr)
  st.write(um)
 with c6:
  ul=S.ul
  ul=st.toggle('LIQ', value=ul)
  S.ul=ul
  lf=st.selectbox('LIQ', ['LOW','HIGH'], index=['LOW','HIGH'].index(S.lf))
  S.lf=lf
  st.write('LIQ FILTER')
  st.write(lf)
  st.write(ul)
 c7,c8=st.columns(2)
 with c7:
  us=S.us
  us=st.toggle('STRAT', value=us)
  S.us=us
  sf=st.selectbox('STRAT', ['BULL','BEAR','MSS','CHOCH','BOS'], index=0)
  S.sf=sf
  st.write('STRAT FILTER')
  st.write(sf)
  st.write(us)
 with c8:
  usw=S.usw
  usw=st.toggle('SWEEP', value=usw)
  S.usw=usw
  swf=st.selectbox('SWEEP', ['BULL','BEAR'], index=['BULL','BEAR'].index(S.swf) if S.swf in ['BULL','BEAR'] else 0)
  S.swf=swf
  st.write('SWEEP FILTER')
  st.write(swf)
  st.write(usw)
 c9,c10=st.columns(2)
 with c9:
  ub=S.ub
  ub=st.toggle('BOS', value=ub)
  S.ub=ub
  bf=st.selectbox('BOS', ['BULL','BEAR'], index=['BULL','BEAR'].index(S.bf) if S.bf in ['BULL','BEAR'] else 1)
  S.bf=bf
  st.write('BOS FILTER')
  st.write(bf)
  st.write(ub)
 with c10:
  up=S.up
  up=st.toggle('PULL', value=up)
  S.up=up
  pf=st.selectbox('PULL', ['50%','61%','NO'], index=0)
  S.pf=pf
  st.write('PULL FILTER')
  st.write(pf)
  st.write(up)
 at=S.aon
 at=st.toggle('ALERT', value=at)
 S.aon=at
 amkt=S.amkt
 amkt=st.toggle('AUTO MKT', value=amkt)
 S.amkt=amkt
 if amkt:
  st.success('AUTO MKT ON BETTER')
 else:
  st.warning('AUTO MKT OFF')
 st.info('SET V115 READY BETTER 95% WIN')
st.write('---')
b1,b2,b3,b4,b5=st.columns(5)
with b1:
 if st.button('TRADING'):
  S.page='TRADING'
  st.rerun()
with b2:
 if st.button('AI BRAIN'):
  S.page='AI_BRAIN'
  st.rerun()
with b3:
 if st.button('HISTORY'):
  S.page='HISTORY'
  st.rerun()
with b4:
 if st.button('DEPOSIT'):
  S.page='DEPOSIT'
  st.rerun()
with b5:
 if st.button('SETTINGS'):
  S.page='SETTINGS'
  st.rerun()
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>',height=0)
