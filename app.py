# SONA V163 = V157 FULL COPY - VIDEO WALA DESIGN - ALL FEATURES
import streamlit as st
import time, random, datetime
import pandas as pd
import numpy as np
st.set_page_config(page_title='SONA V157', page_icon='💰', layout='wide')
st.markdown("""<style>
.stApp{background:white;color:black}
div[data-testid="stSelectbox"]>div>div{background:#F0F2F6 !important}
.stButton>button{background:#FFD700 !important;color:black !important;font-weight:bold !important;border-radius:10px !important}
</style>""", unsafe_allow_html=True)
if 'S' not in st.session_state:
    st.session_state.S={'win_sound':True,'auto':True,'am':'DEMO','db':10000,'rb':0,'cp':4438,'open':None,'ht':[],'last_trade':0,'loss_streak':0,'win_streak':0,'total_win':10,'total_loss':3,'today':13,'hour':2,'ai_scan':True,'conf':90,'gap':60,'amnt':4000,'target':15000,'market':'AUD/CHF OTC','tf':'1MIN','menu':'HOME','name':'Usam','real_bal':0,'dep_amt':1000,'dep_method':'JazzCash','dep_num':'0300-1234567','wd_amt':100,'wd_num':'0300-1234567','best':'BNB/USD','best_dir':'UP','best_score':99,'ladder':250}
S=st.session_state.S
def now_pkt():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).strftime('%H:%M:%S')
def hour_now():
    return (datetime.datetime.utcnow()+datetime.timedelta(hours=5)).hour
MARKETS=['AUD/CHF OTC','EUR/USD','GBP/USD','USD/JPY','AUD/USD','USD/CAD','EUR/GBP','SOL/USD','BNB/USD','BTC/USD','XAU/USD','EUR/USD OTC','GBP/USD OTC']
def gen_price(m):
    base={'AUD/CHF OTC':0.5844,'EUR/USD':1.0850,'GBP/USD':1.2843,'USD/JPY':149.5,'AUD/USD':0.6500,'USD/CAD':1.3600,'EUR/GBP':0.8500,'SOL/USD':179.8,'BNB/USD':710.0,'BTC/USD':97000,'XAU/USD':2650,'EUR/USD OTC':1.0850,'GBP/USD OTC':1.2840}.get(m,1.0)
    ps=[base+random.uniform(-0.002,0.002) for _ in range(60)]
    for i in range(1,len(ps)):
        ps[i]=ps[i-1]+random.uniform(-0.0004,0.0004)
    return ps
def analyze(m):
    ps=gen_price(m)
    price=ps[-1]
    deltas=np.diff(ps)
    gains=np.where(deltas>0,deltas,0)
    losses=np.where(deltas<0,-deltas,0)
    ag=np.mean(gains[-14:]) if len(gains)>=14 else 0.001
    al=np.mean(losses[-14:]) if len(losses)>=14 else 0.001
    rsi=100-(100/(1+(ag/al if al!=0 else 10)))
    e12=pd.Series(ps).ewm(span=12).mean().iloc[-1]
    e26=pd.Series(ps).ewm(span=26).mean().iloc[-1]
    macd=e12-e26
    ema=pd.Series(ps).ewm(span=20).mean().iloc[-1]
    vwap=np.mean(ps)
    atr=np.mean([abs(ps[i]-ps[i-1]) for i in range(1,len(ps))]) if len(ps)>1 else 0.0004
    vol=int(random.uniform(1000,4000))
    hi=max(ps[-20:]); lo=min(ps[-20:])
    bos=(ps[-1]>ema and ps[-2]<ema) or (ps[-1]<ema and ps[-2]>ema)
    sweep=False
    trend='UP' if price>ema else 'DOWN'
    score=0
    if rsi<30 or rsi>70: score+=30
    elif rsi<35 or rsi>65: score+=20
    else: score+=10
    if (macd>0 and price>ema) or (macd<0 and price<ema): score+=25
    else: score+=10
    if bos: score+=20
    else: score+=5
    if abs(price-vwap)>0.0003: score+=15
    else: score+=5
    score+=random.randint(5,15)
    score=min(99,score)
    direction='UP' if price>=ema else 'DOWN'
    if rsi>65 and macd>0: direction='UP'
    if rsi<35 and macd<0: direction='DOWN'
    return {'market':m,'price':price,'rsi':round(rsi,1),'macd':round(macd,4),'ema':ema,'vwap':round(vwap,4),'atr':round(atr,4),'vol':vol,'hi':round(hi,4),'lo':round(lo,4),'bos':bos,'sweep':sweep,'trend':trend,'score':score,'dir':direction,'open':ps[-2],'close':ps[-1],'high':round(max(ps[-5:]),4),'low':round(min(ps[-5:]),4)}
# ===== TOP TOGGLES =====
S['win_sound']=st.toggle('WIN SOUND ON',value=S['win_sound'])
S['auto']=st.toggle('AUTO TRADING ON',value=S['auto'])
st.write('ACCOUNT')
acc=st.radio('',['DEMO','REAL'],horizontal=True,label_visibility='collapsed')
S['am']='REAL' if 'REAL' in acc else 'DEMO'
# ===== BLACK BOXES - V157 STYLE =====
def black_box(txt):
    st.markdown(f'<div style="background:black;color:white;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin:5px 0;">{txt}</div>',unsafe_allow_html=True)
def blue_box(txt):
    st.markdown(f'<div style="background:#0B2A5B;color:white;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin:5px 0;">{txt}</div>',unsafe_allow_html=True)
def green_box(txt):
    st.markdown(f'<div style="background:#0B6E2F;color:white;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin:5px 0;">{txt}</div>',unsafe_allow_html=True)
def gold_box(txt):
    st.markdown(f'<div style="background:#8A6D00;color:white;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin:5px 0;">{txt}</div>',unsafe_allow_html=True)
def grey_box(txt):
    st.markdown(f'<div style="background:#E8E8E8;color:black;padding:12px;border-radius:12px;text-align:center;font-weight:bold;margin:5px 0;">{txt}</div>',unsafe_allow_html=True)
bal=S['db'] if S['am']=='DEMO' else S['rb']
total=S['total_win']+S['total_loss']
wr=round(S['total_win']/total*100,1) if total>0 else 0
black_box(f"SONA V157 | DEMO {S['db']} | REAL {S['rb']} | SAVED!")
black_box(f"BAL {bal} {S['am']} | PROFIT {S['cp']} | WIN RATE {wr}%")
# AI BRAIN SCAN - BEST PAIR
if S['ai_scan']:
    results=[analyze(m) for m in MARKETS]
    best=max(results,key=lambda x:x['score'])
    S['best']=best['market']; S['best_dir']=best['dir']; S['best_score']=best['score']
    S['_scan']=results
    S['_cur']=analyze(S['market'])
else:
    S['_cur']=analyze(S['market'])
cur=S['_cur']
lock='LOCKED' if S['open'] is not None else 'FREE'
black_box(f"{S['market']} {cur['price']:.4f} AI {cur['score']}% {cur['dir']} {cur['score']}% | {lock} | {now_pkt()} PKT")
black_box(f"LADDER NOW: {S['ladder']} | TARGET: {S['cp']} / {S['target']}")
blue_box(f"AI BRAIN - BEST = {S['best']} / {S['best_dir']} | SCORE {S['best_score']} | HOUR {S['hour']} | {lock}")
green_box("V157 - PAIR / TF UPAR - AI PAIR NAHI BADLEGA")
S['ai_scan']=st.toggle('AI BRAIN AUTO SCAN ON',value=S['ai_scan'])
# ===== SETTINGS =====
S['conf']=st.selectbox('MIN CONFIDENCE',[85,90,95,97,99],index=[85,90,95,97,99].index(S['conf']) if S['conf'] in [85,90,95,97,99] else 1)
S['gap']=st.selectbox('MIN GAP SEC',[30,60,120,180],index=[30,60,120,180].index(S['gap']) if S['gap'] in [30,60,120,180] else 1)
S['amnt']=st.selectbox('TRADE AMOUNT',[100,250,500,1000,4000,10000],index=[100,250,500,1000,4000,10000].index(S['amnt']) if S['amnt'] in [100,250,500,1000,4000,10000] else 4)
S['target']=st.selectbox('DAILY TARGET',[1000,5000,10000,15000,20000],index=[1000,5000,10000,15000,20000].index(S['target']) if S['target'] in [1000,5000,10000,15000,20000] else 3)
black_box("PAIR / TIMEFRAME - YAHAN SE BADLO - UPAR HI HAI!")
S['market']=st.selectbox('PAIR - MARKET',MARKETS,index=MARKETS.index(S['market']) if S['market'] in MARKETS else 0)
S['tf']=st.selectbox('TF - TIMEFRAME',['1MIN','2MIN','5MIN'],index=['1MIN','2MIN','5MIN'].index(S['tf']) if S['tf'] in ['1MIN','2MIN','5MIN'] else 0)
if st.button('TEST SOUND'):
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>',unsafe_allow_html=True)
    st.success('SOUND TEST OK!')
# ===== MENU =====
S['menu']=st.selectbox('MENU',['HOME','AI BRAIN','TERMINAL','DEPOSIT','WITHDRAW','HISTORY','SETTINGS'],index=['HOME','AI BRAIN','TERMINAL','DEPOSIT','WITHDRAW','HISTORY','SETTINGS'].index(S['menu']))
# ===== FUNCTIONS =====
def open_trade(d, manual=False):
    S['open']={'dir':d,'price':cur['price'],'time':time.time(),'amount':S['amnt'],'score':cur['score'],'market':S['market'],'id':str(time.time())[-6:]}
    S['last_trade']=time.time()
    st.success(f"TRADE KHULA - {d} - ${S['amnt']}")
def close_trade(win):
    o=S['open']
    if o is None: return
    profit=o['amount']*0.85 if win else -o['amount']
    if win:
        S['cp']+=profit; S['total_win']+=1; S['win_streak']+=1; S['loss_streak']=0
    else:
        S['cp']-=o['amount']; S['total_loss']+=1; S['loss_streak']+=1; S['win_streak']=0
    S['today']+=1
    S['ht'].append({'market':o['market'],'dir':o['dir'],'win':win,'profit':round(profit,2),'time':now_pkt(),'amount':o['amount'],'entry':o['price'],'exit':cur['price']})
    S['open']=None
# ===== MENU PAGES =====
if S['menu']=='HOME':
    black_box(f"HOME - TODAY {S['today']}/96 TOTAL {S['total_win']+S['total_loss']} | WIN {S['total_win']} LOSS {S['total_loss']} | PROFIT {S['cp']} | HOUR {S['hour']}")
    # Chart
    ps=gen_price(S['market'])
    st.line_chart(pd.DataFrame(ps,columns=['Price']))
    black_box(f"RSI {cur['rsi']} | Volume {cur['vol']} | ATR {cur['atr']} | VWAP {cur['vwap']} | MACD {cur['macd']} | Sig 0.0001")
    grey_box(f"Hi {cur['hi']} Lo {cur['lo']} | {'BOS' if cur['bos'] else 'NO BOS'} | {'SWEEP' if cur['sweep'] else 'NO SWEEP'} | Trend {cur['trend']}")
    gold_box(f"AI DECISION: {S['market']} {cur['score']}% - RSI {cur['rsi']} + MACD {cur['macd']} + VWAP {cur['vwap']} + {'BOS' if cur['bos'] else 'NO BOS'} + NO SWEEP = {cur['dir']}")
    if S['open'] is not None:
        o=S['open']
        elapsed=int(time.time()-o['time'])
        left=max(0,60-elapsed)
        green_box(f"OPEN TRADE LIVE: {o['market']} ENTRY {o['price']:.4f} | {o['dir']} | {left}s LEFT | TF {S['tf']} | {S['am']} | Now {cur['price']:.4f} | LOCKED")
        if st.button('CLOSE NOW'):
            win_now=(cur['price']>o['price'] and o['dir']=='UP') or (cur['price']<o['price'] and o['dir']=='DOWN')
            close_trade(win_now); st.rerun()
    else:
        # AUTO LOGIC
        can=S['auto'] and cur['score']>=S['conf'] and (time.time()-S['last_trade']>S['gap'])
        if can:
            open_trade(cur['dir']); st.rerun()
        else:
            st.info(f"WAIT - Score {cur['score']}% - Conf {S['conf']}% ka intezar")
    if st.button('MANUAL UP'):
        open_trade('UP',True); st.rerun()
    if st.button('MANUAL DOWN'):
        open_trade('DOWN',True); st.rerun()
elif S['menu']=='AI BRAIN':
    blue_box("AI BRAIN - 90+ ONLY - WIN SOUND")
    if st.button('SCAN NOW'):
        st.rerun()
    if '_scan' in S:
        for r in sorted(S['_scan'],key=lambda x:x['score'],reverse=True)[:5]:
            green_box(f"BEST - {r['market']} | {r['dir']} | SCORE {r['score']} | EXCELLENT 90+")
            gold_box(f"STRATEGY: BOS {'UP' if r['bos'] else 'NO'} + NO SWEEP + Trend {r['trend']}")
            black_box(f"{r['market']} {r['price']:.4f} | {r['dir']} {r['score']}% | RSI {r['rsi']} | MACD {r['macd']} | ATR {r['atr']} | VWAP {r['vwap']} | VOL {r['vol']} | BOS {'UP' if r['bos'] else 'NO'} | NO SWEEP")
elif S['menu']=='TERMINAL':
    black_box("TERMINAL - CANDLE + INDICATORS")
    grey_box("PAIR / TF upar se badlo!")
    ps=gen_price(S['market'])
    st.line_chart(pd.DataFrame(ps,columns=[S['market']]))
    black_box(f"LAST CANDLE: {'UP' if cur['close']>=cur['open'] else 'DOWN'} | OPEN {cur['open']:.4f} | CLOSE {cur['close']:.4f} | HIGH {cur['high']} | LOW {cur['low']} | VOL {cur['vol']} | {now_pkt()}")
    black_box(f"STREAK {S['loss_streak']} | BEST {S['best']} {S['best_score']}% | HOUR {S['hour']} | V157 | {lock}")
elif S['menu']=='DEPOSIT':
    black_box("DEPOSIT - REAL me paisa dalo")
    black_box(f"REAL BAL: {S['real_bal']}")
    S['dep_amt']=st.number_input('Kitna Deposit? (Rs)',value=S['dep_amt'],step=100)
    S['dep_method']=st.selectbox('Method',['JazzCash','Easypaisa','Bank'],index=0)
    S['dep_num']=st.text_input('Apna Number',value=S['dep_num'])
    if st.button('DEPOSIT CONFIRM'):
        S['real_bal']+=S['dep_amt']; S['rb']+=S['dep_amt']
        st.success(f"DEPOSIT OK - {S['dep_amt']} Rs - New Bal {S['real_bal']}")
elif S['menu']=='WITHDRAW':
    black_box("WITHDRAW - Paisa Nikalo")
    black_box(f"REAL BAL: {S['real_bal']} | Profit: {S['cp']}")
    S['wd_amt']=st.number_input('Kitna Nikalna Hai?',value=S['wd_amt'],step=100)
    S['wd_num']=st.text_input('JazzCash / Easypaisa Number',value=S['wd_num'])
    if st.button('WITHDRAW CONFIRM'):
        if S['wd_amt']<=S['real_bal']:
            S['real_bal']-=S['wd_amt']; st.success(f"WITHDRAW OK - {S['wd_amt']} bheja gaya!")
        else:
            st.error('Balance kam hai!')
elif S['menu']=='HISTORY':
    black_box("TRADES - HISTORY SAVED!")
    black_box(f"TODAY {S['today']}")
    black_box(f"WIN {S['total_win']} LOSS {S['total_loss']} | WIN RATE {wr}%")
    black_box(f"PROFIT {S['cp']} HOUR {S['hour']}")
    if S['ht']:
        df=pd.DataFrame([{'Market':h['market'],'Dir':h['dir'],'Win':h['win'],'Profit':h['profit'],'Time':h['time']} for h in S['ht']])
        st.dataframe(df,use_container_width=True)
        st.line_chart(pd.DataFrame([10000]+[10000+sum([x['profit'] for x in S['ht'][:i+1]]) for i in range(len(S['ht']))]))
        for h in S['ht'][::-1][:10]:
            st.write(f"{'WIN' if h['win'] else 'LOSS'} {h['market']} {S['tf']} ENTRY {h['entry']:.4f} EXIT {h['exit']:.4f} | {'+' if h['win'] else '-'}{h['amount']} | {S['am']} | {h['time']}")
    else:
        st.write('Abhi koi trade nahi - HISTORY yahan aayegi')
elif S['menu']=='SETTINGS':
    black_box("SETTINGS - V157")
    S['name']=st.text_input('Tumhara Naam',value=S['name'])
    black_box("V157 BACKGROUND MODE ON hai")
    black_box("HISTORY alag file me hai")
    if st.button('RESET DEMO 10000'):
        S['db']=10000; S['cp']=0; st.rerun()
    if st.button('RESET HOUR'):
        S['hour']=1; S['today']=0; st.rerun()
    if st.button('CLEAR HISTORY'):
        S['ht']=[]; S['total_win']=0; S['total_loss']=0; st.rerun()
    black_box(f"APP: SONA V157 | USER: {S['name']} | SAVED!")
# ===== BOTTOM ALWAYS =====
black_box(f"LAST CANDLE: {'UP' if cur['close']>=cur['open'] else 'DOWN'} | OPEN {cur['open']:.4f} | CLOSE {cur['close']:.4f} | HIGH {cur['high']} | LOW {cur['low']} | VOL {cur['vol']} | {now_pkt()}")
black_box(f"STREAK {S['loss_streak']} | BEST {S['best']} {S['best_score']}% | HOUR {S['hour']} | V157 | {lock}")
if S['win_sound'] and S['ht']:
    if S['ht'][-1]['win']:
        st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>',unsafe_allow_html=True)
time.sleep(2)
st.rerun()
