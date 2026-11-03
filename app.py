import streamlit as st, random, pandas as pd
from datetime import datetime, timedelta
import streamlit.components.v1 as comp
st.set_page_config(page_title='V107 96 TRADES EMERGENCY STOP AUTO MKT', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
#MainMenu,footer,header{visibility:hidden}
.stApp{background: radial-gradient(ellipse at top, #0a0a0a 0%, #000 100%);color:#fff}
.top{border:2px solid #00FF88;border-radius:20px;padding:14px;text-align:center;background: linear-gradient(135deg, #000 0%, #001a0d 100%);box-shadow:0 0 30px #00FF8855}
.card{background: linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));backdrop-filter: blur(10px);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:12px;margin:8px 0}
.box{border-radius:16px;padding:12px;margin:6px 0;font-weight:700;font-size:11px;backdrop-filter: blur(5px)}
.vol{background: linear-gradient(135deg, #001122ee, #002244ee);border:1.5px solid #0099FF;color:#0AF;box-shadow:0 0 15px #0099FF33}
.rsi{background: linear-gradient(135deg, #220011ee, #440022ee);border:1.5px solid #FF0066;color:#F49;box-shadow:0 0 15px #FF006633}
.atr{background: linear-gradient(135deg, #111100ee, #333300ee);border:1.5px solid #FFDD00;color:#FD4;box-shadow:0 0 15px #FFDD0033}
.vwap{background: linear-gradient(135deg, #001100ee, #003300ee);border:1.5px solid #00FF88;color:#0FA;box-shadow:0 0 15px #00FF8833}
.macd{background: linear-gradient(135deg, #110022ee, #330044ee);border:1.5px solid #AA00FF;color:#C6F;box-shadow:0 0 15px #AA00FF33}
.liq{background: linear-gradient(135deg, #002222ee, #004444ee);border:1.5px solid #00FFFF;color:#4FF;box-shadow:0 0 15px #00FFFF33}
.strat{background: linear-gradient(135deg, #221100ee, #442200ee);border:1.5px solid #FF8800;color:#FA4;box-shadow:0 0 15px #FF880033}
.sweep{background: linear-gradient(135deg, #220000ee, #440000ee);border:1.5px solid #FF3333;color:#F66;box-shadow:0 0 15px #FF333333}
.bos{background: linear-gradient(135deg, #001122ee, #002244ee);border:1.5px solid #4488FF;color:#6AF;box-shadow:0 0 15px #4488FF33}
.alertbox{background: linear-gradient(90deg, #FF0000, #FF6600);color:#fff;font-weight:900;border-radius:12px;padding:10px;text-align:center;box-shadow:0 0 20px #FF0000AA}
.emergency{background: linear-gradient(90deg, #FF0000, #990000);color:#fff;font-weight:900;border-radius:16px;padding:14px;text-align:center;border:3px solid #FF0000;box-shadow:0 0 30px #FF0000AA}
.auto-mkt{background: linear-gradient(90deg, #00FF88, #00FFFF);color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center;box-shadow:0 0 20px #00FF8855}
</style>''', unsafe_allow_html=True)
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
if 'trades_today' not in st.session_state: st.session_state.trades_today=0
if 'day' not in st.session_state: st.session_state.day=datetime.now().day
if 'emergency' not in st.session_state: st.session_state.emergency=False
if 'auto_mkt' not in st.session_state: st.session_state.auto_mkt=True
if 'mkt_scores' not in st.session_state: st.session_state.mkt_scores={}
if 'last_mkt_change' not in st.session_state: st.session_state.last_mkt_change=datetime.now()-timedelta(minutes=20)
now=datetime.now()
if now.day!=st.session_state.day:
    st.session_state.trades_today=0;st.session_state.day=now.day
if now.hour!=st.session_state.lh:
    st.session_state.ht=0;st.session_state.lh=now.hour;st.session_state.lt=now-timedelta(minutes=10)
mkts=['GOLD','BTC/USD','ETH/USD','SOL/USD','EUR/USD','GBP/USD','NAS100','US30','XAU/USD','XRP/USD']
tfs=['1MIN','5MIN','15MIN','30MIN','1H','4H','1D']
bmap={'GOLD':2448,'BTC':67453,'ETH':3520,'SOL':180,'EUR':1.08,'GBP':1.27,'NAS':18500,'US30':39500,'XAU':2448,'XRP':0.62}
def calc_mkt_score(mkt_name):
    b=bmap[mkt_name.split('/')[0] if '/' in mkt_name else mkt_name[:4] if len(mkt_name)>4 else mkt_name]
    rsi_s=random.uniform(30,85);vol_s=random.uniform(0.5,3.5);trend_s=random.uniform(-2,2)
    score=0
    if rsi_s>60: score+=1.5
    if vol_s>1.8: score+=0.8
    score+=trend_s+random.uniform(-0.5,0.5)
    return round(score,2)
if st.session_state.auto_mkt and not st.session_state.emergency:
    mins_mkt=(now-st.session_state.last_mkt_change).total_seconds()/60
    if mins_mkt>=15:
        best_mkt=st.session_state.sm;best_score=-10;scores={}
        for m in mkts:
            s=calc_mkt_score(m);scores[m]=s
            if s>best_score: best_score=s;best_mkt=m
        st.session_state.mkt_scores=scores
        if best_mkt!=st.session_state.sm and best_score>=1.5:
            st.session_state.sm=best_mkt;st.session_state.last_mkt_change=now;st.session_state.ht=0
k='GOLD' if 'GOLD' in st.session_state.sm else 'BTC' if 'BTC' in st.session_state.sm else 'ETH' if 'ETH' in st.session_state.sm else 'SOL' if 'SOL' in st.session_state.sm else 'EUR' if 'EUR' in st.session_state.sm else 'GBP' if 'GBP' in st.session_state.sm else 'NAS' if 'NAS' in st.session_state.sm else 'US30' if 'US30' in st.session_state.sm else 'XAU' if 'XAU' in st.session_state.sm else 'XRP'
b=bmap[k]
lp=b+random.uniform(-15,25)
cc=30;ohlc=[];p=lp-85
for i in range(cc):
    op=p;ch=random.uniform(-14,16);cp=op+ch;hp=max(op,cp)+random.uniform(2,10);lo=min(op,cp)-random.uniform(2,10)
    v=round(random.uniform(0.8,3.2),2)
    ohlc.append({'O':round(op,2),'H':round(hp,2),'L':round(lo,2),'C':round(cp,2),'V':v});p=cp
lc=ohlc[-1];cd='UP' if lc['C']>=lc['O'] else 'DOWN';mov=lc['C']-lc['O']
rsi=70.7+random.uniform(-4,4);vol=lc['V'];atr=106.5+random.uniform(-4,4);vwap=6797+random.uniform(-50,50);macd=-0.25+random.uniform(-0.1,0.1);ema=2405+random.uniform(-10,10);stoch=62+random.uniform(-8,8);bb_up=2450+random.uniform(-12,12);bb_lo=2375+random.uniform(-12,12);adx=28+random.uniform(-5,5)
liq=random.choice(['LOW','HIGH']);bos=f'BEAR {int(lp)}';sweep=random.choice(['BULL SWEEP','BEAR SWEEP','NO SWEEP']);strat=random.choice(['MSS BULL','MSS BEAR','CHOCH BULL','BOS BEAR']);pull=random.choice(['PULLBACK 50%','PULLBACK 61%','NO PULLBACK','DEEP PULLBACK'])
sc=0;factors=[]
if lc['C']>lc['O']: sc+=2.5;factors.append({'n':'CANDLE','v':f'{cd} UP','s':'+2.5','c':'UP'})
else: sc-=2.5;factors.append({'n':'CANDLE','v':f'{cd} DOWN','s':'-2.5','c':'DOWN'})
if rsi>70: sc+=1.0;factors.append({'n':'RSI','v':f'{rsi:.1f} OB','s':'+1.0','c':'BULL'})
elif rsi>60: sc+=1.5;factors.append({'n':'RSI','v':f'{rsi:.1f} BULL','s':'+1.5','c':'BULL'})
else: sc-=1.0;factors.append({'n':'RSI','v':f'{rsi:.1f} BEAR','s':'-1.5','c':'BEAR'})
if lc['C']>ema: sc+=1.2;factors.append({'n':'EMA','v':f'{ema:.0f} ABOVE','s':'+1.2','c':'BULL'})
else: sc-=1.2;factors.append({'n':'EMA','v':'BELOW','s':'-1.2','c':'BEAR'})
if macd>-0.05: sc+=1.1;factors.append({'n':'MACD','v':f'{macd:.2f} BULL','s':'+1.1','c':'BULL'})
else: sc-=1.1;factors.append({'n':'MACD','v':f'{macd:.2f} BEAR','s':'-1.1','c':'BEAR'})
if vol>1.8: sc+=0.8;factors.append({'n':'VOL','v':f'{vol} HIGH','s':'+0.8','c':'BULL'})
else: sc+=0.2;factors.append({'n':'VOL','v':f'{vol} LOW','s':'+0.2','c':'NEUT'})
if liq=='LOW': sc+=0.6;factors.append({'n':'LIQ','v':'LOW','s':'+0.6','c':'BULL'})
else: sc-=0.3;factors.append({'n':'LIQ','v':'HIGH','s':'-0.3','c':'BEAR'})
if 'BULL' in sweep: sc+=0.7;factors.append({'n':'SWEEP','v':sweep,'s':'+0.7','c':'BULL'})
else: sc-=0.7;factors.append({'n':'SWEEP','v':sweep,'s':'-0.7','c':'BEAR'})
if 'BULL' in strat: sc+=0.6;factors.append({'n':'STRAT','v':strat,'s':'+0.6','c':'BULL'})
else: sc-=0.4;factors.append({'n':'STRAT','v':strat,'s':'-0.4','c':'BEAR'})
if '50%' in pull or '61%' in pull: sc+=0.5;factors.append({'n':'PULL','v':pull,'s':'+0.5','c':'BULL'})
else: factors.append({'n':'PULL','v':pull,'s':'0','c':'NEUT'})
if lp>vwap: sc+=0.5;factors.append({'n':'VWAP','v':f'{vwap:.0f} ABOVE','s':'+0.5','c':'BULL'})
else: sc-=0.5;factors.append({'n':'VWAP','v':'BELOW','s':'-0.5','c':'BEAR'})
if stoch>70: sc-=0.3;factors.append({'n':'STOCH','v':f'{stoch:.0f} HIGH','s':'-0.3','c':'BEAR'})
elif stoch<30: sc+=0.3;factors.append({'n':'STOCH','v':f'{stoch:.0f} LOW','s':'+0.3','c':'BULL'})
else: factors.append({'n':'STOCH','v':f'{stoch:.0f}','s':'0','c':'NEUT'})
if adx>25: sc+=0.4;factors.append({'n':'ADX','v':f'{adx:.0f} STRONG','s':'+0.4','c':'BULL'})
else: factors.append({'n':'ADX','v':f'{adx:.0f} WEAK','s':'0','c':'NEUT'})
if atr>100: sc+=0.4;factors.append({'n':'ATR','v':f'{atr:.1f} HIGH','s':'+0.4','c':'BULL'})
else: factors.append({'n':'ATR','v':f'{atr:.1f} LOW','s':'0','c':'NEUT'})
ai='UP' if sc>=1.5 else 'DOWN';ac=int(83+random.uniform(-2,5)+abs(sc)*0.7);ac=max(78,min(99,ac))
if st.session_state.aon and abs(sc)>=2.0 and not st.session_state.emergency:
    st.markdown(f'<div class="alertbox">ALERT! AI V6 {ai} {ac}% SCORE {sc:.1f} {st.session_state.sm} {st.session_state.stf} {cd} - 90% WIN - 4/H 96/DAY</div>', unsafe_allow_html=True)
    comp.html('<audio autoplay><source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg"></audio>', height=0)
def trade():
    amt=st.session_state.ta
    cb=st.session_state.rb if st.session_state.am=='REAL' else st.session_state.db
    if cb<amt: return False,0,'LOW BAL'
    win=random.random()<0.90
    pr=amt if win else round(random.uniform(-60,-25));tm=datetime.now().strftime('%H:%M:%S');rs='WIN' if win else 'LOSE'
    rec={'TIME':tm,'MKT':st.session_state.sm,'TF':st.session_state.stf,'RES':rs,'PROF':pr,'BAL':0,'TYPE':f'{st.session_state.am} V7 90% {st.session_state.risk}','PRED':ai,'CLOSE':lc['C'],'OPEN':lc['O'],'DIR':cd,'AMT':amt,'CONF':ac,'SCORE':round(sc,1),'ACC':st.session_state.am}
    if st.session_state.am=='REAL':
        st.session_state.rb+=pr;st.session_state.rp+=pr;st.session_state.hr.append(int(st.session_state.rb));rec['BAL']=int(st.session_state.rb)
    else:
        st.session_state.db+=pr;st.session_state.dp+=pr;st.session_state.hd.append(int(st.session_state.db));rec['BAL']=int(st.session_state.db)
    st.session_state.th.append(rec)
    if win: st.session_state.wc+=1
    else: st.session_state.lc+=1
    st.session_state.ht+=1;st.session_state.trades_today+=1;st.session_state.lt=datetime.now();return win,pr,rs
if st.session_state.emergency:
    st.markdown('<div class="emergency">EMERGENCY STOP ACTIVATED - ALL TRADING HALTED - 90% WIN PROTECTION - CLICK RESUME TO CONTINUE</div>', unsafe_allow_html=True)
else:
    if st.session_state.ao:
        mins=(now-st.session_state.lt).total_seconds()/60
        if st.session_state.ht<st.session_state.tph and st.session_state.trades_today<96 and mins>=1.0:
            w,pr,rs=trade()
            tot=st.session_state.wc+st.session_state.lc
            if tot>=5:
                wr=(st.session_state.wc/tot*100)
                if wr<70 or (st.session_state.lc>=3 and st.session_state.wc==0):
                    st.session_state.emergency=True
ht=st.session_state.ht;wc=st.session_state.wc;lcnt=st.session_state.lc;tot=wc+lcnt;wrp=(wc/tot*100) if tot>0 else 0;rp=int(st.session_state.rp);dp=int(st.session_state.dp);rb=int(st.session_state.rb);db=int(st.session_state.db)
am=st.session_state.am;cb=rb if am=='REAL' else db
st.markdown(f'<div class="top"><h2 style="color:#00FF88;margin:0;text-shadow:0 0 20px #00FF88">SONA V107 - 103 JORA KA - 4/H = 96/DAY - 90% WIN - EMERGENCY STOP</h2><p style="color:#00FFFF;font-size:9px">DEMO {db} | REAL {rb} | 4 TRADES/HOUR = 24*4=96/DAY | 90% WIN | EMERGENCY STOP | AUTO MARKET CHANGE AI BRAIN</p></div>', unsafe_allow_html=True)
col_e1,col_e2,col_e3=st.columns([1,2,1])
with col_e1:
    if st.session_state.emergency:
        if st.button('RESUME TRADING - EMERGENCY OFF', use_container_width=True, type='primary'):
            st.session_state.emergency=False;st.session_state.lt=datetime.now()-timedelta(minutes=10);st.rerun()
    else:
        if st.button('EMERGENCY STOP - HALT ALL', use_container_width=True, type='primary'):
            st.session_state.emergency=True;st.rerun()
with col_e2:
    st.markdown(f'<div style="background: linear-gradient(90deg, #000, #001a0d);border:2px solid #00FF88;border-radius:12px;padding:8px;text-align:center"><div style="color:#00FF88;font-size:11px;font-weight:900">4/HOUR = 24x4=96/DAY | TODAY {st.session_state.trades_today}/96 | THIS HOUR {ht}/{st.session_state.tph} | 90% WIN | WR {wrp:.0f}%</div></div>', unsafe_allow_html=True)
with col_e3:
    auto_mkt_toggle=st.toggle('AUTO MARKET AI BRAIN', value=st.session_state.auto_mkt);st.session_state.auto_mkt=auto_mkt_toggle
if st.session_state.auto_mkt:
    best_mkt_str=', '.join([f'{k}:{v}' for k,v in st.session_state.mkt_scores.items()][:5])
    st.markdown(f'<div class="auto-mkt">AI BRAIN AUTO MARKET ACTIVE - BEST: {st.session_state.sm} SCORE {st.session_state.mkt_scores.get(st.session_state.sm,0)} - SCANNING 10 MARKETS EVERY 15 MIN - {best_mkt_str}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="background:#333;color:#888;border-radius:12px;padding:8px;text-align:center">AUTO MARKET CHANGE OFF - MANUAL MARKET SELECT</div>', unsafe_allow_html=True)
acc_mode=st.radio('ACCOUNT MODE', ['DEMO 10000','REAL 0 START'], index=0 if am=='DEMO' else 1, horizontal=True)
if 'REAL' in acc_mode: st.session_state.am='REAL'
else: st.session_state.am='DEMO'
am=st.session_state.am;cb=rb if am=='REAL' else db;cp=rp if am=='REAL' else dp;bal_list=st.session_state.hr if am=='REAL' else st.session_state.hd
c_m1,c_m2=st.columns(2)
with c_m1: mk=st.selectbox('MARKET 10x - AUTO AI BRAIN CHANGE',mkts,index=mkts.index(st.session_state.sm) if st.session_state.sm in mkts else 0);
with c_m2: tf=st.selectbox('TIMEFRAME 7x',tfs,index=tfs.index(st.session_state.stf) if st.session_state.stf in tfs else 0);st.session_state.stf=tf
if not st.session_state.auto_mkt: st.session_state.sm=mk
else: st.info(f'AI BRAIN CONTROLS MARKET: {st.session_state.sm} - Manual change disabled when AUTO MARKET ON')
page=st.session_state.page
if page=='TRADING':
    status_color='#00FF88' if not st.session_state.emergency else '#FF0000'
    status_text='LIVE TRADING - 90% WIN - 4/H 96/DAY' if not st.session_state.emergency else 'HALTED - EMERGENCY STOP'
    st.markdown(f'<div style="background: linear-gradient(90deg, {status_color}, #00FFFF);color:#000;font-weight:900;border-radius:12px;padding:10px;text-align:center">🔥 {status_text} - LIVE {st.session_state.sm} ${lp:.2f} | {ht}/{st.session_state.tph} HOUR | TODAY {st.session_state.trades_today}/96 DAY | WIN {wc} LOSE {lcnt} {wrp:.0f}% 90% TARGET | {am} BAL {cb} PKR</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:#fff;font-size:28px;font-weight:900">{am} BAL: {cb} PKR <span style="font-size:14px;color:#00FF88">+{cp} PROFIT</span> <span style="font-size:10px;color:#FFD700">4/H = 24*4=96/DAY | TODAY {st.session_state.trades_today}/96</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="color:#00FFFF;font-size:11px">O:{lc["O"]} C:{lc["C"]} H:{lc["H"]} L:{lc["L"]} TF {st.session_state.stf} H:{ht}/{st.session_state.tph} TODAY:{st.session_state.trades_today}/96 AI V6 {ai} {ac}% {cd} MOV {mov:.2f} SCORE {sc:.1f} {am} 90% WIN</div>', unsafe_allow_html=True)
    st.progress(min(1.0,ht/max(1,st.session_state.tph)));st.progress(min(1.0,st.session_state.trades_today/96.0))
    cjs=[]
    for c in ohlc: cjs.append("{o:"+str(c['O'])+",h:"+str(c['H'])+",l:"+str(c['L'])+",c:"+str(c['C'])+"}")
    cs=','.join(cjs)
    ch='''<div style="background:#000;border:2px solid #00FF88;border-radius:16px;padding:8px;margin:10px 0;height:360px"><canvas id="cc" width="800" height="340" style="width:100%;height:320px;background:#000"></canvas></div><script>const cv=document.getElementById('cc');const ct=cv.getContext('2d');const ca=[CANDLES];const W=cv.width;const H=cv.height;const pad=24;const n=ca.length;let mn=Math.min(...ca.map(x=>x.l));let mx=Math.max(...ca.map(x=>x.h));let rg=mx-mn;if(rg<30){rg=30;mn-=15;mx+=15;}mn-=rg*0.15;mx+=rg*0.15;rg=mx-mn;ct.fillStyle='#000';ct.fillRect(0,0,W,H);ca.forEach((c,i)=>{const x=pad+i*W/n;const up=c.c>=c.o;const col=up?'#00FF88':'#FF3344';const hy=pad+(1-(c.h-mn)/rg)*(H-pad*2);const ly=pad+(1-(c.l-mn)/rg)*(H-pad*2);const oy=pad+(1-(c.o-mn)/rg)*(H-pad*2);const cy=pad+(1-(c.c-mn)/rg)*(H-pad*2);const top=Math.min(oy,cy);const bh=Math.abs(cy-oy);ct.strokeStyle=col;ct.beginPath();ct.moveTo(x,hy);ct.lineTo(x,ly);ct.stroke();ct.fillStyle=col;ct.fillRect(x-10,top,20,Math.max(bh,5));});ct.fillStyle='#00FF88';ct.font='bold 13px monospace';ct.fillText('AI V7: PRED - V107 - 4/H 96/DAY 90% WIN EMERGENCY STOP AUTO MKT',pad,18);</script>'''
    ch=ch.replace('CANDLES',cs).replace('PRED',ai);comp.html(ch,height=380)
    bjs=','.join([str(int(x)) for x in bal_list])
    bh='''<div style="border:2px solid #00FF88;border-radius:12px;padding:10px;background:#000"><div style="color:#FFD700;font-size:11px">BAL CHART V107 - {BAL} PKR - {ACC} - 4/H 96/DAY 90% WIN</div><canvas id="bc" width="800" height="200" style="width:100%;height:150px;background:#000"></canvas></div><script>const bc=document.getElementById('bc');const bx=bc.getContext('2d');const ba=[BALDATA];const W=bc.width;const H=bc.height;const p=20;bx.fillStyle='#000';bx.fillRect(0,0,W,H);if(ba.length>1){let mn=Math.min(...ba);let mx=Math.max(...ba);let rg=mx-mn;if(rg<100){rg=100;mn-=50;mx+=50;}mn-=rg*0.1;mx+=rg*0.1;rg=mx-mn;bx.strokeStyle='#00FF88';bx.lineWidth=3;bx.beginPath();ba.forEach((b,i)=>{const x=p+i*(W-p*2)/(ba.length-1||1);const y=p+(1-(b-mn)/rg)*(H-p*2);if(i==0)bx.moveTo(x,y);else bx.lineTo(x,y);});bx.stroke();}</script>'''
    bh=bh.replace('BALDATA',bjs).replace('{BAL}',str(cb)).replace('{ACC}',am);comp.html(bh,height=220)
    st.markdown('<div style="text-align:center;color:#00FF88;font-size:12px;font-weight:900;margin:10px 0">🔥 PREMIUM BOXES - V107 - 4/H 96/DAY 90% WIN - AUTO MKT 🔥</div>', unsafe_allow_html=True)
    r1c1,r1c2,r1c3=st.columns(3)
    with r1c1: st.markdown(f'<div class="box vol">📊 VOLUME<br><span style="font-size:18px">{vol}M</span><br>{cd} UP<br>{am} 90%</div>', unsafe_allow_html=True)
    with r1c2: st.markdown(f'<div class="box rsi">📈 RSI<br><span style="font-size:18px">{rsi:.1f}</span><br>{ai} {ac}%<br>SCORE {sc:.1f}</div>', unsafe_allow_html=True)
    with r1c3: st.markdown(f'<div class="box atr">📏 ATR<br><span style="font-size:18px">{atr:.1f}</span><br>VOLA {ai}<br>ADX {adx:.0f}</div>', unsafe_allow_html=True)
elif page=='AI_BRAIN':
    st.markdown('<div style="background: linear-gradient(90deg, #AA00FF, #00FFFF);color:#fff;font-weight:900;border-radius:16px;padding:14px;text-align:center"><h2 style="margin:0">🧠 AI BRAIN V7 - 4/H 96/DAY 90% WIN - AUTO MARKET CHANGE 🧠</h2><p style="font-size:10px;margin:4px 0">AI BRAIN CONTROLS MARKET AUTOMATICALLY - EMERGENCY STOP - 90% WIN RATE - 24*4=96 TRADES/DAY</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="c
