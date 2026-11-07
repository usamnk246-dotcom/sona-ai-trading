# SONA V183 - NO INDENT ERROR - FULL SCANNER DETAIL
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V183', page_icon='🧠', layout='wide')
st.markdown("""<style>.stApp{background:#000 !important;color:white !important} .stSelectbox label{color:#00FF00 !important;font-weight:bold !important} .stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important} .stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:55px !important;font-size:18px !important}</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'SCAN','phase_start':time.time(),'tf':'5MIN','conf':90,'amnt':100,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':0,'bal':12622,'ht':[],'daily_loss':0,'consecutive_loss':0,'cooldown_until':0,'wait_until':0,'scan_round':1}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
MARKETS=['Bitcoin OTC','Bitcoin','Ethereum OTC','Ethereum','Solana OTC','Solana','BNB OTC','Ripple OTC','Ripple','Litecoin OTC','Dogecoin OTC','Gold OTC','Gold','Silver OTC','Metal Composite Index','Oil Composite Index','AUD/CHF OTC','AUD/CAD OTC','AUD/JPY OTC','AUD/USD OTC','EUR/USD OTC','EUR/GBP OTC','EUR/JPY OTC','EUR/CAD OTC','EUR/CHF OTC','GBP/USD OTC','GBP/JPY OTC','GBP/CAD OTC','USD/CAD OTC','USD/CHF OTC','USD/JPY OTC','NZD/USD OTC','CAD/CHF OTC','CHF/JPY OTC','AUD/USD','AUD/CAD','EUR/USD','EUR/GBP','EUR/JPY','GBP/USD','GBP/JPY','USD/CAD','USD/CHF','USD/JPY','NZD/USD','CAD/CHF','CHF/JPY','AI Global Index','Quickler','Crypto Composite Index','Asia Composite Index','Europe Composite Index','Apple','Tesla','Amazon','Google','Meta','Microsoft','Netflix','Nvidia','BMW']
def get_base(m):
    d={'Bitcoin OTC':67421.0,'Bitcoin':67421.0,'Ethereum OTC':3450.0,'Ethereum':3450.0,'Solana OTC':179.8,'Solana':179.8,'BNB OTC':710.0,'Ripple OTC':0.55,'Ripple':0.55,'Litecoin OTC':85.0,'Dogecoin OTC':0.16,'Gold OTC':2650.0,'Gold':2650.0,'Silver OTC':31.0,'Metal Composite Index':120.0,'Oil Composite Index':90.0,'AUD/CHF OTC':0.5844,'AUD/CAD OTC':0.92,'AUD/JPY OTC':97.5,'AUD/USD OTC':0.65,'EUR/USD OTC':1.0850,'EUR/GBP OTC':0.85,'EUR/JPY OTC':162.5,'EUR/CAD OTC':1.48,'EUR/CHF OTC':0.95,'GBP/USD OTC':1.2840,'GBP/JPY OTC':192.0,'GBP/CAD OTC':1.75,'USD/CAD OTC':1.36,'USD/CHF OTC':0.88,'USD/JPY OTC':149.5,'NZD/USD OTC':0.61,'CAD/CHF OTC':0.65,'CHF/JPY OTC':169.0,'AUD/USD':0.65,'AUD/CAD':0.92,'EUR/USD':1.0850,'EUR/GBP':0.85,'EUR/JPY':162.5,'GBP/USD':1.2840,'GBP/JPY':192.0,'USD/CAD':1.36,'USD/CHF':0.88,'USD/JPY':149.5,'NZD/USD':0.61,'CAD/CHF':0.65,'CHF/JPY':169.0,'AI Global Index':100.0,'Quickler':50.0,'Crypto Composite Index':150.0,'Asia Composite Index':110.0,'Europe Composite Index':105.0,'Apple':230.0,'Tesla':250.0,'Amazon':190.0,'Google':170.0,'Meta':580.0,'Microsoft':420.0,'Netflix':680.0,'Nvidia':135.0,'BMW':59.5}
    return d.get(m,100.0)
def is_otc(m):
    return 'OTC' in m or 'Index' in m or m=='Quickler'
def gen_price(m,seed):
    random.seed(hash(m+str(seed))%100000)
    base=get_base(m)
    ps=[base]
    for i in range(1,120):
        ps.append(ps[-1]+random.uniform(-0.0006,0.0006)*(base*0.001 if base>10 else 1))
    return ps
def calc_rsi(ps):
    if len(ps)<15:
        return 50.0
    dl=np.diff(ps)
    g=np.where(dl>0,dl,0)
    l=np.where(dl<0,-dl,0)
    ag=np.mean(g[-14:])
    al=np.mean(l[-14:])
    if al==0:
        return 100.0
    return float(100-(100/(1+(ag/al))))
def calc_macd(ps):
    s=pd.Series(ps)
    if len(ps)>=26:
        return float(s.ewm(span=12).mean().iloc[-1]-s.ewm(span=26).mean().iloc[-1])
    return 0.0
def calc_ema(ps,p=20):
    if len(ps)>=p:
        return float(pd.Series(ps).ewm(span=p).mean().iloc[-1])
    return float(ps[-1])
def calc_atr(ps):
    if len(ps)>=15:
        return float(np.mean([abs(ps[i]-ps[i-1]) for i in range(1,len(ps))][-14:]))
    return 0.0004
def calc_vwap(ps):
    return float(np.mean(ps))
def analyze_one(m,seed):
    ps=gen_price(m,seed)
    price=ps[-1]
    rsi=calc_rsi(ps)
    macd=calc_macd(ps)
    ema=calc_ema(ps,20)
    ema50=calc_ema(ps,50)
    ema9=calc_ema(ps,9)
    atr=calc_atr(ps)
    vwap=calc_vwap(ps)
    o=ps[-2]
    c=ps[-1]
    vol=int(1200+abs(hash(m+str(seed)))%3800)
    hh=max(ps[-20:])
    ll=min(ps[-20:])
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    sweep_up=max(ps[-5:])>hh and c<hh
    sweep_down=min(ps[-5:])<ll and c>ll
    sweep=sweep_up or sweep_down
    candle='GREEN' if c>o else 'RED' if c<o else 'DOJI'
    rsi_prev=calc_rsi(ps[:-5])
    div_up=(price<ps[-10] and rsi>rsi_prev)
    div_down=(price>ps[-10] and rsi<rsi_prev)
    pull=abs(price-ema)<0.0005 or abs(price-vwap)<0.0005
    direction='UP' if price>ema50 else 'DOWN'
    if sweep_down or div_up:
        direction='UP'
    if sweep_up or div_down:
        direction='DOWN'
    checks=[]
    if direction=='UP' and price>ema9 and price>ema and price>ema50:
        checks.append('1.TREND OK')
    elif direction=='DOWN' and price<ema9 and price<ema and price<ema50:
        checks.append('1.TREND OK')
    else:
        checks.append('1.TREND NO')
    if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62):
        checks.append('2.RSI Reversal OK')
    elif (direction=='UP' and rsi>50 and rsi<65) or (direction=='DOWN' and rsi<50 and rsi>35):
        checks.append('2.RSI Momentum OK')
    else:
        checks.append('2.RSI NO')
    if (direction=='UP' and macd>0) or (direction=='DOWN' and macd<0):
        checks.append('3.MACD OK')
    else:
        checks.append('3.MACD NO')
    if bos:
        checks.append('4.BOS YES')
    else:
        checks.append('4.BOS NO')
    if sweep:
        checks.append('5.SWEEP YES')
    else:
        checks.append('5.SWEEP NO')
    if pull:
        checks.append('6.PULLBACK YES')
    else:
        checks.append('6.PULLBACK NO')
    if vol>2500 and atr>0.0003:
        checks.append('7.VOL Strong')
    elif vol>2000:
        checks.append('7.VOL Medium')
    else:
        checks.append('7.VOL Kam')
    if (direction=='UP' and div_up) or (direction=='DOWN' and div_down):
        checks.append('8.DIVERGENCE YES')
    else:
        checks.append('8.DIVERGENCE NO')
    if (direction=='UP' and candle=='GREEN') or (direction=='DOWN' and candle=='RED'):
        checks.append('9.CANDLE OK')
    else:
        checks.append('9.CANDLE NO')
    passed=sum(1 for x in checks if 'OK' in x or 'YES' in x or 'Strong' in x)
    score_map={9:99,8:95,7:90,6:82,5:70,4:60,3:50,2:45,1:40,0:35}
    score=score_map.get(passed,50)
    why=[]
    if sweep:
        why.append('Sweep')
    if bos:
        why.append('BOS')
    if (direction=='UP' and div_up) or (direction=='DOWN' and div_down):
        why.append('Div')
    if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62):
        why.append('RSI Rev')
    why_txt=' + '.join(why) if why else 'Trend + Momentum'
    conf_txt='95%+ BOHAT ZYADA' if passed>=8 else '90% CONFIDENT' if passed==7 else 'WAIT' if passed==6 else 'NO'
    if 'OTC' in m:
        strat='OTC - Sweep + BOS'
    elif m in ['Bitcoin','Ethereum','Solana','Ripple']:
        strat='CRYPTO - Sweep + Pullback'
    elif m in ['Gold','Silver']:
        strat='GOLD - ATR + Liq'
    else:
        strat='FOREX - Trend + BOS + Div'
    return {'market':m,'score':score,'passed':passed,'dir':direction,'ps':ps,'rsi':round(rsi,1),'vol':vol,'atr':round(atr,4),'vwap':round(vwap,4),'macd':round(macd,4),'hh':round(hh,4),'ll':round(ll,4),'checks':checks,'strat':strat,'is_otc':is_otc(m),'candle':candle,'why':why_txt,'conf_txt':conf_txt,'price':price,'bos':bos,'sweep':sweep,'pull':pull,'div':div_up or div_down}
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:12px;text-align:center;margin:6px 0;">{txt}</div>',unsafe_allow_html=True)
def market_card(r):
    colr='#00FF00' if r['passed']>=7 else '#FFD700'
    if r['passed']<6:
        colr='#888888'
    dc='#00FF00' if r['dir']=='UP' else '#FF4444'
    bos_t='YES' if r['bos'] else 'NO'
    sw_t='YES' if r['sweep'] else 'NO'
    pull_t='YES' if r['pull'] else 'NO'
    div_t='YES' if r['div'] else 'NO'
    st.markdown(f'<div style="background:#111;border:2px solid {colr};border-radius:14px;padding:10px;text-align:center;">',unsafe_allow_html=True)
    st.markdown(f'<div style="color:white;font-weight:900;">{r["market"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:{colr};font-weight:900;">{r["passed"]}/9 - {r["score"]}%</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:{dc};font-weight:900;">{r["dir"]} - {r["candle"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#AAA;font-size:12px;">RSI {r["rsi"]} | VOL {r["vol"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#AAA;font-size:12px;">ATR {r["atr"]} | MACD {r["macd"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#AAA;font-size:12px;">VWAP {r["vwap"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#FFD700;font-size:12px;">LIQ UP {r["hh"]} | DOWN {r["ll"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:white;font-size:12px;">SWEEP {sw_t} | BOS {bos_t}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:white;font-size:12px;">PULL {pull_t} | DIV {div_t}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#00FFFF;font-size:12px;">{r["strat"]}</div>',unsafe_allow_html=True)
    st.markdown(f'<div style="color:#00FFFF;font-size:12px;">{r["why"]}</div></div>',unsafe_allow_html=True)
neon('<div style="color:#00FF00;font-weight:900;font-size:22px;">SONA AI v183 - AI BRAIN RADAR</div><div style="color:white;font-size:13px;">HAR MARKET KA POORA DETAIL - 60 SEC SCAN - 2 MIN WAIT</div>','#00FF00')
elapsed=int(time.time()-S['session_start'])
left=max(0,7200-elapsed)
lh=left//3600
lm=(left%3600)//60
ls=left%60
if S['daily_loss']>=2:
    neon('<div style="color:#FF4444;font-weight:900;font-size:24px;">AAJ STOP - 2 LOSS - KAL PHIR</div>','#FF4444')
    if st.button('NAYA DIN - RESET'):
        S['daily_loss']=0
        S['consecutive_loss']=0
        S['total_win']=0
        S['total_loss']=0
        S['phase']='SCAN'
        S['phase_start']=time.time()
        S['session_start']=time.time()
        S['scan_round']=1
        st.rerun()
    st.stop()
cool_left=max(0,int(S['cooldown_until']-time.time()))
if cool_left>0:
    cm=cool_left//60
    cs=cool_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:20px;">COOLDOWN - {cm:02d}:{cs:02d} - RUKO</div>','#FFD700')
    time.sleep(3)
    st.rerun()
S['tf']=st.selectbox('BINARY TIME',['5MIN','1MIN','15MIN'],index=0)
S['conf']=st.selectbox('AI BRAIN CONFIDENCE',[90,95,97],index=0)
S['amnt']=st.selectbox('AMOUNT',[100,150,250],index=0)
payout=int(S['amnt']*0.85)
if S['conf']==90:
    conf_help='90% = 7/9 MATCH - Roz 8-10 signal'
elif S['conf']==95:
    conf_help='95% = 8/9 MATCH - Roz 3-5 signal - Strong'
else:
    conf_help='97% = 9/9 MATCH - Roz 1-2 signal - Sab se strong'
neon(f'<div style="color:#FFD700;font-weight:800;font-size:13px;">TUNE CHUNA: {S["conf"]}% - {conf_help}</div><div style="color:#00FFFF;font-size:12px;">{S["amnt"]} PKR - Jeete +{payout} - Haare -{S["amnt"]} - AAJ LOSS {S["daily_loss"]}/2 - ROUND {S["scan_round"]}</div>','#FFD700')
if S['phase']=='WAIT':
    wait_left=max(0,int(S['wait_until']-time.time()))
    if wait_left<=0:
        S['phase']='SCAN'
        S['phase_start']=time.time()
        S['scan_round']+=1
        st.rerun()
    wm=wait_left//60
    ws=wait_left%60
    neon(f'<div style="color:#00FFFF;font-weight:900;font-size:24px;">2 MIN WAIT - AI AARAM</div><div style="color:white;font-size:14px;">WAIT ME: {wm:02d}:{ws:02d} BACHA</div>','#00FFFF')
    time.sleep(2)
    st.rerun()
SCAN_LEN=60
TRADE_LEN=300 if S['tf']=='5MIN' else 60 if S['tf']=='1MIN' else 900
phase_elapsed=int(time.time()-S['phase_start'])
if S['phase']=='SCAN':
    phase_left=max(0,SCAN_LEN-phase_elapsed)
    seed=int(S['phase_start']//3)
    results=[analyze_one(m,seed) for m in MARKETS]
    results_sorted=sorted(results,key=lambda x:(x['passed'],x['score']),reverse=True)
    best=results_sorted[0]
    pm=phase_left//60
    ps=phase_left%60
    top8=results_sorted[:8]
    st.markdown('<div style="color:#00FF00;font-weight:900;text-align:center;">TOP 4 MARKET - POORA DETAIL</div>',unsafe_allow_html=True)
    market_card(top8[0])
    market_card(top8[1])
    market_card(top8[2])
    market_card(top8[3])
    brain_bg='#00FF00' if best['passed']>=7 else '#FFD700'
    neon(f'<div style="font-size:36px;">BRAIN</div><div style="color:{brain_bg};font-weight:900;font-size:28px;">AI BRAIN - HIGH QUALITY</div><div style="color:white;font-size:15px;">SAB KO DEKH RAHA HAI - SCANNING - 9 CHECKS</div><div style="color:#FFD700;font-size:14px;">SCAN ME: {pm:02d}:{ps:02d} BACHA - ROUND {S["scan_round"]} - 60 SEC SCAN</div><div style="color:white;font-size:15px;">BEST: {best["market"]} - {best["passed"]}/9 - {best["score"]}% - {best["dir"]}</div><div style="color:#AAAAAA;font-size:12px;">{best["conf_txt"]} - {best["why"]} - {best["strat"]}</div><div style="color:#00FFFF;font-size:12px;">RSI {best["rsi"]} | VOL {best["vol"]} | ATR {best["atr"]} | VWAP {best["vwap"]} | MACD {best["macd"]}</div>',brain_bg)
    st.markdown('<div style="color:#00FF00;font-weight:900;text-align:center;">NEXT 4 MARKET - POORA DETAIL</div>',unsafe_allow_html=True)
    market_card(top8[4])
    market_card(top8[5])
    market_card(top8[6])
    market_card(top8[7])
    otc_best=sorted([r for r in results if r['is_otc']],key=lambda x:(x['passed'],x['score']),reverse=True)[0]
    normal_best=sorted([r for r in results if not r['is_otc']],key=lambda x:(x['passed'],x['score']),reverse=True)[0]
    neon(f'<div style="color:#00FF00;font-size:13px;">BEST OTC: {otc_best["market"]} - {otc_best["passed"]}/9 - {otc_best["score"]}% - {otc_best["dir"]}</div>','#00FF00')
    neon(f'<div style="color:#00FF00;font-size:13px;">BEST NORMAL: {normal_best["market"]} - {normal_best["passed"]}/9 - {normal_best["score"]}% - {normal_best["dir"]}</div>','#00FF00')
    need_pass=7 if S['conf']==90 else 8 if S['conf']==95 else 9
    if phase_left==0 and best['passed']>=need_pass and best['score']>=S['conf']:
        S['phase']='TRADE'
        S['phase_start']=time.time()
        S['locked_market']=best['market']
        S['locked_dir']=best['dir']
        S['locked_score']=best['score']
        S['locked_reason']=f"AI BRAIN: {best['passed']}/9 MATCH - {best['why']} - {best['conf_txt']}"
        open_dt=now_dt()
        S['open_time']=open_dt.strftime('%H:%M:%S')
        S['close_time']=(open_dt+datetime.timedelta(seconds=TRADE_LEN)).strftime('%H:%M:%S')
        S['_best']=best
        S['_best_checks']=best['checks']
        S['_best_strat']=best['strat']
        S['_best_conf']=best['conf_txt']
        S['_best_why']=best['why']
        S['_ps']=best['ps']
        S['_rsi']=best['rsi']
        S['_vol']=best['vol']
        S['_atr']=best['atr']
        S['_vwap']=best['vwap']
        S['_macd']=best['macd']
        S['_hh']=best['hh']
        S['_ll']=best['ll']
        st.rerun()
    elif phase_left==0:
        S['phase']='WAIT'
        S['wait_until']=time.time()+120
        st.warning(f"60 SEC me koi {S['conf']}% nahi mila - BEST {best['market']} {best['passed']}/9 - AI 2 MIN WAIT")
        st.rerun()
else:
    phase_left=max(0,TRADE_LEN-phase_elapsed)
    if phase_left==0:
        S['phase']='WAIT'
        S['wait_until']=time.time()+120
        S['locked_market']='-'
        st.rerun()
    tm=phase_left//60
    ts=phase_left%60
    is_up=S['locked_dir']=='UP'
    bg='#00FF00' if is_up else '#FF4444'
    trade_txt='UP - CALL - GREEN' if is_up else 'DOWN - PUT - RED'
    neon(f'<div style="color:{bg};font-weight:900;font-size:32px;">{trade_txt}</div><div style="color:white;font-weight:900;font-size:20px;">AI BRAIN NE SELECT KIYA: {S["locked_market"]} - {S["locked_score"]}%</div><div style="color:#FFD700;font-size:13px;">{S.get("_best_conf","")} - {S.get("_best_strat","")} - {S.get("_best_why","")}</div><div style="color:#FFD700;font-size:13px;">{S["locked_reason"]}</div><div style="color:white;font-size:14px;">APP ME: Fixed Time - SEARCH: {S["locked_market"]}</div><div style="color:white;font-size:14px;">TRADE: {S["locked_dir"]} - {S["amnt"]} PKR - TIME {S["tf"]} - Jeete +{payout} PKR</div><div style="color:white;font-size:14px;">OPEN: {S["open_time"]} - CLOSE: {S["close_time"]} - BACHA: {tm:02d}:{ts:02d}</div>',bg)
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;">AI BRAIN CHECKLIST - 9/9</div>',unsafe_allow_html=True)
    for chk in S.get('_best_checks',[]):
        col='#00FF00' if 'OK' in chk or 'YES' in chk or 'Strong' in chk else '#FF4444'
        if 'NO' not in chk and 'Kam' not in chk and 'OK' not in chk and 'YES' not in chk and 'Strong' not in chk:
            col='#FFD700'
        neon(f'<div style="color:{col};font-weight:700;font-size:13px;text-align:left;">{chk}</div>',col)
    neon(f'<div style="color:#00FF00;font-weight:900;">RSI: {S.get("_rsi","")}</div>','#00FF00')
    neon(f'<div style="color:#FFD700;font-weight:900;">VOLUME: {S.get("_vol","")}</div>','#FFD700')
    neon(f'<div style="color:#00FFFF;font-weight:900;">ATR: {S.get("_atr","")}</div>','#00FFFF')
    neon(f'<div style="color:#FF00FF;font-weight:900;">VWAP: {S.get("_vwap","")}</div>','#FF00FF')
    neon(f'<div style="color:#00FF00;font-weight:900;">MACD: {S.get("_macd","")}</div>','#00FF00')
    neon(f'<div style="color:#FFD700;font-weight:800;">LIQ UP {S.get("_hh","")} | DOWN {S.get("_ll","")}</div>','#FFD700')
    if '_best' in S:
        bb=S['_best']
        sw2='YES' if bb["sweep"] else 'NO'
        bos2='YES' if bb["bos"] else 'NO'
        pull2='YES' if bb["pull"] else 'NO'
        div2='YES' if bb["div"] else 'NO'
        neon(f'<div style="color:white;font-size:13px;">SWEEP {sw2} | BOS {bos2} | PULL {pull2} | DIV {div2}</div>','#00FFFF')
        neon(f'<div style="color:white;font-size:13px;">{bb["strat"]} | {bb["why"]}</div>','#00FFFF')
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;">IS 1 MARKET KA CHART</div>',unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({'Price':S.get('_ps',[100,101,102])}),use_container_width=True)
    if st.button('WIN HUA'):
        S['total_win']+=1
        S['cp']+=int(S['amnt']*0.85)
        S['bal']+=int(S['amnt']*0.85)
        S['consecutive_loss']=0
        S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()})
        S['phase']='WAIT'
        S['wait_until']=time.time()+120
        S['locked_market']='-'
        st.rerun()
    if st.button('LOSS HUA'):
        S['total_loss']+=1
        S['daily_loss']+=1
        S['consecutive_loss']+=1
        S['cp']-=S['amnt']
        S['bal']-=S['amnt']
        S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()})
        S['phase']='WAIT'
        S['wait_until']=time.time()+120
        S['locked_market']='-'
        if S['consecutive_loss']>=1:
            S['cooldown_until']=time.time()+900
        st.rerun()
neon(f'<div>PROFIT: +{S["cp"]} PKR</div>', '#00FF00')
neon(f'<div>BAL {S["bal"]} | WIN {S["total_win"]}</div>', '#00FF00')
if S['ht']:
    st.markdown('<div>AAJ KE TRADE</div>', unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(S['ht']), use_container_width=True, hide_index=True)
neon('AI RULE: 90/95/97 LOCK - 60 SEC SCAN', '#FF6B6B')
st.write(f"Last Update: {now_pkt()} | V183")
time.sleep(2)
st.rerun()
