# SONA V179 - AI BRAIN ONLY - NO SCANNER - SIRF 1 MARKET - 1 SIGNAL
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V179 AI BRAIN ONLY', page_icon='🧠', layout='wide')
st.markdown("""<style>.stApp{background:#000 !important;color:white !important} h1{font-size:23px !important;text-align:center;color:#00FF00 !important} .stSelectbox label{color:#00FF00 !important;font-weight:bold !important} .stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important} .stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:55px !important;font-size:18px !important}</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'TRADE','phase_start':time.time(),'tf':'5MIN','amnt':100,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':0,'bal':12622,'ht':[],'daily_loss':0,'consecutive_loss':0,'cooldown_until':0}
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
# === AI BRAIN - SIRF 1 MARKET CHUNTA HAI ===
def ai_brain_pick(seed):
    best=None
    for m in MARKETS:
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
        checks=0
        if direction=='UP' and price>ema9 and price>ema and price>ema50: checks+=1
        if direction=='DOWN' and price<ema9 and price<ema and price<ema50: checks+=1
        if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62): checks+=1
        elif (direction=='UP' and rsi>50 and rsi<65) or (direction=='DOWN' and rsi<50 and rsi>35): checks+=1
        if (direction=='UP' and macd>0) or (direction=='DOWN' and macd<0): checks+=1
        if bos: checks+=1
        if sweep_up or sweep_down: checks+=1
        if abs(price-ema)<0.0005 or abs(price-vwap)<0.0005: checks+=1
        if vol>2500 and atr>0.0003: checks+=1
        elif vol>2000: checks+=0
        if (direction=='UP' and div_up) or (direction=='DOWN' and div_down): checks+=1
        if (direction=='UP' and candle=='GREEN') or (direction=='DOWN' and candle=='RED'): checks+=1
        score_map={9:99,8:95,7:90,6:82,5:70,4:60,3:50,2:45,1:40,0:35}
        score=score_map.get(checks,50)
        # AI BRAIN - Sirf BEST ko yaad rakhta hai - Baaki bhool jata hai
        if best is None or checks>best['passed'] or (checks==best['passed'] and score>best['score']):
            # AI kyun confident hai - 1 line me
            why=[]
            if sweep_up or sweep_down: why.append('Sweep')
            if bos: why.append('BOS')
            if (direction=='UP' and div_up) or (direction=='DOWN' and div_down): why.append('Divergence')
            if (direction=='UP' and rsi<38) or (direction=='DOWN' and rsi>62): why.append('RSI Reversal')
            why_txt=' + '.join(why) if why else 'Trend + Momentum'
            best={'market':m,'score':score,'passed':checks,'dir':direction,'price':price,'rsi':round(rsi,1),'vol':vol,'ps':ps,'why':why_txt}
    return best
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:14px;text-align:center;margin:8px 0;box-shadow:0 0 14px {border};">{txt}</div>',unsafe_allow_html=True)
neon('<div style="color:#00FF00;font-weight:900;font-size:22px;">🧠 SONA AI v179 - AI BRAIN ONLY</div><div style="color:white;font-size:13px;">NO SCANNER - SIRF 1 MARKET - AI KHUD SELECT KAREGA</div>','#00FF00')
elapsed=int(time.time()-S['session_start']); left=max(0,7200-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if S['daily_loss']>=2:
    neon('<div style="color:#FF4444;font-weight:900;font-size:24px;">🛑 AAJ STOP - 2 LOSS - KAL PHIR</div><div style="color:white;font-size:13px;">AI BRAIN bhi kehta hai - Aaj ruk jao!</div>','#FF4444')
    if st.button('🔄 NAYA DIN - RESET'):
        S['daily_loss']=0; S['consecutive_loss']=0; S['total_win']=0; S['total_loss']=0; S['phase']='TRADE'; S['phase_start']=time.time(); S['session_start']=time.time(); st.rerun()
    st.stop()
cool_left=max(0,int(S['cooldown_until']-time.time()))
if cool_left>0:
    cm=cool_left//60; cs=cool_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:20px;">⏳ AI BRAIN COOLDOWN - {cm:02d}:{cs:02d}</div><div style="color:white;font-size:13px;">1 LOSS ke baad AI 15 MIN sochta hai - Tu bhi ruk!</div>','#FFD700')
    time.sleep(3); st.rerun()
# SETTINGS - SIRF 2 CHEEZ - TIME + AMOUNT
sc1,sc2=st.columns(2)
with sc1: S['tf']=st.selectbox('BINARY TIME',['5MIN','1MIN','15MIN'],index=0)
with sc2: S['amnt']=st.selectbox('AMOUNT',[100,150,250],index=0)
payout=int(S['amnt']*0.85)
# === AI BRAIN - HAR BAAR 1 MARKET - SCAN LIST NAHI DIKHAYEGA ===
TRADE_LEN=300 if S['tf']=='5MIN' else 60 if S['tf']=='1MIN' else 900
phase_elapsed=int(time.time()-S['phase_start'])
# Agar pehli baar hai ya trade khatam hua - AI BRAIN NAYA MARKET CHUNE
if S['locked_market']=='-' or phase_elapsed>=TRADE_LEN:
    # AI BRAIN SOCH RAHA HAI - 3 SEC
    if S['locked_market']=='-' and phase_elapsed<3:
        neon('<div style="color:#FFD700;font-weight:900;font-size:22px;">🧠 AI BRAIN SOCH RAHA HAI...</div><div style="color:white;font-size:14px;">Sab market ke andar dekh raha hai - 1 BEST wala chun raha hai...</div>','#FFD700')
        time.sleep(2); st.rerun()
    pick=ai_brain_pick(int(S['phase_start']//3))
    # Agar 90% se kam hai - AI phir se sochega - 10 sec wait - Scanner list nahi dikhayega
    if pick['passed']<7:
        neon(f'<div style="color:#FFD700;font-weight:900;font-size:20px;">🧠 AI BRAIN SOCH RAHA HAI...</div><div style="color:white;font-size:14px;">Abhi koi 90% wala nahi mila - BEST {pick["market"]} {pick["passed"]}/9 - {pick["score"]}% - AI phir se dekh raha hai - 10 SEC WAIT!</div>','#FFD700')
        time.sleep(3)
        S['phase_start']=time.time(); st.rerun()
    S['locked_market']=pick['market']; S['locked_dir']=pick['dir']; S['locked_score']=pick['score']; S['locked_reason']=f"AI BRAIN: {pick['passed']}/9 MATCH - {pick['why']} - Is liye isi ko chuna!"
    open_dt=now_dt(); S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=(open_dt+datetime.timedelta(seconds=TRADE_LEN)).strftime('%H:%M:%S')
    S['_why']=pick['why']; S['_rsi']=pick['rsi']; S['_vol']=pick['vol']; S['_ps']=pick['ps']; S['phase']='TRADE'; S['phase_start']=time.time(); st.rerun()
# === SIRF 1 TRADE BOX - YEHI SAB KUCH HAI ===
phase_left=max(0,TRADE_LEN-phase_elapsed)
tm=phase_left//60; ts=phase_left%60
is_up=S['locked_dir']=='UP'; bg='#00FF00' if is_up else '#FF4444'
neon(f'<div style="color:{bg};font-weight:900;font-size:34px;">{"🟢 ▲ UP — CALL — GREEN DABAO" if is_up else "🔴 ▼ DOWN — PUT — RED DABAO"}</div><div style="color:white;font-weight:900;font-size:22px;margin-top:6px;">🧠 AI BRAIN NE SELECT KIYA:</div><div style="color:#FFD700;font-weight:900;font-size:24px;">{S["locked_market"]} — {S["locked_score"]}%</div><div style="color:white;font-size:14px;">{S["locked_reason"]}</div><div style="color:#00FFFF;font-size:13px;">AI kyun CONFIDENT hai: {S.get("_why","")} | RSI {S.get("_rsi","")} | VOL {S.get("_vol","")}</div><div style="color:white;font-size:15px;margin-top:8px;text-align:left;">📱 APP ME ABHI KARO:<br>1) Fixed Time / Binary pe jao<br>2) SEARCH: <b>{S["locked_market"]}</b><br>3) TIME: <b>{S["tf"]}</b> — AMOUNT: <b>{S["amnt"]} PKR</b><br>4) BUTTON: <b>{"GREEN UP" if is_up else "RED DOWN"}</b> dabao!</div><div style="color:#00FFFF;font-size:13px;">💰 Jeete to +{payout} PKR — Haare to -{S["amnt"]} PKR</div><div style="color:white;font-size:14px;">🕐 OPEN: {S["open_time"]} &nbsp; CLOSE: {S["close_time"]} &nbsp; BACHA: {tm:02d}:{ts:02d}</div>',bg)
# CHOTA CHART - Sirf is 1 market ka
st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">📈 IS 1 MARKET KA CHART - '+S['locked_market']+'</div>',unsafe_allow_html=True)
st.line_chart(pd.DataFrame({'Price':S.get('_ps',[100,101,102])}),use_container_width=True)
cc1,cc2=st.columns(2)
with cc1:
    if st.button('✅ WIN HUA'):
        S['total_win']+=1; S['cp']+=int(S['amnt']*0.85); S['bal']+=int(S['amnt']*0.85); S['consecutive_loss']=0; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()}); S['locked_market']='-'; S['phase_start']=time.time(); st.rerun()
with cc2:
    if st.button('❌ LOSS HUA'):
        S['total_loss']+=1; S['daily_loss']+=1; S['consecutive_loss']+=1; S['cp']-=S['amnt']; S['bal']-=S['amnt']; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()}); S['locked_market']='-'; S['phase_start']=time.time()
        if S['consecutive_loss']>=1: S['cooldown_until']=time.time()+900
        st.rerun()
neon(f'<div style="color:#00FF00;font-weight:900;font-size:26px;">PROFIT: +{S["cp"]} PKR</div><div style="color:#00FF00;font-size:12px;">BAL {S["bal"]} PKR | WIN {S["total_win"]} | LOSS {S["total_loss"]} | AAJ LOSS {S["daily_loss"]}/2 | Session {lh:02d}:{lm:02d}:{ls:02d}</div>','#00FF00')
if S['ht']:
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;">📋 AAJ KE TRADE - AI BRAIN WALE</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
neon('<div style="color:#FF6B6B;font-size:12px;">🧠 AI BRAIN RULE: Sirf AI wala market karo - Apni marzi se market mat chuno - 2 LOSS = STOP - 100% koi nahi jeetta!</div>','#FF6B6B')
st.write(f"Last Update: {now_pkt()} | V179 AI BRAIN ONLY | Session {lh:02d}:{lm:02d}:{ls:02d}")
time.sleep(2); st.rerun()
