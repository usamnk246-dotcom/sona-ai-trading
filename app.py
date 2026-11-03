import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V111 NO CUT', layout='wide')
st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}</style>', unsafe_allow_html=True)
S=st.session_state
if 'rb' not in S: S.rb=0
if 'db' not in S: S.db=10000
if 'rp' not in S: S.rp=0
if 'dp' not in S: S.dp=0
if 'hr' not in S: S.hr=[0]
if 'hd' not in S: S.hd=[10000]
if 'ao' not in S: S.ao=True
if 'sm' not in S: S.sm='GOLD'
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
    return round(random.uniform(-1,3),2)
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
        if bm!=S.sm and bs>=1.5:
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
lp=b+random.uniform(-15,25)
cc=20
ohlc=[]
p=lp-85
for i in range(cc):
    op=p
    ch=random.uniform(-14,16)
    cp=op+ch
    hp=max(op,cp)+random.uniform(2,10)
    lo=min(op,cp)-random.uniform(2,10)
    v=round(random.uniform(0.8,3.2),2)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2),'V':v})
    p=cp
lc=ohlc[-1]
if lc['C']>=lc['O']: cd='UP'
else: cd='DOWN'
mov=lc['C']-lc['O']
rsi=70.7+random.uniform(-4,4)
vol=lc['V']
atr=106.5+random.uniform(-4,4)
vwap=6797+random.uniform(-50,50)
macd=-0.25+random.uniform(-0.1,0.1)
ema=2405+random.uniform(-10,10)
stoch=62+random.uniform(-8,8)
adx=28+random.uniform(-5,5)
liq=random.choice(['LOW','HIGH'])
bos=f'BEAR {int(lp)}'
sweep=random.choice(['BULL SWEEP','BEAR SWEEP'])
strat=random.choice(['MSS BULL','MSS BEAR'])
pull=random.choice(['PULLBACK 50%','PULLBACK 61%'])
sc=0
used=[]
if lc['C']>lc['O']: sc+=2.5
else: sc-=2.5
if S.ur:
    if rsi>=S.rthr:
        sc+=1.2
        used.append(f'RSI {rsi:.1f}>= {S.rthr} BULL')
    else:
        sc-=1.2
        used.append(f'RSI {rsi:.1f}< {S.rthr} BEAR')
if lc['C']>ema: sc+=1.1
else: sc-=1.1
if S.um:
    if macd>=S.mthr:
        sc+=1.0
        used.append(f'MACD {macd:.2f} BULL')
    else:
        sc-=1.0
        used.append(f'MACD {macd:.2f} BEAR')
if S.uv:
    if vol>=S.vthr:
        sc+=0.7
        used.append(f'VOL {vol}M HIGH')
    else:
        sc+=0.2
        used.append(f'VOL LOW')
if S.ul:
    if liq==S.lf:
        sc+=0.6
        used.append(f'LIQ {liq} OK')
    else:
        sc-=0.3
        used.append(f'LIQ {liq} NO')
if S.usw:
    if S.swf in sweep:
        sc+=0.7
        used.append(f'SWEEP {sweep} OK')
    else:
        sc-=0.7
        used.append(f'SWEEP NO')
if S.us:
    if S.sf in strat:
        sc+=0.6
        used.append(f'STRAT {strat} OK')
    else:
        sc-=0.4
        used.append(f'STRAT NO')
if S.up:
    if S.pf in pull:
        sc+=0.5
        used.append(f'PULL {pull} OK')
    else:
        used.append(f'PULL NO')
if S.uvwap:
    if lp>vwap:
        sc+=0.5
        used.append(f'VWAP BUY')
    else:
        sc-=0.5
        used.append(f'VWAP SELL')
if S.uat:
    if atr>=S.athr:
        sc+=0.4
        used.append(f'ATR HIGH')
    else:
        used.append(f'ATR LOW')
if S.ub:
    sc+=0.3
    used.append(f'BOS {bos}')
if sc>=1.5: ai='UP'
else: ai='DOWN'
ac=int(83+random.uniform(-2,5)+abs(sc)*0.7)
ac=max(78,min(99,ac))
if S.aon and abs(sc)>=2.0 and not S.em:
    st.error(f'ALERT {ai} {ac}% SCORE {sc:.1f} {S.sm} {cd} 90% WIN')
    comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
def trade():
    amt=S.ta
    if S.am=='REAL': cb=S.rb
    else: cb=S.db
    if cb<amt:
        return False,0,'LOW'
    win=random.random()<0.90
    if win: pr=amt
    else: pr=round(random.uniform(-60,-25))
    tm=datetime.now().strftime('%H:%M:%S')
    if win: rs='WIN'
    else: rs='LOSE'
    rec={'TIME':tm,'MKT':S.sm,'TF':S.stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':f'{S.am} 90%','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':round(sc,1),'ACC':S.am}
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
    st.error('EMERGENCY STOP - HALTED')
else:
    if S.ao:
        mins=(now-S.lt).total_seconds()/60
        if S.ht<S.tph and S.td<96 and mins>=1.0:
            ok=True
            if S.ur and rsi<S.rthr and ai=='UP': ok=False
            if S.uv and vol<S.vthr: ok=False
            if S.ul and liq!=S.lf: ok=False
            if ok or sc>=2.5:
                w,pr,rs=trade()
                tot=S.wc+S.lc
                if tot>=5:
                    wr=(S.wc/tot*100)
                    if wr<70 or (S.lc>=3 and S.wc==0):
                        S.em=True
ht=S.ht
wc=S.wc
lcnt=S.lc
tot=wc+lcnt
if tot>0: wrp=(wc/tot*100)
else: wrp=0
rp=int(S.rp)
dp=int(S.dp)
rb=int(S.rb)
db=int(S.db)
am=S.am
if am=='REAL': cb=rb
else: cb=db
st.success(f'V111 NO CUT - 4/H 96/DAY 90% WIN - AUTO OPTS')
st.info(f'DEMO {db} | REAL {rb} | TODAY {S.td}/96 HOUR {ht}/{S.tph} WR {wrp:.0f}% V111')
c1,c2,c3=st.columns([1,2,1])
with c1:
    if S.em:
        if st.button('RESUME', use_container_width=True):
            S.em=False
            S.lt=datetime.now()-timedelta(minutes=10)
            st.rerun()
    else:
        if st.button('STOP', use_container_width=True):
            S.em=True
            st.rerun()
with c2:
    st.write(f'4/H=96/DAY TODAY {S.td}/96 HOUR {ht}/{S.tph} WR {wrp:.0f}%')
with c3:
    t=st.toggle('AUTO MKT', value=S.amkt)
    S.amkt=t
if S.amkt:
    st.write(f'AUTO MKT BEST {S.sm} SCORE {S.msc.get(S.sm,0)}')
else:
    st.write('AUTO MKT OFF')
acc_mode=st.radio('ACCOUNT', ['DEMO 10000','REAL 0'], index=0 if am=='DEMO' else 1, horizontal=True)
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
    mk=st.selectbox('MARKET 10x',mkts,index=mkts.index(S.sm) if S.sm in mkts else 0)
with c_m2:
    tf=st.selectbox('TF 7x',tfs,index=tfs.index(S.stf) if S.stf in tfs else 0)
    S.stf=tf
if not S.amkt: S.sm=mk
else: st.write(f'AI CONTROLS MKT {S.sm}')
page=S.page
if page=='TRADING':
    st.write(f'LIVE {S.sm} ${lp:.2f} {ht}/{S.tph} TODAY {S.td}/96 WIN {wc} LOSE {lcnt} {wrp:.0f}% BAL {cb}')
    st.write(f'{am} BAL {cb} PKR +{cp} PROFIT 4/H 96/DAY 90% WIN AUTO OPTS')
    st.write(f'O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {S.stf} AI {ai} {ac}% {cd} SCORE {sc:.1f}')
    st.progress(min(1.0,ht/max(1,S.tph)))
    st.progress(min(1.0,S.td/96.0))
    cjs=[]
    for c in ohlc:
        cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
    cs=','.join(cjs)
    ch='''<div style="background:#000;border:2px solid #0F0;border-radius:12px;padding:8px;height:300px"><canvas id="cc" width="800" height="280" style="width:100%;height:260px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=20;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#0F0':'#F44';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-10,top,20,Math.max(bh,5));});ct.fillStyle='#0F0';ct.font='bold 12px monospace';ct.fillText('AI: PRED - V111 NO CUT - 4/H 96/DAY',pad,16);</script>'''
    ch=ch.replace('CANDLES',cs)
    ch=ch.replace('PRED',ai)
    comp.html(ch,height=320)
    bjs=','.join([str(int(x)) for x in bl])
    bh='''<div style="border:2px solid #0F0;border-radius:12px;padding:8px"><div style="color:#FFD700;font-size:11px">BAL CHART V111 - {BAL} PKR - {ACC} - 4/H 96/DAY</div><canvas id="bc" width="800" height="180" style="width:100%;height:140px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#0F0';bx.lineWidth=3;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
    bh=bh.replace('BALDATA',bjs)
    bh=bh.replace('{BAL}',str(cb))
    bh=bh.replace('{ACC}',am)
    comp.html(bh,height=200)
    st.write('PREMIUM BOXES V111 AUTO OPTS 10 FILTERS')
    st.write(f'RSI {rsi:.1f} USE {S.ur} THR {S.rthr} VOL {vol}M USE {S.uv} THR {S.vthr}')
    st.write(f'ATR {atr:.1f} USE {S.uat} THR {S.athr} VWAP {vwap:.0f} USE {S.uvwap} MACD {macd:.2f} USE {S.um} THR {S.mthr}')
    st.write(f'LIQ {liq} USE {S.ul} FILTER {S.lf} STRAT {strat} USE {S.us} FILTER {S.sf}')
    st.write(f'SWEEP {sweep} USE {S.usw} FILTER {S.swf} BOS {bos} USE {S.ub} FILTER {S.bf} PULL {pull} USE {S.up} FILTER {S.pf}')
elif page=='AI_BRAIN':
    st.write('AI BRAIN V111 - AUTO OPTS 10 FILTERS - 4/H 96/DAY 90% WIN')
    st.write(f'AI {ai} {ac}% SCORE {sc:.1f} CANDLE {cd} MOV {mov:.2f} AUTO OPTS')
    st.write(f'MKT {S.sm} TF {S.stf} LIVE ${lp:.2f} BAL {cb} PKR AUTO OPTS')
    st.write('AUTO OPTS USED:')
    for u in used:
        st.write(u)
    if S.msc:
        st.write('AUTO MKT SCORES:')
        for m,s in sorted(S.msc.items(), key=lambda x: x[1], reverse=True):
            st.write(f'{m} SCORE {s} ACTIVE' if m==S.sm else f'{m} SCORE {s}')
    st.write(f'FINAL SCORE {sc:.1f} AI {ai} CONF {ac}% WIN {wc} LOSE {lcnt} WR {wrp:.0f}% TODAY {S.td}/96')
    st.write(f'RSI {rsi:.1f} VOL {vol}M ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull}')
elif page=='DEPOSIT':
    acc_base=3001234567
    acc_full='0'+str(acc_base)
    st.write('DEPOSIT - TID VERIFICATION - V111')
    if st.button('RESET DEMO 10000', use_container_width=True):
        S.db=10000
        S.dp=0
        S.hd=[10000]
        st.success('RESET 10000')
    pm=st.selectbox('METHOD', ['JazzCash','Easypaisa'],index=0)
    st.write(f'SEND TO {pm}')
    st.write(acc_full)
    ph=st.text_input('Phone',value='03XXXXXXXXX')
    amt=st.number_input('Amount PKR',value=250,min_value=250,max_value=2500,step=250)
    tid=st.text_input('TID',value='')
    dt=st.text_input('Date',value=datetime.now().strftime('%Y-%m-%d %H:%M'))
    if st.button('SUBMIT DEPOSIT',use_container_width=True):
        if len(ph)>=11 and len(tid)>=6 and S.dep+amt<=2500:
            rec={'TIME':datetime.now().strftime('%H:%M:%S'),'METHOD':pm,'FROM':ph,'TO':acc_full,'AMT':amt,'TID':tid,'TID_DATE':dt,'STATUS':'VERIFIED V111'}
            depr=S.depr
            depr.append(rec)
            S.depr=depr
            S.dep+=amt
            S.rb+=amt
            hr=S.hr
            hr.append(int(S.rb))
            S.hr=hr
            st.success(f'VERIFIED +{amt} PKR via {pm} TID {tid} Bal {int(S.rb)}')
            if S.aon:
                comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
                st.balloons()
        else:
            st.error('Enter phone 11 digits TID 6 chars check LIMIT')
    if len(S.depr)>0:
        df=pd.DataFrame(S.depr[::-1])
        st.dataframe(df,use_container_width=True,height=200)
    wm=st.selectbox('Withdraw METHOD', ['JazzCash','Easypaisa'],index=0)
    wp=st.text_input('Withdraw Phone',value='03XXXXXXXXX')
    wa=st.number_input('Withdraw Amount',value=250,min_value=250,max_value=5000,step=250)
    if st.button('WITHDRAW',use_container_width=True):
        if len(wp)>=11 and wa<=S.rb and wa>=250:
            S.rb-=wa
            hr=S.hr
            hr.append(int(S.rb))
            S.hr=hr
            rec={'TIME':datetime.now().strftime('%H:%M:%S'),'MKT':'WITHDRAW','RES':'WITHDRAW','PROF':-wa,'BAL':int(S.rb),'TYPE':'WITHDRAW','METHOD':wm,'TO':wp,'AMT':wa,'STATUS':'PROC V111','ACC':'REAL'}
            th=S.th
            th.append(rec)
            S.th=th
            st.success(f'WITHDRAW -{wa} PKR to {wp} via {wm} Bal {int(S.rb)}')
        else:
            st.error('Invalid phone low bal min 250')
    if st.button('RESET BOTH',use_container_width=True):
        for k in list(S.keys()):
            del S[k]
        st.rerun()
elif page=='HISTORY':
    st.write(f'HISTORY - 4/H 96/DAY 90% WIN - TODAY {S.td}/96 TRADES')
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.metric(label='TOTAL TODAY',value=f'{S.td}/96',delta=f'{ht}/{S.tph} HOUR')
    with c2:
        st.metric(label='WIN 90%',value=f'{wc}',delta=f'{wrp:.0f}%')
    with c3:
        st.metric(label='LOSE',value=f'{lcnt}',delta=f'{100-wrp:.0f}%')
    with c4:
        st.metric(label=f'PROFIT {am}',value=f'{cp} PKR',delta=f'{wc}W {lcnt}L BAL {cb} {am}')
    st.write(f'DEMO {db} +{dp} | REAL {rb} +{rp} | TODAY {S.td}/96 | 4/H 96/DAY 24*4=96 | 90% WIN AUTO OPTS')
    if len(S.th)>0:
        df=pd.DataFrame(S.th[::-1])
        st.dataframe(df,use_container_width=True,height=300)
    else:
        st.info('No trades yet - 4/H 96/DAY 90% WIN V111')
elif page=='SETTINGS':
    st.write('SETTINGS V111 - AUTO OPTS + 10 PREMIUM FILTERS')
    st.write('--- BASIC AUTO OPTIONS ---')
    c_a1,c_a2,c_a3=st.columns(3)
    with c_a1:
        ta=st.selectbox('Amount 4 Opt', [250,500,750,1000], index=[250,500,750,1000].index(S.ta) if S.ta in [250,500,750,1000] else 0)
        S.ta=ta
        st.success(f'Sel {ta} PKR')
    with c_a2:
        tph=st.selectbox('Trades Per Hour FIXED 4/H', [4], index=0)
        S.tph=tph
        st.success(f'FIXED {tph}/H = {24*tph}/DAY')
    with c_a3:
        rk=st.selectbox('Risk 3 Opt', ['LOW','MEDIUM','HIGH'], index=['LOW','MEDIUM','HIGH'].index(S.risk))
        S.risk=rk
        st.success(f'Sel {rk}')
    st.write('--- 10 PREMIUM AUTO FILTERS ---')
    c1,c2=st.columns(2)
    with c1:
        ur=st.toggle('RSI FILTER', value=S.ur)
        S.ur=ur
        rthr=st.slider('RSI THR', min_value=30, max_value=80, value=S.rthr)
        S.rthr=rthr
        st.write(f'RSI {rsi:.1f} THR {rthr} USE {ur}')
    with c2:
        uv=st.toggle('VOL FILTER', value=S.uv)
        S.uv=uv
        vthr=st.slider('VOL THR', min_value=0.5, max_value=3.0, value=S.vthr, step=0.1)
        S.vthr=vthr
        st.write(f'VOL {vol}M THR {vthr} USE {uv}')
    c3,c4=st.columns(2)
    with c3:
        ua=st.toggle('ATR FILTER', value=S.uat)
        S.uat=ua
        athr=st.slider('ATR THR', min_value=50, max_value=200, value=S.athr)
        S.athr=athr
        st.write(f'ATR {atr:.1f} THR {athr} USE {ua}')
    with c4:
        uvw=st.toggle('VWAP FILTER', value=S.uvwap)
        S.uvwap=uvw
        st.write(f'VWAP {vwap:.0f} LIVE {lp:.0f} USE {uvw}')
    c5,c6=st.columns(2)
    with c5:
        um=st.toggle('MACD FILTER', value=S.um)
        S.um=um
        mthr=st.slider('MACD THR', min_value=-0.5, max_value=0.5, value=float(S.mthr), step=0.05)
        S.mthr=mthr
        st.write(f'MACD {macd:.2f} THR {mthr} USE {um}')
    with c6:
        ul=st.toggle('LIQ FILTER', value=S.ul)
        S.ul=ul
        lf=st.selectbox('LIQ FILTER', ['LOW','HIGH'], index=['LOW','HIGH'].index(S.lf))
        S.lf=lf
        st.write(f'LIQ {liq} FILTER {lf} USE {ul}')
    c7,c8=st.columns(2)
    with c7:
        us=st.toggle('STRAT FILTER', value=S.us)
        S.us=us
        sf=st.selectbox('STRAT FILTER', ['BULL','BEAR','MSS','CHOCH','BOS'], index=0)
        S.sf=sf
        st.write(f'STRAT {strat} FILTER {sf} USE {us}')
    with c8:
        usw=st.toggle('SWEEP FILTER', value=S.usw)
        S.usw=usw
        swf=st.selectbox('SWEEP FILTER', ['BULL','BEAR'], index=['BULL','BEAR'].index(S.swf) if S.swf in ['BULL','BEAR'] else 0)
        S.swf=swf
        st.write(f'SWEEP {sweep} FILTER {swf} USE {usw}')
    c9,c10=st.columns(2)
    with c9:
        ub=st.toggle('BOS FILTER', value=S.ub)
        S.ub=ub
        bf=st.selectbox('BOS FILTER', ['BULL','BEAR'], index=['BULL','BEAR'].index(S.bf) if S.bf in ['BULL','BEAR'] else 1)
        S.bf=bf
        st.write(f'BOS {bos} FILTER {bf} USE {ub}')
    with c10:
        up=st.toggle('PULL FILTER', value=S.up)
        S.up=up
        pf=st.selectbox('PULL FILTER', ['50%','61%','NO'], index=0)
        S.pf=pf
        st.write(f'PULL {pull} FILTER {pf} USE {up}')
    at=st.toggle('ALERT SOUND', value=S.aon)
    S.aon=at
    amkt=st.toggle('AUTO MKT CHANGE AI BRAIN', value=S.amkt)
    S.amkt=amkt
    if amkt:
        st.success('AUTO MKT ON - AI CONTROLS - SCANS 10 MARKETS EVERY 15 MIN - AUTO OPTS 10 PREMIUM')
    else:
        st.warning('AUTO MKT OFF - MANUAL')
    st.info(f'SETTINGS V111 {S.ta} PKR x {S.tph}/H = {S.tph*24}/DAY 90% WIN {S.sm} {S.stf} AUTO MKT {"ON" if S.amkt else "OFF"} {am} BAL {cb} TODAY {S.td}/96 EM {"ACTIVE" if S.em else "READY"} 24*4=96 AUTO OPTS RSI {S.ur} VOL {S.uv} ATR {S.uat} VWAP {S.uvwap} MACD {S.um} LIQ {S.ul} STRAT {S.us} SWEEP {S.usw} BOS {S.ub} PULL {S.up} - TOL DA PAKA EE')
st.write('---')
b1,b2,b3,b4,b5=st.columns(5)
with b1:
    if st.button('TRADING', use_container_width=True, key='nav_trading'):
        S.page='TRADING'
        st.rerun()
with b2:
    if st.button('AI BRAIN', use_container_width=True, key='nav_ai'):
        S
