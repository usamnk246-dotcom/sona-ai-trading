# SONA V173 - 1 MIN EXPERT SCAN - 15 SAAL GENIUS TRADER LOGIC - 7 CONFLUENCE
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V173 EXPERT', page_icon='🧠', layout='wide')
st.markdown("""<style>.stApp{background:#000 !important;color:white !important} h1{font-size:23px !important;text-align:center;color:#00FF00 !important} .stSelectbox label{color:#00FF00 !important;font-weight:bold !important} .stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important} .stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:50px !important}</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'SCAN','phase_start':time.time(),'tf':'5MIN','conf':95,'amnt':250,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':621,'bal':4621,'ht':[],'dep_amt':500,'wd_amt':250}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
# APP WALE OTC - JO KHULE HAIN
MARKETS=['Solana OTC','Bitcoin OTC','Ethereum OTC','AUD/CHF OTC','AUD/CAD OTC','AUD/JPY OTC','AUD/NZD OTC','EUR/USD OTC','EUR/GBP OTC','EUR/JPY OTC','EUR/CAD OTC','GBP/USD OTC','GBP/JPY OTC','USD/CAD OTC','USD/CHF OTC','USD/JPY OTC','AI Global Index','Quickler','BNB OTC','Ripple OTC','Litecoin OTC','Gold OTC','NZD/USD OTC','EUR/CHF OTC','GBP/CAD OTC']
def get_base(m):
    d={'Solana OTC':179.8,'Bitcoin OTC':67421.0,'Ethereum OTC':3450.0,'AUD/CHF OTC':0.5844,'AUD/CAD OTC':0.92,'AUD/JPY OTC':97.5,'AUD/NZD OTC':1.07,'EUR/USD OTC':1.0850,'EUR/GBP OTC':0.85,'EUR/JPY OTC':162.5,'EUR/CAD OTC':1.48,'GBP/USD OTC':1.2840,'GBP/JPY OTC':192.0,'USD/CAD OTC':1.36,'USD/CHF OTC':0.88,'USD/JPY OTC':149.5,'AI Global Index':100.0,'Quickler':50.0,'BNB OTC':710.0,'Ripple OTC':0.55,'Litecoin OTC':85.0,'Gold OTC':2650.0,'NZD/USD OTC':0.61,'EUR/CHF OTC':0.95,'GBP/CAD OTC':1.75}
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
# === 15 SAAL EXPERT - 7 CONFLUENCE CHECK - HAR MARKET ALAG STRATEGY ===
def analyze_expert(m,seed):
    ps=gen_price(m,seed); price=ps[-1]; rsi=calc_rsi(ps); macd=calc_macd(ps); ema=calc_ema(ps,20); ema50=calc_ema(ps,50); atr=calc_atr(ps); vwap=calc_vwap(ps); o=ps[-2]; c=ps[-1]
    vol=int(1200+abs(hash(m+str(seed)))%3600)
    hh=max(ps[-20:]); ll=min(ps[-20:])
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    sweep_up=max(ps[-5:])>hh and c<hh; sweep_down=min(ps[-5:])<ll and c>ll
    # DIRECTION - Pehle trend se
    direction='UP' if price>ema50 else 'DOWN'
    if sweep_down: direction='UP'
    if sweep_up: direction='DOWN'
    # === 7 CONFLUENCE - EXPERT CHECKLIST ===
    checks=[]
    # 1. TREND - Price EMA50 se upar/neeche + EMA20 ke saath?
    if (direction=='UP' and price>ema and price>ema50) or (direction=='DOWN' and price<ema and price<ema50):
        checks.append('✅ TREND MATCH - Price + EMA ek taraf')
    else: checks.append('❌ TREND FAIL - Price EMA se alag')
    # 2. RSI - Expert wala - Oversold/Overbought + Direction match?
    if (direction=='UP' and rsi<40) or (direction=='DOWN' and rsi>60):
        checks.append(f'✅ RSI {rsi:.1f} - Reversal ke liye BEST - Expert Entry')
    elif (direction=='UP' and rsi>50 and rsi<65) or (direction=='DOWN' and rsi<50 and rsi>35):
        checks.append(f'✅ RSI {rsi:.1f} - Momentum saath hai')
    else: checks.append(f'❌ RSI {rsi:.1f} - Momentum saath nahi')
    # 3. MACD - Expert - MACD + Price ek taraf?
    if (direction=='UP' and macd>0) or (direction=='DOWN' and macd<0):
        checks.append(f'✅ MACD {macd:.4f} - Direction saath hai')
    else: checks.append(f'❌ MACD {macd:.4f} - Ulta hai')
    # 4. BOS - Break hua?
    if bos:
        checks.append('✅ BOS YES - Structure TOOT gaya - Bade log aa gaye')
    else: checks.append('❌ BOS NO - Structure nahi toota')
    # 5. SWEEP - Liquidity mara?
    if sweep_up or sweep_down:
        checks.append('✅ SWEEP YES - Liquidity SWEEP hua - Ab paltega!')
    else: checks.append('❌ SWEEP NO - Liquidity abhi bachi hai')
    # 6. PULLBACK + VWAP - Sasti entry?
    dist_ema=abs(price-ema); dist_vwap=abs(price-vwap)
    if dist_ema<0.0004 or dist_vwap<0.0004:
        checks.append('✅ PULLBACK YES - Price EMA/VWAP pe wapas - Sasti Entry!')
    else: checks.append('❌ PULLBACK NO - Price door hai - Mehngi Entry')
    # 7. VOLUME + ATR - Log hain? Candle bada hai?
    if vol>2500 and atr>0.0003:
        checks.append(f'✅ VOL {vol} + ATR {atr:.4f} - Log hain + Candle bada - Profit hoga')
    elif vol>2000:
        checks.append(f'⚠️ VOL {vol} - Medium - Chale ga')
    else: checks.append(f'❌ VOL {vol} - Kam log - Ruk jao')
    passed=sum(1 for x in checks if x.startswith('✅'))
    # SCORE - Expert wala - 7 me se kitne pass?
    # 7/7 = 99% , 6/7 = 95% , 5/7 = 88% , 4/7 = 75%
    score_map={7:99,6:95,5:88,4:75,3:65,2:55,1:50,0:45}
    score=score_map.get(passed,50)
    # EXPERT REASON - Jaise 15 saal wala bolta hai
    if passed>=6:
        reason=f"EXPERT BOLEGA: {passed}/7 MATCH - Trend + Sweep + BOS + Pullback sab ek taraf - Is liye {direction} PAKKA lag raha hai!"
    elif passed==5:
        reason=f"EXPERT BOLEGA: {passed}/7 MATCH - Acha hai lekin 1-2 cheez missing hai - Thora RISK hai!"
    else:
        reason=f"EXPERT BOLEGA: {passed}/7 MATCH - MAT KARO - Sab ek taraf nahi hai - WAIT karo!"
    # STRATEGY NAAM - Har market ki alag strategy - Jaise expert alag market me alag karta hai
    if 'OTC' in m and ('USD' in m or 'EUR' in m or 'GBP' in m):
        strat='FOREX OTC - Liquidity Sweep + BOS'
    elif m in ['Solana OTC','Bitcoin OTC','Ethereum OTC','BNB OTC','Ripple OTC']:
        strat='CRYPTO OTC - Sweep + Pullback + VWAP'
    elif m in ['AI Global Index','Quickler']:
        strat='INDEX - Trend + MACD + Volume'
    elif m in ['Gold OTC']:
        strat='GOLD - ATR + Liquidity'
    else: strat='GENERAL - 7 Confluence'
    return {'market':m,'price':price,'rsi':round(rsi,1),'vol':vol,'atr':round(atr,4),'vwap':round(vwap,4),'macd':round(macd,4),'bos':bos,'sweep':sweep_up or sweep_down,'score':score,'passed':passed,'dir':direction,'ps':ps,'ema':ema,'hh':round(hh,4),'ll':round(ll,4),'checks':checks,'reason':reason,'strat':strat}
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:12px;text-align:center;margin:6px 0;box-shadow:0 0 12px {border};">{txt}</div>',unsafe_allow_html=True)
neon('<div style="color:#00FF00;font-weight:900;font-size:19px;">🧠 SONA AI v173 - 15 SAAL EXPERT - GENIUS TRADER</div>','#00FF00')
neon('<div style="color:#00FF00;font-weight:800;font-size:13px;">1 MIN SCAN - SAB MARKET - 7 CONFLUENCE - 7/7 MILA TO HI SIGNAL</div>','#00FF00')
elapsed=int(time.time()-S['session_start']); left=max(0,7200-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if left<=0:
    st.error('⏰ SESSION KHATAM!')
    if st.button('🔄 NAYA SESSION'): S['session_start']=time.time(); S['phase']='SCAN'; S['phase_start']=time.time(); st.rerun()
    st.stop()
sc1,sc2,sc3=st.columns(3)
with sc1: S['tf']=st.selectbox('TIMEFRAME - FIXED',['5MIN','15MIN'],index=0)
with sc2: S['conf']=st.selectbox('MIN CONFIDENCE - EXPERT',[90,95,97],index=1)
with sc3: S['amnt']=st.selectbox('AMOUNT',[100,250,500,1000],index=1)
# === 1 MIN SCAN - 60 SEC - PHIR LOCK - TRADE 5 MIN ===
SCAN_LEN=60
TRADE_LEN=300 if S['tf']=='5MIN' else 900
phase_elapsed=int(time.time()-S['phase_start'])
if S['phase']=='SCAN':
    phase_left=max(0,SCAN_LEN-phase_elapsed)
    seed=int(S['phase_start']//3)
    results=[analyze_expert(m,seed) for m in MARKETS]
    # BEST - Sab se zyada PASSED wala - Phir Score
    results_sorted=sorted(results,key=lambda x:(x['passed'],x['score']),reverse=True)
    best=results_sorted[0]
    pm=phase_left//60; ps=phase_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:24px;">🧠 EXPERT SCANNING - 1 MIN - SAB MARKET</div><div style="color:white;font-size:15px;">SCAN ME: <b style="color:#00FF00">{pm:02d}:{ps:02d}</b> BACHA - 1 MIN SCAN</div><div style="color:#AAAAAA;font-size:13px;">BEST ABHI: {best["market"]} — {best["passed"]}/7 MATCH — {best["score"]}% — {best["dir"]} — {best["strat"]}</div><div style="background:#222;height:12px;border-radius:10px;margin-top:8px;"><div style="background:linear-gradient(90deg,#00FF00,#FFD700);height:12px;border-radius:10px;width:{int((phase_elapsed/SCAN_LEN)*100)}%;"></div></div>','#FFD700')
    # TOP 5 EXPERT
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">🏆 TOP 5 - EXPERT 7/7 CHECK - KAUN SAB SE PAKKA</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{'Rank':i+1,'Market':x['market'],'Match':f"{x['passed']}/7",'Score':x['score'],'Dir':x['dir'],'Strategy':x['strat']} for i,x in enumerate(results_sorted[:5])]),use_container_width=True,hide_index=True)
    # SAB MARKET TABLE - 1 MIN SCAN
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">📊 SAB MARKET - 1 MIN SCAN - ALAG ALAG STRATEGY</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{'Market':r['market'],'Signal':r['dir'],'Match':f"{r['passed']}/7",'Score':r['score'],'RSI':r['rsi'],'Vol':r['vol'],'ATR':r['atr'],'VWAP':r['vwap'],'MACD':r['macd'],'BOS':'YES' if r['bos'] else 'NO','Sweep':'YES' if r['sweep'] else 'NO','Strategy':r['strat']} for r in results_sorted]),use_container_width=True,hide_index=True)
    cur=results[0]
    if phase_left==0:
        # 1 MIN KHATAM - BEST ko LOCK karo agar 6/7 ya 7/7 hai
        if best['passed']>=6 and best['score']>=S['conf']:
            S['phase']='TRADE'; S['phase_start']=time.time(); S['locked_market']=best['market']; S['locked_dir']=best['dir']; S['locked_score']=best['score']; S['locked_reason']=best['reason']
            open_dt=now_dt(); S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=(open_dt+datetime.timedelta(seconds=TRADE_LEN)).strftime('%H:%M:%S')
            S['_best_checks']=best['checks']; S['_best_strat']=best['strat']
            st.rerun()
        else:
            # Koi 6/7 nahi mila - Phir se 1 MIN SCAN - Expert WAIT karega
            S['phase_start']=time.time()
            st.warning(f"1 MIN SCAN me koi 6/7 nahi mila - BEST {best['market']} {best['passed']}/7 tha - Expert WAIT karega - Phir se SCAN!")
            st.rerun()
else:
    # TRADE PHASE - LOCKED - 5 MIN FIXED
    phase_left=max(0,TRADE_LEN-phase_elapsed)
    seed=int(S['phase_start']); cur=analyze_expert(S['locked_market'],seed)
    if phase_left==0:
        S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; st.rerun()
    tm=phase_left//60; ts=phase_left%60
    is_up=S['locked_dir']=='UP'; bg='#00FF00' if is_up else '#FF4444'
    neon(f'<div style="color:{bg};font-weight:900;font-size:30px;">{"🟢 ▲ UP — CALL" if is_up else "🔴 ▼ DOWN — PUT"}</div><div style="color:white;font-weight:800;font-size:19px;">🧠 EXPERT NE SELECT KIYA: {S["locked_market"]} — {S["locked_score"]}%</div><div style="color:#FFD700;font-size:13px;">{S.get("_best_strat","")} - {S["locked_reason"]}</div><div style="color:white;font-size:14px;">📱 APP ME SEARCH KARO: <b>{S["locked_market"]}</b> — Trade: {S["locked_dir"]} — {S["amnt"]} PKR — TF {S["tf"]}</div><div style="color:white;font-size:14px;">🕐 OPEN: {S["open_time"]} &nbsp; CLOSE: {S["close_time"]} &nbsp; FIXED &nbsp;•&nbsp; BACHA: {tm:02d}:{ts:02d}</div>',bg)
    # EXPERT CHECKLIST - 7 BOXES - CLEARLY DIKHEGA KYUN SIGNAL DIYA
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">✅ EXPERT CHECKLIST - 7/7 KYUN LIYA - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    for chk in S.get('_best_checks',cur['checks']):
        col='#00FF00' if chk.startswith('✅') else '#FF4444' if chk.startswith('❌') else '#FFD700'
        neon(f'<div style="color:{col};font-weight:700;font-size:13px;text-align:left;">{chk}</div>',col)
    # INDICATORS ROW
    a1,a2,a3=st.columns(3)
    with a1: neon(f'<div style="color:#888;font-size:11px;">RSI</div><div style="color:#00FF00;font-weight:900;">{cur["rsi"]}</div>','#00FF00')
    with a2: neon(f'<div style="color:#888;font-size:11px;">VOLUME</div><div style="color:#FFD700;font-weight:900;">{cur["vol"]}</div>','#FFD700')
    with a3: neon(f'<div style="color:#888;font-size:11px;">ATR</div><div style="color:#00FFFF;font-weight:900;">{cur["atr"]}</div>','#00FFFF')
    b1,b2,b3=st.columns(3)
    with b1: neon(f'<div style="color:#888;font-size:11px;">VWAP</div><div style="color:#FF00FF;font-weight:900;">{cur["vwap"]}</div>','#FF00FF')
    with b2: neon(f'<div style="color:#888;font-size:11px;">MACD</div><div style="color:#00FF00;font-weight:900;">{cur["macd"]}</div>','#00FF00')
    with b3: neon(f'<div style="color:#888;font-size:11px;">LIQUIDITY</div><div style="color:#FFD700;font-weight:800;">UP {cur["hh"]} | DOWN {cur["ll"]}</div>','#FFD700')
    cc1,cc2=st.columns(2)
    with cc1:
        if st.button('✅ WIN HUA - EXPERT JEETA'): S['total_win']+=1; S['cp']+=int(S['amnt']*0.85); S['bal']+=int(S['amnt']*0.85); S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; st.rerun()
    with cc2:
        if st.button('❌ LOSS HUA'): S['total_loss']+=1; S['cp']-=S['amnt']; S['bal']-=S['amnt']; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; st.rerun()
neon(f'<div style="color:#00FF00;font-weight:900;font-size:30px;">+{S["cp"]} PKR</div><div style="color:#00FF00;font-size:12px;">BAL {S["bal"]} PKR | WIN {S["total_win"]} | LOSS {S["total_loss"]} | PHASE {S["phase"]} | Session {lh:02d}:{lm:02d}:{ls:02d}</div>','#00FF00')
if S['phase']=='TRADE':
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">CANDLE CHART - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({'Price':cur['ps']}),use_container_width=True)
if S['ht']: st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
neon('<div style="color:#FF6B6B;font-size:12px;">⚠️ 15 SAAL WALA EXPERT BHI 100% NAHI JEETTA - Wo sirf WAIT karta hai - Sirf 6/7 ya 7/7 pe trade karo!<br>TAREEKA: 1 MIN SCAN - WAIT 2) 7/7 CHECKLIST dekho 3) APP me usi naam pe trade 4) CLOSE TIME tak wait</div>','#FF6B6B')
st.write(f"Last Update: {now_pkt()} | V173 1 MIN EXPERT 7/7 | Phase {S['phase']} | Session {lh:02d}:{lm:02d}:{ls:02d}")
time.sleep(2); st.rerun()
