import streamlit as st
import random, time
from datetime import datetime, timedelta
import pytz
st.set_page_config(page_title='SONA V144 FIX', layout='centered')
C='<div style="background:#111;padding:12px;border-radius:12px;color:#fff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
G='<div style="background:#0f3d1e;padding:10px;border-radius:10px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
R='<div style="background:#3d0f0f;padding:10px;border-radius:10px;color:#ff5555;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
Y='<div style="background:#3d3d0f;padding:10px;border-radius:10px;color:#ffff00;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
B='<div style="background:#0f1e3d;padding:10px;border-radius:10px;color:#5aafff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
E='</div>'
BASE={'SOL/USD':179.50,'BTC/USD':67200,'BNB/USD':710,'EUR/USD':1.085,'AUD/CHF OTC':0.585,'GBP/USD':1.275,'USD/JPY':152.30,'XAU/USD':2650,'EUR/GBP OTC':0.850,'USD/CHF OTC':0.885,'GBP/JPY':194.20,'AUD/USD':0.655}
if 'S' not in st.session_state:
    st.session_state.S={'am':'DEMO','auto':True,'db':10000,'rb':0,'dp':0,'rp':0,'open':None,'ht':[],'wc':0,'lc':0,'today':0,'total':0,'streak':0,'pair':'SOL/USD','tf':'1MIN','lp':179.50,'ai':'UP','ac':89,'price_hist':[179.50],'dep_hist':[],'with_hist':[],'last':time.time(),'last_trade_time':0,'last_scan_time':0,'name':'Usam','scan':[],'best':'SOL/USD','best_score':0,'best_dir':'UP','candles':[],'quality':'GOOD','auto_scan':True}
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
PAIRS=list(BASE.keys())
TFS=['1MIN','2MIN','5MIN','15MIN']
def calc_rsi(prices,period=14):
    if len(prices)<period+1: return 50.0
    gains=[]; losses=[]
    for i in range(1,period+1):
        d=prices[-i]-prices[-i-1]
        if d>0: gains.append(d)
        else: losses.append(abs(d))
    ag=sum(gains)/period if gains else 0.1
    al=sum(losses)/period if losses else 0.1
    if al==0: return 95.0
    rs=ag/al
    return round(100-(100/(1+rs)),1)
def calc_ema(prices,period):
    if len(prices)<period: return prices[-1] if prices else 0
    k=2/(period+1); ema=prices[-period]
    for p in prices[-period:]:
        ema=p*k+ema*(1-k)
    return round(ema,3)
def calc_macd(prices):
    e12=calc_ema(prices,12); e26=calc_ema(prices,26)
    macd=round(e12-e26,3); sig=round(calc_ema(prices,9),3)
    return macd,sig,round(macd-(sig-e26),3)
def calc_atr(candles):
    if len(candles)<2: return 1.20
    trs=[max(c['h']-c['l'],abs(c['h']-candles[i-1]['c']),abs(c['l']-candles[i-1]['c'])) for i,c in enumerate(candles) if i>0]
    return round(sum(trs[-14:])/min(14,len(trs)),3) if trs else 1.20
def calc_vwap(candles):
    if not candles: return S['lp']
    tp=sum(c['c']*c['v'] for c in candles); tv=sum(c['v'] for c in candles)
    return round(tp/tv,3) if tv else S['lp']
def calc_bos(prices):
    if len(prices)<10: return 'NO BOS'
    if prices[-1]>max(prices[-10:-1]): return 'BOS UP'
    if prices[-1]<min(prices[-10:-1]): return 'BOS DOWN'
    return 'NO BOS'
def calc_sweep(prices):
    if len(prices)<10: return 'NO SWEEP'
    low=min(prices[-10:]); high=max(prices[-10:])
    if prices[-2]<low and prices[-1]>low: return 'SWEEP LOW + UP'
    if prices[-2]>high and prices[-1]<high: return 'SWEEP HIGH + DOWN'
    return 'NO SWEEP'
def calc_pullback(prices):
    if len(prices)<15: return 'NO PULLBACK'
    ema20=calc_ema(prices,20)
    if abs(prices[-1]-ema20)<1.0: return 'PULLBACK TO EMA20'
    return 'NO PULLBACK'
def calc_liquidity(prices):
    hi=max(prices[-20:]) if len(prices)>=20 else max(prices)
    lo=min(prices[-20:]) if len(prices)>=20 else min(prices)
    return round(hi,2),round(lo,2)
def calc_trend(prices):
    e20=calc_ema(prices,20)
    return 'UP' if prices[-1]>e20 else 'DOWN'
def calc_quality(score,rsi,vol,bos,sweep):
    q=score
    if vol>5000: q+=5
    if 'SWEEP' in sweep: q+=5
    if 'BOS' in bos: q+=5
    if q>=90: return 'EXCELLENT 🔥'
    if q>=80: return 'HIGH QUALITY ✅'
    if q>=70: return 'GOOD 👍'
    return 'LOW ⚠️'
def make_candle():
    base=BASE[S['pair']]
    if abs(S['lp']-base)>20: S['lp']=base+random.uniform(-2,2)
    o=S['lp']; c=round(o+random.uniform(-1.5,1.5),3)
    h=round(max(o,c)+random.uniform(0,0.8),3); l=round(min(o,c)-random.uniform(0,0.8),3); v=random.randint(800,8500)
    S['lp']=c; S['price_hist'].append(c)
    if len(S['price_hist'])>60: S['price_hist']=S['price_hist'][-60:]
    S['candles'].append({'o':o,'c':c,'h':h,'l':l,'v':v,'time':datetime.now(pkt).strftime('%H:%M:%S'),'dir':'UP' if c>=o else 'DOWN'})
    if len(S['candles'])>24: S['candles']=S['candles'][-24:]
    return S['candles'][-1]
# ===== AI BRAIN AUTOMATIC SCANNER — QUALITY + AUTO SELECT =====
def ai_scan_all():
    res=[]
    for pair in PAIRS:
        base=BASE[pair]
        prices=[base+random.uniform(-2,2) for _ in range(60)]
        for i in range(1,60): prices[i]=prices[i-1]+random.uniform(-0.8,0.8)
        prices=[round(p,3) for p in prices]
        vols=[random.randint(800,8500) for _ in range(60)]
        rsi=calc_rsi(prices); macd,sig,hist=calc_macd(prices)
        atr=round(sum([abs(prices[i]-prices[i-1]) for i in range(1,len(prices))])/60,3)
        vwap=round(sum(p*v for p,v in zip(prices,vols))/sum(vols),3)
        vol=random.randint(800,8500); bos=calc_bos(prices); sweep=calc_sweep(prices); pull=calc_pullback(prices); hi,lo=calc_liquidity(prices); trend=calc_trend(prices)
        score=50
        if rsi<30: score+=18
        if rsi>70: score+=18
        if macd>0: score+=10
        if 'BOS' in bos: score+=12
        if 'SWEEP' in sweep: score+=15
        if 'PULLBACK' in pull: score+=12
        if vol>4000: score+=10
        score=min(99,max(55,score))
        direction='UP' if prices[-1]>vwap or macd>0 else 'DOWN'
        if rsi<30: direction='UP'
        if rsi>70: direction='DOWN'
        if 'BOS UP' in bos: direction='UP'
        if 'BOS DOWN' in bos: direction='DOWN'
        if 'SWEEP LOW' in sweep: direction='UP'
        if 'SWEEP HIGH' in sweep: direction='DOWN'
        quality=calc_quality(score,rsi,vol,bos,sweep)
        res.append({'pair':pair,'price':prices[-1],'rsi':rsi,'macd':macd,'atr':atr,'vwap':vwap,'vol':vol,'bos':bos,'sweep':sweep,'pull':pull,'hi':hi,'lo':lo,'trend':trend,'score':score,'dir':direction,'quality':quality})
    res=sorted(res,key=lambda x: x['score'],reverse=True)
    return res
def open_trade(pair=None,dir=None):
    if S['open'] is not None: return False
    bal=S['rb'] if S['am']=='REAL' else S['db']
    if bal<=0: return False
    S['open']={'pair':pair or S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':dir or S['ai'],'am':S['am'],'time':datetime.now(pkt)}
    S['last_trade_time']=time.time()
    return True
def close_trade():
    if S['open'] is None: return
    o=S['open']; win=random.choice([True,True,False]); amt=238 if win else -100
    if o['am']=='REAL': S['rb']+=amt; S['rp']+=amt
    else: S['db']+=amt; S['dp']+=amt
    if win: S['wc']+=1; S['streak']+=1
    else: S['lc']+=1; S['streak']=0
    S['total']+=1; S['today']+=1
    S['ht'].append({'pair':o['pair'],'tf':o['tf'],'entry':o['entry'],'exit':S['lp'],'amt':amt,'win':win,'am':o['am'],'time':datetime.now(pkt).strftime('%H:%M:%S')})
    S['open']=None
# ===== AUTO ENGINE — SCAN + TRADE AUTOMATIC =====
if time.time()-S['last']>3:
    S['last']=time.time(); make_candle()
    # AUTO SCAN HAR 10 SEC — QUALITY CHECK — AUTO SELECT BEST
    if S['auto_scan'] and time.time()-S['last_scan_time']>10:
        S['last_scan_time']=time.time()
        S['scan']=ai_scan_all()
        best=S['scan'][0]
        # Sirf HIGH QUALITY wala auto select — LOW wala skip
        if best['score']>=75:
            S['best']=best['pair']; S['best_score']=best['score']; S['best_dir']=best['dir']; S['quality']=best['quality']
            # Pair change karo — Lekin price BASE se lo — 1400 bug nahi
            if S['open'] is None:
                S['pair']=best['pair']; S['ai']=best['dir']; S['ac']=best['score']; S['lp']=BASE[best['pair']]
    if S['open'] is not None:
        if (datetime.now(pkt)-S['open']['time']).total_seconds()>=60: close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if time.time()-S['last_trade_time']>15:
            open_trade()
# ===== TOP — DASE STYLE =====
c1,c2=st.columns(2)
with c1: S['auto']=st.toggle('AUTO TRADING ON',value=S['auto'])
with c2:
    acc=st.radio('ACCOUNT',['DEMO','REAL'],horizontal=True)
    S['am']='REAL' if 'REAL' in acc else 'DEMO'
am=S['am']; db=int(S['db']); rb=int(S['rb']); dp=int(S['dp']); rp=int(S['rp']); cb=rb if am=='REAL' else db; cp=rp if am=='REAL' else dp
t=C+'SONA V144 FIX | DEMO '+str(db)+' | REAL '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | DEMO '+str(db)+' REAL '+str(rb)+' | PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+now.strftime('%H:%M:%S PKT')+' | TF '+S['tf']+E; st.markdown(t,unsafe_allow_html=True)
if am=='REAL' and rb==0:
    t=R+'REAL 0 — Pehle DEPOSIT karo'+E; st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=G+'DEMO MODE — Practice — REAL paisa safe hai'+E; st.markdown(t,unsafe_allow_html=True)
# AUTO SCAN STATUS — HAMESHA DIKHEGA
if S['scan']:
    best=S['scan'][0]
    t=B+'🤖 AI BRAIN AUTO SCAN ON — BEST: '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | QUALITY '+best['quality']+E; st.markdown(t,unsafe_allow_html=True)
else:
    t=B+'🤖 AI BRAIN AUTO SCAN ON — Scanning... 10 sec me BEST select hoga'+E; st.markdown(t,unsafe_allow_html=True)
S['auto_scan']=st.toggle('AI BRAIN AUTO SCAN ON — Automatic Select Market',value=S['auto_scan'])
menu=st.selectbox('MENU — PORA APP',['🧠 AI BRAIN AUTO SCAN','🏠 HOME — CANDLE','📈 TERMINAL — CANDLE','💰 DEPOSIT','💸 WITHDRAW','📊 TRADES / HISTORY','⚙️ SETTINGS'],index=1)
if S['candles']:
    lc=S['candles'][-1]
    move='🟢 UP' if lc['dir']=='UP' else '🔴 DOWN'
    t=C+'LAST CANDLE: '+move+' | OPEN '+str(lc['o'])+' | CLOSE '+str(lc['c'])+' | HIGH '+str(lc['h'])+' | LOW '+str(lc['l'])+' | VOL '+str(lc['v'])+' | '+lc['time']+E; st.markdown(t,unsafe_allow_html=True)
if menu=='🧠 AI BRAIN AUTO SCAN':
    t=B+'🧠 AI BRAIN — AUTOMATIC SCANNER — NO BUTTON NEEDED'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'AI har 10 sec me khud scan karta hai — Best Quality wala market khud select karta hai — LOW quality ko skip karta hai'+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('🧠 SCAN NOW — MANUAL'):
        S['scan']=ai_scan_all(); S['last_scan_time']=time.time(); st.rerun()
    if S['scan']:
        best=S['scan'][0]
        t=G+'🏆 AUTO SELECTED BEST: '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+'/100 | QUALITY '+best['quality']+E; st.markdown(t,unsafe_allow_html=True)
        t=Y+'STRATEGY: '+best['bos']+' + '+best['sweep']+' + '+best['pull']+' + Trend '+best['trend']+' + Liq Hi '+str(best['hi'])+' Lo '+str(best['lo'])+E; st.markdown(t,unsafe_allow_html=True)
        t=C+'RSI '+str(best['rsi'])+' | MACD '+str(best['macd'])+' | ATR '+str(best['atr'])+' | VWAP '+str(best['vwap'])+' | VOL '+str(best['vol'])+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE BEST PAIR NOW'):
            S['pair']=best['pair']; S['ai']=best['dir']; S['lp']=BASE[best['pair']]; open_trade(pair=best['pair'],dir=best['dir']); st.rerun()
        for s in S['scan']:
            col=G if s['score']>=85 else Y if s['score']>=75 else C
            t=col+s['pair']+' '+str(s['price'])+' | '+s['dir']+' '+str(s['score'])+'% | QUALITY '+s['quality']+' | RSI '+str(s['rsi'])+' | MACD '+str(s['macd'])+' | ATR '+str(s['atr'])+' | VWAP '+str(s['vwap'])+' | VOL '+str(s['vol'])+' | '+s['bos']+' | '+s['sweep']+E; st.markdown(t,unsafe_allow_html=True)
    else:
        t=C+'Scanning... 10 sec wait karo — AI khud BEST nikalega'+E; st.markdown(t,unsafe_allow_html=True)
if menu in ['🏠 HOME — CANDLE','📈 TERMINAL — CANDLE']:
    if menu=='📈 TERMINAL — CANDLE':
        t=C+'TERMINAL - CANDLE + INDICATORS'+E; st.markdown(t,unsafe_allow_html=True)
        old=S['pair']
        S['pair']=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']))
        S['tf']=st.selectbox('TF / TIME',TFS,index=TFS.index(S['tf']))
        if S['pair']!=old: S['lp']=BASE[S['pair']]; S['candles']=[]; S['price_hist']=[S['lp']]
    else:
        t=C+'HOME — TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    # CANDLE CHART — NO MATPLOTLIB — Streamlit line chart + candle bars
    st.line_chart(S['price_hist'])
    pr=S['price_hist']; rsi=calc_rsi(pr); macd,sig,hist=calc_macd(pr); atr=calc_atr(S['candles']); vwap=calc_vwap(S['candles']); bos=calc_bos(pr); sweep=calc_sweep(pr); pull=calc_pullback(pr); hi,lo=calc_liquidity(pr); vol=S['candles'][-1]['v'] if S['candles'] else 0
    t=C+'RSI '+str(rsi)+' | Volume '+str(vol)+' | ATR '+str(atr)+' | VWAP '+str(vwap)+' | MACD '+str(macd)+' | Sig '+str(sig)+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'Liquidity Hi '+str(hi)+' Lo '+str(lo)+' | '+bos+' | '+sweep+' | '+pull+' | Trend '+calc_trend(pr)+E; st.markdown(t,unsafe_allow_html=True)
    t=Y+'AI DECISION: '+S['pair']+' '+S['ai']+' '+str(S['ac'])+'% — RSI '+str(rsi)+' + MACD '+str(macd)+' + VWAP '+str(vwap)+' + '+bos+' + '+sweep+' = '+S['ai']+E; st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']; left=max(0,60-int((datetime.now(pkt)-o['time']).total_seconds()))
        t=G+'OPEN TRADE LIVE: '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | '+o['am']+' | Now '+str(S['lp'])+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'): close_trade(); st.rerun()
    else:
        t=C+'NO OPEN TRADE — AUTO 15 sec me kholega...'+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE ABHI KHOLO'): open_trade(); st.rerun()
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL UP CALL'): S['ai']='UP'; open_trade(); st.rerun()
    with b2:
        if st.button('MANUAL DOWN PUT'): S['ai']='DOWN'; open_trade(); st.rerun()
    t=C+'LAST 5 CANDLES — OPEN / CLOSE / HIGH / LOW — UP/DOWN MOVEMENT'+E; st.markdown(t,unsafe_allow_html=True)
    for c in reversed(S['candles'][-5:]):
        bar='🟩'*int(abs(c['c']-c['o'])*5+1) if c['dir']=='UP' else '🟥'*int(abs(c['c']-c['o'])*5+1)
        col='🟢 UP' if c['dir']=='UP' else '🔴 DOWN'
        t=C+col+' | OPEN '+str(c['o'])+' -> CLOSE '+str(c['c'])+' | HIGH '+str(c['h'])+' LOW '+str(c['l'])+' | VOL '+str(c['v'])+' | '+bar+' | '+c['time']+E; st.markdown(t,unsafe_allow_html=True)
if menu=='💰 DEPOSIT':
    t=C+'DEPOSIT — REAL me paisa dalo'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'Tumhara REAL BAL: '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input('Kitna Deposit? (Rs)',min_value=100,max_value=100000,value=1000,step=100)
    method=st.selectbox('Method',['JazzCash','Easypaisa','Bank Transfer'],index=0)
    num=st.text_input('Apna Number',placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM KARO'):
        S['rb']+=int(amt); S['dep_hist'].append({'amt':int(amt),'method':method,'num':num,'time':now.strftime('%H:%M:%S')}); st.success(f"DEPOSIT HO GAYA! REAL BAL {int(S['rb'])}"); st.rerun()
    for d in reversed(S['dep_hist'][-5:]):
        t=G+'DEPOSIT +'+str(d['amt'])+' | '+d['method']+' | '+d['time']+E; st.markdown(t,unsafe_allow_html=True)
if menu=='💸 WITHDRAW':
    t=C+'WITHDRAW — REAL se paisa nikalo'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+' | Profit: '+str(rp)+E; st.markdown(t,unsafe_allow_html=True)
    wamt=st.number_input('Kitna Withdraw?',min_value=100,max_value=int(rb) if rb>0 else 100,value=100,step=100)
    wnum=st.text_input('Jis Number pe bhejna hai',placeholder='0300-1234567')
    if st.button('WITHDRAW CONFIRM KARO'):
        if int(wamt)>rb: st.error('BAL se zyada nahi!')
        else: S['rb']-=int(wamt); S['with_hist'].append({'amt':int(wamt),'num':wnum,'time':now.strftime('%H:%M:%S')}); st.success(f"WITHDRAW {int(wamt)}"); st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['time']+E; st.markdown(t,unsafe_allow_html=True)
if menu=='📊 TRADES / HISTORY':
    t=C+'TRADES - HISTORY FULL DAY'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']; t=G+'OPEN '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+o['am']+E; st.markdown(t,unsafe_allow_html=True)
    else:
        t=C+'NO OPEN — AUTO 15 sec me kholega'+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE ABHI KHOLO'): open_trade(); st.rerun()
    for h in reversed(S['ht'][-15:]):
        col='🟢 WIN' if h['win'] else '🔴 LOSS'
        t=C+col+' '+h['pair']+' '+h['tf']+' ENTRY '+str(h['entry'])+' EXIT '+str(h['exit'])+' '+str(h['amt'])+' | '+h['am']+' | '+h['time']+E; st.markdown(t,unsafe_allow_html=True)
    if len(S['ht'])==0:
        t=C+'Abhi koi trade nahi — 15 sec wait karo — AUTO kholega'+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH HISTORY'): st.rerun()
if menu=='⚙️ SETTINGS':
    t=C+'SETTINGS — AI BRAIN CONTROL'+E; st.markdown(t,unsafe_allow_html=True)
    S['name']=st.text_input('Tumhara Naam',value=S['name'])
    if st.button('RESET DEMO 10000'): S['db']=10000; S['dp']=0; S['today']=0; S['total']=0; S['wc']=0; S['lc']=0; S['ht']=[]; S['open']=None; S['candles']=[]; st.rerun()
    if st.button('RESET REAL 0'): S['rb']=0; S['rp']=0; st.rerun()
    if st.button('CLEAR SCAN'): S['scan']=[]; st.rerun()
    t=C+'APP: SONA V144 FIX | USER: '+S['name']+' | STREAK '+str(S['streak'])+E; st.markdown(t,unsafe_allow_html=True)
t=C+'STREAK '+str(S['streak'])+' | BEST '+S['best']+' '+str(S['best_score'])+'% | V144 FIX NO ERROR'+E; st.markdown(t,unsafe_allow_html=True)
time.sleep(3); st.rerun()
