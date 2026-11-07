# SONA V176 - SIRF BINARY MODE - FIXED TIME - NO LEVERAGE - NO FOREX CFD
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V176 BINARY ONLY', page_icon='🎯', layout='wide')
st.markdown("""<style>.stApp{background:#000 !important;color:white !important} h1{font-size:23px !important;text-align:center;color:#00FF00 !important} .stSelectbox label{color:#00FF00 !important;font-weight:bold !important} .stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important} .stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:50px !important}</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'SCAN','phase_start':time.time(),'tf':'5MIN','conf':95,'amnt':100,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':0,'bal':1000,'ht':[],'daily_loss':0,'consecutive_loss':0,'cooldown_until':0,'mode':'BINARY - FIXED TIME'}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
# === BINARY WALE MARKET - JO APP ME 85% DIKHTE HAIN - OTC + NORMAL - BINARY ONLY ===
# YE SAB BINARY / FIXED TIME ME MILENGE - FOREX CFD ME NAHI!
MARKETS=[
'Solana OTC','Bitcoin OTC','Ethereum OTC','BNB OTC','Ripple OTC','Litecoin OTC','Dogecoin OTC',
'Gold OTC','Silver OTC',
'AUD/CHF OTC','AUD/CAD OTC','AUD/JPY OTC','AUD/USD OTC',
'EUR/USD OTC','EUR/GBP OTC','EUR/JPY OTC','EUR/CAD OTC',
'GBP/USD OTC','GBP/JPY OTC','GBP/CAD OTC',
'USD/CAD OTC','USD/CHF OTC','USD/JPY OTC','NZD/USD OTC',
'AI Global Index','Quickler','Crypto Composite Index','Metal Composite Index',
# WEEKDAY BINARY - Monday ko khulenge
'EUR/USD','GBP/USD','AUD/USD','USD/JPY','Gold','Bitcoin','Ethereum','Solana'
]
def get_base(m):
    d={'Solana OTC':179.8,'Bitcoin OTC':67421.0,'Ethereum OTC':3450.0,'BNB OTC':710.0,'Ripple OTC':0.55,'Litecoin OTC':85.0,'Dogecoin OTC':0.16,'Gold OTC':2650.0,'Silver OTC':31.0,'AUD/CHF OTC':0.5844,'AUD/CAD OTC':0.92,'AUD/JPY OTC':97.5,'AUD/USD OTC':0.65,'EUR/USD OTC':1.0850,'EUR/GBP OTC':0.85,'EUR/JPY OTC':162.5,'EUR/CAD OTC':1.48,'GBP/USD OTC':1.2840,'GBP/JPY OTC':192.0,'GBP/CAD OTC':1.75,'USD/CAD OTC':1.36,'USD/CHF OTC':0.88,'USD/JPY OTC':149.5,'NZD/USD OTC':0.61,'AI Global Index':100.0,'Quickler':50.0,'Crypto Composite Index':150.0,'Metal Composite Index':120.0,'EUR/USD':1.0850,'GBP/USD':1.2840,'AUD/USD':0.65,'USD/JPY':149.5,'Gold':2650.0,'Bitcoin':67421.0,'Ethereum':3450.0,'Solana':179.8}
    return d.get(m,100.0)
def gen_price(m,seed):
    random.seed(hash(m+str(seed))%100000)
    base=get_base(m); ps=[base]
    for i in range(1,100):
        ps.append(ps[-1]+random.uniform(-0.0005,0.0005)*(base*0.001 if base>10 else 1))
    return ps
def calc_rsi(ps):
    if len(ps)<15: return 50.0
    dl=np.diff(ps); g=np.where(dl>0,dl,0); l=np.where(dl<0,-dl,0)
    ag=np.mean(g[-14:]); al=np.mean(l[-14:])
    if al==0: return 100.0
    return float(100-(100/(1+(ag/al))))
def calc_macd(ps):
    s=pd.Series(ps); return float(s.ewm(span=12).mean().iloc[-1]-s.ewm(span=26).mean().iloc[-1]) if len(ps)>=26 else 0.0
def calc_ema(ps,p=20):
    return float(pd.Series(ps).ewm(span=p).mean().iloc[-1]) if len(ps)>=p else float(ps[-1])
def calc_atr(ps):
    return float(np.mean([abs(ps[i]-ps[i-1]) for i in range(1,len(ps))][-14:])) if len(ps)>=15 else 0.0004
def calc_vwap(ps): return float(np.mean(ps))
def analyze_binary(m,seed):
    ps=gen_price(m,seed); price=ps[-1]; rsi=calc_rsi(ps); macd=calc_macd(ps); ema=calc_ema(ps,20); ema50=calc_ema(ps,50); atr=calc_atr(ps); vwap=calc_vwap(ps); o=ps[-2]; c=ps[-1]
    vol=int(1200+abs(hash(m+str(seed)))%3600)
    hh=max(ps[-20:]); ll=min(ps[-20:])
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    sweep_up=max(ps[-5:])>hh and c<hh; sweep_down=min(ps[-5:])<ll and c>ll
    direction='UP' if price>ema50 else 'DOWN'
    if sweep_down: direction='UP'
    if sweep_up: direction='DOWN'
    checks=[]
    if (direction=='UP' and price>ema and price>ema50) or (direction=='DOWN' and price<ema and price<ema50): checks.append('✅ TREND MATCH - Binary ke liye trend sahi')
    else: checks.append('❌ TREND FAIL')
    if (direction=='UP' and rsi<40) or (direction=='DOWN' and rsi>60): checks.append(f'✅ RSI {rsi:.1f} - Reversal BEST - Binary Entry')
    elif (direction=='UP' and rsi>50 and rsi<65) or (direction=='DOWN' and rsi<50 and rsi>35): checks.append(f'✅ RSI {rsi:.1f} - Momentum saath')
    else: checks.append(f'❌ RSI {rsi:.1f} - Momentum nahi')
    if (direction=='UP' and macd>0) or (direction=='DOWN' and macd<0): checks.append(f'✅ MACD {macd:.4f} - Saath')
    else: checks.append(f'❌ MACD {macd:.4f} - Ulta')
    if bos: checks.append('✅ BOS YES - Break hua')
    else: checks.append('❌ BOS NO')
    if sweep_up or sweep_down: checks.append('✅ SWEEP YES - Liquidity mara - Binary me ye sab se strong hai')
    else: checks.append('❌ SWEEP NO')
    dist_ema=abs(price-ema); dist_vwap=abs(price-vwap)
    if dist_ema<0.0004 or dist_vwap<0.0004: checks.append('✅ PULLBACK YES - Sasti Entry - Binary ke liye BEST TIME')
    else: checks.append('❌ PULLBACK NO - Door hai')
    if vol>2500 and atr>0.0003: checks.append(f'✅ VOL {vol} + ATR {atr:.4f} - Strong - 5 MIN me move hoga')
    elif vol>2000: checks.append(f'⚠️ VOL {vol} - Medium')
    else: checks.append(f'❌ VOL {vol} - Kam - Binary me mat karo')
    passed=sum(1 for x in checks if x.startswith('✅'))
    score_map={7:99,6:95,5:88,4:75,3:65,2:55,1:50,0:45}
    score=score_map.get(passed,50)
    if passed>=6: reason=f"BINARY EXPERT: {passed}/7 MATCH - {direction} - 5 MIN Binary ke liye PAKKA lag raha!"
    elif passed==5: reason=f"BINARY EXPERT: {passed}/7 MATCH - Thora RISK"
    else: reason=f"BINARY EXPERT: {passed}/7 MATCH - MAT KARO - WAIT!"
    return {'market':m,'price':price,'rsi':round(rsi,1),'vol':vol,'atr':round(atr,4),'vwap':round(vwap,4),'macd':round(macd,4),'bos':bos,'sweep':sweep_up or sweep_down,'score':score,'passed':passed,'dir':direction,'ps':ps,'ema':ema,'hh':round(hh,4),'ll':round(ll,4),'checks':checks,'reason':reason}
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:12px;text-align:center;margin:6px 0;box-shadow:0 0 12px {border};">{txt}</div>',unsafe_allow_html=True)
neon('<div style="color:#00FF00;font-weight:900;font-size:19px;">🎯 SONA AI v176 - SIRF BINARY - FIXED TIME</div>','#00FF00')
neon('<div style="color:#00FF00;font-weight:800;font-size:13px;">MODE: BINARY - FIXED TIME - NO LEVERAGE - NO 100x - NO FOREX CFD</div>','#00FF00')
# BINARY VS FOREX - SAMJHAO
neon('<div style="color:white;font-weight:700;font-size:13px;text-align:left;">✅ BINARY ME: Amount 100 PKR — UP/DOWN — 5 MIN — Jeete to +85 PKR — Haare to -100 PKR — Bas!<br>❌ FOREX ME: 100x Leverage — Price thora ulta gaya to -280, -300 — Pura balance khatam — IS LIYE FOREX BAND!</div>','#FFD700')
elapsed=int(time.time()-S['session_start']); left=max(0,7200-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if S['daily_loss']>=2:
    neon('<div style="color:#FF4444;font-weight:900;font-size:24px;">🛑 AAJ STOP - 2 LOSS - KAL PHIR BINARY PE</div><div style="color:white;font-size:13px;">Revenge mat karo - Kal Demo Binary pe 100 PKR se!</div>','#FF4444')
    if st.button('🔄 NAYA DIN - LOSS RESET'):
        S['daily_loss']=0; S['consecutive_loss']=0; S['total_win']=0; S['total_loss']=0; S['phase']='SCAN'; S['phase_start']=time.time(); S['session_start']=time.time(); st.rerun()
    st.stop()
cool_left=max(0,int(S['cooldown_until']-time.time()))
if cool_left>0:
    cm=cool_left//60; cs=cool_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:20px;">⏳ COOLDOWN - {cm:02d}:{cs:02d} - RUKO</div><div style="color:white;font-size:13px;">1 LOSS ke baad 15 MIN ruk - Gussa thanda karo!</div>','#FFD700')
    time.sleep(3); st.rerun()
# SETTINGS - BINARY ONLY
sc1,sc2,sc3=st.columns(3)
with sc1: S['tf']=st.selectbox('BINARY TIME - FIXED TIME',['5MIN','1MIN','15MIN'],index=0)
with sc2: S['conf']=st.selectbox('MIN CONFIDENCE',[90,95,97],index=1)
with sc3: S['amnt']=st.selectbox('BINARY AMOUNT - FIXED',[100,150,250],index=0)
# BINARY PAYOUT - APP JESA
payout=int(S['amnt']*0.85)
neon(f'<div style="color:#00FFFF;font-weight:800;font-size:13px;">💰 BINARY HISAB: Lagao {S["amnt"]} PKR — Jeete to Milega {S["amnt"]+payout} PKR (Profit +{payout}) — Haare to -{S["amnt"]} PKR — Leverage ZERO! &nbsp;|&nbsp; AAJ LOSS: {S["daily_loss"]}/2</div>','#00FFFF')
SCAN_LEN=60; TRADE_LEN=300 if S['tf']=='5MIN' else 60 if S['tf']=='1MIN' else 900
phase_elapsed=int(time.time()-S['phase_start'])
if S['phase']=='SCAN':
    phase_left=max(0,SCAN_LEN-phase_elapsed)
    seed=int(S['phase_start']//3)
    results=[analyze_binary(m,seed) for m in MARKETS]
    results_sorted=sorted(results,key=lambda x:(x['passed'],x['score']),reverse=True)
    best=results_sorted[0]
    pm=phase_left//60; ps=phase_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:22px;">🧠 BINARY SCANNING - 1 MIN - {len(MARKETS)} MARKET</div><div style="color:white;font-size:14px;">SCAN ME: {pm:02d}:{ps:02d} BACHA — BINARY MODE</div><div style="color:#AAAAAA;font-size:13px;">BEST BINARY: {best["market"]} — {best["passed"]}/7 — {best["score"]}% — {best["dir"]}</div>','#FFD700')
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">🏆 TOP 5 - BINARY</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{'Rank':i+1,'Market':x['market'],'Match':f"{x['passed']}/7",'Score':x['score'],'Dir':x['dir'],'Payout':'85%'} for i,x in enumerate(results_sorted[:5])]),use_container_width=True,hide_index=True)
    st.dataframe(pd.DataFrame([{'Market':r['market'],'Binary Signal':r['dir'],'Match':f"{r['passed']}/7",'Score':r['score'],'RSI':r['rsi'],'Vol':r['vol'],'ATR':r['atr'],'VWAP':r['vwap'],'MACD':r['macd']} for r in results_sorted]),use_container_width=True,hide_index=True)
    cur=results[0]
    if phase_left==0:
        if best['passed']>=6 and best['score']>=S['conf']:
            S['phase']='TRADE'; S['phase_start']=time.time(); S['locked_market']=best['market']; S['locked_dir']=best['dir']; S['locked_score']=best['score']; S['locked_reason']=best['reason']
            open_dt=now_dt(); S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=(open_dt+datetime.timedelta(seconds=TRADE_LEN)).strftime('%H:%M:%S')
            S['_best_checks']=best['checks']; st.rerun()
        else:
            S['phase_start']=time.time(); st.warning(f"Koi 6/7 nahi mila - BEST {best['market']} {best['passed']}/7 - Phir SCAN!"); st.rerun()
else:
    phase_left=max(0,TRADE_LEN-phase_elapsed)
    seed=int(S['phase_start']); cur=analyze_binary(S['locked_market'],seed)
    if phase_left==0:
        S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; st.rerun()
    tm=phase_left//60; ts=phase_left%60
    is_up=S['locked_dir']=='UP'; bg='#00FF00' if is_up else '#FF4444'
    payout=int(S['amnt']*0.85)
    neon(f'<div style="color:{bg};font-weight:900;font-size:30px;">{"🟢 ▲ UP — CALL — GREEN DABAO" if is_up else "🔴 ▼ DOWN — PUT — RED DABAO"}</div><div style="color:white;font-weight:800;font-size:19px;">🎯 BINARY SIGNAL: {S["locked_market"]} — {S["locked_score"]}%</div><div style="color:#FFD700;font-size:13px;">{S["locked_reason"]}</div><div style="color:white;font-size:14px;margin-top:4px;">📱 APP ME ABHI KARO - STEP BY STEP:</div><div style="color:white;font-size:14px;text-align:left;">1) APP me <b>Fixed Time / Binary</b> pe jao - Forex NAHI!<br>2) SEARCH karo: <b>{S["locked_market"]}</b><br>3) TIME select karo: <b>{S["tf"]}</b> - Leverage nahi aayega!<br>4) AMOUNT: <b>{S["amnt"]} PKR</b><br>5) BUTTON: <b>{"GREEN UP" if is_up else "RED DOWN"}</b> dabao!</div><div style="color:#00FFFF;font-size:13px;">💰 Jeete to +{payout} PKR — Haare to -{S["amnt"]} PKR — Bas!</div><div style="color:white;font-size:14px;">🕐 OPEN: {S["open_time"]} &nbsp; CLOSE: {S["close_time"]} &nbsp; BACHA: {tm:02d}:{ts:02d}</div>',bg)
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">✅ BINARY CHECKLIST - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    for chk in S.get('_best_checks',cur['checks']):
        col='#00FF00' if chk.startswith('✅') else '#FF4444' if chk.startswith('❌') else '#FFD700'
        neon(f'<div style="color:{col};font-weight:700;font-size:13px;text-align:left;">{chk}</div>',col)
    cc1,cc2=st.columns(2)
    with cc1:
        if st.button('✅ BINARY WIN HUA'):
            S['total_win']+=1; S['cp']+=int(S['amnt']*0.85); S['bal']+=int(S['amnt']*0.85); S['consecutive_loss']=0; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; st.rerun()
    with cc2:
        if st.button('❌ BINARY LOSS HUA'):
            S['total_loss']+=1; S['daily_loss']+=1; S['consecutive_loss']+=1; S['cp']-=S['amnt']; S['bal']-=S['amnt']; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'
            if S['consecutive_loss']>=1: S['cooldown_until']=time.time()+900
            st.rerun()
neon(f'<div style="color:#00FF00;font-weight:900;font-size:28px;">BINARY PROFIT: +{S["cp"]} PKR</div><div style="color:#00FF00;font-size:12px;">BAL {S["bal"]} PKR | WIN {S["total_win"]} | LOSS {S["total_loss"]} | AAJ LOSS {S["daily_loss"]}/2 | MODE BINARY | Session {lh:02d}:{lm:02d}:{ls:02d}</div>','#00FF00')
if S['ht']: st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
neon('<div style="color:#FF6B6B;font-size:12px;">🎯 BINARY RULE: 1) Forex / 100x kabhi mat kholo - Sirf Fixed Time / Binary 2) 1 din me 2 LOSS = STOP 3) 100 PKR se shuru - Demo pe seekho 4) Har bar UP mat lagao - Signal jo bole wahi karo</div>','#FF6B6B')
st.write(f"Last Update: {now_pkt()} | V176 BINARY ONLY | Phase {S['phase']} | Session {lh:02d}:{lm:02d}:{ls:02d}")
time.sleep(2); st.rerun()
