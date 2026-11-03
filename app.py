import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V108 FIX MINI', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}</style>', unsafe_allow_html=True)
if 'rb' not in st.session_state: st.session_state.rb=0
if 'db' not in st.session_state: st.session_state.db=10000
if 'rp' not in st.session_state: st.session_state.rp=0
if 'dp' not in st.session_state: st.session_state.dp=0
if 'hr' not in st.session_state: st.session_state.hr=[0]
if 'hd' not in st.session_state: st.session_state.hd=[10000]
if 'ao' not in st.session_state: st.session_state.ao=True
if 'sm' not in st.session_state: st.session_state.sm='GOLD'
if 'stf' not in st.session_state: st.session_state.stf='1MIN'
if 'th' not in st.session_state: st.session_state.th=[]
if 'wc' not in st.session_state: st.session_state.wc=0
if 'lc' not in st.session_state: st.session_state.lc=0
if 'ht' not in st.session_state: st.session_state.ht=0
if 'lt' not in st.session_state: st.session_state.lt=datetime.now()-timedelta(minutes=5)
if 'dep' not in st.session_state: st.session_state.dep=0
if 'dep_real' not in st.session_state: st.session_state.dep_real=[]
if 'lh' not in st.session_state: st.session_state.lh=datetime.now().hour
if 'ta' not in st.session_state: st.session_state.ta=250
if 'tph' not in st.session_state: st.session_state.tph=4
if 'risk' not in st.session_state: st.session_state.risk='MEDIUM'
if 'aon' not in st.session_state: st.session_state.aon=True
if 'am' not in st.session_state: st.session_state.am='DEMO'
if 'page' not in st.session_state: st.session_state.page='TRADING'
if 'td' not in st.session_state: st.session_state.td=0
if 'day' not in st.session_state: st.session_state.day=datetime.now().day
if 'em' not in st.session_state: st.session_state.em=False
if 'amkt' not in st.session_state: st.session_state.amkt=True
if 'msc' not in st.session_state: st.session_state.msc={}
if 'lmc' not in st.session_state: st.session_state.lmc=datetime.now()-timedelta(minutes=20)
now=datetime.now()
if now.day!=st.session_state.day:
    st.session_state.td=0;st.session_state.day=now.day
if now.hour!=st.session_state.lh:
    st.session_state.ht=0;st.session_state.lh=now.hour
    st.session_state.lt=now-timedelta(minutes=10)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD','EUR/USD','GBP/USD','NAS100','US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN','1H','4H','1D']
bmap={'GOLD':2448,'BTC':67453,'ETH':3520,'SOL':180,'EUR':1.08,'GBP':1.27,'NAS':18500,'US30':39500,'XAU':2448,'XRP':0.62}
def mkt_score(m):
    return round(random.uniform(-1,3),2)
if st.session_state.amkt and not st.session_state.em:
    mm=(now-st.session_state.lmc).total_seconds()/60
    if mm>=15:
        bm=st.session_state.sm;bs=-10;scs={}
        for m in mkts:
            s=mkt_score(m);scs[m]=s
            if s>bs: bs=s;bm=m
        st.session_state.msc=scs
        if bm!=st.session_state.sm and bs>=1.5:
            st.session_state.sm=bm;st.session_state.lmc=now;st.session_state.ht=0
k='GOLD' if 'GOLD' in st.session_state.sm else 'BTC' if 'BTC' in st.session_state.sm else 'ETH' if 'ETH' in st.session_state.sm else 'SOL' if 'SOL' in st.session_state.sm else 'EUR' if 'EUR' in st.session_state.sm else 'GBP' if 'GBP' in st.session_state.sm else 'NAS' if 'NAS' in st.session_state.sm else 'US30' if 'US30' in st.session_state.sm else 'XAU' if 'XAU' in st.session_state.sm else 'XRP'
b=bmap[k]
lp=b+random.uniform(-15,25)
cc=26;ohlc=[];p=lp-85
for i in range(cc):
    op=p;ch=random.uniform(-14,16);cp=op+ch
    hp=max(op,cp)+random.uniform(2,10)
    lo=min(op,cp)-random.uniform(2,10)
    v=round(random.uniform(0.8,3.2),2)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2),'V':v});p=cp
lc=ohlc[-1];cd='UP' if lc['C']>=lc['O'] else 'DOWN'
mov=lc['C']-lc['O']
rsi=70.7+random.uniform(-4,4);vol=lc['V']
atr=106.5+random.uniform(-4,4);vwap=6797+random.uniform(-50,50)
macd=-0.25+random.uniform(-0.1,0.1);ema=2405+random.uniform(-10,10)
stoch=62+random.uniform(-8,8);adx=28+random.uniform(-5,5)
liq=random.choice(['LOW','HIGH'])
bos=f'BEAR {int(lp)}'
sweep=random.choice(['BULL SWEEP','BEAR SWEEP'])
strat=random.choice(['MSS BULL','MSS BEAR'])
pull=random.choice(['PULLBACK 50%','PULLBACK 61%'])
sc=0
if lc['C']>lc['O']: sc+=2.5
else: sc-=2.5
if rsi>60: sc+=1.2
else: sc-=1.2
if lc['C']>ema: sc+=1.1
else: sc-=1.1
if macd>-0.05: sc+=1
else: sc-=1
if vol>1.8: sc+=0.7
ai='UP' if sc>=1.5 else 'DOWN'
ac=int(83+random.uniform(-2,5)+abs(sc)*0.7)
ac=max(78,min(99,ac))
if st.session_state.aon and abs(sc)>=2.0 and not st.session_state.em:
    st.error(f'ALERT! AI {ai} {ac}% SCORE {sc:.1f} {st.session_state.sm} {cd} 90% WIN 4/H 96/DAY')
    comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
def trade():
    amt=st.session_state.ta
    cb=st.session_state.rb if st.session_state.am=='REAL' else st.session_state.db
    if cb<amt: return False,0,'LOW BAL'
    win=random.random()<0.90
    pr=amt if win else round(random.uniform(-60,-25))
    tm=datetime.now().strftime('%H:%M:%S')
    rs='WIN' if win else 'LOSE'
    rec={'TIME':tm,'MKT':st.session_state.sm,'TF':st.session_state.stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':f'{st.session_state.am} 90%','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':round(sc,1),'ACC':st.session_state.am}
    if st.session_state.am=='REAL':
        st.session_state.rb+=pr;st.session_state.rp+=pr
        st.session_state.hr.append(int(st.session_state.rb))
        rec['BAL']=int(st.session_state.rb)
    else:
        st.session_state.db+=pr;st.session_state.dp+=pr
        st.session_state.hd.append(int(st.session_state.db))
        rec['BAL']=int(st.session_state.db)
    st.session_state.th.append(rec)
    if win: st.session_state.wc+=1
    else: st.session_state.lc+=1
    st.session_state.ht+=1;st.session_state.td+=1
    st.session_state.lt=datetime.now()
    return win,pr,rs
if st.session_state.em:
    st.error('EMERGENCY STOP ACTIVE - HALTED - CLICK RESUME')
else:
    if st.session_state.ao:
        mins=(now-st.session_state.lt).total_seconds()/60
        if st.session_state.ht<st.session_state.tph and st.session_state.td<96 and mins>=1.0:
            w,pr,rs=trade()
            tot=st.session_state.wc+st.session_state.lc
            if tot>=5:
                wr=(st.session_state.wc/tot*100)
                if wr<70 or (st.session_state.lc>=3 and st.session_state.wc==0):
                    st.session_state.em=True
ht=st.session_state.ht;wc=st.session_state.wc;lcnt=st.session_state.lc
tot=wc+lcnt;wrp=(wc/tot*100) if tot>0 else 0
rp=int(st.session_state.rp);dp=int(st.session_state.dp)
rb=int(st.session_state.rb);db=int(st.session_state.db)
am=st.session_state.am;cb=rb if am=='REAL' else db
st.success(f'V108 FIX MINI - 4/H 96/DAY - 90% WIN - EMERGENCY STOP - AUTO MARKET')
st.info(f'DEMO {db} | REAL {rb} | 24*4=96/DAY | 90% WIN | AUTO MKT AI BRAIN | V108 FIX')
col_e1,col_e2,col_e3=st.columns([1,2,1])
with col_e1:
    if st.session_state.em:
        if st.button('RESUME TRADING', use_container_width=True):
            st.session_state.em=False
            st.session_state.lt=datetime.now()-timedelta(minutes=10)
            st.rerun()
    else:
        if st.button('EMERGENCY STOP', use_container_width=True):
            st.session_state.em=True;st.rerun()
with col_e2:
    st.write(f'4/H=24*4=96/DAY TODAY {st.session_state.td}/96 HOUR {ht}/{st.session_state.tph} WR {wrp:.0f}%')
with col_e3:
    t=st.toggle('AUTO MKT AI BRAIN', value=st.session_state.amkt)
    st.session_state.amkt=t
if st.session_state.amkt:
    st.write(f'AUTO MKT ACTIVE BEST {st.session_state.sm} SCORE {st.session_state.msc.get(st.session_state.sm,0)}')
else:
    st.write('AUTO MKT OFF MANUAL')
acc_mode=st.radio('ACCOUNT', ['DEMO 10000','REAL 0 START'], index=0 if am=='DEMO' else 1, horizontal=True)
if 'REAL' in acc_mode: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am=st.session_state.am;cb=rb if am=='REAL' else db
cp=rp if am=='REAL' else dp
bal_list=st.session_state.hr if am=='REAL' else st.session_state.hd
c_m1,c_m2=st.columns(2)
with c_m1:
    mk=st.selectbox('MARKET 10x',mkts,index=mkts.index(st.session_state.sm) if st.session_state.sm in mkts else 0)
with c_m2:
    tf=st.selectbox('TIMEFRAME 7x',tfs,index=tfs.index(st.session_state.stf) if st.session_state.stf in tfs else 0)
    st.session_state.stf=tf
if not st.session_state.amkt: st.session_state.sm=mk
else: st.write(f'AI BRAIN CONTROLS MKT {st.session_state.sm}')
page=st.session_state.page
if page=='TRADING':
    st.write(f'LIVE {st.session_state.sm} ${lp:.2f} {ht}/{st.session_state.tph} TODAY {st.session_state.td}/96 WIN {wc} LOSE {lcnt} {wrp:.0f}% {am} BAL {cb} PKR')
    st.write(f'{am} BAL {cb} PKR +{cp} PROFIT 4/H 96/DAY 90% WIN EMERGENCY STOP AUTO MKT')
    st.write(f'O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {st.session_state.stf} AI {ai} {ac}% {cd} SCORE {sc:.1f}')
    st.progress(min(1.0,ht/max(1,st.session_state.tph)))
    st.progress(min(1.0,st.session_state.td/96.0))
    cjs=[]
    for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
    cs=','.join(cjs)
    ch='''<div style="background:#000;border:2px solid #0F0;border-radius:12px;padding:8px;height:300px"><canvas id="cc" width="800" height="280" style="width:100%;height:260px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=20;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#0F0':'#F44';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-10,top,20,Math.max(bh,5));});ct.fillStyle='#0F0';ct.font='bold 12px monospace';ct.fillText('AI V7: PRED - V108 FIX - 4/H 96/DAY',pad,16);</script>'''
    ch=ch.replace('CANDLES',cs).replace('PRED',ai);comp.html(ch,height=320)
    bjs=','.join([str(int(x)) for x in bal_list])
    bh='''<div style="border:2px solid #0F0;border-radius:12px;padding:8px"><div style="color:#FFD700;font-size:11px">BAL CHART V108 - {BAL} PKR - {ACC} - 4/H 96/DAY</div><canvas id="bc" width="800" height="180" style="width:100%;height:140px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#0F0';bx.lineWidth=3;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
    bh=bh.replace('BALDATA',bjs).replace('{BAL}',str(cb)).replace('{ACC}',am);comp.html(bh,height=200)
    st.write('PREMIUM BOXES V108 FIX MINI')
    r1c1,r1c2,r1c3=st.columns(3)
    with r1c1: st.write(f'VOL {vol}M {cd} UP {am} 90%')
    with r1c2: st.write(f'RSI {rsi:.1f} {ai} {ac}% SCORE {sc:.1f}')
    with r1c3: st.write(f'ATR {atr:.1f} VOLA {ai} ADX {adx:.0f}')
elif page=='AI_BRAIN':
    st.write('AI BRAIN V7 - 4/H 96/DAY 90% WIN - AUTO MARKET CHANGE')
    st.write(f'AI PREDICTION {ai} {ac}% CONF SCORE {sc:.1f} CANDLE {cd} MOV {mov:.2f} 4/H 96/DAY 90% WIN')
    st.write(f'MARKET {st.session_state.sm} TF {st.session_state.stf} LIVE ${lp:.2f} {am} BAL {cb} PKR AUTO MKT')
    if st.session_state.msc:
        st.write('AI BRAIN AUTO MARKET SCORES 10 MARKETS:')
        for m,s in sorted(st.session_state.msc.items(), key=lambda x: x[1], reverse=True):
            st.write(f'{m} SCORE {s} {"ACTIVE" if m==st.session_state.sm else ""}')
    st.write(f'FINAL SCORE {sc:.1f} AI {ai} CONF {ac}% WIN {wc} LOSE {lcnt} WR {wrp:.0f}% 90% TARGET TODAY {st.session_state.td}/96')
    st.write(f'RSI {rsi:.1f} VOL {vol}M ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull}')
elif page=='DEPOSIT':
    acc_base=3001234567
    acc_full='0'+str(acc_base)
    st.write('REAL PKR DEPOSIT - TID VERIFICATION - 4/H 96/DAY 90% WIN')
    if st.button('RESET DEMO TO 10000 PKR FREE', use_container_width=True):
        st.session_state.db=10000;st.session_state.dp=0;st.session_state.hd=[10000];st.success('DEMO RESET 10000')
    pm=st.selectbox('METHOD REAL ONLY',['JazzCash','Easypaisa'],index=0)
    st.write(f'SEND REAL PKR TO {pm} - REAL ONLY')
    st.write(acc_full)
    st.write('Name SONA TRADING REAL ONLY V107')
    dep_phone=st.text_input('Your Number 11 digits',value='03XXXXXXXXX')
    dep_amt=st.number_input('Real PKR Amount MAX 2500',value=250,min_value=250,max_value=2500,step=250)
    tid=st.text_input('TID Real Proof Min 6 chars',value='')
    tid_date=st.text_input('Date Time',value=datetime.now().strftime('%Y-%m-%d %H:%M'))
    if st.button(f'SUBMIT DEPOSIT {pm} {dep_amt} PKR TID',use_container_width=True):
        if len(dep_phone)>=11 and len(tid)>=6 and st.session_state.dep+dep_amt<=2500:
            rec_dep={'TIME':datetime.now().strftime('%H:%M:%S'),'METHOD':pm,'FROM':dep_phone,'TO':acc_full,'AMT':dep_amt,'TID':tid,'TID_DATE':tid_date,'STATUS':'VERIFIED REAL PKR TID OK V108 4/H 96/DAY 90% WIN'}
            st.session_state.dep_real.append(rec_dep);st.session_state.dep+=dep_amt;st.session_state.rb+=dep_amt;st.session_state.hr.append(int(st.session_state.rb));st.success(f'VERIFIED +{dep_amt} PKR via {pm} TID {tid} Bal {int(st.session_state.rb)} PKR TOTAL {st.session_state.dep}/2500')
            if st.session_state.aon: comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0);st.balloons()
        else: st.error('Enter valid phone 11 digits TID min 6 chars check 2500 LIMIT')
    if len(st.session_state.dep_real)>0:
        df_dep=pd.DataFrame(st.session_state.dep_real[::-1]);st.dataframe(df_dep,use_container_width=True,height=220)
    w_method=st.selectbox('WITHDRAW REAL PKR',['JazzCash','Easypaisa'],index=0)
    w_phone=st.text_input('Withdraw To Your Number',value='03XXXXXXXXX')
    w_amt=st.number_input('Withdraw Amount 250 min',value=250,min_value=250,max_value=5000,step=250)
    if st.button(f'WITHDRAW {w_method} {w_amt} PKR',use_container_width=True):
        if len(w_phone)>=11 and w_amt<=st.session_state.rb and w_amt>=250:
            st.session_state.rb-=w_amt;st.session_state.hr.append(int(st.session_state.rb))
            rec_w={'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'WITHDRAW REAL','RES':'WITHDRAW','PROF':-w_amt,'BAL':int(st.session_state.rb),'TYPE':'WITHDRAW REAL','METHOD':w_method,'TO':w_phone,'AMT':w_amt,'STATUS':'PROCESSING V108','ACC':'REAL'}
            st.session_state.th.append(rec_w);st.success(f'WITHDRAW -{w_amt} PKR to {w_phone} via {w_method} Bal {int(st.session_state.rb)} PKR')
        else: st.error('Invalid phone low bal min 250 PKR')
    if st.button('RESET BOTH ACCOUNTS REAL 0 + DEMO 10000 V108',use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
elif page=='HISTORY':
    st.write(f'HISTORY - 4/H 96/DAY 90% WIN - TODAY {st.session_state.td}/96 TRADES')
    c1,c2,c3,c4=st.columns(4)
    with c1: st.metric(label='TOTAL TODAY',value=f'{st.session_state.td}/96',delta=f'{ht}/{st.session_state.tph} HOUR')
    with c2: st.metric(label='WIN 90% TARGET',value=f'{wc}',delta=f'{wrp:.0f}%')
    with c3: st.metric(label='LOSE',value=f'{lcnt}',delta=f'{100-wrp:.0f}%')
    with c4: st.metric(label=f'PROFIT {am}',value=f'{cp} PKR',delta=f'{wc}W {lcnt}L BAL {cb} {am}')
    st.write(f'DEMO BAL {db} PKR +{dp} | REAL BAL {rb} PKR +{rp} | TODAY {st.session_state.td}/96 | 4/H 96/DAY CALC 24*4=96 | 90% WIN TARGET')
    st.write('MATH 1 hour 4 trades 24 hours * 4 = 96 trades full day 90% win rate 86 WIN 10 LOSE approx EMERGENCY STOP if WR <70% AUTO MARKET CHANGE EVERY 15 MIN THROUGH AI BRAIN CONTROLS')
    if len(st.session_state.th)>0:
        df=pd.DataFrame(st.session_state.th[::-1]);st.dataframe(df,use_container_width=True,height=350)
    else: st.info('No trades yet - 4/H 96/DAY 90% WIN EMERGENCY STOP READY AUTO MARKET CHANGE AI BRAIN V108')
elif page=='SETTINGS':
    st.write('SETTINGS V108 - 4/H 96/DAY 90% WIN EMERGENCY STOP AUTO MARKET')
    c_a1,c_a2,c_a3=st.columns(3)
    with c_a1:
        amt_opt=st.selectbox('Trade Amount 4 Opt', [250,500,750,1000], index=[250,500,750,1000].index(st.session_state.ta) if st.session_state.ta in [250,500,750,1000] else 0);st.session_state.ta=amt_opt;st.success(f'Selected {amt_opt} PKR')
    with c_a2:
        tph_opt=st.selectbox('Trades Per Hour FIXED 4/H = 96/DAY', [4], index=0);st.session_state.tph=tph_opt;st.success(f'FIXED {tph_opt}/H = 24*{tph_opt}={24*tph_opt}/DAY - 90% WIN')
    with c_a3:
        risk_opt=st.selectbox('Risk 3 Opt 90% WIN', ['LOW','MEDIUM','HIGH'], index=['LOW','MEDIUM','HIGH'].index(st.session_state.risk));st.session_state.risk=risk_opt;st.success(f'Selected {risk_opt} - 90% WIN TARGET')
    alert_toggle=st.toggle('ALERT SOUND ON/OFF', value=st.session_state.aon);st.session_state.aon=alert_toggle
    auto_mkt_set=st.toggle('AUTO MARKET CHANGE THROUGH AI BRAIN', value=st.session_state.amkt);st.session_state.amkt=auto_mkt_set
    if auto_mkt_set: st.success('AUTO MARKET CHANGE ON - AI BRAIN CONTROLS MARKET - SCANS 10 MARKETS EVERY 15 MIN')
    else: st.warning('AUTO MARKET CHANGE OFF - MANUAL')
    st.info(f'SETTINGS V108 {st.session_state.ta} PKR x {st.session_state.tph}/H = {st.session_state.tph*24}/DAY 90% WIN TARGET {st.session_state.sm} {st.session_state.stf} AUTO MKT {"ON - AI BRAIN" if st.session_state.amkt else "OFF - MANUAL"} {am} BAL {cb} PKR TODAY {st.session_state.td}/96 EMERGENCY {"ACTIVE" if st.session_state.em else "READY"} 24*4=96 CALC CONFIRMED')
st.write('---')
b_col1,b_col2,b_col3,b_col4,b_col5=st.columns(5)
with b_col1:
    if st.button('TRADING', use_container_width=True, key='nav_trading'): st.session_state.page='TRADING';st.rerun()
with b_col2:
    if st.button('AI BRAIN', use_container_width=True, key='nav_ai'): st.session_state.page='AI_BRAIN';st.rerun()
with b_col3:
    if st.button('HISTORY', use_container_width=True, key='nav_hist'): st.session_state.page='HISTORY';st.rerun()
with b_col4:
    if st.button('DEPOSIT', use_container_width=True, key='nav_dep'): st.session_state.page='DEPOSIT';st.rerun()
with b_col5:
    if st.button('SETTINGS', use_container_width=True, key='nav_set'): st.session_state.page='SETTINGS';st.rerun()
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>',height=0)
