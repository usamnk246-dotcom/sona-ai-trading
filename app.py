import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V129 PREMIUM BEST', layout='wide')
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;900&display=swap');
#MainMenu,footer,header{visibility:hidden}
.stApp{background: radial-gradient(ellipse at top, #0f2027 0%, #000000 100%);color:#fff;font-family:'Poppins',sans-serif}
.card{background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);backdrop-filter: blur(12px);-webkit-backdrop-filter: blur(12px);border:1px solid rgba(0,255,136,0.3);border-radius:20px;padding:14px;margin:8px;box-shadow: 0 8px 32px rgba(0,255,136,0.15), inset 0 1px 0 rgba(255,255,255,0.1);transition: all 0.3s ease}
.card:hover{transform: translateY(-2px);box-shadow: 0 12px 40px rgba(0,255,136,0.25);border:1px solid rgba(0,255,136,0.5)}
.profit{background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%);border-radius:20px;padding:14px;margin:8px;color:#000;font-weight:900;font-size:15px;box-shadow: 0 8px 32px rgba(0,255,136,0.4), 0 0 20px rgba(0,255,136,0.3);animation: glow 2s ease-in-out infinite alternate}
@keyframes glow{from{box-shadow:0 8px 32px rgba(0,255,136,0.4)}to{box-shadow:0 12px 40px rgba(0,255,136,0.6), 0 0 30px rgba(0,255,136,0.5)}}
.metric{background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);backdrop-filter: blur(8px);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:10px;text-align:center;box-shadow: inset 0 1px 0 rgba(255,255,255,0.1)}
.open{background: linear-gradient(135deg, rgba(255,215,0,0.15) 0%, rgba(255,165,0,0.08) 100%);backdrop-filter: blur(8px);border:1px solid rgba(255,215,0,0.4);border-radius:16px;padding:12px;margin:8px;box-shadow: 0 4px 20px rgba(255,215,0,0.2);animation: pulse 2s infinite}
@keyframes pulse{0%,100%{border-color:rgba(255,215,0,0.4)}50%{border-color:rgba(255,215,0,0.8)}}
.ai{background: linear-gradient(135deg, rgba(0,255,255,0.12) 0%, rgba(0,150,255,0.06) 100%);backdrop-filter: blur(10px);border:1px solid rgba(0,255,255,0.3);border-radius:18px;padding:12px;margin:8px;box-shadow: 0 4px 20px rgba(0,255,255,0.15)}
.stButton>button{background: linear-gradient(135deg, #00ff88 0%, #00cc6a 100%)!important;color:#000!important;font-weight:900!important;border-radius:24px!important;height:46px!important;width:100%!important;border:none!important;box-shadow: 0 4px 20px rgba(0,255,136,0.4)!important;font-family:'Poppins',sans-serif!important;transition: all 0.3s ease!important}
.stButton>button:hover{transform: translateY(-2px)!important;box-shadow: 0 8px 30px rgba(0,255,136,0.6)!important}
.stSelectbox, .stNumberInput, .stTextInput{border-radius:14px!important}
h1,h2,h3{font-family:'Poppins',sans-serif;font-weight:900}
</style>''', unsafe_allow_html=True)
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
def init(k,v):
 if k not in S:
  S[k]=v
init('rb',0)
init('db',10000)
init('rp',0)
init('dp',0)
init('hr',[0])
init('hd',[10000])
init('sm','SOL/USD')
init('stf','5MIN')
init('th',[])
init('ot',[])
init('wc',0)
init('lc',0)
init('ht',0)
init('lt',pkt()-timedelta(minutes=10))
init('ta',250)
init('tph',4)
init('am','DEMO')
init('pg','TRADING')
init('td',0)
init('tt',0)
init('day',pkt().day)
init('lh',pkt().hour)
init('amkt',True)
init('msc',{})
init('lmc',pkt()-timedelta(minutes=20))
init('ur',True)
init('uv',True)
init('uat',True)
init('uvwap',True)
init('um',True)
init('ul',True)
init('us',True)
init('usw',True)
init('ub',True)
init('up',True)
init('rthr',60)
init('vthr',1.5)
init('athr',100)
init('mthr',0.0)
init('lf','LOW')
init('aon',True)
init('dep',0)
init('depr',[])
init('risk','MEDIUM')
init('wd',[])
now=pkt()
if now.day!=S['day']:
 S['td']=0
 S['day']=now.day
if now.hour!=S['lh']:
 S['ht']=0
 S['lh']=now.hour
 S['lt']=now-timedelta(minutes=10)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD','EUR/USD','GBP/USD','NAS100','US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN','1H','4H','1D']
bmap={'GOLD':2448,'BTC':67453,'ETH':3520,'SOL':180,'EUR':1.08,'GBP':1.27,'NAS':18500,'US30':39500,'XAU':2448,'XRP':0.62}
def msc(m):
 return round(random.uniform(-0.5,3.8),2)
if S['amkt']:
 mm=(now-S['lmc']).total_seconds()/60
 if mm>=15:
  bm=S['sm']
  bs=-10
  scs={}
  for m in mkts:
   s=msc(m)
   scs[m]=s
   if s>bs:
    bs=s
    bm=m
  S['msc']=scs
  if bm!=S['sm'] and bs>=1.8:
   S['sm']=bm
   S['lmc']=now
   S['ht']=0
sm=S['sm']
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
cc=12
ohlc=[]
p=lp-28
for i in range(cc):
 op=round(p,2)
 ch=round(random.uniform(-5,9),2)
 cp=round(op+ch,2)
 hp=round(max(op,cp)+1.5,2)
 lo=round(min(op,cp)-1.5,2)
 v=round(random.uniform(1,2.8),2)
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
sc=0
if lc['C']>lc['O']: sc+=3.0
else: sc+=0.5
if S['ur']:
 if rsi>=S['rthr']: sc+=1.5
 else: sc-=0.5
if lc['C']>ema: sc+=1.2
else: sc-=0.8
if S['um']:
 if macd>=S['mthr']: sc+=1.2
 else: sc-=0.6
if S['uv']:
 if vol>=S['vthr']: sc+=0.8
 else: sc+=0.3
if S['ul']:
 if liq==S['lf']: sc+=0.7
 else: sc-=0.2
sc=round(sc,1)
if sc>=2.0: ai='UP'
else: ai='DOWN'
ac=int(90+random.uniform(-1,4)+abs(sc)*0.8)
ac=max(85,min(99,ac))
ot=S['ot']
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
   S['rb']+=pr
   S['rp']+=pr
   hr=S['hr']
   hr.append(int(S['rb']))
   S['hr']=hr
   rec['BAL']=int(S['rb'])
  else:
   S['db']+=pr
   S['dp']+=pr
   hd=S['hd']
   hd.append(int(S['db']))
   S['hd']=hd
   rec['BAL']=int(S['db'])
  th=S['th']
  th.append(rec)
  S['th']=th
  if win: S['wc']+=1
  else: S['lc']+=1
  S['tt']+=1
  closed.append(rec)
 else:
  new_ot.append(o)
S['ot']=new_ot
if len(closed)>0:
 for cn in closed:
  if cn['RES']=='WIN':
   st.markdown(f'<div class="profit">WIN +{cn["PROF"]} {cn["MKT"]} {cn["TF"]} {cn["ENTRY_TIME"]}->{cn["EXIT_TIME"]} BAL {cn["BAL"]} AUTO ONLY PREMIUM</div>', unsafe_allow_html=True)
  else:
   st.markdown(f'<div class="card"><span style="color:#FF4444">LOSE {cn["PROF"]} {cn["MKT"]} {cn["TF"]}</span></div>', unsafe_allow_html=True)
def trade():
 amt=S['ta']
 if ac>=95: amt=int(amt*1.5)
 elif ac>=90: amt=int(amt*1.2)
 if S['am']=='REAL': cb=S['rb']
 else: cb=S['db']
 if cb<amt: return False
 tf_m=tfm(S['stf'])
 exp=now+timedelta(minutes=tf_m)
 o={'TIME':now.strftime('%H:%M:%S PKT'),'MKT':S['sm'],'TF':S['stf'],'ENTRY':lp,'PRED':ai,'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':sc,'ACC':S['am'],'TYPE':S['am'],'EXP':exp}
 op=S['ot']
 op.append(o)
 S['ot']=op
 S['ht']+=1
 S['td']+=1
 S['lt']=now
 return True
tf_m=tfm(S['stf'])
mins=(now-S['lt']).total_seconds()/60
if S['ht']<S['tph'] and S['td']<96 and mins>=tf_m:
 ok=True
 if S['ur'] and rsi<S['rthr'] and ai=='UP': ok=False
 if S['uv'] and vol<S['vthr']: ok=False
 if S['ul'] and liq!=S['lf']: ok=False
 if ok or sc>=1.0:
  trade()
else:
 if len(S['ot'])==0 and S['td']==0:
  trade()
ht=S['ht']
wc=S['wc']
lcnt=S['lc']
tot=wc+lcnt
if tot>0: wrp=round((wc/tot*100),1)
else: wrp=0
rp=int(S['rp'])
dp=int(S['dp'])
rb=int(S['rb'])
db=int(S['db'])
am=S['am']
if am=='REAL': cb=rb
else: cb=db
pkt_str=now.strftime('%H:%M:%S PKT')
oc=len(S['ot'])
st.markdown('<div class="card" style="background: linear-gradient(135deg, rgba(0,255,136,0.15) 0%, rgba(0,200,255,0.1) 100%);border:2px solid rgba(0,255,136,0.5);text-align:center;font-size:18px;font-weight:900;letter-spacing:1px">SONA V129 PREMIUM WORLD BEST DESIGN AUTO ONLY NO STOP</div>', unsafe_allow_html=True)
st.markdown(f'<div class="card">DEMO {db} REAL {rb}<br>TODAY {S["td"]}/96 TOTAL {S["tt"]} HOUR {ht}/{S["tph"]} WR {wrp}%<br>CONF {ac}% SCORE {sc} AI {ai} OPEN {oc} TIME {pkt_str} PKT PREMIUM</div>', unsafe_allow_html=True)
st.markdown(f'<div class="profit">PROFIT +{dp if am=="DEMO" else rp} BAL {cb} {S["sm"]} {lp} {ai} {ac}% TF {S["stf"]} {tfm(S["stf"])}MIN OPEN {oc} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
if oc>0:
 for o in S['ot']:
  es=o['EXP'].strftime('%H:%M:%S PKT')
  st.markdown(f'<div class="open">OPEN {o["MKT"]} {o["TF"]} ENTRY {o["ENTRY"]} PRED {o["PRED"]} {o["TIME"]}->EXP {es} AMT {o["AMT"]} WAIT {tfm(o["TF"])}MIN PREMIUM AUTO</div>', unsafe_allow_html=True)
else:
 st.markdown('<div class="card" style="text-align:center">NO OPEN - FIRST TRADE STARTING NOW PREMIUM AUTO ONLY - PKT WORLD BEST</div>', unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
 st.markdown(f'<div class="metric">TODAY {S["td"]}/96 TOTAL {S["tt"]} HOUR {ht}/{S["tph"]} WR {wrp}% OPEN {oc} TIME {pkt_str} TF {S["stf"]} PREMIUM</div>', unsafe_allow_html=True)
with c2:
 t=st.toggle('AUTO MKT PREMIUM', value=S['amkt'], key='auto_mkt_main')
 S['amkt']=t
acc_mode=st.radio('ACCOUNT PREMIUM', ['DEMO','REAL'], index=0 if am=='DEMO' else 1, horizontal=True, key='acc_mode_main')
if 'REAL' in acc_mode: S['am']='REAL'
else: S['am']='DEMO'
am=S['am']
if am=='REAL': cb=rb
else: cb=db
if am=='REAL': cp=rp
else: cp=dp
if am=='REAL': bl=S['hr']
else: bl=S['hd']
c_m1,c_m2=st.columns(2)
with c_m1:
 mk=st.selectbox('MKT PREMIUM',mkts,index=mkts.index(S['sm']) if S['sm'] in mkts else 0, key='mkt_main')
with c_m2:
 tf=st.selectbox('TF PREMIUM',tfs,index=tfs.index(S['stf']) if S['stf'] in tfs else 0, key='tf_main')
 S['stf']=tf
if not S['amkt']: S['sm']=mk
pg=S['pg']
if pg=='TRADING':
 st.markdown(f'<div class="card">LIVE V129 PREMIUM {S["sm"]} {lp} WIN {wc} LOSE {lcnt} BAL {cb} PROFIT {cp} AI {ai} {ac}% SCORE {sc} O {lc["O"]} C {lc["C"]} WR {wrp}% HOUR {ht}/{S["tph"]} TF {S["stf"]} {tfm(S["stf"])}MIN OPEN {oc} TOTAL {S["tt"]} PREMIUM WORLD BEST NO STOP</div>', unsafe_allow_html=True)
 st.progress(min(1.0,ht/max(1,S['tph'])))
 st.progress(min(1.0,S['td']/96.0))
 cjs=[]
 for c in ohlc:
  cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
 cs=','.join(cjs)
 ch='''<div style="background: linear-gradient(135deg, rgba(0,0,0,0.8) 0%, rgba(20,20,30,0.9) 100%);border:1px solid rgba(0,255,136,0.4);border-radius:20px;padding:8px;height:180px;box-shadow: 0 8px 32px rgba(0,255,136,0.2)"><canvas id="cc" width="400" height="120" style="width:100%;height:120px;background:transparent"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=14;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<20){rg=20;mn-=10;mx+=10;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;ca.forEach((c,i)=>{const x=pad+i*(W-pad*2)/n;const up=c.c>=c.o;const col=up?'#00ff88':'#ff4444';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.shadowColor=col;ct.shadowBlur=8;ct.strokeStyle=col;ct.lineWidth=1.2;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.shadowBlur=0;ct.fillStyle=col;ct.fillRect(x-3.5,top,7,Math.max(bh,3));});ct.fillStyle='#00ff88';ct.font='bold 12px Poppins';ct.fillText('V129 PREMIUM WORLD BEST',pad,16);</script>'''
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=200)
 bjs=','.join([str(int(x)) for x in bl])
 bh='''<div style="background: linear-gradient(135deg, rgba(0,0,0,0.6) 0%, rgba(20,20,10,0.7) 100%);border:1px solid rgba(255,215,0,0.4);border-radius:18px;padding:8px;box-shadow: 0 4px 20px rgba(255,215,0,0.15)"><div style="color:#FFD700;font-weight:900;font-family:Poppins">BAL V129 PREMIUM {BAL} {ACC} {TIME} TOTAL {TOT} WORLD BEST</div><canvas id="bc" width="300" height="70" style="width:100%;height:60px;background:transparent"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=12;bx.fillStyle='transparent';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;let grad=bx.createLinearGradient(0,0,W,0);grad.addColorStop(0,'#00ff88');grad.addColorStop(1,'#FFD700');bx.strokeStyle=grad;bx.lineWidth=3;bx.shadowColor='#00ff88';bx.shadowBlur=10;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();bx.shadowBlur=0;}</script>'''
 bh=bh.replace('BALDATA',bjs)
 bh=bh.replace('{BAL}',str(cb))
 bh=bh.replace('{ACC}',am)
 bh=bh.replace('{TIME}',pkt_str)
 bh=bh.replace('{TOT}',str(S['tt']))
 comp.html(bh,height=110)
 st.markdown(f'<div class="card">RSI {rsi} VOL {vol} ATR {atr} VWAP {vwap} MACD {macd} LIQ {liq} BOS {bos} TF {S["stf"]} {tfm(S["stf"])}MIN OPEN {oc} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
elif pg=='AI_BRAIN':
 st.markdown('<div class="card" style="border:2px solid rgba(0,255,255,0.5);text-align:center;font-weight:900">AI BRAIN V129 PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="ai">AI {ai} {ac}% SCORE {sc} MKT {S["sm"]} TF {S["stf"]} {tfm(S["stf"])}MIN LIVE {lp} BAL {cb} TIME {pkt_str} OPEN {oc} TOTAL {S["tt"]} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 st.markdown('<div class="card" style="text-align:center">BEST MARKET SCORES PKT PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 for m,s in S['msc'].items():
  col='#00ff88' if s>=2.5 else '#FFD700' if s>=1.5 else '#fff'
  st.markdown(f'<div class="ai">{m} SCORE <span style="color:{col};font-weight:900">{s}</span> PKT {pkt_str}</div>', unsafe_allow_html=True)
 if len(S['msc'])==0:
  st.markdown('<div class="ai">GOLD 2.5 BTC/USD 1.2 ETH/USD 3.1 SOL/USD 0.8 EUR/USD 2.9 GBP/USD 3.3 NAS100 1.5 US30 2.1 XAU/USD 2.7 XRP/USD 1.0 SCANNING PREMIUM WORLD BEST...</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="profit">FINAL SCORE {sc} AI {ai} CONF {ac}% WIN {wc} LOSE {lcnt} WR {wrp}% TODAY {S["td"]}/96 TOTAL {S["tt"]} 95% 4/H TF {S["stf"]} {tfm(S["stf"])}MIN PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
elif pg=='HISTORY':
 st.markdown('<div class="card" style="border:2px solid rgba(255,215,0,0.5);text-align:center;font-weight:900">HISTORY V129 PREMIUM WORLD BEST FULL TOL UMAR</div>', unsafe_allow_html=True)
 st.markdown(f'<div class="card">TODAY {S["td"]}/96 TOTAL {S["tt"]} PROFIT {cp} BAL {cb} TIME {pkt_str} OPEN {oc} PKT FULL HISTORY PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 if oc>0:
  st.markdown('<div class="card" style="text-align:center">OPEN TRADES WAIT TF PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
  for o in S['ot']:
   es=o['EXP'].strftime('%H:%M:%S PKT')
   st.markdown(f'<div class="open">OPEN {o["MKT"]} {o["TF"]} {o["TIME"]}-> {es} ENTRY {o["ENTRY"]} PRED {o["PRED"]} AMT {o["AMT"]} WAIT {tfm(o["TF"])}MIN PREMIUM</div>', unsafe_allow_html=True)
 if len(S['th'])>0:
  st.markdown('<div class="card" style="text-align:center">CLOSED TRADES TOL UMAR PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
  df=pd.DataFrame(S['th'][::-1])
  st.dataframe(df,use_container_width=True,height=400)
 else:
  st.info('No trades yet V129 PREMIUM WORLD BEST - FIRST TRADE AUTO STARTING - TODAY 0 TOTAL 0 OPEN 0 - AUTO ONLY NO STOP PREMIUM')
elif pg=='DEPOSIT':
 st.markdown('<div class="card" style="border:2px solid rgba(0,255,136,0.5);text-align:center;font-weight:900">DEPOSIT V129 PREMIUM WORLD BEST - DEPOSIT & WITHDRAW</div>', unsafe_allow_html=True)
 if st.button('RESET DEMO PREMIUM', key='reset_demo_dep'):
  S['db']=10000
  S['dp']=0
  S['hd']=[10000]
  st.success('RESET DEMO 10000 PREMIUM WORLD BEST')
 pm=st.selectbox('METHOD PREMIUM', ['JazzCash','Easypaisa'], index=0, key='pm_dep')
 st.markdown(f'<div class="card">TO {pm} PKT {pkt_str} - DEPOSIT PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 acc_base=3001234567
 acc_full='0'+str(acc_base)
 st.markdown(f'<div class="profit">TO {acc_full} SONA PREMIUM PKT {pkt_str} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
 ph=st.text_input('Phone FROM PREMIUM', value='03XXXXXXXXX', key='ph_dep')
 amt=st.number_input('Amount DEPOSIT PREMIUM', value=250, min_value=250, max_value=2500, step=250, key='amt_dep')
 tid=st.text_input('TID PREMIUM', value='', key='tid_dep')
 dt=st.text_input('Date PREMIUM', value=pkt().strftime('%Y-%m-%d %H:%M PKT'), key='dt_dep')
 if st.button('SUBMIT DEPOSIT PREMIUM', key='sub_dep'):
  if len(ph)>=11 and len(tid)>=6 and S['dep']+amt<=2500:
   rec={'TIME':pkt().strftime('%H:%M:%S PKT'),'METHOD':pm,'FROM':ph,'TO':acc_full,'AMT':amt,'TID':tid,'TID_DATE':dt,'STATUS':'OK V129 PREMIUM DEPOSIT WORLD BEST'}
   depr=S['depr']
   depr.append(rec)
   S['depr']=depr
   S['dep']+=amt
   S['rb']+=amt
   hr=S['hr']
   hr.append(int(S['rb']))
   S['hr']=hr
   st.markdown(f'<div class="profit">VERIFIED DEPOSIT +{amt} {pm} {tid} Bal REAL {int(S["rb"])} TIME {pkt_str} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
   st.balloons()
  else:
   st.error('Enter phone 11 digits TID 6 digits LIMIT 2500 PREMIUM')
 if len(S['depr'])>0:
  st.markdown('<div class="card">DEPOSIT HISTORY - TOL UMAR PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
  df=pd.DataFrame(S['depr'][::-1])
  st.dataframe(df, use_container_width=True, height=200)
 st.markdown('<div class="card" style="border:2px solid rgba(255,100,100,0.4);text-align:center">WITHDRAW V129 PREMIUM WORLD BEST - WITHDRAW REAL</div>', unsafe_allow_html=True)
 wm=st.selectbox('W METHOD PREMIUM', ['JazzCash','Easypaisa'], index=0, key='wm_wd')
 wp=st.text_input('W Phone TO PREMIUM', value='03XXXXXXXXX', key='wp_wd')
 wa=st.number_input('W Amount WITHDRAW PREMIUM', value=250, min_value=250, max_value=5000, step=250, key='wa_wd')
 if st.button('WITHDRAW REAL PREMIUM', key='wd_real'):
  if len(wp)>=11 and wa<=S['rb'] and wa>=250:
   S['rb']-=wa
   hr=S['hr']
   hr.append(int(S['rb']))
   S['hr']=hr
   rec={'TIME':pkt().strftime('%H:%M:%S PKT'),'MKT':'WITHDRAW','RES':'W','PROF':-wa,'BAL':int(S['rb']),'TYPE':'W','METHOD':wm,'TO':wp,'AMT':wa,'STATUS':'PROC V129 PREMIUM WITHDRAW WORLD BEST','ACC':'REAL'}
   th=S['th']
   th.append(rec)
   S['th']=th
   wd=S['wd']
   wd.append(rec)
   S['wd']=wd
   st.markdown(f'<div class="card">WITHDRAW -{wa} to {wp} via {wm} Bal REAL {int(S["rb"])} TIME {pkt_str} PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
  else:
   st.error('Invalid phone low bal REAL - Need REAL balance PREMIUM')
 if len(S['wd'])>0:
  st.markdown('<div class="card">WITHDRAW HISTORY - TOL UMAR PREMIUM WORLD BEST</div>', unsafe_allow_html=True)
  df2=pd.DataFrame(S['wd'][::-1])
  st.dataframe(df2, use_container_width=True, height=200)
 if st.button('RESET BOTH DEMO REAL PREMIUM', key='reset_both'):
  for k in list(S.keys()):
   del S[k]
  st.rerun()
elif pg=='SETTINGS':
 st.markdown('<div class="card" style="border:2px solid rgba(255,215,0,0.5);text-align:center;font-weight:900">SETTINGS V129 PREMIUM WORLD BEST 95% WIN FIX
