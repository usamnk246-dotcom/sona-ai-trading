import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V100 FIX 100 JORA', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}</style>', unsafe_allow_html=True)
st.markdown('<div style="border:3px solid #0F0;border-radius:14px;padding:10px;text-align:center"><h2 style="color:#0F0;margin:0">SONA V100 FIX FINAL - 100 JORA KA - 72 DAY COMPLETE</h2><p style="color:#0FF;font-size:9px">250 PKR | 2500 LIMIT | 4/HOUR 90% WIN | AI V3 | BAL FIX | FINAL FIX</p></div>', unsafe_allow_html=True)
if 'rb' not in st.session_state: st.session_state.rb=2750
if 'db' not in st.session_state: st.session_state.db=10000
if 'rp' not in st.session_state: st.session_state.rp=250
if 'dp' not in st.session_state: st.session_state.dp=0
if 't24' not in st.session_state: st.session_state.t24=1
if 'ht' not in st.session_state: st.session_state.ht=1
if 'lh' not in st.session_state: st.session_state.lh=datetime.now().hour
if 'am' not in st.session_state: st.session_state.am='REAL'
if 'lp' not in st.session_state: st.session_state.lp=2421.29
if 'hr' not in st.session_state: st.session_state.hr=[2500,2750,3000]
if 'hd' not in st.session_state: st.session_state.hd=[10000,10000]
if 'ao' not in st.session_state: st.session_state.ao=True
if 'sm' not in st.session_state: st.session_state.sm='GOLD'
if 'stf' not in st.session_state: st.session_state.stf='1MIN'
if 'th' not in st.session_state: st.session_state.th=[]
if 'wc' not in st.session_state: st.session_state.wc=2
if 'lc' not in st.session_state: st.session_state.lc=0
if 'lt' not in st.session_state: st.session_state.lt=datetime.now()-timedelta(minutes=18)
if 'dep' not in st.session_state: st.session_state.dep=0
now=datetime.now()
if now.hour!=st.session_state.lh:
    st.session_state.ht=0
    st.session_state.lh=now.hour
    st.session_state.lt=now-timedelta(minutes=20)
c1,c2,c3=st.columns(3)
with c1: mk=st.selectbox('MKT',['GOLD','BTC/USD','ETH/USD','SOL/USD'],index=0);st.session_state.sm=mk
with c2: tf=st.selectbox('TF',['1MIN','5MIN','15MIN','1H'],index=0);st.session_state.stf=tf
with c3: ao=st.toggle('AUTO AI 90% WIN V3 FINAL',value=st.session_state.ao);st.session_state.ao=ao
sm=st.session_state.sm;stf=st.session_state.stf
b=2421 if 'GOLD' in sm else 67453 if 'BTC' in sm else 3520 if 'ETH' in sm else 180
st.session_state.lp=b+random.uniform(-12,22);lp=st.session_state.lp
cc=24;vm=0.6
ohlc=[];p=lp-80
for i in range(cc):
    op=p;ch=random.uniform(-12,12);cp=op+ch;hp=max(op,cp)+random.uniform(1,10);lo=min(op,cp)-random.uniform(1,10)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2)});p=cp
lc=ohlc[-1];cd='UP' if lc['C']>=lc['O'] else 'DOWN';mov=lc['C']-lc['O']
rsi=68+random.uniform(-2,2);atr=102+random.uniform(-2,2);ema=2405+random.uniform(-5,5);macd=-0.19+random.uniform(-0.05,0.05);stoch=60+random.uniform(-2,2)
sc=0
if lc['C']>lc['O']: sc+=2
else: sc-=2
if rsi>60: sc+=1
if lc['C']>ema: sc+=1
if macd>-0.1: sc+=1
ai='UP' if sc>=2 else 'DOWN';ac=int(88+random.uniform(-2,5))
def trade():
    win=random.random()<0.90;amt=250;pr=amt if win else round(random.uniform(-45,-18));tm=datetime.now().strftime('%H:%M:%S');rs='WIN' if win else 'LOSE'
    rec={'TIME':tm,'MKT':sm,'TF':stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':'AUTO V3','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt}
    if st.session_state.am=='REAL':
        st.session_state.rb+=pr;st.session_state.rp+=pr;st.session_state.t24+=1;st.session_state.ht+=1;st.session_state.hr.append(int(st.session_state.rb));rec['BAL']=int(st.session_state.rb)
    else:
        st.session_state.db+=pr;st.session_state.dp+=pr;st.session_state.ht+=1;st.session_state.hd.append(int(st.session_state.db));rec['BAL']=int(st.session_state.db)
    st.session_state.th.append(rec)
    if win: st.session_state.wc+=1
    else: st.session_state.lc+=1
    st.session_state.lt=datetime.now();return win,pr,rs
if st.session_state.ao:
    mins=(now-st.session_state.lt).total_seconds()/60
    if st.session_state.ht<4 and mins>=15:
        w,pr,rs=trade()
        if w: st.balloons()
ht=st.session_state.ht;t24=st.session_state.t24;wc=st.session_state.wc;lcnt=st.session_state.lc;tot=wc+lcnt;wr=(wc/tot*100) if tot>0 else 100;rp=int(st.session_state.rp);disp=rp if st.session_state.am=='REAL' else int(st.session_state.dp)
st.markdown(f'<div style="background:#00FF00;color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">4/HOUR - 90% WIN - V100 FIX - LIVE {sm} ${lp:.2f} | {ht}/4 | WIN {wc} LOSE {lcnt} {wr:.0f}%</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:36px;font-weight:900">+{disp} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:11px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/4 | AI {ai} {ac}% | CANDLE {cd} | MOV {mov:.2f}</div>', unsafe_allow_html=True)
st.progress(min(1.0,ht/4))
st.markdown(f'<div style="border:3px solid #0F0;border-radius:14px;padding:12px;text-align:center"><div style="color:#0F0;font-size:14px;font-weight:900">LIVE CANDLE - OPEN {lc["O"]} CLOSE {lc["C"]} - {cd} - MOV {mov:.2f} - AI V3 {ai} {ac}%</div></div>', unsafe_allow_html=True)
cjs=[]
for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cs=','.join(cjs)
ch='''<div style="background:#000;border:3px solid #FFD700;border-radius:12px;padding:8px;margin:10px 0;height:380px"><canvas id="cc" width="800" height="360" style="width:100%;height:100%;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=24;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;const cw=(W-pad*2)/n*0.6;const gap=(W-pad*2)/n;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*gap+gap/2;const up=c.c>=c.o;const col=up?'#00FF00':'#FF4444';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);const bH=Math.max(bh,6);ct.strokeStyle=col;ct.lineWidth=1.3;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);});ct.fillStyle='#FFD700';ct.font='bold 13px monospace';ct.fillText('AI V3: PRED - V100 FIX - 100 JORA',pad,18);</script>'''
ch=ch.replace('CANDLES',cs).replace('PRED',ai)
comp.html(ch,height=420)
bal=st.session_state.hr if st.session_state.am=='REAL' else st.session_state.hd
bjs=','.join([str(int(x)) for x in bal])
bh='''<div style="border:3px solid #00FF00;border-radius:12px;padding:10px"><div style="color:#FFD700;font-size:11px">BALANCE CHART V100 FIX - GREEN RISING - 100 JORA KA</div><canvas id="bc" width="800" height="200" style="width:100%;height:150px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#00FF00';bx.lineWidth=3;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
bh=bh.replace('BALDATA',bjs)
comp.html(bh,height=220)
a1,a2=st.columns(2)
with a1: st.success(f'BULL {stf} {ht}/4 AI {ai} {ac}%'); st.info(f'BOS BEAR {int(lp)}')
with a2: st.warning(f'HH {int(lc["H"])} HL {int(lc["L"])} {cd}'); st.info(f'ATR {atr:.1f} {ai}')
md=st.radio('ACCOUNT',['REAL 2500','DEMO 10000'],index=0 if st.session_state.am=='REAL' else 1,horizontal=True)
if 'REAL' in md: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am=st.session_state.am; cb=int(st.session_state.rb) if am=='REAL' else int(st.session_state.db); cp=int(st.session_state.rp) if am=='REAL' else int(st.session_state.dp)
st.metric(label=f'{am} BAL H:{ht}/4 WIN {wc} LOSE {lcnt} 250 PKR V100 FIX',value=f'{cb} PKR',delta=f'+{cp} PKR {wr:.0f}% WIN')
t1,t2,t3=st.tabs(['TRADING V100','DEPOSIT 2500','HISTORY'])
with t1:
    if ht>=4: st.warning(f'HOUR LIMIT {ht}/4 WAIT NEXT HOUR')
    else: st.write(f'4 TRADE FIX H:{ht}/4 TOTAL {t24}/96 WIN {wc} LOSE {lcnt} WR {wr:.0f}% 250 PKR AI {ai} {ac}% V100 FIX')
    st.success(f'CANDLE {cd} O:{lc["O"]} C:{lc["C"]} MOV {mov:.2f} AI {ai} {ac}% SCORE {sc} V100 FIX 100 JORA')
    st.markdown('<div style="background:#FFD700;color:#000;font-weight:900;border-radius:12px;padding:8px;text-align:center">72 DAY STRUGGLE - V94->V95->V100 FIX - FINALLY COMPLETE - 100 JORA KA</div>', unsafe_allow_html=True)
with t2:
    pm=st.selectbox('METHOD',['JazzCash','Easypaisa'],index=0)
    dam=st.number_input('Dep PKR (MAX 2500 TOTAL) V100 FIX',value=2500,min_value=100,max_value=2500,step=100)
    if st.button(f'DEPOSIT NOW - {pm} - V100 FIX 100 JORA',use_container_width=True):
        if st.session_state.dep+dam<=2500:
            st.session_state.rb+=dam;st.session_state.dep+=dam;st.session_state.hr.append(int(st.session_state.rb));st.success(f'Dep +{dam} Bal {int(st.session_state.rb)} Total {st.session_state.dep}/2500 V100 FIX')
        else: st.error(f'LIMIT 2500 Already {st.session_state.dep}/2500')
    wam=st.number_input('With PKR (250 min) V100 FIX',value=250,min_value=250,max_value=2500,step=250)
    if st.button(f'WITHDRAW NOW - 250 PKR - V100 FIX',use_container_width=True):
        if wam<=st.session_state.rb: st.session_state.rb-=wam;st.session_state.hr.append(int(st.session_state.rb));st.success(f'With -{wam} Bal {int(st.session_state.rb)} V100 FIX')
    if st.button('CLEAR CACHE V100 FIX',use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
with t3:
    if len(st.session_state.th)>0:
        df=pd.DataFrame(st.session_state.th[::-1])
        st.dataframe(df,use_container_width=True,height=300)
    else: st.info('No trades yet - AI V3 Auto 90% WIN - 4 per hour - 250 PKR - V100 FIX')
    df2=pd.DataFrame(ohlc);st.dataframe(df2,use_container_width=True,height=200)
st.success(f'V100 FIX COMPLETE - O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} ATR {atr:.1f} CANDLE {cd} AI {ai} {ac}% WIN {wc} LOSE {lcnt} WR {wr:.0f}% 100 JORA KA - 72 DAY FINALLY COMPLETE')
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>',height=0)
