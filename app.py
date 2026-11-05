import streamlit as st
import random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V133',layout='wide')
C='<div class="card">'
P='<div class="profit">'
O='<div class="open">'
A1='<div class="ai">'
E='</div>'
CSS='''<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:#0A0A0A;color:#fff}
.card{background:#1A1A1A;border:1px solid #222}
.card{border-radius:16px;padding:12px;margin:6px}
.profit{background:#0F0;border-radius:16px}
.profit{padding:12px;margin:6px;color:#000}
.profit{font-weight:900}
.open{background:#2A2A00;border:1px solid #FD0}
.open{border-radius:14px;padding:10px;margin:6px}
.ai{background:#0A1A2A;border:1px solid #0FF}
.ai{border-radius:14px;padding:10px;margin:6px}
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
init('sm','EUR/USD OTC')
init('stf','1MIN')
init('th',[])
init('ot',[])
init('wc',0)
init('lc',0)
init('ht',0)
init('lt',pkt()-timedelta(minutes=20))
init('ta',280)
init('tph',4)
init('am','DEMO')
init('pg','TERMINAL')
init('td',0)
init('tt',0)
init('day',pkt().day)
init('lh',pkt().hour)
init('amkt',True)
init('auto',True)
init('msc',{})
init('lmc',pkt()-timedelta(minutes=20))
init('rthr',60)
init('vthr',1.5)
init('athr',100)
init('mthr',0.0)
init('lf','LOW')
init('aon',True)
init('dep',0)
init('depr',[])
init('wd',[])
init('tasks',0)
now=pkt()
if now.day!=S['day']:
 S['td']=0
 S['day']=now.day
if now.hour!=S['lh']:
 S['ht']=0
 S['lh']=now.hour
 S['lt']=now-timedelta(minutes=20)
mkts=['EUR/USD OTC','GBP/USD OTC','AUD/CAD OTC']
mkts+=['AUD/CHF OTC','AUD/JPY OTC','AUD/NZD OTC']
mkts+=['BNB OTC','Bitcoin OTC','Gold OTC']
mkts+=['EUR/USD','BTC/USD','ETH/USD','SOL/USD']
tfs=['1MIN','2MIN','5MIN','15MIN']
tfs+=['30MIN','1H','4H','1D']
bmap={'EUR':1.0922,'GBP':1.27,'AUD':0.65}
bmap['BNB']=600
bmap['Bitcoin']=67453
bmap['Gold']=2448
bmap['BTC']=67453
bmap['ETH']=3520
bmap['SOL']=180
def msc(m):
 return round(random.uniform(0.5,3.8),2)
if S['amkt']:
 mm=(now-S['lmc']).total_seconds()/60
 if mm>=5:
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
  if bm!=S['sm']:
   S['sm']=bm
   S['lmc']=now
sm=S['sm']
if 'EUR' in sm: k='EUR'
elif 'GBP' in sm: k='GBP'
elif 'AUD' in sm: k='AUD'
elif 'BNB' in sm: k='BNB'
elif 'Bitcoin' in sm: k='Bitcoin'
elif 'Gold' in sm: k='Gold'
elif 'BTC' in sm: k='BTC'
elif 'ETH' in sm: k='ETH'
else: k='SOL'
b=bmap[k]
lp=round(b+random.uniform(-0.02,0.03),4)
if k in ['BTC','Bitcoin','Gold','BNB']:
 lp=round(b+random.uniform(-10,20),2)
cc=20
ohlc=[]
p=lp-0.01 if k=='EUR' else lp-20
for i in range(cc):
 op=round(p,4) if k=='EUR' else round(p,2)
 ch=round(random.uniform(-0.001,0.0015),4)
 if k!='EUR': ch=round(random.uniform(-5,9),2)
 cp=round(op+ch,4) if k=='EUR' else round(op+ch,2)
 hp=round(max(op,cp)+0.0005,4)
 if k!='EUR': hp=round(max(op,cp)+1.5,2)
 lo=round(min(op,cp)-0.0005,4)
 if k!='EUR': lo=round(min(op,cp)-1.5,2)
 v=round(random.uniform(1,2.8),2)
 ohlc.append({'O':op,'H':hp,'L':lo})
 ohlc[-1]['C']=cp
 ohlc[-1]['V']=v
 p=cp
lc=ohlc[-1]
if lc['C']>=lc['O']: cd='UP'
else: cd='DOWN'
rsi=round(55+random.uniform(-5,15),1)
vol=lc['V']
atr=round(95+random.uniform(-8,12),1)
vwap=round(6750+random.uniform(-30,50),1)
macd=round(random.uniform(-0.1,0.15),2)
ema=round(lp-random.uniform(-0.01,0.01),4)
liq='LOW'
bos='BULL' if lp>vwap else 'BEAR'
sc=round(random.uniform(2.5,4.5),1)
if sc>=2.0: ai='UP'
else: ai='DOWN'
ac=int(85+random.uniform(0,10))
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
  if random.random()<0.6: win=True
  if win: pr=int(o['AMT']*0.85)
  else: pr=-o['AMT']
  tm=now.strftime('%H:%M:%S PKT')
  dt2=now.strftime('%Y-%m-%d')
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
  rec['DATE']=dt2
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
if S['auto']:
 if len(S['ot'])==0 and S['td']==0:
  trade()
 elif S['ht']<4 and mins>=15:
  trade()
 elif S['ht']<4 and len(S['ot'])==0 and mins>=5:
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
st.markdown(C+'SONA V133 OLYMP STYLE'+E,unsafe_allow_html=True)
t=C+'DEMO '+str(db)+' REAL '+str(rb)+E
st.markdown(t,unsafe_allow_html=True)
t=C+'TODAY '+str(S['td'])+'/96 TOTAL '+str(S['tt'])
t+=' HOUR '+str(ht)+'/4 WR '+str(wrp)+E
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
 t=C+'NO OPEN - AUTO TRADE STARTING'+E
 st.markdown(t,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
 t='<div class="metric">TODAY '+str(S['td'])+E
 st.markdown(t,unsafe_allow_html=True)
with c2:
 t=st.toggle('AUTO TRADING ON',value=S['auto'],key='auto_home')
 S['auto']=t
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
pg=S['pg']
if pg=='HOME':
 st.markdown(C+'HOME - Demo account'+E,unsafe_allow_html=True)
 t=C+'Demo account D'+str(cb)+' REAL '+str(rb)+E
 st.markdown(t,unsafe_allow_html=True)
 c_h1,c_h2=st.columns(2)
 with c_h1:
  if st.button('Withdraw',key='wd_home'):
   S['pg']='DEPOSIT'
   st.rerun()
 with c_h2:
  if st.button('Deposit',key='dep_home'):
   S['pg']='DEPOSIT'
   st.rerun()
 st.markdown(C+'Ready, set, race!'+E,unsafe_allow_html=True)
 t=C+'Join tournament every day'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'Compete for share of $12,695 RFT'+E
 st.markdown(t,unsafe_allow_html=True)
 st.markdown(C+'Tasks & Rewards 4 Available'+E,unsafe_allow_html=True)
 t=C+'Trade until USD 200 turnover'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'on EUR/CAD OTC - Accept Task'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'Make 6 profit row on EUR'+E
 st.markdown(t,unsafe_allow_html=True)
 if st.button('Accept Task',key='task_home'):
  S['tasks']+=1
  st.success('Task Accepted')
 st.markdown(C+'Lucky Race - How streak?'+E,unsafe_allow_html=True)
 t=C+'Maximize bonus benefits'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'Daily prize inside'+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='TRADES':
 st.markdown(C+'TRADES - History Full Day'+E,unsafe_allow_html=True)
 t=C+'Fixed Time InZone Forex Stocks'+E
 st.markdown(t,unsafe_allow_html=True)
 st.markdown(C+'History - Show All'+E,unsafe_allow_html=True)
 if oc>0:
  st.markdown(C+'OPEN TRADES WAIT'+E,unsafe_allow_html=True)
  for o in S['ot']:
   es=o['EXP'].strftime('%H:%M:%S PKT')
   t=O+'OPEN '+o['MKT']+' '+o['TF']+' '+o['TIME']+E
   st.markdown(t,unsafe_allow_html=True)
   t=O+'-> '+es+' ENTRY '+str(o['ENTRY'])+E
   st.markdown(t,unsafe_allow_html=True)
 if len(S['th'])>0:
  df=pd.DataFrame(S['th'][::-1])
  st.dataframe(df,use_container_width=True,height=400)
  for r in S['th'][::-1][:10]:
   col='#0F0' if r['PROF']>=0 else '#F44'
   t=C+r['MKT']+' 90% '+r['TF']+' D'+str(r['AMT'])+E
   st.markdown(t,unsafe_allow_html=True)
   t=C+'Profit '+str(r['PROF'])+' '+r['RES']+E
   st.markdown(t,unsafe_allow_html=True)
 else:
  st.info('No trades yet V133 - AUTO STARTING')
 st.markdown(C+'Open Full History'+E,unsafe_allow_html=True)
 t=C+'OCTOBER 26 - Full Day History'+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='TERMINAL':
 st.markdown(C+'TERMINAL - Fixed Time'+E,unsafe_allow_html=True)
 t=C+'DEMO D'+str(cb)+' '+S['sm']+' 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'Fixed Time InZone Forex Stocks'+E
 st.markdown(t,unsafe_allow_html=True)
 c_m1,c_m2=st.columns(2)
 with c_m1:
  mk=st.selectbox('MKT TERM',mkts,key='mk_term')
 with c_m2:
  tf=st.selectbox('TF TERM',tfs,key='tf_term')
  S['stf']=tf
 if not S['amkt']: S['sm']=mk
 t=C+'LIVE '+S['sm']+' '+str(lp)+' WIN '+str(wc)+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'BAL '+str(cb)+' PROFIT '+str(cp)+' AI '+ai+E
 st.markdown(t,unsafe_allow_html=True)
 cjs=[]
 for c in ohlc:
  cjs.append('{o:'+str(c['O'])+',h:'+str(c['H']))
  cjs[-1]+= ',l:'+str(c['L'])+',c:'+str(c['C'])+'}'
 cs=','.join(cjs)
 ch='<div style="background:#111;border:1px"'
 ch+=' solid #0F0;border-radius:12px;padding:5px"'
 ch+='><canvas id="cc" width="350" height="120"'
 ch+=' style="width:100%;height:120px"></canvas></div>'
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
 ch+=" '#0F0';ct.fillText('V133 TERMINAL',pad,12);"
 ch+='</script>'
 ch=ch.replace('CANDLES',cs)
 comp.html(ch,height=180)
 c_a1,c_a2=st.columns(2)
 with c_a1:
  ta=st.selectbox('Amount TERM',[280,250,500],key='ta_term')
  S['ta']=ta
 with c_a2:
  dur=st.selectbox('Duration TERM',['1MIN','2MIN','5MIN'],key='dur_term')
  S['stf']=dur
 c_d1,c_d2=st.columns(2)
 with c_d1:
  if st.button('Down',key='down_term'):
   st.error('AUTO ONLY - Manual OFF')
 with c_d2:
  if st.button('Up',key='up_term'):
   st.error('AUTO ONLY - Manual OFF')
 pot=int(S['ta']*0.85)
 t=P+'Potential profit: D'+str(pot)+' AUTO ONLY'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'CANDLE TIME FRAME 30s 1m 2m 5m 10m 15m'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'CHART TYPE Area Candlestick Heikin Ash'+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='MARKET':
 st.markdown(C+'MARKET - Assets'+E,unsafe_allow_html=True)
 st.markdown(C+'Signal Scanners'+E,unsafe_allow_html=True)
 t=A1+'AI-powered Signal adjusts'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'to your trading activity'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'Dynamic Fast flow Medium signals'+E
 st.markdown(t,unsafe_allow_html=True)
 st.markdown(C+'Profitability Favorites'+E,unsafe_allow_html=True)
 for m,s in S['msc'].items():
  t=A1+m+' 85% SCORE '+str(s)+' PKT '+pkt_str+E
  st.markdown(t,unsafe_allow_html=True)
 if len(S['msc'])==0:
  for m in mkts:
   t=A1+m+' 85% PKT '+pkt_str+E
   st.markdown(t,unsafe_allow_html=True)
 t=A1+'AI Global Index 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'Metal Composite Index 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'Oil Composite Index 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'Quickler 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=A1+'Asia Composite Index 85%'+E
 st.markdown(t,unsafe_allow_html=True)
 t=P+'FINAL SCORE '+str(sc)+' AI '+ai+' CONF '+str(ac)+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='HELP':
 st.markdown(C+'HELP - Support 24/7'+E,unsafe_allow_html=True)
 st.markdown(C+'Support - We here for you 24/7'+E,unsafe_allow_html=True)
 st.markdown(C+'Help Center - Get to know platform'+E,unsafe_allow_html=True)
 st.markdown(C+'Education - Expand knowledge'+E,unsafe_allow_html=True)
 st.markdown(C+'Trading Tutorials - Learn open trade'+E,unsafe_allow_html=True)
 st.markdown(C+'Trading Conditions - Beneficial'+E,unsafe_allow_html=True)
 st.markdown(C+'SETTINGS V133 - No Dup'+E,unsafe_allow_html=True)
 t=C+'TIME '+pkt_str+' TF '+S['stf']+' OPEN '+str(oc)+E
 st.markdown(t,unsafe_allow_html=True)
 rv=S['rthr']
 rv=st.slider('RSI VAL',30,80,rv,key='rv_help')
 S['rthr']=rv
 st.write(rv)
 vv=S['vthr']
 vv=st.slider('VOL VAL',5,30,int(vv*10),key='vv_help')
 vv=vv/10
 S['vthr']=vv
 st.write(vv)
 av=S['athr']
 av=st.slider('ATR VAL',50,200,av,key='av_help')
 S['athr']=av
 st.write(av)
 mv=S['mthr']
 mv=st.slider('MACD VAL',-50,50,int(mv*100),key='mv_help')
 mv=mv/100
 S['mthr']=mv
 st.write(mv)
 lf=st.selectbox('LIQ VAL',['LOW','HIGH'],key='lf_help')
 S['lf']=lf
 st.write(lf)
 pf=st.selectbox('PULL VAL',['50%','61%','NO'],key='pf_help')
 S['pf']=pf
 st.write(pf)
 t=C+'SET V133 READY 95% WIN'+E
 st.markdown(t,unsafe_allow_html=True)
elif pg=='DEPOSIT':
 st.markdown(C+'DEPOSIT V133 - Payments'+E,unsafe_allow_html=True)
 if st.button('RESET DEMO',key='rd_dep'):
  S['db']=10000
  S['dp']=0
  S['hd']=[10000]
  st.success('RESET 10000')
 st.markdown(C+'Payments - Deposit Withdraw'+E,unsafe_allow_html=True)
 st.markdown(C+'Internal Transfer Transactions'+E,unsafe_allow_html=True)
 pm=st.selectbox('METHOD DEP',['JazzCash','Easypaisa'],key='pm_dep')
 t=C+'Bank transfer / Easypaisa / JazzCash'+E
 st.markdown(t,unsafe_allow_html=True)
 t=C+'BinancePay USDT Bank card RAAST'+E
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
   rec['STATUS']='OK V133'
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
 st.markdown(C+'WITHDRAW V133'+E,unsafe_allow_html=True)
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
   rec['STATUS']='PROC V133'
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
st.write('---')
b1,b2,b3,b4,b5=st.columns(5)
with b1:
 if st.button('Home',key='b_home'):
  S['pg']='HOME'
  st.rerun()
with b2:
 if st.button('Trades',key='b_trad'):
  S['pg']='TRADES'
  st.rerun()
with b3:
 if st.button('Terminal',key='b_term'):
  S['pg']='TERMINAL'
  st.rerun()
with b4:
 if st.button('Market',key='b_mkt'):
  S['pg']='MARKET'
  st.rerun()
with b5:
 if st.button('Help',key='b_help'):
  S['pg']='HELP'
  st.rerun()
b6,b7=st.columns(2)
with b6:
 if st.button('Deposit',key='b_dep2'):
  S['pg']='DEPOSIT'
  st.rerun()
with b7:
 if st.button('Withdraw',key='b_wd2'):
  S['pg']='DEPOSIT'
  st.rerun()
comp.html('<script>setTimeout(function(){window.location.reload();},10000);</script>',height=0)
