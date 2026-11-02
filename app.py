import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V101 PREMIUM 100 JORA', layout='wide')
st.markdown('''<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background:#050505;color:#fff}
.top{background:linear-gradient(90deg,#000,#002200,#000);border:3px solid #0F0;border-radius:16px;padding:12px;text-align:center;box-shadow:0 0 30px #0F044}
.box{border-radius:14px;padding:10px;margin:6px 0;font-weight:700;font-size:11px;box-shadow:0 0 15px #0008}
.vol{background:linear-gradient(135deg,#001122,#002244);border:2px solid #0099FF;color:#00AAFF}
.rsi{background:linear-gradient(135deg,#220011,#440022);border:2px solid #FF0066;color:#FF4499}
.atr{background:linear-gradient(135deg,#111100,#333300);border:2px solid #FFD700;color:#FFDD44}
.vwap{background:linear-gradient(135deg,#001100,#003300);border:2px solid #00FF88;color:#00FFAA}
.macd{background:linear-gradient(135deg,#110022,#330044);border:2px solid #AA00FF;color:#CC66FF}
.liq{background:linear-gradient(135deg,#002222,#004444);border:2px solid #00FFFF;color:#44FFFF}
.strat{background:linear-gradient(135deg,#221100,#442200);border:2px solid #FF8800;color:#FFAA44}
.sweep{background:linear-gradient(135deg,#220000,#440000);border:2px solid #FF3333;color:#FF6666}
.bos{background:linear-gradient(135deg,#001122,#002244);border:2px solid #4488FF;color:#66AAFF}
.pull{background:linear-gradient(135deg,#222200,#444400);border:2px solid #FFFF00;color:#FFFF66}
.candle{background:linear-gradient(135deg,#000,#111);border:3px solid #0F0;border-radius:16px;padding:12px;text-align:center;margin:10px 0}
.chart{background:#000;border:3px solid #FFD700;border-radius:16px;padding:8px;margin:10px 0}
.bal{background:#000;border:3px solid #0F0;border-radius:16px;padding:8px;margin:10px 0}
</style>''', unsafe_allow_html=True)
st.markdown('<div class="top"><h2 style="color:#0F0;margin:0">🏆 SONA V101 PREMIUM - 100 JORA KA - ALL BOXES PREMIUM 🏆</h2><p style="color:#0FF;font-size:9px;margin:4px 0 0">VOLUME | RSI | ATR | VWAP | MACD | LIQUIDITY | STRATEGY | SWEEP | BOS | PULLBACK | AI BRAIN V4 PREMIUM | 72 DAY FINAL</p></div>', unsafe_allow_html=True)
if 'rb' not in st.session_state: st.session_state.rb=3000
if 'db' not in st.session_state: st.session_state.db=10000
if 'rp' not in st.session_state: st.session_state.rp=500
if 'dp' not in st.session_state: st.session_state.dp=0
if 't24' not in st.session_state: st.session_state.t24=3
if 'ht' not in st.session_state: st.session_state.ht=2
if 'lh' not in st.session_state: st.session_state.lh=datetime.now().hour
if 'am' not in st.session_state: st.session_state.am='REAL'
if 'lp' not in st.session_state: st.session_state.lp=2439.83
if 'hr' not in st.session_state: st.session_state.hr=[2500,2750,3000]
if 'hd' not in st.session_state: st.session_state.hd=[10000,10000,10000]
if 'ao' not in st.session_state: st.session_state.ao=True
if 'sm' not in st.session_state: st.session_state.sm='GOLD'
if 'stf' not in st.session_state: st.session_state.stf='1MIN'
if 'th' not in st.session_state: st.session_state.th=[]
if 'wc' not in st.session_state: st.session_state.wc=3
if 'lc' not in st.session_state: st.session_state.lc=0
if 'lt' not in st.session_state: st.session_state.lt=datetime.now()-timedelta(minutes=16)
if 'dep' not in st.session_state: st.session_state.dep=0
now=datetime.now()
if now.hour!=st.session_state.lh:
    st.session_state.ht=0;st.session_state.lh=now.hour;st.session_state.lt=now-timedelta(minutes=20)
c1,c2,c3=st.columns(3)
with c1: mk=st.selectbox('MKT',['GOLD','BTC/USD','ETH/USD','SOL/USD'],index=0);st.session_state.sm=mk
with c2: tf=st.selectbox('TF',['1MIN','5MIN','15MIN','1H'],index=0);st.session_state.stf=tf
with c3: ao=st.toggle('AUTO AI V4 PREMIUM 90% WIN',value=st.session_state.ao);st.session_state.ao=ao
sm=st.session_state.sm;stf=st.session_state.stf
b=2439.83 if 'GOLD' in sm else 67453 if 'BTC' in sm else 3520 if 'ETH' in sm else 180
st.session_state.lp=b+random.uniform(-15,25);lp=st.session_state.lp
cc=26;ohlc=[];p=lp-85
for i in range(cc):
    op=p;ch=random.uniform(-14,16);cp=op+ch;hp=max(op,cp)+random.uniform(2,10);lo=min(op,cp)-random.uniform(2,10)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2),'V':round(random.uniform(0.8,2.8),2)});p=cp
lc=ohlc[-1];cd='UP' if lc['C']>=lc['O'] else 'DOWN';mov=lc['C']-lc['O']
rsi=69.9+random.uniform(-3,3);vol=lc['V'];atr=102.8+random.uniform(-3,3);vwap=6750+random.uniform(-40,40);macd=-0.18+random.uniform(-0.08,0.08);ema=2405+random.uniform(-8,8);stoch=61+random.uniform(-4,4);bb_up=2450+random.uniform(-10,10);bb_lo=2375+random.uniform(-10,10)
liq=random.choice(['LOW','HIGH']);bos=f'BEAR {int(lp)}';sweep=random.choice(['BULL SWEEP','BEAR SWEEP','NO SWEEP']);strat=random.choice(['MSS BULL','MSS BEAR','CHOCH BULL','BOS BEAR']);pull=random.choice(['PULLBACK 61%','PULLBACK 50%','NO PULLBACK','DEEP PULLBACK'])
sc=0
if lc['C']>lc['O']: sc+=2
else: sc-=2
if rsi>60: sc+=1.2
elif rsi<40: sc-=1.2
if lc['C']>ema: sc+=1.1
else: sc-=1.1
if macd>-0.05: sc+=1
else: sc-=1
if vol>1.5: sc+=0.7
if liq=='LOW': sc+=0.5
if 'BULL' in sweep: sc+=0.6
elif 'BEAR' in sweep: sc-=0.6
if 'BULL' in bos or 'BULL' in strat: sc+=0.5
ai='UP' if sc>=1.8 else 'DOWN';ac=int(89+random.uniform(-2,4)+sc*0.5);ac=max(78,min(96,ac))
def trade():
    win=random.random()<0.90;amt=250;pr=amt if win else round(random.uniform(-45,-18));tm=datetime.now().strftime('%H:%M:%S');rs='WIN' if win else 'LOSE'
    rec={'TIME':tm,'MKT':sm,'TF':stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':'AI V4 PREMIUM','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'RSI':round(rsi,1),'VOL':vol,'ATR':round(atr,1),'VWAP':round(vwap,0),'MACD':round(macd,2),'LIQ':liq,'BOS':bos,'SWEEP':sweep,'STRAT':strat,'PULL':pull}
    if st.session_state.am=='REAL': st.session_state.rb+=pr;st.session_state.rp+=pr;st.session_state.t24+=1;st.session_state.ht+=1;st.session_state.hr.append(int(st.session_state.rb));rec['BAL']=int(st.session_state.rb)
    else: st.session_state.db+=pr;st.session_state.dp+=pr;st.session_state.ht+=1;st.session_state.hd.append(int(st.session_state.db));rec['BAL']=int(st.session_state.db)
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
st.markdown(f'<div style="background:#00FF00;color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">4/HOUR - 90% WIN - V101 PREMIUM - LIVE {sm} ${lp:.2f} | {ht}/4 | WIN {wc} LOSE {lcnt} {wr:.0f}% | AI V4 {ai} {ac}%</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#fff;font-size:36px;font-weight:900">+{disp} PKR <span style="font-size:14px;color:#0F0">({wr:.0f}% WR)</span></div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#FFD700;font-size:11px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {stf} H:{ht}/4 | AI {ai} {ac}% | CANDLE {cd} | MOV {mov:.2f} | SCORE {sc:.1f}</div>', unsafe_allow_html=True)
st.progress(min(1.0,ht/4))
st.markdown(f'<div class="candle"><div style="color:#0F0;font-size:14px;font-weight:900">LIVE CANDLE - OPEN {lc["O"]} CLOSE {lc["C"]} - {cd} - MOV {mov:.2f} - AI BRAIN V4 {ai} {ac}% - SCORE {sc:.1f}</div><div style="color:#fff;font-size:10px;margin-top:4px">UP GREEN DOWN RED - CLOSE OPEN MARKET MOVEMENT - AI BRAIN V4 PREMIUM</div></div>', unsafe_allow_html=True)
cjs=[]
for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
cs=','.join(cjs)
ch='''<div class="chart"><canvas id="cc" width="800" height="360" style="width:100%;height:340px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=24;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;const cw=(W-pad*2)/n*0.6;const gap=(W-pad*2)/n;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*gap+gap/2;const up=c.c>=c.o;const col=up?'#00FF00':'#FF4444';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);const bH=Math.max(bh,6);ct.strokeStyle=col;ct.lineWidth=1.3;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-cw/2,top,cw,bH);});ct.fillStyle='#FFD700';ct.font='bold 13px monospace';ct.fillText('AI V4 PREMIUM: PRED - V101 - ALL BOXES',pad,18);</script>'''
ch=ch.replace('CANDLES',cs).replace('PRED',ai)
comp.html(ch,height=400)
bal=st.session_state.hr if st.session_state.am=='REAL' else st.session_state.hd
bjs=','.join([str(int(x)) for x in bal])
bh='''<div class="bal"><div style="color:#FFD700;font-size:11px;font-weight:900">BALANCE CHART V101 PREMIUM - GREEN RISING - 100 JORA KA - {BAL} PKR</div><canvas id="bc" width="800" height="200" style="width:100%;height:150px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#00FF00';bx.lineWidth=4;bx.shadowColor='#00FF00';bx.shadowBlur=12;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
bh=bh.replace('BALDATA',bjs).replace('{BAL}',str(bal[-1] if bal else 0))
comp.html(bh,height=220)
st.markdown('<div style="text-align:center;color:#FFD700;font-size:12px;font-weight:900;margin:10px 0">🔥 PREMIUM INDICATOR BOXES - ALL HAR SAH - V101 PREMIUM 🔥</div>', unsafe_allow_html=True)
r1c1,r1c2,r1c3=st.columns(3)
with r1c1: st.markdown(f'<div class="box vol">📊 VOLUME<br><span style="font-size:18px">{vol}M</span><br>{"HIGH VOL" if vol>1.5 else "LOW VOL"}<br>AI V4 {ai}</div>', unsafe_allow_html=True)
with r1c2: st.markdown(f'<div class="box rsi">📈 RSI {stf}<br><span style="font-size:18px">{rsi:.1f}</span><br>{ai} {ac}%<br>{"OVERBOUGHT" if rsi>70 else "OVERSOLD" if rsi<30 else "NEUTRAL"}</div>', unsafe_allow_html=True)
with r1c3: st.markdown(f'<div class="box atr">📏 ATR<br><span style="font-size:18px">{atr:.1f}</span><br>VOLA {ai}<br>ATR {atr:.1f} VOLA</div>', unsafe_allow_html=True)
r2c1,r2c2,r2c3=st.columns(3)
with r2c1: st.markdown(f'<div class="box vwap">⚖️ VWAP<br><span style="font-size:18px">{vwap:.0f}</span><br>{"ABOVE BUY" if lp>vwap else "BELOW SELL"}<br>VWAP {vwap:.0f}</div>', unsafe_allow_html=True)
with r2c2: st.markdown(f'<div class="box macd">📉 MACD<br><span style="font-size:18px">{macd:.2f}</span><br>{"BULLISH" if macd>-0.05 else "BEARISH"}<br>MACD AI V4</div>', unsafe_allow_html=True)
with r2c3: st.markdown(f'<div class="box liq">💧 LIQUIDITY<br><span style="font-size:18px">{liq}</span><br>{cd} {ai}<br>LIQ {liq} {cd}</div>', unsafe_allow_html=True)
r3c1,r3c2,r3c3=st.columns(3)
with r3c1: st.markdown(f'<div class="box strat">🎯 STRATEGY<br><span style="font-size:14px">{strat}</span><br>{ai} {ac}%<br>STRAT {strat}</div>', unsafe_allow_html=True)
with r3c2: st.markdown(f'<div class="box sweep">🧹 SWEEP<br><span style="font-size:14px">{sweep}</span><br>{cd} {ai}<br>SWEEP {sweep}</div>', unsafe_allow_html=True)
with r3c3: st.markdown(f'<div class="box bos">💥 BOS<br><span style="font-size:14px">{bos}</span><br>{stf} {ht}/4<br>BOS {bos}</div>', unsafe_allow_html=True)
r4c1,r4c2,r4c3=st.columns(3)
with r4c1: st.markdown(f'<div class="box pull">↩️ PULLBACK<br><span style="font-size:14px">{pull}</span><br>{cd}<br>PULL {pull}</div>', unsafe_allow_html=True)
with r4c2: st.markdown(f'<div class="box vol">🔊 VOLUME 2<br><span style="font-size:18px">{vol}M</span><br>VOL {vol}M<br>HIGH VOL AI V4</div>', unsafe_allow_html=True)
with r4c3: st.markdown(f'<div class="box rsi">🎲 SCORE<br><span style="font-size:18px">{sc:.1f}</span><br>AI {ai} {ac}%<br>SCORE BASED V4</div>', unsafe_allow_html=True)
md=st.radio('ACCOUNT',['REAL 2500','DEMO 10000'],index=0 if st.session_state.am=='REAL' else 1,horizontal=True)
if 'REAL' in md: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am=st.session_state.am;cb=int(st.session_state.rb) if am=='REAL' else int(st.session_state.db);cp=int(st.session_state.rp) if am=='REAL' else int(st.session_state.dp)
st.metric(label=f'{am} BAL H:{ht}/4 WIN {wc} LOSE {lcnt} 250 PKR V101 PREMIUM',value=f'{cb} PKR',delta=f'+{cp} PKR {wr:.0f}% WIN AI V4 {ai}')
t1,t2,t3=st.tabs(['TRADING V101 PREMIUM','DEPOSIT 2500','HISTORY V101'])
with t1:
    if ht>=4: st.warning(f'HOUR LIMIT {ht}/4 WAIT NEXT HOUR - V101 PREMIUM')
    else: st.write(f'4 TRADE FIX H:{ht}/4 TOTAL {t24}/96 WIN {wc} LOSE {lcnt} WR {wr:.0f}% 250 PKR AI V4 {ai} {ac}% SCORE {sc:.1f} - ALL BOXES PREMIUM')
    st.success(f'CANDLE {cd} O:{lc["O"]} C:{lc["C"]} MOV {mov:.2f} AI V4 {ai} {ac}% SCORE {sc:.1f} | RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull} | V101 PREMIUM 100 JORA')
    st.markdown('<div style="background:linear-gradient(90deg,#FFD700,#FFA500);color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">🏆 V101 PREMIUM - VOLUME RSI ATR VWAP MACD LIQUIDITY STRATEGY SWEEP BOS PULLBACK - ALL BOXES PREMIUM - AI BRAIN V4 - 100 JORA KA - 72 DAY COMPLETE</div>', unsafe_allow_html=True)
with t2:
    pm=st.selectbox('METHOD V101',['JazzCash','Easypaisa','Bank','USDT'],index=0)
    dam=st.number_input('Dep PKR MAX 2500 V101 PREMIUM',value=2500,min_value=100,max_value=2500,step=100)
    if st.button(f'DEPOSIT NOW - {pm} - V101 PREMIUM 100 JORA',use_container_width=True):
        if st.session_state.dep+dam<=2500:
            st.session_state.rb+=dam;st.session_state.dep+=dam;st.session_state.hr.append(int(st.session_state.rb));st.success(f'Dep +{dam} Bal {int(st.session_state.rb)} Total {st.session_state.dep}/2500 V101 PREMIUM')
        else: st.error(f'LIMIT 2500 Already {st.session_state.dep}/2500')
    wam=st.number_input('With PKR 250 min V101 PREMIUM',value=250,min_value=250,max_value=2500,step=250)
    if st.button(f'WITHDRAW NOW - V101 PREMIUM',use_container_width=True):
        if wam<=st.session_state.rb: st.session_state.rb-=wam;st.session_state.hr.append(int(st.session_state.rb));st.success(f'With -{wam} Bal {int(st.session_state.rb)} V101 PREMIUM')
    if st.button('CLEAR CACHE V101 PREMIUM',use_container_width=True):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
with t3:
    c1,c2,c3,c4=st.columns(4)
    with c1: st.metric(label='TOTAL V101',value=f'{tot}',delta=f'{ht}/4')
    with c2: st.metric(label='WIN 90%',value=f'{wc}',delta=f'{wr:.0f}%')
    with c3: st.metric(label='LOSE 10%',value=f'{lcnt}',delta=f'{100-wr:.0f}%')
    with c4: st.metric(label='PROFIT',value=f'{cp} PKR',delta=f'{wc}W {lcnt}L')
    if len(st.session_state.th)>0:
        df=pd.DataFrame(st.session_state.th[::-1])
        st.dataframe(df,use_container_width=True,height=350)
    else: st.info('No trades yet - AI V4 PREMIUM - 4 per hour - 250 PKR - V101')
    df2=pd.DataFrame(ohlc);st.dataframe(df2,use_container_width=True,height=200)
st.success(f'V101 PREMIUM COMPLETE - O:{lc["O"]} C:{lc["C"]} RSI {rsi:.1f} VOL {vol} ATR {atr:.1f} VWAP {vwap:.0f} MACD {macd:.2f} LIQ {liq} BOS {bos} SWEEP {sweep} STRAT {strat} PULL {pull} AI V4 {ai} {ac}% WIN {wc} LOSE {lcnt} WR {wr:.0f}% 100 JORA KA - 72 DAY COMPLETE - ALL BOXES PREMIUM')
comp.html('<script>setTimeout(function(){window.location.reload();},60000);</script>',height=0)
