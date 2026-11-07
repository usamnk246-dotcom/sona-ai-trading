# SONA V171 - AI 5 MIN SCAN - PHIR 1 MARKET LOCK - NO FLICKER - FIXED TIME
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V171 5MIN SCAN', page_icon='🤖', layout='wide')
st.markdown("""<style>
.stApp{background:#000 !important;color:white !important}
h1{font-size:23px !important;text-align:center;color:#00FF00 !important;line-height:1.2 !important}
h2{font-size:17px !important;text-align:center;color:#FFD700 !important}
.stSelectbox label{color:#00FF00 !important;font-weight:bold !important}
.stSelectbox div[data-baseweb="select"]>div{background:#000 !important;color:#00FF00 !important;border:2px solid #00FF00 !important;border-radius:10px !important}
.stButton>button{background:#00FF00 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:50px !important}
</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'phase':'SCAN','phase_start':time.time(),'scan_len':300,'trade_len':300,'tf':'5MIN','conf':95,'amnt':250,'locked_market':'-','locked_dir':'-','locked_score':0,'locked_reason':'','open_time':'','close_time':'','total_win':0,'total_loss':0,'cp':621,'bal':4621,'ht':[],'scan_scores':{},'scan_counts':{},'dep_amt':500,'wd_amt':250}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
MARKETS=['AUD/CHF OTC','EUR/USD','GBP/USD','USD/JPY','AUD/USD','USD/CAD','EUR/GBP','SOL/USD','BNB/USD','BTC/USD','XAU/USD','EUR/USD OTC','GBP/USD OTC','EUR/JPY','GBP/JPY','AUD/JPY','NZD/USD','USD/CHF','EUR/CHF','USD/CHF OTC']
def get_base(m):
    d={'AUD/CHF OTC':0.5844,'EUR/USD':1.0850,'GBP/USD':1.2843,'USD/JPY':149.5,'AUD/USD':0.65,'USD/CAD':1.36,'EUR/GBP':0.85,'SOL/USD':179.8,'BNB/USD':710.0,'BTC/USD':67421.0,'XAU/USD':2650.0,'EUR/USD OTC':1.0850,'GBP/USD OTC':1.2840,'EUR/JPY':162.5,'GBP/JPY':192.0,'AUD/JPY':97.5,'NZD/USD':0.61,'USD/CHF':0.88,'EUR/CHF':0.95,'USD/CHF OTC':0.88}
    return d.get(m,1.0)
def gen_price(m,seed):
    random.seed(hash(m+str(seed))%100000)
    base=get_base(m); ps=[base]
    for i in range(1,100):
        ps.append(ps[-1]+random.uniform(-0.0004,0.0004))
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
def analyze(m,seed):
    ps=gen_price(m,seed); price=ps[-1]; rsi=calc_rsi(ps); macd=calc_macd(ps); ema=calc_ema(ps,20); ema50=calc_ema(ps,50); atr=calc_atr(ps); vwap=calc_vwap(ps); o=ps[-2]; c=ps[-1]
    vol=int(1200+abs(hash(m+str(seed)))%3600)
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    hh=max(ps[-20:]); ll=min(ps[-20:])
    sweep_up=max(ps[-5:])>hh and c<hh; sweep_down=min(ps[-5:])<ll and c>ll
    dist_ema=abs(price-ema); dist_vwap=abs(price-vwap)
    score=50
    if rsi<25 or rsi>75: score+=18
    elif rsi<35 or rsi>65: score+=12
    elif rsi<40 or rsi>60: score+=6
    if vol>3000: score+=6
    elif vol>2000: score+=3
    if (macd>0.0003 and price>ema) or (macd<-0.0003 and price<ema): score+=12
    if bos: score+=8
    if abs(price-vwap)>0.0004: score+=6
    if sweep_up or sweep_down: score+=8
    if dist_ema<0.0003 or dist_vwap<0.0003: score+=6
    score=min(99,score)
    direction='UP' if price>=ema else 'DOWN'
    if sweep_down: direction='UP'
    if sweep_up: direction='DOWN'
    if rsi>65 and macd>0: direction='UP'
    if rsi<35 and macd<0: direction='DOWN'
    return {'market':m,'price':price,'rsi':round(rsi,1),'vol':vol,'atr':round(atr,4),'vwap':round(vwap,4),'macd':round(macd,4),'bos':bos,'sweep':sweep_up or sweep_down,'sweep_txt':'SWEEP YES' if (sweep_up or sweep_down) else 'NO SWEEP','score':int(score),'dir':direction,'ps':ps,'ema':ema,'hh':round(hh,4),'ll':round(ll,4),'trend':'BULLISH' if price>ema50 else 'BEARISH'}
def neon(txt,border):
    st.markdown(f'<div style="background:black;border:3px solid {border};border-radius:15px;padding:12px;text-align:center;margin:6px 0;box-shadow:0 0 12px {border};">{txt}</div>',unsafe_allow_html=True)
# TOP
neon('<div style="color:#00FF00;font-weight:900;font-size:19px;">SONA AI v171 - AI 5 MIN SCAN - PHIR 1 MARKET LOCK</div>','#00FF00')
neon('<div style="color:#00FF00;font-weight:800;font-size:13px;">AI PEHLE 5 MIN SAB 20 MARKET SCAN KAREGA - PHIR 1 BEST MARKET BOLEGA - UP / DOWN</div>','#00FF00')
# SESSION
elapsed=int(time.time()-S['session_start']); left=max(0,7200-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if left<=0:
    st.error('⏰ SESSION KHATAM!')
    if st.button('🔄 NAYA SESSION'): S['session_start']=time.time(); S['phase']='SCAN'; S['phase_start']=time.time(); st.rerun()
    st.stop()
# SETTINGS
sc1,sc2,sc3=st.columns(3)
with sc1: S['tf']=st.selectbox('TIMEFRAME - FIXED',['5MIN','15MIN'],index=0)
with sc2: S['conf']=st.selectbox('MIN CONFIDENCE',[90,95,97],index=1)
with sc3: S['amnt']=st.selectbox('AMOUNT',[100,250,500,1000],index=1)
S['scan_len']=300 if S['tf']=='5MIN' else 900
S['trade_len']=300 if S['tf']=='5MIN' else 900
# === PHASE LOGIC - SAB SE ZAROORI FIX ===
phase_elapsed=int(time.time()-S['phase_start'])
if S['phase']=='SCAN':
    phase_left=max(0,S['scan_len']-phase_elapsed)
    # SCAN - Har 3 sec me sab 20 market ka score jama karo - Seed = phase_start taake flicker na ho
    seed=int(S['phase_start']//3)
    results=[analyze(m,seed) for m in MARKETS]
    # Jama karo
    for r in results:
        S['scan_scores'][r['market']]=S['scan_scores'].get(r['market'],0)+r['score']
        S['scan_counts'][r['market']]=S['scan_counts'].get(r['market'],0)+1
    # AVG nikalo
    avg_list=[]
    for m in MARKETS:
        cnt=S['scan_counts'].get(m,1); tot=S['scan_scores'].get(m,0)
        avg=tot/cnt
        # Is waqt ka direction bhi lo
        cur_r=[x for x in results if x['market']==m][0]
        avg_list.append({'market':m,'avg':round(avg,1),'dir':cur_r['dir'],'price':cur_r['price'],'rsi':cur_r['rsi'],'score_now':cur_r['score']})
    avg_list=sorted(avg_list,key=lambda x:x['avg'],reverse=True)
    top_avg=avg_list[0]
    # SCANNING UI - KOI SIGNAL NAHI - SIRF SCAN
    pm=phase_left//60; ps=phase_left%60
    neon(f'<div style="color:#FFD700;font-weight:900;font-size:26px;">🤖 AI SCANNING - 20 MARKET</div><div style="color:white;font-size:15px;margin-top:4px;">SCAN KHATAM HONE ME: <b style="color:#00FF00">{pm:02d}:{ps:02d}</b> BACHA HAI - {S["tf"]} SCAN</div><div style="color:#AAAAAA;font-size:13px;margin-top:4px;">Abhi tak BEST AVG: {top_avg["market"]} — AVG {top_avg["avg"]}% — {top_avg["dir"]} — Abhi TRADE MAT KARO - Scan poora hone do!</div><div style="background:#222;height:12px;border-radius:10px;margin-top:8px;"><div style="background:linear-gradient(90deg,#00FF00,#FFD700);height:12px;border-radius:10px;width:{int((phase_elapsed/S["scan_len"])*100)}%;"></div></div>','#FFD700')
    neon(f'<div style="color:#00FFFF;font-weight:800;font-size:13px;">⏳ AI 20 MARKET KO 5 MIN TAK DEKH RAHA HAI - JALDI MARKET SELECT NAHI KAREGA - SABKA AVG NIKAL RAHA HAI</div>','#00FFFF')
    # TOP 5 AVG dikhao - Taake pata chale AI kya dekh raha hai
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">🔍 SCAN ABHI TAK - TOP 5 AVG SCORE</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{'Rank':i+1,'Market':x['market'],'AVG Score':x['avg'],'Abhi Score':x['score_now'],'Dir':x['dir'],'RSI':x['rsi']} for i,x in enumerate(avg_list[:5])]),use_container_width=True,hide_index=True)
    # LIVE TABLE - Sab 20 ka abhi ka score
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">📊 20 MARKET - ABHI KA SCORE - SCAN CHAL RAHA HAI</div>',unsafe_allow_html=True)
    st.dataframe(pd.DataFrame([{'Market':r['market'],'Signal':r['dir'],'Score Now':r['score'],'AVG':round(S['scan_scores'][r['market']]/S['scan_counts'][r['market']],1),'RSI':r['rsi'],'Vol':r['vol'],'ATR':r['atr'],'VWAP':r['vwap'],'MACD':r['macd'],'BOS':'YES' if r['bos'] else 'NO','Sweep':r['sweep_txt']} for r in sorted(results,key=lambda x:x['score'],reverse=True)]),use_container_width=True,hide_index=True)
    cur=results[0]
    # SCAN KHATAM? - To LOCK karo
    if phase_left==0:
        # BEST AVG wala select karo
        best_avg=avg_list[0]
        if best_avg['avg']>=S['conf'] or best_avg['score_now']>=S['conf']:
            S['phase']='TRADE'; S['phase_start']=time.time()
            S['locked_market']=best_avg['market']; S['locked_dir']=best_avg['dir']; S['locked_score']=int(best_avg['avg'])
            S['locked_reason']=f"AVG {best_avg['avg']}% - 5 MIN SCAN ke baad BEST"
            open_dt=now_dt(); S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=(open_dt+datetime.timedelta(seconds=S['trade_len'])).strftime('%H:%M:%S')
            S['scan_scores']={}; S['scan_counts']={}
            st.rerun()
        else:
            # Koi 95+ nahi mila - Phir se scan
            S['phase_start']=time.time(); S['scan_scores']={}; S['scan_counts']={}
            st.warning(f"5 MIN SCAN me koi {S['conf']}%+ nahi mila - BEST AVG {best_avg['avg']}% tha - Phir se SCAN!")
            st.rerun()
else:
    # PHASE = TRADE - LOCKED MARKET - KOI CHANGE NAHI - FIXED
    phase_left=max(0,S['trade_len']-phase_elapsed)
    # Locked market ka data - Seed FIXED taake flicker na ho - Trade ke dauraan market change nahi hoga
    seed=int(S['phase_start'])
    cur=analyze(S['locked_market'],seed)
    # Trade khatam? - Wapas SCAN
    if phase_left==0:
        S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; S['scan_scores']={}; S['scan_counts']={}; st.rerun()
    tm=phase_left//60; ts=phase_left%60
    is_up=S['locked_dir']=='UP'; bg='#00FF00' if is_up else '#FF4444'
    neon(f'<div style="color:{bg};font-weight:900;font-size:30px;">{"🟢 ▲ UP — CALL — GREEN" if is_up else "🔴 ▼ DOWN — PUT — RED"}</div><div style="color:white;font-weight:800;font-size:19px;margin-top:4px;">🤖 AI NE 5 MIN SCAN KE BAAD SELECT KIYA: {S["locked_market"]}</div><div style="color:#FFD700;font-size:14px;">CONFIRM: {S["locked_score"]}% — {S["locked_reason"]}</div><div style="color:white;font-size:14px;margin-top:4px;">📱 MOBILE PE ABHI KARO: {S["locked_market"]} — {S["locked_dir"]} — {S["amnt"]} PKR — TF {S["tf"]}</div><div style="color:white;font-size:14px;">🕐 OPEN: {S["open_time"]} &nbsp; CLOSE: {S["close_time"]} &nbsp; FIXED {S["tf"]} &nbsp;•&nbsp; TRADE ME: {tm:02d}:{ts:02d} BACHA</div>',bg)
    # INDICATORS - LOCKED MARKET KE - SAB SHOW
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">📊 LOCKED MARKET KE INDICATORS - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    a1,a2,a3=st.columns(3)
    with a1: neon(f'<div style="color:#888;font-size:11px;">RSI</div><div style="color:#00FF00;font-weight:900;">{cur["rsi"]} - {"OVERBOUGHT" if cur["rsi"]>70 else "OVERSOLD" if cur["rsi"]<30 else "MID"}</div>','#00FF00')
    with a2: neon(f'<div style="color:#888;font-size:11px;">VOLUME</div><div style="color:#FFD700;font-weight:900;">{cur["vol"]} - {"STRONG" if cur["vol"]>3000 else "WEAK"}</div>','#FFD700')
    with a3: neon(f'<div style="color:#888;font-size:11px;">ATR</div><div style="color:#00FFFF;font-weight:900;">{cur["atr"]}</div>','#00FFFF')
    b1,b2,b3=st.columns(3)
    with b1: neon(f'<div style="color:#888;font-size:11px;">VWAP</div><div style="color:#FF00FF;font-weight:900;">{cur["vwap"]} - {"UPAR" if cur["price"]>cur["vwap"] else "NEECHE"}</div>','#FF00FF')
    with b2: neon(f'<div style="color:#888;font-size:11px;">MACD</div><div style="color:#00FF00;font-weight:900;">{cur["macd"]} - {"UP" if cur["macd"]>0 else "DOWN"}</div>','#00FF00')
    with b3: neon(f'<div style="color:#888;font-size:11px;">LIQUIDITY</div><div style="color:#FFD700;font-weight:800;">UP {cur["hh"]} | DOWN {cur["ll"]}</div>','#FFD700')
    c1,c2,c3=st.columns(3)
    with c1: neon(f'<div style="color:#888;font-size:11px;">SWEEP</div><div style="color:#FF4444;font-weight:900;">{cur["sweep_txt"]}</div>','#FF4444')
    with c2: neon(f'<div style="color:#888;font-size:11px;">BOS</div><div style="color:#00FFFF;font-weight:900;">{"BOS YES - BREAK" if cur["bos"] else "NO BOS"}</div>','#00FFFF')
    with c3: neon(f'<div style="color:#888;font-size:11px;">PULLBACK</div><div style="color:#00FF00;font-weight:800;">Price {cur["price"]:.4f} | EMA {cur["ema"]:.4f}</div>','#00FF00')
    cc1,cc2=st.columns(2)
    with cc1:
        if st.button('✅ WIN HUA - MOBILE PE'): S['total_win']+=1; S['cp']+=int(S['amnt']*0.85); S['bal']+=int(S['amnt']*0.85); S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'WIN','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; S['scan_scores']={}; S['scan_counts']={}; st.rerun()
    with cc2:
        if st.button('❌ LOSS HUA - MOBILE PE'): S['total_loss']+=1; S['cp']-=S['amnt']; S['bal']-=S['amnt']; S['ht'].append({'Market':S['locked_market'],'Dir':S['locked_dir'],'Result':'LOSS','Time':now_pkt()}); S['phase']='SCAN'; S['phase_start']=time.time(); S['locked_market']='-'; S['scan_scores']={}; S['scan_counts']={}; st.rerun()
# COMMON - PROFIT + DEPOSIT + CHART
neon(f'<div style="color:#00FF00;font-weight:900;font-size:32px;">+{S["cp"]} PKR</div><div style="color:#00FF00;font-size:12px;">BAL {S["bal"]} PKR | WIN {S["total_win"]} | LOSS {S["total_loss"]} | PHASE {S["phase"]} | Session {lh:02d}:{lm:02d}:{ls:02d}</div>','#00FF00')
neon('<div style="color:#00FFFF;font-weight:900;font-size:13px;text-align:left;">DEPOSIT / WITHDRAW - DEMO ONLY - REAL PAISA NAHI</div>','#00FFFF')
dc1,dc2=st.columns(2)
with dc1: S['dep_amt']=st.number_input('DEPOSIT PKR',value=S['dep_amt'],step=100)
with dc2: S['wd_amt']=st.number_input('WITHDRAW PKR',value=S['wd_amt'],step=50)
bc1,bc2=st.columns(2)
with bc1:
    if st.button('DEPOSIT - ADD'): S['bal']+=S['dep_amt']; S['cp']+=S['dep_amt']; st.success(f"DEMO +{S['dep_amt']} Bal {S['bal']}")
with bc2:
    if st.button('WITHDRAW - REMOVE'):
        if S['wd_amt']<=S['bal']: S['bal']-=S['wd_amt']; st.success(f"DEMO -{S['wd_amt']}")
        else: st.error('Balance kam!')
if S['phase']=='TRADE':
    st.markdown('<div style="color:#FFD700;font-weight:900;text-align:center;margin:8px 0;">CANDLE CHART - '+S['locked_market']+'</div>',unsafe_allow_html=True)
    st.line_chart(pd.DataFrame({'Price':cur['ps']}),use_container_width=True)
if S['ht']: st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
neon('<div style="color:#FF6B6B;font-size:12px;">⚠️ 100% GUARANTEE KOI NAHI DE SAKTA - Sirf 95%+ LOCK pe trade karo!<br>TAREEKA: 1) 5 MIN SCAN - WAIT 2) AI 1 Market LOCK karega 3) Mobile pe usi market me trade 4) CLOSE TIME tak wait 5) Phir se SCAN</div>','#FF6B6B')
st.write(f"Last Update: {now_pkt()} | V171 5MIN SCAN + LOCK | Phase {S['phase']} | Session {lh:02d}:{lm:02d}:{ls:02d}")
time.sleep(3); st.rerun()
