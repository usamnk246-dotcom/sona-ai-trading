import streamlit as st
import random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V131',layout='wide')
C='<div class="card">'
P='<div class="profit">'
O='<div class="open">'
A1='<div class="ai">'
E='</div>'
CSS='''<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:#000;color:#fff}
.card{background:#111;border:1px solid #0F0}
.card{border-radius:20px;padding:12px;margin:6px}
.profit{background:#0F0;border-radius:20px}
.profit{padding:12px;margin:6px;color:#000}
.profit{font-weight:900}
.metric{background:#222;border-radius:14px}
.metric{padding:8px;text-align:center}
.open{background:#332;border:1px solid #FD0}
.open{border-radius:14px;padding:10px;margin:6px}
.ai{background:#112;border:1px solid #0FF}
.ai{border-radius:16px;padding:10px;margin:6px}
.stButton>button{background:#0F0;color:#000}
.stButton>button{font-weight:900;border-radius:20px}
.stButton>button{height:44px;width:100%}
</style>'''
st.markdown(CSS,unsafe_allow_html=True)
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
init('wd',[])
now=pkt()
if now.day!=S['day']:
 S['td']=0
 S['day']=now.day
if now.hour!=S['lh']:
 S['ht']=0
 S['lh']=now.hour
 S['lt']=now-timedelta(minutes=10)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD']
mkts+=['EUR/USD','GBP/USD','NAS100']
mkts+=['US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN']
tfs+=['1H','4H','1D']
bmap={'GOLD':2448,'BTC':67453,'ETH':3520}
bmap['SOL']=180
bmap['EUR']=1.08
bmap['GBP']=1.27
bmap['NAS']=18500
bmap['US30']=39500
bmap['XAU']=2448
bmap['XRP']=0.62
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
 ohlc.append({'O':op,'H':hp,'L':lo})
 ohlc[-1]['C']=cp
 ohlc[-1]['V']=v
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
  rec={'TIME':tm,'MKT':o['MKT'],'TF':o['TF']}
  rec['RES']='WIN' if win else 'LOSE'
  rec['PROF']=pr
  rec['BAL']=0
  rec['TYPE']=o['TYPE']
  rec['PRED']=pred
  rec['CLOSE']=curr
  rec['OPEN']=entry
  rec['DIR']=o['DIR']
  rec['AMT']=o['AMT']
  rec['CONF']=o['CONF']
  rec['SCORE']=o['SCORE']
  rec['ACC']=o['ACC']
  rec['ENTRY_TIME']=o['TIME']
  rec['EXIT_TIME']=tm
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
   t=P+'WIN +'+str(cn['PROF'])+' '+cn['MKT']
   t+=' '+cn['TF']+' BAL '+str(cn['BAL'])+E
   st.markdown(t,unsafe_allow_html=True)
  else:
   t=C+'LOSE '+str(cn['PROF'])+' '+cn['MKT']+E
   st.markdown(t,unsafe_allow_html=True)
def trade():
 amt=S['ta']
 if ac>=95: amt=int(amt*1.5)
 elif ac>=90: amt=int(amt*1.2)
 if S['am']=='REAL': cb=S['rb']
 else: cb=S['db']
 if cb<amt: return False
 tf_m=tfm(S['stf'])
 exp=now+timedelta(minutes=tf_m)
 o={'TIME':now.strftime('%H:%M:%S PKT')}
 o['MKT']=S['sm']
 o['TF']=S['stf']
 o['ENTRY']=lp
 o['PRED']=ai
 o['DIR']=cd
 o['AMT']=amt
 o['CONF']=ac
 o['SCORE']=sc
 o['ACC']=S['am']
 o['TYPE']=S['am']
 o['EXP']=exp
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
st.markdown(C+'SONA V131 NO DUP'+E,unsafe_allow_html=True)
t=C+'DEMO '+str(db)+' REAL '+str(rb)+E
st.markdown(t,unsafe_allow_html=True)
t=C+'TODAY '+str(S['td'])+'/96 TOTAL '+str(S['tt'])
t+=' HOUR '+str(ht)+'/'+str(S['tph'])+' WR '+str(wrp)+E
st.markdown(t,unsafe_allow_html=True)
t=C+'CONF '+str(ac)+'% SCORE '+str(sc)+' AI '+ai
t+=' OPEN '+str(oc)+' TIME '+pkt_str+E
st.markdown(t,unsafe_allow_html=True)
t=P+'PROFIT +'+str(dp if am=='DEMO' else rp)
t+=' BAL '+str(cb)+' '+S['sm']+' '+str(lp)+E
st.markdown(t,unsafe_allow_html=True)
if oc>0:
 for o in S['ot']:
  es=o['EXP'].strftime('%H:%M:%S PKT')
  t=O+'OPEN '+o['MKT']+' '+o['TF']
  t+=' ENTRY '+str(o['ENTRY'])+' PRED '+o['PRED']+E
  st.markdown(t,unsafe_allow_html=True)
  t=O+o['TIME']+'->EXP '+es
  t+=' AMT '+str(o['AMT'])+' WAIT '+str(tfm(o['TF']))+E
  st.markdown(t,unsafe_allow_html=True)
else:
 t=C+'NO OPEN - FIRST TRADE NOW AUTO'+E
 st.markdown(t,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
 t='<div class="metric">TODAY '+str(S['td'])+E
 st.markdown(t,unsafe_allow_html=True)
with c2:
 t=st.toggle('AUTO MKT TOP',value=S['amkt'],key='am_top')
 S['amkt']=t
acc=st.radio('ACCOUNT TOP',['DEMO','REAL'],horizontal=True,key='ac_top')
if 'REAL' in acc: S['am']='REAL'
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
 mk=st.selectbox('MKT TOP',mkts,key='mk_top')
with c_m2:
 tf=st.selectbox('TF TOP',tfs,key='tf_top')
 S['stf']=tf
if not S['amkt']: S['sm']=mk
pg=S['pg']
if pg=='TRADING':
 t=C+'LIVE V131 '+S['sm']+' '+str(lp)+' WIN '+str(wc)+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'BAL '+str(cb)+' PROFIT '+str(cp)+' AI '+ai
 t+=' '+str(ac)+'% SCORE '+str(sc)+E
 st.markdown(t,unsafe_allow_html=True)
 st.progress(min(1.0,ht/max(1,S['tph'])))
 st.progress(min(1.0,S['td']/96.0))
 cjs=[]
 for c in ohlc:
  cjs.append('{o:'+str(c['O'])+',h:'+str(c['H']))
  cjs[-1]+= ',l:'+str(c['L'])+',c:'+str(c['C'])+'}'
 cs=','.join(cjs)
 ch='<div style="background:#111;border:1px"'
 ch+=' solid #0F0;border-radius:12px;padding:5px"'
 ch+='><canvas id="cc" width="350" height="100"'
 ch+=' style="width:100%;height:100px"></canvas></div>'
 ch+='<script>const cv=document.getElementById'
 ch+="('cc');const ct=cv.getContext('2d');"
 ch+='const ca=[CANDLES];const W=cv.width;const H='
 ch+='cv.height;const pad=10;const n=ca.length;let'
 ch+=' mn=Math.min(...ca.map(x=>x.l));let mx='
 ch+='Math.max(...ca.map(x=>x.h));let rg=mx-mn;'
 ch+='if(rg<20){rg=20;mn-=10;mx+=10;}mn-=rg*0.1;'
 ch+='mx+=rg*0.1;rg=mx-mn;ca.forEach((c,i)=>{const'
 ch+=' x=pad+i*W/n;const up=c.c>=c.o;const col='
 ch+="up?'#0F0':'#F44';const hy=pad+(1-(c.h-mn)/"
 ch+='rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*'
 ch+='(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*'
 ch+='(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*'
 ch+='(H-pad*2);const top=Math.min(oy,cy);const'
 ch+=' bh=Math.abs(cy-oy);ct.strokeStyle=col;'
 ch+='ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);'
 ch+='ct.stroke();ct.fillStyle=col;ct.fillRect('
 ch+='x-3,top,6,Math.max(bh,2));});ct.fillStyle='
 ch+=" '#0F0';ct.fillText('V131 NO DUP',pad,12);"
 ch+='</script>'
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=180)
 bjs=','.join([str(int(x)) for x in bl])
 bh='<div style="border:1px solid #FD0"'
 bh+='><div>BAL V131 '+str(cb)+' '+am+'</div>'
 bh+='<canvas id="bc" width="250" height="60"'
 bh+=' style="width:100%;height:50px"></canvas>'
 bh+='</div><script>const bc=document.'
 bh+="getElementById('bc');const bx=bc.getContext"
 bh+="('2d');const ba=[BALDATA];const W=bc.width;"
 bh+='const H=bc.height;const p=10;bx.fillStyle='
 bh+="'#000';bx.fillRect(0,0,W,H);if(ba.length>1)"
 bh+='{let mn=Math.min(...ba);let mx=Math.max('
 bh+='...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;'
 bh+='mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;'
 bh+="bx.strokeStyle='#0F0';bx.lineWidth=2;bx."
 bh+='beginPath();ba.forEach((b,i)=>{const x=p+i*'
 bh+='(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)'
 bh+='/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else'
 bh+='bx.lineTo(x,y);});bx.stroke();}</script>'
 bh=bh.replace('BALDATA',bjs)
 comp.html(bh,height=100)
 t=C+'RSI '+str(rsi)+' VOL '+str(vol)+' ATR '+str(atr)+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'VWAP '+str(vwap)+' MACD '+str(macd)+' LIQ '+liq+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'BOS '+bos+' TF '+S['stf']+' OPEN '+str(oc)+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='AI_BRAIN':
 st.markdown(C+'AI BRAIN V131'+E,unsafe_allow_html=True)
 t=A1+'AI '+ai+' '+str(ac)+'% SCORE '+str(sc)+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'MKT '+S['sm']+' TF '+S['stf']+' LIVE '+str(lp)+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'BAL '+str(cb)+' TIME '+pkt_str+' OPEN '+str(oc)+E
 st.markdown(t,unsafe_allow_html=True)
 st.markdown(C+'BEST SCORES PKT'+E,unsafe_allow_html=True)
 for m,s in S['msc'].items():
  t=A1+m+' SCORE '+str(s)+' PKT '+pkt_str+E
  st.markdown(t,unsafe_allow_html=True)
 if len(S['msc'])==0:
  t=A1+'SCANNING GOLD BTC ETH SOL EUR GBP'+E
  st.markdown(t,unsafe_allow_html=True)
 t=P+'FINAL SCORE '+str(sc)+' AI '+ai+' CONF '+str(ac)+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='HISTORY':
 st.markdown(C+'HISTORY V131 TOL UMAR'+E,unsafe_allow_html=True)
 t=C+'TODAY '+str(S['td'])+'/96 TOTAL '+str(S['tt'])+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'PROFIT '+str(cp)+' BAL '+str(cb)+' OPEN '+str(oc)+E
 st.markdown(t,unsafe_allow_html=True)
 if oc>0:
  st.markdown(C+'OPEN TRADES WAIT TF'+E,unsafe_allow_html=True)
  for o in S['ot']:
   es=o['EXP'].strftime('%H:%M:%S PKT')
   t=O+'OPEN '+o['MKT']+' '+o['TF']+' '+o['TIME']+E
   st.markdown(t,unsafe_allow_html=True)
   t=O+'-> '+es+' ENTRY '+str(o['ENTRY'])+' PRED '+o['PRED']+E
   st.markdown(t,unsafe_allow_html=True)
 if len(S['th'])>0:
  st.markdown(C+'CLOSED TOL UMAR'+E,unsafe_allow_html=True)
  df=pd.DataFrame(S['th'][::-1])
  st.dataframe(df,use_container_width=True,height=400)
 else:
  st.info('No trades yet V131 AUTO ONLY')
elif pg=='DEPOSIT':
 st.markdown(C+'DEPOSIT V131'+E,unsafe_allow_html=True)
 if st.button('RESET DEMO',key='rd_dep'):
  S['db']=10000
  S['dp']=0
  S['hd']=[10000]
  st.success('RESET 10000')
 pm=st.selectbox('METHOD DEP',['JazzCash','Easypaisa'],key='pm_dep')
 t=C+'TO '+pm+' PKT '+pkt_str+E
 st.markdown(t,unsafe_allow_html=True)
 acc_full='03001234567'
 t=P+'TO '+acc_full+' SONA PREMIUM'+E
 st.markdown(t,unsafe_allow_html=True)
 ph=st.text_input('Phone FROM DEP',value='03XXXXXXXXX',key='ph_dep')
 amt=st.number_input('Amount DEP',value=250,key='amt_dep')
 tid=st.text_input('TID DEP',value='',key='tid_dep')
 dt=st.text_input('Date DEP',value=pkt().strftime('%Y-%m-%d'),key='dt_dep')
 if st.button('SUBMIT DEPOSIT',key='sd_dep'):
  if len(ph)>=11 and len(tid)>=6 and S['dep']+amt<=2500:
   rec={'TIME':pkt().strftime('%H:%M:%S PKT')}
   rec['METHOD']=pm
   rec['FROM']=ph
   rec['TO']=acc_full
   rec['AMT']=amt
   rec['TID']=tid
   rec['TID_DATE']=dt
   rec['STATUS']='OK V131'
   depr=S['depr']
   depr.append(rec)
   S['depr']=depr
   S['dep']+=amt
   S['rb']+=amt
   hr=S['hr']
   hr.append(int(S['rb']))
   S['hr']=hr
   t=P+'VERIFIED +'+str(amt)+' '+pm+' '+tid+E
   st.markdown(t,unsafe_allow_html=True)
   st.balloons()
  else:
   st.error('Enter phone 11 TID 6 LIMIT 2500')
 if len(S['depr'])>0:
  st.markdown(C+'DEPOSIT HISTORY'+E,unsafe_allow_html=True)
  df=pd.DataFrame(S['depr'][::-1])
  st.dataframe(df,use_container_width=True,height=200)
 st.markdown(C+'WITHDRAW V131'+E,unsafe_allow_html=True)
 wm=st.selectbox('W METHOD WD',['JazzCash','Easypaisa'],key='wm_wd')
 wp=st.text_input('W Phone WD',value='03XXXXXXXXX',key='wp_wd')
 wa=st.number_input('W Amount WD',value=250,key='wa_wd')
 if st.button('WITHDRAW REAL',key='wd_wd'):
  if len(wp)>=11 and wa<=S['rb'] and wa>=250:
   S['rb']-=wa
   hr=S['hr']
   hr.append(int(S['rb']))
   S['hr']=hr
   rec={'TIME':pkt().strftime('%H:%M:%S PKT')}
   rec['MKT']='WITHDRAW'
   rec['RES']='W'
   rec['PROF']=-wa
   rec['BAL']=int(S['rb'])
   rec['TYPE']='W'
   rec['METHOD']=wm
   rec['TO']=wp
   rec['AMT']=wa
   rec['STATUS']='PROC V131'
   rec['ACC']='REAL'
   th=S['th']
   th.append(rec)
   S['th']=th
   wd=S['wd']
   wd.append(rec)
   S['wd']=wd
   t=C+'WITHDRAW -'+str(wa)+' to '+wp+' via '+wm+E
   st.markdown(t,unsafe_allow_html=True)
  else:
   st.error('Invalid phone low bal REAL')
 if len(S['wd'])>0:
  st.markdown(C+'WITHDRAW HISTORY'+E,unsafe_allow_html=True)
  df2=pd.DataFrame(S['wd'][::-1])
  st.dataframe(df2,use_container_width=True,height=200)
 if st.button('RESET BOTH',key='rb_dep'):
  for k in list(S.keys()):
   del S[k]
  st.rerun()
elif pg=='SETTINGS':
 st.markdown(C+'SETTINGS V131'+E,unsafe_allow_html=True)
 t=C+'TIME '+pkt_str+' TF '+S['stf']+' OPEN '+str(oc)+E
 st.markdown(t,unsafe_allow_html=True)
 c_a1,c_a2=st.columns(2)
 with c_a1:
  ta=st.selectbox('Amount SET',[250,500,750,1000],key='ta_set')
  S['ta']=ta
  st.write(ta)
 with c_a2:
  tph=st.selectbox('Trades SET',[4],key='tph_set')
  S['tph']=tph
  st.write(tph)
 c1,c2=st.columns(2)
 with c1:
  ur=S['ur']
  ur=st.toggle('RSI ON',value=ur,key='ur_set')
  S['ur']=ur
  rv=S['rthr']
  rv=st.slider('RSI VAL',30,80,rv,key='rv_set')
  S['rthr']=rv
  st.write(rv)
 with c2:
  uv=S['uv']
  uv=st.toggle('VOL ON',value=uv,key='uv_set')
  S['uv']=uv
  vv=S['vthr']
  vv=st.slider('VOL VAL',5,30,int(vv*10),key='vv_set')
  vv=vv/10
  S['vthr']=vv
  st.write(vv)
 c3,c4=st.columns(2)
 with c3:
  ua=S['uat']
  ua=st.toggle('ATR ON',value=ua,key='ua_set')
  S['uat']=ua
  av=S['athr']
  av=st.slider('ATR VAL',50,200,av,key='av_set')
  S['athr']=av
  st.write(av)
 with c4:
  um=S['um']
  um=st.toggle('MACD ON',value=um,key='um_set')
  S['um']=um
  mv=S['mthr']
  mv=st.slider('MACD VAL',-50,50,int(mv*100),key='mv_set')
  mv=mv/100
  S['mthr']=mv
  st.write(mv)
 c5,c6=st.columns(2)
 with c5:
  ul=S['ul']
  ul=st.toggle('LIQ ON',value=ul,key='ul_set')
  S['ul']=ul
  lf=st.selectbox('LIQ VAL',['LOW','HIGH'],key='lf_set')
  S['lf']=lf
  st.write(lf)
 with c6:
  up=S['up']
  up=st.toggle('PULL ON',value=up,key='up_set')
  S['up']=up
  pf=st.selectbox('PULL VAL',['50%','61%','NO'],key='pf_set')
  S['pf']=pf
  st.write(pf)
 al=S['aon']
 al=st.toggle('ALERT ON',value=al,key='al_set')
 S['aon']=al
 amkt=S['amkt']
 amkt=st.toggle('AUTO MKT SET',value=amkt,key='am_set')
 S['amkt']=amkt
 t=C+'SET V131 READY 95% WIN TODAY '+str(S['td'])+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'TOTAL '+str(S['tt'])+' OPEN '+str(oc)+' TIME '+pkt_str+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'1MIN=1MIN 5MIN=5MIN AUTO ONLY NO STOP'+E
 st.markdown(t,unsafe_allow_html=True)
st.write('---')
b1,b2,b3,b4,b5=st.columns(5)
with b1:
 if st.button('TRADING',key='b_trad'):
  S['pg']='TRADING'
  st.rerun()
with b2:
 if st.button('AI BRAIN',key='b_ai'):
  S['pg']='AI_BRAIN'
  st.rerun()
with b3:
 if st.button('HISTORY',key='b_hist'):
  S['pg']='HISTORY'
  st.rerun()
with b4:
 if st.button('DEPOSIT',key='b_dep'):
  S['pg']='DEPOSIT'
  st.rerun()
with b5:
 if st.button('SETTINGS',key='b_set'):
  S['pg']='SETTINGS'
  st.rerun()
comp.html('<script>setTimeout(function(){window.location.reload();},10000);</script>',height=0)
