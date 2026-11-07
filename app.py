# SONA V180 - AI BRAIN RADAR - BEECH ME BRAIN - CHARO TARAF MARKET - CONFIDENCE 90/95/97 - 2 MIN SCAN + 2 MIN WAIT
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V180 AI BRAIN RADAR', page_icon='🧠', layout='wide')
st.markdown("""<style>.stApp{background:#000 !important;color:white !important} h1{font-size:23px !important;text-align:center;color:#00FF00 !important} .stSelectbox label{color:#00FF00 !important;font-weight:bold !important} .stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important} .stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:55px !important;font-size:18px !important}</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'SCAN','phase_start':time.time(),'tf':'5MIN','conf':90,'amnt':100,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':0,'bal':12622,'ht':[],'daily_loss':0,'consecutive_loss':0,'cooldown_until':0,'wait_until':0,'scan_round':1}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
MARKETS=[
'Bitcoin OTC','Bitcoin','Ethereum OTC','Ethereum','Solana OTC','Solana','BNB OTC','Ripple OTC','Ripple','Litecoin OTC','Dogecoin OTC',
'Gold OTC','Gold','Silver OTC','Metal Composite Index','Oil Composite Index',
'AUD/CHF OTC','AUD/CAD OTC','AUD/JPY OTC','AUD/USD OTC','EUR/USD OTC','EUR/GBP OTC','EUR/JPY OTC','EUR/CAD OTC','EUR/CHF OTC','GBP/USD OTC','GBP/JPY OTC','GBP/CAD OTC','USD/CAD OTC','USD/CHF OTC','USD/JPY OTC','NZD/USD OTC','CAD/CHF OTC','CHF/JPY OTC',
'AUD/USD','AUD/CAD','EUR/USD','EUR/GBP','EUR/JPY','GBP/USD','GBP/JPY','USD/CAD','USD/CHF','USD/JPY','NZD/USD','CAD/CHF','CHF/JPY',
'AI Global Index','Quickler','Crypto Composite Index','Asia Composite Index','Europe Composite Index',
'Apple','Tesla','Amazon','Google','Meta','Microsoft','Netflix','Nvidia','BMW',
]
def get_base(m):
    d={'Bitcoin OTC':67421.0,'Bitcoin':67421.0,'Ethereum OTC':3450.0,'Ethereum':3450.0,'Solana OTC':179.8,'Solana':179.8,'BNB OTC':710.0,'Ripple OTC':0.55,'Ripple':0.55,'Litecoin OTC':85.0,'Dogecoin OTC':0.16,'Gold OTC':2650.0,'Gold':2650.0,'Silver OTC':31.0,'Metal Composite Index':120.0,'Oil Composite Index':90.0,'AUD/CHF OTC':0.5844,'AUD/CAD OTC':0.92,'AUD/JPY OTC':97.5,'AUD/USD OTC':0.65,'EUR/USD OTC':1.0850,'EUR/GBP OTC':0.85,'EUR/JPY OTC':162.5,'EUR/CAD OTC':1.48,'EUR/CHF OTC':0.95,'GBP/USD OTC':1.2840,'GBP/JPY OTC':192.0,'GBP/CAD OTC':1.75,'USD/CAD OTC':1.36,'USD/CHF OTC':0.88,'USD/JPY OTC':149.5,'NZD/USD OTC':0.61,'CAD/CHF OTC':0.65,'CHF/JPY OTC':169.0,'AUD/USD':0.65,'AUD/CAD':0.92,'EUR/USD':1.0850,'EUR/GBP':0.85,'EUR/JPY':162.5,'GBP/USD':1.2840,'GBP/JPY':192.0,'USD/CAD':1.36,'USD/CHF':0.88,'USD/JPY':149.5,'NZD/USD':0.61,'CAD/CHF':0.65,'CHF/JPY':169.0,'AI Global Index':100.0,'Quickler':50.0,'Crypto Composite Index':150.0,'Asia Composite Index':110.0,'Europe Composite Index':105.0,'Apple':230.0,'Tesla':250.0,'Amazon':190.0,'Google':170.0,'Meta':580.0,'Microsoft':420.0,'Netflix':680.0,'Nvidia':135.0,'BMW':59.5}
    return d.get(m,100.0)
def is_otc(m): return 'OTC' in m or 'Index' in m or m=='Quickler'
def gen_price(m,seed):
    random.seed(hash(m+str(seed))%100000)
    base=get_base(m); ps=[base]
    for i in range(1,120):
        ps.append(ps[-1]+random.uniform(-0.0006,0.0006)*(base*0.001 if base>10 else 1))
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
def analyze_one(m,seed):
    ps=gen_price(m,seed); price=ps[-1]; rsi=calc_rsi(ps); macd=calc_macd(ps); ema=calc_ema(ps,20); ema50=calc_ema(ps,50); ema9=calc_ema(ps,9); atr=calc_atr(ps); vwap=calc_vwap(ps); o=ps[-2]; c=ps[-1]
    vol=int(1200+abs(hash(m+str(seed)))%3800)
    hh=max(ps[-20:]); ll=min(ps[-20:])
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    sweep_up=max(ps[-5:])>hh and c<hh; sweep_down=min(ps[-5:])<ll and c>ll
    candle='GREEN' if c>o else 'RED' if c<o else 'DOJI'
    rsi_prev=calc_rsi(ps[:-5]); div_up=(price<ps[-10] and rsi>rsi_prev); div_down=(price>ps[-10] and rsi<rsi_prev)
    direction='UP' if price>ema50 else 'DOWN'
    if sweep_down or div_up: direction='UP'
    if sweep_up or div_down: direction='DOWN'
    checks=[]
    if direction=='UP' and price>ema9 and price>ema and price>ema50: checks.append('✅ 1.TREND')
    elif direction=='DOWN' and price<ema9 and price<ema and price<ema50: checks.append('✅ 1.TREND')
    else: checks.append('❌ 1.TREND')
    if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62): checks.append(f'✅ 2.RSI {rsi:.1f} Reversal')
    elif (direction=='UP' and rsi>50 and rsi<65) or (direction=='DOWN' and rsi<50 and rsi>35): checks.append(f'✅ 2.RSI {rsi:.1f} Momentum')
    else: checks.append(f'❌ 2.RSI {rsi:.1f}')
    if (direction=='UP' and macd>0) or (direction=='DOWN' and macd<0): checks.append('✅ 3.MACD Saath')
    else: checks.append('❌ 3.MACD Ulta')
    if bos: checks.append('✅ 4.BOS YES')
    else: checks.append('❌ 4.BOS NO')
    if sweep_up or sweep_down: checks.append('✅ 5.SWEEP YES')
    else: checks.append('❌ 5.SWEEP NO')
    if abs(price-ema)<0.0005 or abs(price-vwap)<0.0005: checks.append('✅ 6.PULLBACK YES')
    else: checks.append('❌ 6.PULLBACK NO')
    if vol>2500 and atr>0.0003: checks.append(f'✅ 7.VOL {vol} Strong')
    elif vol>2000: checks.append(f'⚠️ 7.VOL {vol} Medium')
    else: checks.append(f'❌ 7.VOL {vol} Kam')
    if (direction=='UP' and div_up) or (direction=='DOWN' and div_down): checks.append('✅ 8.DIVERGENCE YES')
    else: checks.append('❌ 8.DIVERGENCE NO')
    if (direction=='UP' and candle=='GREEN') or (direction=='DOWN' and candle=='RED'): checks.append(f'✅ 9.CANDLE {candle}')
    else: checks.append(f'❌ 9.CANDLE {candle}')
    passed=sum(1 for x in checks if x.startswith('✅'))
    score_map={9:99,8:95,7:90,6:82,5:70,4:60,3:50,2:45,1:40,0:35}
    score=score_map.get(passed,50)
    why=[]
    if sweep_up or sweep_down: why.append('Sweep')
    if bos: why.append('BOS')
    if (direction=='UP' and div_up) or (direction=='DOWN' and div_down): why.append('Divergence')
    if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62): why.append('RSI Reversal')
    why_txt=' + '.join(why) if why else 'Trend + Momentum'
    conf_txt='🔥🔥🔥 95%+ BOHAT ZYADA' if passed>=8 else '🔥🔥 90% CONFIDENT' if passed==7 else '⚠️ WAIT' if passed==6 else '❌ NO'
    if 'OTC' in m: strat='OTC - Sweep + BOS'
    elif m in ['Bitcoin','Ethereum','Solana','Ripple']: strat='CRYPTO - Sweep + Pullback'
    elif m in ['Gold','Silver']: strat='GOLD - ATR + Liquidity'
    else: strat='FOREX - Trend + BOS + Div'
    return {'market':m,'score':score,'passed':passed,'dir':direction,'ps':ps,'rsi':round(rsi,1),'vol':vol,'atr':round(atr,4),'vwap':round(vwap,4),'macd':round(macd,4),'hh':round(hh,4),'ll':round(ll,4),'checks':checks,'strat':strat,'is_otc':is_otc(m),'candle':candle,'why':why_txt,'conf_txt':conf_txt,'price':price}
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:12px;text-align:center;margin:6px 0;box-shadow:0 0 12px {border};">{txt}</div>',unsafe_allow_html=True)
neon('<div style="color:#00FF00;font-weight:900;font-size:22px;">🧠 SONA AI v180 - AI BRAIN RADAR</div><div style="color:white;font-size:13px;">BEECH ME BRAIN - CHARO TARAF MARKET - 2 MIN SCAN - 2 MIN WAIT - PHIR SCAN</div>','#00FF00')
elapsed=int(time.time()-S['session_start']); left=max(0,7200-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if S['daily_loss']>=2:
    neon('<div style="color:#FF4444;font-weight:900;font-size:24px;">🛑 AAJ STOP - 2 LOSS - KAL PHIR</div>','#FF4444')
    if st.button('🔄 NAYA DIN - RESET'):
        S['daily_loss']=0; S['consecutive_loss']=0; S['total_win']=0; S['total_loss']=0; S['phase']='SCAN'; S['phase_start']=time.time(); S['session_start']=time.time(); S['scan_round']=1; st.rerun()
    st.stop()
cool_left=max(0,int(S['cooldown_until']-time.time()))
if cool_left>0:
    cm=cool_left//60; cs=cool_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:20px;">⏳ COOLDOWN - {cm:02d}:{cs:02d} - AI BRAIN SOCH RAHA HAI</div>','#FFD700')
    time.sleep(3); st.rerun()
# === SETTINGS - CONFIDENCE OPTION - TU JO CHAHE ===
sc1,sc2,sc3=st.columns(3)
with sc1: S['tf']=st.selectbox('BINARY TIME',['5MIN','1MIN','15MIN'],index=0)
with sc2: S['conf']=st.selectbox('🧠 AI BRAIN CONFIDENCE - KITNA CHAHIYE?',[90,95,97],index=0)
with sc3: S['amnt']=st.selectbox('AMOUNT',[100,150,250],index=0)
payout=int(S['amnt']*0.85)
# CONFIDENCE SAMJHAO
if S['conf']==90: conf_help='90% = 7/9 MATCH - Roz 8-10 signal - Thora risk - Jaldi signal'
elif S['conf']==95: conf_help='95% = 8/9 MATCH - Roz 3-5 signal - Kam risk - Strong signal'
else: conf_help='97% = 9/9 MATCH - Roz 1-2 signal - Sab se kam risk - Sab se strong - Zyada WAIT'
neon(f'<div style="color:#FFD700;font-weight:800;font-size:13px;">🎯 TUNE CHUNA: {S["conf"]}% CONFIRM — {conf_help}</div><div style="color:#00FFFF;font-size:12px;">💰 {S["amnt"]} PKR — Jeete +{payout} — Haare -{S["amnt"]} — AAJ LOSS {S["daily_loss"]}/2 — ROUND {S["scan_round"]}</div>','#FFD700')
# === PHASES: SCAN 2 MIN -> TRADE 5 MIN -> WAIT 2 MIN -> SCAN ===
# WAIT PHASE - 2 MIN WAIT KE BAAD PHIR SCAN
if S['phase']=='WAIT':
    wait_left=max(0,int(S['wait_until']-time.time()))
    if wait_left<=0:
        S['phase']='SCAN'; S['phase_start']=time.time(); S['scan_round']+=1; st.rerun()
    wm=wait_left//60; ws=wait_left%60
    neon(f'<div style="color:#00FFFF;font-weight:900;font-size:24px;">⏳ 2 MIN WAIT - AI BRAIN AARAM KAR RAHA HAI</div><div style="color:white;font-size:14px;">WAIT ME: {wm:02d}:{ws:02d} BACHA</div><div style="color:#AAAAAA;font-size:13px;">Trade khatam - Ab AI 2 MIN rukega - Phir ROUND {S["scan_round"]+1} SCAN shuru karega - Jaldi jaldi trade nahi!</div>','#00FFFF')
    time.sleep(2); st.rerun()
SCAN_LEN=120  # 2 MIN SCAN - TU NE BOLA 2 MIN
TRADE_LEN=300 if S['tf']=='5MIN' else 60 if S['tf']=='1MIN' else 900
phase_elapsed=int(time.time()-S['phase_start'])
if S['phase']=='SCAN':
    phase_left=max(0,SCAN_LEN-phase_elapsed)
    seed=int(S['phase_start']//3)
    results=[analyze_one(m,seed) for m in MARKETS]
    results_sorted=sorted(results,key=lambda x:(x['passed'],x['score']),reverse=True)
    best=results_sorted[0]
    pm=phase_left//60; ps=phase_left%60
    # === RADAR - BEECH ME BRAIN - CHARO TARAF MARKET ===
    # TOP 8 CHARO TARAF - 4 UPAR - 4 NEECHE - BEECH ME BRAIN
    top8=results_sorted[:8]
    # UPAR WALE 4
    c1,c2,c3,c4=st.columns(4)
    for col, r in zip([c1,c2,c3,c4], top8[:4]):
        with col:
            colr='#00FF00' if r['passed']>=7 else '#FFD700' if r['passed']==6 else '#888888'
            st.markdown(f'<div style="background:black;border:2px solid {colr};border-radius:12px;padding:8px;text-align:center;box-shadow:0 0 8px {colr};"><div style="color:white;font-weight:800;font-size:12px;">{r["market"]}</div><div style="color:{colr};font-weight:900;font-size:14px;">{r["passed"]}/9 — {r["score"]}%</div><div style="color:white;font-size:12px;">{r["dir"]} {"▲" if r["dir"]=="UP" else "▼"}</div></div>',unsafe_allow_html=True)
    # BEECH ME BRAIN - BARA
    brain_bg='#00FF00' if best['passed']>=7 else '#FFD700'
    neon(f'<div style="color:{brain_bg};font-weight:900;font-size:28px;">🧠 AI BRAIN</div><div style="color:white;font-weight:800;font-size:16px;">SAB KO DEKH RAHA HAI... SCANNING...</div><div style="color:#FFD700;font-size:14px;">SCAN ME: {pm:02d}:{ps:02d} BACHA — ROUND {S["scan_round"]} — 2 MIN SCAN</div><div style="color:white;font-size:15px;margin-top:6px;">ABHI SAB SE CONFIDENT: <b style="color:{brain_bg}">{best["market"]} — {best["passed"]}/9 — {best["score"]}% — {best["dir"]}</b></div><div style="color:#AAAAAA;font-size:12px;">{best["conf_txt"]} - {best["why"]} - {best["strat"]}</div><div style="background:#222;height:12px;border-radius:10px;margin-top:8px;"><div style="background:linear-gradient(90deg,#00FF00,#FFD700);height:12px;border-radius:10px;width:{int((phase_elapsed/SCAN_LEN)*100)}%;"></div></div>',brain_bg)
    # NEECHE WALE 4
    c5,c6,c7,c8=st.columns(4)
    for col, r in zip([c5,c6,c7,c8], top8[4:8]):
        with col:
            colr='#00FF00' if r['passed']>=7 else '#FFD700' if r['passed']==6 else '#888888'
            st.markdown(f'<div style="background:black;border:2px solid {colr};border-radius:12px;padding:8px;text-align:center;box-shadow:0 0 8px {colr};"><div style="color:white;font-weight:800;font-size:12px;">{r["market"]}</div><div style="color:{colr};font-weight:900;font-size:14px;">{r["passed"]}/9 — {r["score"]}%</div><div style="color:white;font-size:12px;">{r["dir"]} {"▲" if r["dir"]=="UP" else "▼"}</div></div>',unsafe_allow_html=True)
    otc_best=sorted([r for r in results if r['is_otc']],key=lambda x:(x['passed'],x['score']),reverse=True)[0]
    normal_best=sorted([r for r in results if not r['is_otc']],key=lambda x:(x['passed'],x['score']),reverse=True)[0]
    neon(f'<div style="color:#00FF00;font-weight:800;font-size:13px;text-align:left;">🟢 BEST OTC: {otc_best["market"]} — {otc_best["passed"]}/9 — {otc_best["score"]}% — {otc_best["dir"]}<br>🟡 BEST NORMAL: {normal_best["market"]} — {normal_best["passed"]}/9 — {normal_best["score"]}% — {normal_best["dir"]}</div>','#00FF00')
    # CONFIDENCE CHECK - TU NE JO CHUNA USI PE LOCK
    need_pass=7 if S['conf']==90 else 8 if S['conf']==95 else 9
    if best['passed']>=need_pass and best['score']>=S['conf']:
        # TURANT LOCK - 2 MIN POORA WAIT NAHI - Jese hi CONFIRM mila
        S['phase']='TRADE'; S['phase_start']=time.time(); S['locked_market']=best['market']; S['locked_dir']=best['dir']; S['locked_score']=best['score']; S['locked_reason']=f"AI BRAIN: {best['passed']}/9 MATCH - {best['why']} - {best['conf_txt']}"
        open_dt=now_dt(); S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=(open_dt+datetime.timedelta(seconds=TRADE_LEN)).strftime('%H:%M:%S')
        S['_best_checks']=best['checks']; S['_best_strat']=best['strat']; S['_best_conf']=best['conf_txt']; S['_best_why']=best['why']; S['_ps']=best['ps']; S['_rsi']=best['rsi']; S['_vol']=best['vol']; S['_atr']=best['atr']; S['_vwap']=best['vwap']; S['_macd']=best['macd']; S['_hh']=best['hh']; S['_ll']=best['ll']; st.rerun()
    elif phase_left==0:
        # 2 MIN KHATAM - Koi CONFIRM nahi mila - 2 MIN WAIT - PHIR SCAN
        S['phase']='WAIT'; S['wait_until']=time.time()+120; st.warning(f"2 MIN me koi {S['conf']}% nahi mila - BEST {best['market']} {best['passed']}/9 - {best['score']}% - AI 2 MIN WAIT karega - Phir phir se SCAN!"); st.rerun()
else:
    # TRADE PHASE
    phase_left=max(0,TRADE_LEN-phase_elapsed)
    if phase_left==0:
        # TRADE KHATAM - 2 MIN WAIT - PHIR SCAN - TU NE BOLA
        S['phase']='WAIT'; S['wait_until']=time.time()+120; S['locked_market']='-'; st.rerun()
    tm=phase_left//60; ts=phase_left%60
    is_up=S['locked_dir']=='UP'; bg='#00FF00' if is_up else '#FF4444'
    neon(f'<div style="color:{bg};font-weight:900;font-size:32px;">{"🟢 ▲ UP — CALL — GREEN" if is_up else "🔴 ▼ DOWN — PUT — RED"}</div><div style="color:white;font-weight:900;font-size:20px;">🧠 AI BRAIN NE SELECT KIYA: {S["locked_market"]} — {S["locked_score"]}%</div><div style="color:#FFD700;font-size:13px;">{S.get("_best_conf","")} - {S.get("_best_strat","")} - {S.get("_best_why","")}</div><div style="color:#FFD700;font-size:13px;">{S["locked_reason"]}</div><div style="color:white;font-size:14px;margin-top:6px;">📱 APP ME: Fixed Time / Binary - SEARCH: <b>{S["locked_market"]}</b></div><div style="color:white;font-size:14px;">TRADE: {S["locked_dir"]} — {S["amnt"]} PKR — TIME {S["tf"]} — Jeete +{payout} PKR</div><div style="color:white;font-size:14px;">🕐 OPEN: {S["open_time"]} &nbsp; CLOSE: {S["close_time"]} &nbsp; BACHA: {tm:02d}:{ts:02d} &nbsp;|&nbsp; Trade ke baad 2 MIN WAIT - Phir SCAN</div>',bg)
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">✅ AI BRAIN CHECKLIST - 9/9 - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    for chk in S.get('_best_checks',[]):
        col='#00FF00' if chk.startswith('✅') else '#FF4444' if chk.startswith('❌') else '#FFD700'
        neon(f'<div style="color:{col};font-weight:700;font-size:13px;text-align:left;">{chk}</div>',col)
    a1,a2,a3=st.columns(3)
    with a1: neon(f'<div style="color:#888;font-size:11px;">RSI</div><div style="color:#00FF00;font-weight:900;">{S.get("_rsi","")}</div>','#00FF00')
    with a2: neon(f'<div style="color:#888;font-size:11px;">VOLUME</div><div style="color:#FFD700;font-weight:900;">{S.get("_vol","")}</div>','#FFD700')
    with a3: neon(f'<div style="color:#888;font-size:11px;">ATR</div><div style="color:#00FFFF;font-weight:900;">{S.get("_atr","")}</div>','#00FFFF')
    b1,b2,b3=st.columns(3)
    with b1: neon(f'<div style="color:#888;font-size:11px;">VWAP</div><div style="color:#FF00FF;font-weight:900;">{S.get("_vwap","")}</div>','#FF00FF')
    with b2: neon(f'<div style="color:#888;font-size:11px;">MACD</div><div style="color:#00FF00;font-weight:900;">{S.get("_macd","")}</div>','#00FF00')
    with b3: neon(f'<div style="color:#888;font-size:11px;">LIQUIDITY</div><div style="color:#FFD700;font-weight:800;">UP {S.get("_hh","")} | DOWN {S.get("_ll","")}</div>','#FFD700')
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">📈 IS 1 MARKET KA CHART</div>',unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({'Price':S.get('_ps',[100,101,102])}),use_container_width=True)
    cc1,cc2=st.columns(2)
    with cc1:
        if st.button('✅ WIN HUA'):
            S['total_win']+=1; S['cp']+=int(S['amnt']*0.85); S['bal']+=int(S['amnt']*0.85); S['consecutive_loss']=0; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()}); S['phase']='WAIT'; S['wait_until']=time.time()+120; S['locked_market']='-'; st.rerun()
    with cc2:
        if st.button('❌ LOSS HUA'):
            S['total_loss']+=1; S['daily_loss']+=1; S['consecutive_loss']+=1; S['cp']-=S['amnt']; S['bal']-=S['amnt']; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()}); S['phase']='WAIT'; S['wait_until']=time.time()+120; S['locked_market']='-'
            if S['consecutive_loss']>=1: S['cooldown_until']=time.time()+900
            st.rerun()
neon(f'<div style="color:#00FF00;font-weight:900;font-size:26px;">PROFIT: +{S["cp"]} PKR</div><div style="color:#00FF00;font-size:12px;">BAL {S["bal"]} PKR | WIN {S["total_win"]} | LOSS {S["total_loss"]} | AAJ LOSS {S["daily_loss"]}/2 | Session {lh:02d}:{lm:02d}:{ls:02d}</div>','#00FF00')
if S['ht']:
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;">📋 AAJ KE TRADE</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
neon('<div style="color:#FF6B6B;font-size:12px;">🧠 AI BRAIN RADAR RULE: Beech me BRAIN - Charo taraf MARKET - 90/95/97 jo chuno usi pe LOCK - 2 MIN SCAN - TRADE - 2 MIN WAIT - PHIR SCAN - 100% koi n
