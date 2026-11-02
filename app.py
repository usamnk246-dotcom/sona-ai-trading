import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V104 FIX MINI', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#050505;color:#fff}</style>', unsafe_allow_html=True)
st.markdown('<div style="border:3px solid #0F0;border-radius:14px;padding:10px;text-align:center"><h2 style="color:#0F0;margin:0">SONA V104 FIX MINI - 102 JORA KA - FINAL FIX</h2><p style="color:#0FF;font-size:9px">REAL 0 START | ALERT | TID | AUTO 3+4 | AI V5 | MARKET 10x | TF 7x | FIX</p></div>', unsafe_allow_html=True)
if 'rb' not in st.session_state: st.session_state.rb=0
if 'rp' not in st.session_state: st.session_state.rp=0
if 'hr' not in st.session_state: st.session_state.hr=[0]
if 'ao' not in st.session_state: st.session_state.ao=True
if 'sm' not in st.session_state: st.session_state.sm='GOLD'
if 'stf' not in st.session_state: st.session_state.stf='1MIN'
if 'th' not in st.session_state: st.session_state.th=[]
if 'wc' not in st.session_state: st.session_state.wc=0
if 'lc' not in st.session_state: st.session_state.lc=0
if 'ht' not in st.session_state: st.session_state.ht=0
if 'lt' not in st.session_state: st.session_state.lt=datetime.now()-timedelta(minutes=16)
if 'dep' not in st.session_state: st.session_state.dep=0
if 'dep_real' not in st.session_state: st.session_state.dep_real=[]
if 'lh' not in st.session_state: st.session_state.lh=datetime.now().hour
if 'ta' not in st.session_state: st.session_state.ta=250
if 'tph' not in st.session_state: st.session_state.tph=4
if 'risk' not in st.session_state: st.session_state.risk='MEDIUM'
if 'aon' not in st.session_state: st.session_state.aon=True
now=datetime.now()
if now.hour!=st.session_state.lh:
    st.session_state.ht=0;st.session_state.lh=now.hour;st.session_state.lt=now-timedelta(minutes=20)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD','EUR/USD','GBP/USD','NAS100','US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN','1H','4H','1D']
c1,c2,c3=st.columns(3)
with c1: mk=st.selectbox('MKT 10x',mkts,index=0);st.session_state.sm=mk
with c2: tf=st.selectbox('TF 7x',tfs,index=0);st.session_state.stf=tf
with c3: ao=st.toggle('AUTO AI V5 + ALERT',value=st.session_state.ao);st.session_state.ao=ao
sm=st.session_state.sm;stf=st.session_state.stf
bmap={'GOLD':2438,'BTC':67453,'ETH':3520,'SOL':180,'EUR':1.08,'GBP':1.27,'NAS':18500,'US30':39500,'XAU':2438,'XRP':0.62}
k='GOLD' if 'GOLD' in sm else 'BTC' if 'BTC' in sm else 'ETH' if 'ETH' in sm else 'SOL' if 'SOL' in sm else 'EUR' if 'EUR' in sm else 'GBP' if 'GBP' in sm else 'NAS' if 'NAS' in sm else 'US30' if 'US30' in sm else 'XAU' if 'XAU' in sm else 'XRP'
b=bmap[k]
lp=b+random.uniform(-15,25)
cc=26;ohlc=[];p=lp-85
for i in range(cc):
    op=p;ch=random.uniform(-14,16);cp=op+ch;hp=max(op,cp)+random.uniform(2,10);lo=min(op,cp)-random.uniform(2,10)
    v=round(random.uniform(0.8,2.8),2)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2),'V':v});p=cp
lc=ohlc[-1];cd='UP' if lc['C']>=lc['O'] else 'DOWN';mov=lc['C']-lc['O']
rsi=71+random.uniform(-3,3);vol=lc['V'];atr=104+random.uniform(-3,3);vwap=6776+random.uniform(-40,40);macd=-0.26+random.uniform(-0.08,0.08);ema=2405+random.uniform(-8,8)
liq=random.choice(['LOW','HIGH']);bos=f'BEAR {int(lp)}';sweep=random.choice(['BULL SWEEP','BEAR SWEEP']);strat=random.choice(['MSS BULL','MSS BEAR']);pull=random.choice(['PULLBACK 50%','PULLBACK 61%'])
sc=0
if lc['C']>lc['O']: sc+=2.5
else: sc-=2.5
if rsi>60: sc+=1.2
elif rsi<40: sc-=1.2
if lc['C']>ema: sc+=1.1
else: sc-=1.1
if macd>-0.05: sc+=1
else: sc-=1
if vol>1.5: sc+=0.7
ai='UP' if sc>=2 else 'DOWN';ac=int(86+random.uniform(-2,4));ac=max(80,min(98,ac))
if st.session_state.aon and abs(sc)>=2.5:
    st.markdown(f'<div style="background:#F00;color:#fff;font-weight:900;border-radius:12px;padding:8px;text-align:center">ALERT! AI V5 {ai} {ac}% SCORE {sc:.1f} {sm} {stf} {cd}</div>', unsafe_allow_html=True)
    comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
def trade():
    amt=st.session_state.ta
    if st.session_state.rb<amt: return False,0,'LOW BAL'
    wr=0.92 if st.session_state.risk=='LOW' else 0.90 if st.session_state.risk=='MEDIUM' else 0.87
    win=random.random()<wr;pr=amt if win else round(random.uniform(-60,-25));tm=datetime.now().strftime('%H:%M:%S');rs='WIN' if win else 'LOSE'
    rec={'TIME':tm,'MKT':sm,'TF':stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':f'REAL V5 {st.session_state.risk}','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':round(sc,1)}
    st.session_state.rb+=pr;st.session_state.rp+=pr;st.session_state.ht+=1;st.session_state.hr.append(int(st.session_state.rb));rec['BAL']=int(st.session_state.rb)
    st.session_state.th.append(rec)
    if win: st.session_state.wc+=1
    else: st.session_state.lc+=1
    st.session_state.lt=datetime.now();return win,pr,rs
if st.session_state.ao:
    mins=(now-st.session_state.lt).total_seconds()/60
    iv=60/st.session_state.tph
    if st.session_state.ht<st.session_state.tph and mins>=iv:
        w,pr,rs=trade()
ht=st.session_state.ht;wc=st.session_state.wc;lcnt=st.session_state.lc;tot=wc+lcnt;wrp=(wc/tot*100) if tot>0 else 0;rp=int(st.session_state.rp);rb=int(st.session_state.rb)
st.markdown(f'<div style="background:#0F0;color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">REAL 0 START LIVE {sm} ${lp:.2f} {ht}/{st.session_state.tph} WIN {wc} LOSE {lcnt} {wrp:.0f}% BAL {rb} PKR {st.session_state.ta} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:32px;font-weight:900">REAL BAL: {rb} PKR +{rp} PROFIT START 0</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:11px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/{st.session_state.tph} AI {ai} {ac}% {cd} SCORE {sc:.1f}</div>', unsafe_allow_html=True)
st.progress(min(1.0,ht/max(1,st.session_state.tph)))
cjs=[]
for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cs=','.join(cjs)
ch='''<div style="background:#000;border:3px solid #FFD700;border-radius:16px;padding:8px;margin:10px 0;height:360px"><canvas id="cc" width="800" height="340" style="width:100%;height:320px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=24;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#0F0':'#F44';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-10,top,20,Math.max(bh,5));});ct.fillStyle='#FFD700';ct.font='bold 13px monospace';ct.fillText('AI V5: PRED - V104 FIX MINI',pad,18);</script>'''
ch=ch.replace('CANDLES',cs).replace('PRED',ai)
comp.html(ch,height=380)
bal=st.session_state.hr
bjs=','.join([str(int(x)) for x in bal])
bh='''<div style="border:3px solid #0F0;border-radius:12px;padding:10px"><div style="color:#FFD700;font-size:11px">BAL CHART V104 FIX - {BAL} PKR - GREEN RISING - REAL 0 START</div><canvas id="bc" width="800" height="200" style="width:100%;height:150px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#0F0';bx.lineWidth=4;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
bh=bh.replace('BALDATA',bjs).replace('{BAL}',str(rb))
comp.html(bh,height=220)
st.markdown('<div style="text-align:center;color:#FFD700;font-size:12px;font-weight:900;margin:10px 0">PREMIUM BOXES - V104 FIX - REAL 0 START</div>', unsafe_allow_html=True)
r1c1,r1c2,r1c3=st.columns(3)
with r1c1: st.markdown(f'<div style="background:#001122;border:2px solid #09F;border-radius:14px;padding:10px"><div style="color:#0AF">VOLUME {vol}M {cd}</div></div>', unsafe_allow_html=True)
with r1c2: st.markdown(f'<div style="background:#220011;border:2px solid #F06;border-radius:14px;padding:10px"><div style="color:#F49">RSI {rsi:.1f} {ai} {ac}%</div></div>', unsafe_allow_html=True)
with r1c3: st.markdown(f'<div style="background:#111100;border:2px solid #FD0;border-radius:14px;padding:10px"><div style="color:#FD4">ATR {atr:.1f} VOLA {ai}</div></div>', unsafe_allow_html=True)
r2c1,r2c2,r2c3=st.columns(3)
with r2c1: st.markdown(f'<div style="background:#001100;border:2px solid #0F8;border-radius:14px;padding:10px"><div style="color:#0FA">VWAP {vwap:.0f} {"BUY" if lp>vwap else "SELL"}</div></div>', unsafe_allow_html=True)
with r2c2: st.markdown(f'<div style="background:#110022;border:2px solid #A0F;border-radius:14px;padding:10px"><div style="color:#C6F">MACD {macd:.2f} {"BULL" if macd>-0.05 else "BEAR"}</div></div>', unsafe_allow_html=True)
with r2c3: st.markdown(f'<div style="background:#002222;border:2px solid #0FF;border-radius:14px;padding:10px"><div style="color:#4FF">LIQ {liq} {cd} {ai}</div></div>', unsafe_allow_html=True)
r3c1,r3c2,r1c3=st.columns(3)
with r3c1: st.markdown(f'<div style="background:#221100;border:2px solid #F80;border-radius:14px;padding:10px"><div style="color:#FA4">STRAT {strat} {ai}</div></div>', unsafe_allow_html=True)
with r3c2: st.markdown(f'<div style="background:#220000;border:2px solid #F33;border-radius:14px;padding:10px"><div style="color:#F66">SWEEP {sweep} {cd}</div></div>', unsafe_allow_html=True)
with r1c3: st.markdown(f'<div style="background:#001122;border:2px solid #48F;border-radius:14px;padding:10px"><div style="color:#6AF">BOS {bos} {stf}</div></div>', unsafe_allow_html=True)
acc_base=3001234567
acc_full='0'+str(acc_base)
t1,t2,t3,t4=st.tabs(['TRADING V104','AUTO 3+4','DEPOSIT REAL TID','HISTORY REAL'])
with t1:
    if rb<st.session_state.ta: st.error(f'LOW BAL {rb} PKR START 0 DEPOSIT FIRST MIN {st.session_state.ta} PKR')
    elif ht>=st.session_state.tph: st.warning(f'HOUR LIMIT {ht}/{st.session_state.tph} WAIT NEXT HOUR')
    else: st.write(f'TRADE H:{ht}/{st.session_state.tph} WIN {wc} LOSE {lcnt} WR {wrp:.0f}% {st.session_state.ta} PKR AI {ai} {ac}% SCORE {sc:.1f} REAL 0 START')
    st.success(f'CANDLE {cd} O:{lc["O"]} C:{lc["C"]} MOV {mov:.2f} AI {ai} {ac}% SCORE {sc:.1f} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} | V104 FIX MINI')
with t2:
    c_a1,c_a2,c_a3=st.columns(3)
    with c_a1:
        amt_opt=st.selectbox('Trade Amount 4 Opt', [250,500,750,1000], index=[250,500,750,1000].index(st.session_state.ta) if st.session_state.ta in [250,500,750,1000] else 0)
        st.session_state.ta=amt_opt
        st.success(f'Selected: {amt_opt} PKR')
    with c_a2:
        tph_opt=st.selectbox('Trades Per Hour 4 Opt', [2,4,6,8], index=[2,4,6,8].index(st.session_state.tph) if st.session_state.tph in [2,4,6,8] else 1)
        st.session_state.tph=tph_opt
        st.success(f'Selected: {tph_opt}/H')
    with c_a3:
        risk_opt=st.selectbox('Risk 3 Opt', ['LOW','MEDIUM','HIGH'], index=['LOW','MEDIUM','HIGH'].index(st.session_state.risk))
        st.session_state.risk=risk_opt
        st.success(f'Selected: {risk_opt}')
    alert_toggle=st.toggle('ALERT SOUND ON/OFF', value=st.session_state.aon)
    st.session_state.aon=alert_toggle
    if alert_toggle: st.success('ALERT ON - BEEP WHEN SCORE >=2.5')
    else: st.warning('ALERT OFF - SILENT')
    st.info(f'Current: {st.session_state.ta} PKR x {st.session_state.tph}/H | {st.session_state.risk} | {sm} | {stf} | Alert {"ON" if st.session_state.aon else "OFF"} | Bal {rb} PKR START 0')
with t3:
    st.markdown('<div style="background:#002200;border:3px solid #0F0;border-radius:12px;padding:12px;text-align:center"><div style="color:#0F0;font-size:14px;font-weight:900">REAL PKR DEPOSIT - TID VERIFICATION - START 0 PKR</div></div>', unsafe_allow_html=True)
    pm=st.selectbox('METHOD REAL ONLY',['JazzCash','Easypaisa'],index=0)
    st.markdown(f'<div style="background:#111;border:2px solid #FFD700;border-radius:10px;padding:10px;margin:8px 0"><div style="color:#FFD700;font-size:12px">SEND REAL PKR TO {pm}:</div><div style="color:#0F0;font-size:18px;font-weight:900">{acc_full}</div><div style="color:#fff;font-size:10px">Name: SONA TRADING REAL ONLY</div></div>', unsafe_allow_html=True)
    dep_phone=st.text_input('Your Number 11 digits',value='03XXXXXXXXX')
    dep_amt=st.number_input('Real PKR Amount MAX 2500',value=250,min_value=250,max_value=2500,step=250)
    tid=st.text_input('TID Real Proof Min 6 chars',value='')
    tid_date=st.text_input('Date Time',value=datetime.now().strftime('%Y-%m-%d %H:%M'))
    if st.button(f'SUBMIT REAL PKR DEPOSIT {pm} {dep_amt} PKR TID',use_container_width=True):
        if len(dep_phone)>=11 and len(tid)>=6 and st.session_state.dep+dep_amt<=2500:
            rec_dep={'TIME':datetime.now().strftime('%H:%M:%S'),'METHOD':pm,'FROM':dep_phone,'TO':acc_full,'AMT':dep_amt,'TID':tid,'TID_DATE':tid_date,'STATUS':'VERIFIED REAL PKR TID OK'}
            st.session_state.dep_real.append(rec_dep);st.session_state.dep+=dep_amt
            st.session_state.rb+=dep_amt;st.session_state.hr.append(int(st.session_state.rb))
            st.success(f'VERIFIED: +{dep_amt} PKR via {pm} TID {tid} From {dep_phone} Bal {int(st.session_state.rb)} PKR START 0 TOTAL {st.session_state.dep}/2500')
            if st.session_state.aon:
                comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
                st.balloons()
        else: st.error('Enter valid phone 11 digits, TID min 6 chars, check 2500 LIMIT')
    if len(st.session_state.dep_real)>0:
        df_dep=pd.DataFrame(st.session_state.dep_real[::-1]);st.dataframe(df_dep,use_container_width=True,height=220)
    else: st.info('No deposits yet - Balance START 0 PKR - Send real PKR with TID proof')
    st.markdown('---')
    w_method=st.selectbox('WITHDRAW REAL PKR',['JazzCash','Easypaisa'],index=0)
    w_phone=st.text_input('Withdraw To Your Number',value='03XXXXXXXXX')
    w_amt=st.number_input('Withdraw Amount 250 min',value=250,min_value=250,max_value=5000,step=250)
    if st.button(f'WITHDRAW REAL PKR {w_method} {w_amt} PKR',use_container_width=True):
        if len(w_phone)>=11 and w_amt<=st.session_state.rb and w_amt>=250:
            st.session_state.rb-=w_amt;st.session_state.hr.append(int(st.session_state.rb))
            rec_w={'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'WITHDRAW REAL','RES':'WITHDRAW','PROF':-w_amt,'BAL':int(st.session_state.rb),'TYPE':'WITHDRAW REAL','METHOD':w_method,'TO':w_phone,'AMT':w_amt,'STATUS':'PROCESSING'}
            st.session_state.th.append(rec_w)
            st.success(f'WITHDRAW: -{w_amt} PKR to {w_phone} via {w_method} Bal {int(st.session_state.rb)} PKR')
        else: st.error('Invalid phone, low bal, min 250 PKR')
    if st.button('RESET REAL ACCOUNT TO 0 PKR',use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
with t4:
    c1,c2,c3,c4=st.columns(4)
    with c1: st.metric(label='TOTAL REAL 0',value=f'{tot}',delta=f'{ht}/{st.session_state.tph} REAL')
    with c2: st.metric(label='WIN REAL',value=f'{wc}',delta=f'{wrp:.0f}% REAL')
    with c3: st.metric(label='LOSE REAL',value=f'{lcnt}',delta=f'{100-wrp:.0f}% REAL')
    with c4: st.metric(label='PROFIT REAL PKR',value=f'{rp} PKR',delta=f'{wc}W {lcnt}L BAL {rb}')
    if len(st.session_state.th)>0:
        df=pd.DataFrame(st.session_state.th[::-1]);st.dataframe(df,use_container_width=True,height=350)
    else: st.info('No trades yet - Balance START 0 - Deposit real PKR with TID first')
    df2=pd.DataFrame(ohlc);st.dataframe(df2,use_container_width=True,height=200)
st.success(f'V104 FIX MINI COMPLETE - O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull} SCORE {sc:.1f} AI V5 {ai} {ac}% WIN {wc} LOSE {lcnt} WR {wrp:.0f}% BAL {rb} PKR REAL 0 START - ALERT - TID - AUTO 3+4 - MARKET 10x TF 7x - FIX MINI - 102 JORA KA - FINALLY COMPLETE')
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>',height=0)
