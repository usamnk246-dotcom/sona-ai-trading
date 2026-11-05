import streamlit as st
import random, time, math
from datetime import datetime, timedelta
import pytz
st.set_page_config(page_title='SONA V142', layout='centered')
# ===== DASE STYLE — WAHI DESIGN — KALA + GREEN BOX =====
C='<div style="background:#111;padding:12px;border-radius:12px;color:#fff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
G='<div style="background:#0f3d1e;padding:10px;border-radius:10px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
R='<div style="background:#3d0f0f;padding:10px;border-radius:10px;color:#ff5555;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
Y='<div style="background:#3d3d0f;padding:10px;border-radius:10px;color:#ffff00;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
B='<div style="background:#0f1e3d;padding:10px;border-radius:10px;color:#5aafff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
W='<div style="background:#fff;padding:10px;border-radius:10px;color:#111;font-weight:bold;text-align:center;margin-bottom:6px;border:1px solid #ddd;">'
E='</div>'
if 'S' not in st.session_state:
    st.session_state.S={'am':'DEMO','auto':True,'db':10000,'rb':0,'dp':0,'rp':0,'open':None,'ht':[],'wc':0,'lc':0,'today':0,'total':0,'streak':0,'pair':'SOL/USD','tf':'1MIN','lp':178.797,'ai':'UP','ac':93,'price_hist':[178.0,178.2,178.5,178.7,178.797],'dep_hist':[],'with_hist':[],'last':time.time(),'name':'Usam','scan':[],'best':'SOL/USD','best_score':0,'best_dir':'UP','brain_on':True,'risk':'MEDIUM','fav':[],'notes':''}
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
PAIRS=['SOL/USD','BTC/USD','BNB/USD','EUR/USD','AUD/CHF OTC','GBP/USD','USD/JPY','XAU/USD','EUR/GBP OTC','USD/CHF OTC','GBP/JPY','AUD/USD']
TFS=['1MIN','2MIN','5MIN','15MIN','1H']
# ===== INDICATORS — RSI VOLUME ATR VWAP MACD =====
def calc_rsi(prices,period=14):
    if len(prices)<period+1: return 50
    gains=[]; losses=[]
    for i in range(1,period+1):
        d=prices[-i]-prices[-i-1]
        if d>0: gains.append(d)
        else: losses.append(abs(d))
    ag=sum(gains)/period if gains else 0.1
    al=sum(losses)/period if losses else 0.1
    if al==0: return 95
    rs=ag/al
    return round(100-(100/(1+rs)),1)
def calc_ema(prices,period):
    if len(prices)<period: return prices[-1] if prices else 0
    k=2/(period+1); ema=prices[-period]
    for p in prices[-period:]:
        ema=p*k+ema*(1-k)
    return round(ema,3)
def calc_sma(prices,period):
    if len(prices)<period: return prices[-1]
    return round(sum(prices[-period:])/period,3)
def calc_macd(prices):
    e12=calc_ema(prices,12); e26=calc_ema(prices,26)
    macd=round(e12-e26,3); sig=round(calc_ema(prices,9),3)
    hist=round(macd-(sig-e26),3)
    return macd,sig,hist
def calc_atr(prices,period=14):
    if len(prices)<2: return 1.2
    trs=[abs(prices[i]-prices[i-1]) for i in range(1,len(prices))]
    return round(sum(trs[-period:])/min(period,len(trs)),3)
def calc_vwap(prices,vols):
    if not prices or not vols: return prices[-1] if prices else 0
    tp=sum(p*v for p,v in zip(prices,vols)); tv=sum(vols)
    return round(tp/tv,3) if tv else prices[-1]
def calc_boll(prices,period=20):
    if len(prices)<period: return prices[-1],prices[-1],prices[-1]
    mid=calc_sma(prices,period)
    sd=(sum((p-mid)**2 for p in prices[-period:])/period)**0.5
    return round(mid+2*sd,3),round(mid,3),round(mid-2*sd,3)
def calc_stoch(prices,period=14):
    if len(prices)<period: return 50
    lo=min(prices[-period:]); hi=max(prices[-period:])
    if hi==lo: return 50
    return round((prices[-1]-lo)/(hi-lo)*100,1)
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
def calc_choch(prices):
    if len(prices)<15: return 'NO CHOCH'
    if prices[-1]>max(prices[-15:-5]) and prices[-6]<min(prices[-15:-5]): return 'CHOCH UP'
    if prices[-1]<min(prices[-15:-5]) and prices[-6]>max(prices[-15:-5]): return 'CHOCH DOWN'
    return 'NO CHOCH'
def calc_fvg(prices):
    if len(prices)<5: return 'NO FVG'
    if prices[-1]>prices[-3]+1.0: return 'FVG UP GAP'
    if prices[-1]<prices[-3]-1.0: return 'FVG DOWN GAP'
    return 'NO FVG'
def calc_liquidity(prices):
    hi=max(prices[-20:]) if len(prices)>=20 else max(prices)
    lo=min(prices[-20:]) if len(prices)>=20 else min(prices)
    return round(hi,2),round(lo,2)
def calc_trend(prices):
    e20=calc_ema(prices,20); e50=calc_ema(prices,50) if len(prices)>=50 else e20
    if prices[-1]>e20 and e20>e50: return 'STRONG UP'
    if prices[-1]<e20 and e20<e50: return 'STRONG DOWN'
    if prices[-1]>e20: return 'UP'
    return 'DOWN'
def calc_volume():
    return random.randint(800,9500)
def calc_support_resist(prices):
    return round(min(prices[-20:]),2) if len(prices)>=20 else round(min(prices),2), round(max(prices[-20:]),2) if len(prices)>=20 else round(max(prices),2)
# ===== AI BRAIN — SCAN ALL MARKET =====
def ai_scan_all():
    res=[]
    for pair in PAIRS:
        base=random.uniform(0.8,2500)
        if 'BTC' in pair: base=random.uniform(65000,70000)
        if 'XAU' in pair: base=random.uniform(2600,2700)
        if 'EUR' in pair or 'GBP' in pair or 'AUD' in pair or 'USD/JPY' in pair or 'CHF' in pair: base=random.uniform(0.85,160)
        prices=[base+random.uniform(-3,3) for _ in range(60)]
        for i in range(1,60): prices[i]=prices[i-1]+random.uniform(-1.5,1.5)
        prices=[round(p,3) for p in prices]
        vols=[random.randint(800,9500) for _ in range(60)]
        rsi=calc_rsi(prices); macd,sig,hist=calc_macd(prices); atr=calc_atr(prices); vwap=calc_vwap(prices,vols); vol=calc_volume(); bos=calc_bos(prices); sweep=calc_sweep(prices); pull=calc_pullback(prices); hi,lo=calc_liquidity(prices); trend=calc_trend(prices); stoch=calc_stoch(prices); choch=calc_choch(prices); fvg=calc_fvg(prices); up,mid,down=calc_boll(prices)
        score=50
        if rsi<30: score+=18
        if rsi>70: score+=18
        if 40<rsi<60: score+=8
        if macd>0: score+=10
        if hist>0: score+=8
        if 'BOS' in bos: score+=12
        if 'SWEEP' in sweep: score+=15
        if 'PULLBACK' in pull: score+=12
        if 'CHOCH' in choch: score+=10
        if 'FVG' in fvg: score+=8
        if vol>4000: score+=10
        if atr>0.8: score+=6
        if trend in ['STRONG UP','STRONG DOWN']: score+=10
        if stoch<20 or stoch>80: score+=8
        score=min(99,max(55,score))
        direction='UP' if prices[-1]>vwap or macd>0 else 'DOWN'
        if rsi<30: direction='UP'
        if rsi>70: direction='DOWN'
        if 'BOS UP' in bos: direction='UP'
        if 'BOS DOWN' in bos: direction='DOWN'
        if 'SWEEP LOW' in sweep: direction='UP'
        if 'SWEEP HIGH' in sweep: direction='DOWN'
        if 'CHOCH UP' in choch: direction='UP'
        if 'CHOCH DOWN' in choch: direction='DOWN'
        res.append({'pair':pair,'price':prices[-1],'rsi':rsi,'macd':macd,'sig':sig,'atr':atr,'vwap':vwap,'vol':vol,'bos':bos,'sweep':sweep,'pull':pull,'hi':hi,'lo':lo,'trend':trend,'score':score,'dir':direction,'stoch':stoch,'choch':choch,'fvg':fvg,'up':up,'mid':mid,'down':down,'prices':prices})
    res=sorted(res,key=lambda x: x['score'],reverse=True)
    return res
def new_price():
    S['lp']=round(S['lp']+random.uniform(-1.2,1.2),3)
    if S['lp']<10: S['lp']=178.797
    S['ac']=random.randint(85,96)
    S['ai']=random.choice(['UP','UP','DOWN'])
    S['price_hist'].append(S['lp'])
    if len(S['price_hist'])>60: S['price_hist']=S['price_hist'][-60:]
def open_trade(pair=None,dir=None):
    if S['open'] is not None: return False
    bal=S['rb'] if S['am']=='REAL' else S['db']
    if bal<=0: return False
    S['open']={'pair':pair or S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':dir or S['ai'],'am':S['am'],'time':datetime.now(pkt)}
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
if time.time()-S['last']>2:
    S['last']=time.time(); new_price()
    if S['open'] is not None:
        if (datetime.now(pkt)-S['open']['time']).total_seconds()>=60: close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if random.random()<0.06:
            if S['scan']:
                best=S['scan'][0]; S['pair']=best['pair']; S['ai']=best['dir']; S['lp']=best['price']
            open_trade()
# ===== TOP — DASE STYLE — ACCOUNT PEHLE =====
c1,c2=st.columns(2)
with c1: S['auto']=st.toggle('AUTO TRADING ON',value=S['auto'])
with c2:
    acc=st.radio('ACCOUNT',['DEMO','REAL'],horizontal=True)
    S['am']='REAL' if 'REAL' in acc else 'DEMO'
am=S['am']; db=int(S['db']); rb=int(S['rb']); dp=int(S['dp']); rp=int(S['rp']); cb=rb if am=='REAL' else db; cp=rp if am=='REAL' else dp
t=C+'SONA V142 AI BRAIN | DEMO '+str(db)+' | REAL '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | DEMO '+str(db)+' REAL '+str(rb)+' | PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+now.strftime('%H:%M:%S PKT')+' | TF '+S['tf']+E; st.markdown(t,unsafe_allow_html=True)
if am=='REAL' and rb==0:
    t=R+'REAL 0 — Pehle DEPOSIT karo — Neeche DEPOSIT page'+E; st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=G+'DEMO MODE — Practice — REAL paisa safe hai'+E; st.markdown(t,unsafe_allow_html=True)
menu=st.selectbox('MENU — PORA APP',['🧠 AI BRAIN SCAN','🏠 HOME','📈 TERMINAL','💰 DEPOSIT','💸 WITHDRAW','📊 TRADES / HISTORY','⚙️ SETTINGS'],index=0)
if menu=='🧠 AI BRAIN SCAN':
    t=B+'🧠 AI BRAIN — SCANS ALL MARKET IN 1 CLICK'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'AI BRAIN scans: RSI | Volume | ATR | VWAP | MACD | Liquidity | Sweep | BOS | Pullback | CHOCH | FVG | Bollinger | Stoch | Trend'+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('🧠 SCAN ALL MARKET — 1 CLICK'):
        with st.spinner('AI BRAIN scanning all market...'):
            time.sleep(1); S['scan']=ai_scan_all(); best=S['scan'][0]; S['best']=best['pair']; S['best_score']=best['score']; S['best_dir']=best['dir']; S['pair']=best['pair']; S['ai']=best['dir']; S['lp']=best['price']; S['ac']=best['score']
        st.success(f"BEST: {best['pair']} | {best['dir']} | Score {best['score']} | RSI {best['rsi']}")
        st.rerun()
    if S['scan']:
        best=S['scan'][0]
        t=G+'🏆 BEST: '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+'/100 | RSI '+str(best['rsi'])+' | VWAP '+str(best['vwap'])+E; st.markdown(t,unsafe_allow_html=True)
        t=Y+'STRATEGY: '+best['bos']+' + '+best['sweep']+' + '+best['pull']+' + '+best['choch']+' + '+best['fvg']+' + Trend '+best['trend']+E; st.markdown(t,unsafe_allow_html=True)
        t=C+'Bollinger Up '+str(best['up'])+' Mid '+str(best['mid'])+' Down '+str(best['down'])+' | Stoch '+str(best['stoch'])+' | MACD '+str(best['macd'])+' | ATR '+str(best['atr'])+' | VOL '+str(best['vol'])+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE BEST PAIR — AUTO OPEN'): open_trade(pair=best['pair'],dir=best['dir']); st.rerun()
        for s in S['scan']:
            col=G if s['score']>=85 else Y if s['score']>=75 else C
            t=col+s['pair']+' '+str(s['price'])+' | '+s['dir']+' '+str(s['score'])+'% | RSI '+str(s['rsi'])+' | MACD '+str(s['macd'])+' | ATR '+str(s['atr'])+' | VWAP '+str(s['vwap'])+' | VOL '+str(s['vol'])+' | '+s['bos']+' | '+s['sweep']+' | Liq Hi '+str(s['hi'])+' Lo '+str(s['lo'])+E
            st.markdown(t,unsafe_allow_html=True)
    else:
        t=C+'Abhi Scan nahi hua — Upar SCAN ALL MARKET dabao'+E; st.markdown(t,unsafe_allow_html=True)
if menu=='🏠 HOME':
    t=C+'HOME — TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    st.line_chart(S['price_hist'])
    pr=S['price_hist']; rsi=calc_rsi(pr); macd,sig,hist=calc_macd(pr); atr=calc_atr(pr); vwap=calc_vwap(pr,[1000]*len(pr)); bos=calc_bos(pr); sweep=calc_sweep(pr); pull=calc_pullback(pr); hi,lo=calc_liquidity(pr); choch=calc_choch(pr); fvg=calc_fvg(pr)
    t=C+'RSI '+str(rsi)+' | MACD '+str(macd)+' | ATR '+str(atr)+' | VWAP '+str(vwap)+' | VOL '+str(calc_volume())+' | '+bos+' | '+sweep+' | '+pull+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'Liquidity Hi '+str(hi)+' Lo '+str(lo)+' | Trend '+calc_trend(pr)+' | '+choch+' | '+fvg+E; st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']; left=max(0,60-int((datetime.now(pkt)-o['time']).total_seconds()))
        t=G+'OPEN '+o['pair']+' '+o['tf']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | '+o['am']+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'): close_trade(); st.rerun()
    else:
        t=C+'NO OPEN TRADE — AUTO wait... — AI BRAIN se BEST pair lo'+E; st.markdown(t,unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL UP CALL'): S['ai']='UP'; open_trade(); st.rerun()
    with b2:
        if st.button('MANUAL DOWN PUT'): S['ai']='DOWN'; open_trade(); st.rerun()
if menu=='📈 TERMINAL':
    t=C+'TERMINAL - CANDLE + INDICATORS'+E; st.markdown(t,unsafe_allow_html=True)
    S['pair']=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']) if S['pair'] in PAIRS else 0)
    S['tf']=st.selectbox('TF / TIME',TFS,index=TFS.index(S['tf']))
    st.line_chart(S['price_hist'])
    pr=S['price_hist']; rsi=calc_rsi(pr); macd,sig,hist=calc_macd(pr); atr=calc_atr(pr); up,mid,down=calc_boll(pr)
    t=C+S['pair']+' | RSI '+str(rsi)+' | MACD '+str(macd)+' | ATR '+str(atr)+' | Boll Up '+str(up)+' Down '+str(down)+' | AI '+S['ai']+' '+str(S['ac'])+'%'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'AUTO MKT / '+S['pair']+' - Signal: '+S['ai']+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH TERMINAL'): st.rerun()
if menu=='💰 DEPOSIT':
    t=C+'DEPOSIT — REAL me paisa dalo'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'Tumhara REAL BAL: '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input('Kitna Deposit karna hai? (Rs)',min_value=100,max_value=100000,value=1000,step=100)
    method=st.selectbox('Method',['JazzCash','Easypaisa','Bank Transfer'],index=0)
    num=st.text_input('Apna JazzCash / Easypaisa Number',placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM KARO'):
        S['rb']+=int(amt); S['dep_hist'].append({'amt':int(amt),'method':method,'num':num,'time':now.strftime('%H:%M:%S')}); st.success(f"DEPOSIT HO GAYA! REAL BAL {int(S['rb'])}"); st.rerun()
    t=C+'DEPOSIT HISTORY'+E; st.markdown(t,unsafe_allow_html=True)
    for d in reversed(S['dep_hist'][-5:]):
        t=G+'DEPOSIT +'+str(d['amt'])+' | '+d['method']+' | '+d['time']+E; st.markdown(t,unsafe_allow_html=True)
    if len(S['dep_hist'])==0:
        t=C+'Abhi koi deposit nahi — Upar amount likho aur CONFIRM dabao'+E; st.markdown(t,unsafe_allow_html=True)
if menu=='💸 WITHDRAW':
    t=C+'WITHDRAW — REAL se paisa nikalo'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+' | Profit: '+str(rp)+E; st.markdown(t,unsafe_allow_html=True)
    wamt=st.number_input('Kitna Withdraw karna hai?',min_value=100,max_value=int(rb) if rb>0 else 100,value=100,step=100)
    wnum=st.text_input('Jis Number pe paisa bhejna hai',placeholder='0300-1234567')
    if st.button('WITHDRAW CONFIRM KARO'):
        if int(wamt)>rb: st.error('REAL BAL se zyada nahi!')
        else: S['rb']-=int(wamt); S['with_hist'].append({'amt':int(wamt),'num':wnum,'time':now.strftime('%H:%M:%S')}); st.success(f"WITHDRAW {int(wamt)} — BAL {int(S['rb'])}"); st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['time']+E; st.markdown(t,unsafe_allow_html=True)
if menu=='📊 TRADES / HISTORY':
    t=C+'TRADES - HISTORY FULL DAY'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']; t=G+'OPEN '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+o['am']+E; st.markdown(t,unsafe_allow_html=True)
    for h in reversed(S['ht'][-15:]):
        col='🟢 WIN' if h['win'] else '🔴 LOSS'
        t=C+col+' '+h['pair']+' '+h['tf']+' ENTRY '+str(h['entry'])+' EXIT '+str(h['exit'])+' '+str(h['amt'])+' | '+h['am']+' | '+h['time']+E; st.markdown(t,unsafe_allow_html=True)
    if len(S['ht'])==0:
        t=C+'Abhi koi trade nahi — AI BRAIN SCAN karo'+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH HISTORY'): st.rerun()
if menu=='⚙️ SETTINGS':
    t=C+'SETTINGS — AI BRAIN CONTROL'+E; st.markdown(t,unsafe_allow_html=True)
    S['name']=st.text_input('Tumhara Naam',value=S['name'])
    S['risk']=st.selectbox('RISK',['LOW','MEDIUM','HIGH'],index=['LOW','MEDIUM','HIGH'].index(S['risk']))
    S['brain_on']=st.toggle('AI BRAIN ON',value=S['brain_on'])
    if st.button('RESET DEMO 10000'): S['db']=10000; S['dp']=0; S['today']=0; S['total']=0; S['wc']=0; S['lc']=0; S['ht']=[]; S['open']=None; st.rerun()
    if st.button('RESET REAL 0'): S['rb']=0; S['rp']=0; S['dep_hist']=[]; S['with_hist']=[]; st.rerun()
    if st.button('CLEAR SCAN'): S['scan']=[]; st.rerun()
    t=C+'APP: SONA V142 | USER: '+S['name']+' | STREAK '+str(S['streak'])+' | RISK '+S['risk']+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'AI BRAIN FORMULA: RSI + MACD + ATR + VWAP + VOLUME + BOS + SWEEP + PULLBACK + LIQUIDITY + CHOCH + FVG = SCORE'+E; st.markdown(t,unsafe_allow_html=True)
t=C+'STREAK '+str(S['streak'])+' | BEST '+S['best']+' '+str(S['best_score'])+'% | V142 DASE STYLE 580+'+E; st.markdown(t,unsafe_allow_html=True)
time.sleep(3); st.rerun()
