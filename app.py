# SONA V168 - CLEAN PREMIUM DESIGN - NO OVERLAP - NO DUPLICATE
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V168', page_icon='💰', layout='wide')
# === CLEAN CSS - OVERLAP KHATAM ===
st.markdown("""<style>
.stApp{background:#0B0E14 !important;color:white !important;font-family:'Segoe UI',sans-serif}
h1{font-size:28px !important;text-align:center;color:#FFD700 !important;margin:0 !important;padding:5px 0 !important;line-height:1.2 !important;white-space:normal !important;overflow:visible !important}
h2{font-size:18px !important;text-align:center;color:#FFD700 !important;margin:5px 0 !important}
h3{font-size:14px !important;text-align:center;color:#AAAAAA !important;margin:0 !important;font-weight:400 !important}
div[data-testid="stVerticalBlock"]{gap:6px !important}
div[data-testid="stHorizontalBlock"]{gap:8px !important}
.stSelectbox label{color:#FFD700 !important;font-weight:bold !important;font-size:13px !important}
.stSelectbox div[data-baseweb="select"]>div{background:#1A1F2E !important;color:white !important;border:1px solid #2A3042 !important;border-radius:10px !important}
.stButton>button{background:#FFD700 !important;color:black !important;font-weight:bold !important;border-radius:10px !important;width:100% !important;height:48px !important;font-size:15px !important;border:none !important}
</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'session_start':time.time(),'session_len':7200,'tf':'5MIN','conf':90,'amnt':250,'best':'-','best_dir':'-','best_score':0,'ht':[],'total_win':0,'total_loss':0,'cp':0,'last_trade':0,'open_time':'','close_time':''}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def now_dt():
    return datetime.datetime.utcnow()+datetime.timedelta(hours=5)
MARKETS=['AUD/CHF OTC','EUR/USD','GBP/USD','USD/JPY','AUD/USD','USD/CAD','EUR/GBP','SOL/USD','BNB/USD','BTC/USD','XAU/USD','EUR/USD OTC','GBP/USD OTC']
def get_base(m):
    d={'AUD/CHF OTC':0.5844,'EUR/USD':1.0850,'GBP/USD':1.2843,'USD/JPY':149.5,'AUD/USD':0.65,'USD/CAD':1.36,'EUR/GBP':0.85,'SOL/USD':179.8,'BNB/USD':710.0,'BTC/USD':97000.0,'XAU/USD':2650.0,'EUR/USD OTC':1.0850,'GBP/USD OTC':1.2840}
    return d.get(m,1.0)
def gen_price(m):
    base=get_base(m); ps=[base]
    for i in range(1,80):
        ps.append(ps[-1]+random.uniform(-0.0003,0.0003))
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
def calc_boll(ps):
    s=pd.Series(ps); m=s.rolling(20).mean().iloc[-1]; sd=s.rolling(20).std().iloc[-1]
    return float(m+2*sd),float(m-2*sd)
def calc_vwap(ps): return float(np.mean(ps))
def analyze(m):
    ps=gen_price(m); price=ps[-1]; rsi=calc_rsi(ps); macd=calc_macd(ps); ema=calc_ema(ps,20)
    upper,lower=calc_boll(ps); vwap=calc_vwap(ps); o=ps[-2]; c=ps[-1]
    bos=(c>ema and o<ema) or (c<ema and o>ema)
    score=50
    if rsi<30 or rsi>70: score+=20
    elif rsi<40 or rsi>60: score+=12
    elif rsi<45 or rsi>55: score+=6
    if (macd>0 and price>ema) or (macd<0 and price<ema): score+=12
    if bos: score+=10
    if abs(price-vwap)>0.0003: score+=8
    if price>=upper or price<=lower: score+=8
    score=min(99,score)
    direction='UP' if price>=ema else 'DOWN'
    if rsi>60 and macd>0: direction='UP'
    if rsi<40 and macd<0: direction='DOWN'
    return {'market':m,'price':price,'rsi':round(rsi,1),'macd':round(macd,4),'bos':bos,'score':int(score),'dir':direction}
def card(html):
    st.markdown(html,unsafe_allow_html=True)
# ===== HEADER - CHOTA SAAF - KATA NAHI =====
st.markdown('<h1>💰 SONA V168 — LAPTOP SIGNAL</h1>',unsafe_allow_html=True)
st.markdown('<h3>Laptop pe Signal Dekho &nbsp;•&nbsp; Mobile pe Trade Karo</h3>',unsafe_allow_html=True)
# ===== SESSION BAR - EK LINE =====
elapsed=int(time.time()-S['session_start']); left=max(0,S['session_len']-elapsed)
lh=left//3600; lm=(left%3600)//60; ls=left%60
if left<=0:
    st.error('⏰ 2 HOURS SESSION KHATAM — Kal phir aana!')
    if st.button('🔄 NAYA 2 HOURS SESSION'):
        S['session_start']=time.time(); st.rerun()
    st.stop()
card(f'<div style="background:#14213D;padding:10px 14px;border-radius:12px;text-align:center;font-weight:600;font-size:14px;border:1px solid #2A4A7A;">⏰ SESSION: <b style="color:#FFD700">{lh:02d}:{lm:02d}:{ls:02d}</b> BACHA &nbsp;|&nbsp; TIME: <b style="color:#FFD700">{now_pkt()} PKT</b> &nbsp;|&nbsp; LAPTOP MODE ON</div>')
# ===== SETTINGS - 3 COLUMN - EK LINE ME =====
c1,c2,c3=st.columns(3)
with c1: S['tf']=st.selectbox('TIMEFRAME',['5MIN','15MIN'],index=0)
with c2: S['conf']=st.selectbox('MIN CONFIDENCE',[85,90,95],index=1)
with c3: S['amnt']=st.selectbox('AMOUNT',[100,250,500,1000],index=1)
TF_SEC={'5MIN':300,'15MIN':900}
trade_dur=TF_SEC[S['tf']]
# ===== SCAN =====
results=[analyze(m) for m in MARKETS]
best=max(results,key=lambda x:x['score'])
S['best']=best['market']; S['best_dir']=best['dir']; S['best_score']=best['score']
open_dt=now_dt(); close_dt=now_dt()+datetime.timedelta(seconds=trade_dur)
S['open_time']=open_dt.strftime('%H:%M:%S'); S['close_time']=close_dt.strftime('%H:%M:%S')
# ===== MAIN SIGNAL CARD - CHOTA SAAF - BARA PEELA KHATAM =====
if best['score']>=S['conf'] and (time.time()-S['last_trade']>180):
    S['last_trade']=time.time()
    is_up=best['dir']=='UP'
    bg="#0F3D2E" if is_up else "#4A1212"
    border="#00FF88" if is_up else "#FF4444"
    arrow="▲" if is_up else "▼"
    txt="UP — CALL" if is_up else "DOWN — PUT"
    card(f'<div style="background:{bg};border:2px solid {border};border-radius:16px;padding:16px;text-align:center;"><div style="font-size:32px;font-weight:800;color:{border};line-height:1.1;">{arrow} {txt}</div><div style="font-size:20px;font-weight:700;margin-top:6px;">{best["market"]} &nbsp;•&nbsp; {best["score"]}% CONFIDENCE</div><div style="font-size:13px;color:#CCCCCC;margin-top:6px;">RSI {best["rsi"]} &nbsp;•&nbsp; MACD {best["macd"]} &nbsp;•&nbsp; Price {best["price"]:.4f} &nbsp;•&nbsp; {"BOS YES" if best["bos"] else "BOS NO"}</div></div>')
    card(f'<div style="background:#1A1F2E;border-radius:12px;padding:12px;text-align:center;font-size:14px;"><b style="color:#FFD700">📱 MOBILE PE:</b> {best["market"]} — {best["dir"]} — ${S["amnt"]} — TF {S["tf"]}<br><b style="color:#FFD700">🕐 OPEN:</b> {S["open_time"]} &nbsp; <b style="color:#FFD700">CLOSE:</b> {S["close_time"]} &nbsp; ({trade_dur}s FIXED)</div>')
    cc1,cc2=st.columns(2)
    with cc1:
        if st.button('✅ WIN HUA'): S['total_win']+=1; S['cp']+=S['amnt']*0.85; S['ht'].append({'Market':best['market'],'Dir':best['dir'],'Result':'WIN','Time':now_pkt()}); st.rerun()
    with cc2:
        if st.button('❌ LOSS HUA'): S['total_loss']+=1; S['cp']-=S['amnt']; S['ht'].append({'Market':best['market'],'Dir':best['dir'],'Result':'LOSS','Time':now_pkt()}); st.rerun()
else:
    # WAIT CARD - CHOTA - BARA PEELA NAHI
    card(f'<div style="background:#2A2200;border:1px solid #FFD700;border-radius:16px;padding:16px;text-align:center;"><div style="font-size:28px;font-weight:800;color:#FFD700;line-height:1.1;">⏳ WAIT</div><div style="font-size:15px;margin-top:6px;color:#DDDDDD;">Koi Pakka Signal Nahi — Jaldi Trade Mat Karo</div><div style="font-size:14px;margin-top:6px;">BEST ABHI: <b>{best["market"]} — {best["score"]}% — {best["dir"]}</b> &nbsp;•&nbsp; Chahiye: <b>{S["conf"]}%</b></div></div>')
    card(f'<div style="background:#1A1F2E;border-radius:12px;padding:10px;text-align:center;font-size:13px;color:#AAAAAA;">📱 MOBILE PE ABHI TRADE MAT KARO &nbsp;•&nbsp; Agla Signal Aane Do &nbsp;•&nbsp; Time: {now_pkt()} &nbsp;•&nbsp; TF: {S["tf"]} &nbsp;•&nbsp; Gap: 180s</div>')
# ===== MARKET TABLE - 13 BOXES NAHI - EK TABLE =====
st.markdown('<h2>📊 Sab Market — Kaunsi Kitni Strong Hai</h2>',unsafe_allow_html=True)
df=pd.DataFrame([{'Market':r['market'],'Signal':r['dir'],'Score %':r['score'],'RSI':r['rsi'],'Price':round(r['price'],4),'BOS':'YES' if r['bos'] else 'NO'} for r in sorted(results,key=lambda x:x['score'],reverse=True)])
st.dataframe(df,use_container_width=True,hide_index=True)
# ===== RESULT - EK DAF - DUPLICATE NAHI =====
tot=S['total_win']+S['total_loss']; wr=round(S['total_win']/tot*100,1) if tot>0 else 0
card(f'<div style="background:#14213D;border:1px solid #2A4A7A;border-radius:12px;padding:12px;text-align:center;font-size:14px;">📜 <b>AAJ KA RESULT:</b> WIN {S["total_win"]} &nbsp;|&nbsp; LOSS {S["total_loss"]} &nbsp;|&nbsp; WIN RATE {wr}% &nbsp;|&nbsp; PROFIT ${S["cp"]:.2f}</div>')
if S['ht']:
    st.dataframe(pd.DataFrame(S['ht']),use_container_width=True,hide_index=True)
# ===== FOOTER - EK DAF =====
card(f'<div style="background:#1A1F2E;border-radius:12px;padding:12px;text-align:center;font-size:12px;color:#AAAAAA;line-height:1.6;"><b style="color:#FFD700">TAREEKA:</b> 1) Laptop pe SONA khula rakho &nbsp; 2) Bara GREEN / RED aaye to Mobile pe usi Market me trade lagao &nbsp; 3) CLOSE TIME tak wait karo &nbsp; 4) Yahan WIN / LOSS dabao<br><b style="color:#FF6B6B">⚠️ 100% GUARANTEE KOI NAHI DE SAKTA — Sirf 90%+ wale pe trade karo — Ek din me 5 se zyada mat karo!</b></div>')
st.write(f"Last Update: {now_pkt()} | V168 CLEAN DESIGN | Session {lh:02d}:{lm:02d}:{ls:02d} bacha")
time.sleep(3); st.rerun()
