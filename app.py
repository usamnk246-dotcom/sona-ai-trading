import streamlit as st
import random, time
from datetime import datetime
import pytz
st.set_page_config(page_title='SONA V149', layout='centered')
C='<div style="background:#111;padding:12px;border-radius:12px;color:#fff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
G='<div style="background:#0f3d1e;padding:10px;border-radius:10px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
R='<div style="background:#3d0f0f;padding:10px;border-radius:10px;color:#ff5555;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
Y='<div style="background:#3d3d0f;padding:10px;border-radius:10px;color:#ffff00;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
B='<div style="background:#0f1e3d;padding:10px;border-radius:10px;color:#5aafff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
E='</div>'
BASE={'SOL/USD':179.50,'BTC/USD':67200,'BNB/USD':710,'EUR/USD':1.085,'AUD/CHF OTC':0.585,'GBP/USD':1.275,'USD/JPY':152.30,'XAU/USD':2650,'EUR/GBP OTC':0.850,'USD/CHF OTC':0.885,'GBP/JPY':194.20,'AUD/USD':0.655}
if 'S' not in st.session_state:
    st.session_state.S={'am':'DEMO','auto':True,'db':10000,'rb':0,'dp':0,'rp':0,'open':None,'ht':[],'wc':0,'lc':0,'today':0,'total':0,'streak':0,'pair':'SOL/USD','tf':'1MIN','lp':179.50,'ai':'UP','ac':89,'price_hist':[179.50]*30,'dep_hist':[],'with_hist':[],'last':time.time(),'last_trade_time':0,'last_scan_time':0,'name':'Usam','scan':[],'best':'SOL/USD','best_score':0,'best_dir':'UP','candles':[],'quality':'GOOD','auto_scan':True,'hour_trades':[],'hour_start':datetime.now(pytz.timezone('Asia/Karachi')).replace(minute=0,second=0,microsecond=0),'min_conf':90,'min_gap_sec':60,'last_win_time':0,'sound_on':True,'last_sound_id':''}
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
PAIRS=list(BASE.keys())
TFS=['1MIN','2MIN','5MIN','15MIN']
def step_for(base):
    return max(base*0.001,0.0005)
def calc_rsi(prices,period=14):
    if len(prices)<period+1:
        return 50.0
    gains=[]
    losses=[]
    for i in range(1,period+1):
        d=prices[-i]-prices[-i-1]
        if d>0:
            gains.append(d)
        else:
            losses.append(abs(d))
    ag=sum(gains)/period if gains else 0.0001
    al=sum(losses)/period if losses else 0.0001
    if al==0:
        return 95.0
    return round(100-(100/(1+ag/al)),1)
def calc_ema(prices,period):
    if len(prices)<period:
        return prices[-1] if prices else 0
    k=2/(period+1)
    ema=prices[-period]
    for p in prices[-period:]:
        ema=p*k+ema*(1-k)
    return round(ema,4)
def calc_macd(prices):
    e12=calc_ema(prices,12)
    e26=calc_ema(prices,26)
    macd=round(e12-e26,4)
    sig=round(calc_ema(prices,9),4)
    return macd,sig,round(macd-(sig-e26),4)
def calc_atr(candles):
    if len(candles)<2:
        return round(step_for(S['lp'])*2,4)
    trs=[]
    for i,c in enumerate(candles):
        if i>0:
            trs.append(max(c['h']-c['l'],abs(c['h']-candles[i-1]['c']),abs(c['l']-candles[i-1]['c'])))
    return round(sum(trs[-14:])/min(14,len(trs)),4) if trs else round(step_for(S['lp'])*2,4)
def calc_vwap(candles):
    if not candles:
        return S['lp']
    tp=sum(c['c']*c['v'] for c in candles)
    tv=sum(c['v'] for c in candles)
    return round(tp/tv,4) if tv else S['lp']
def calc_bos(prices):
    if len(prices)<10:
        return 'NO BOS'
    if prices[-1]>max(prices[-10:-1]):
        return 'BOS UP'
    if prices[-1]<min(prices[-10:-1]):
        return 'BOS DOWN'
    return 'NO BOS'
def calc_sweep(prices):
    if len(prices)<10:
        return 'NO SWEEP'
    low=min(prices[-10:])
    high=max(prices[-10:])
    if prices[-2]<low and prices[-1]>low:
        return 'SWEEP LOW + UP'
    if prices[-2]>high and prices[-1]<high:
        return 'SWEEP HIGH + DOWN'
    return 'NO SWEEP'
def calc_pullback(prices):
    if len(prices)<15:
        return 'NO PULLBACK'
    ema20=calc_ema(prices,20)
    if abs(prices[-1]-ema20)<step_for(S['lp'])*2:
        return 'PULLBACK TO EMA20'
    return 'NO PULLBACK'
def calc_liquidity(prices):
    hi=max(prices[-20:]) if len(prices)>=20 else max(prices)
    lo=min(prices[-20:]) if len(prices)>=20 else min(prices)
    return round(hi,4),round(lo,4)
def calc_trend(prices):
    return 'UP' if prices[-1]>calc_ema(prices,20) else 'DOWN'
def calc_quality(score):
    if score>=90:
        return 'EXCELLENT 90+'
    if score>=80:
        return 'HIGH 80+'
    if score>=70:
        return 'GOOD'
    return 'LOW'
def set_pair(new_pair):
    if S['pair']!=new_pair:
        S['pair']=new_pair
        base=BASE[new_pair]
        S['lp']=base
        S['price_hist']=[base]*30
        S['candles']=[]
def make_candle():
    base=BASE[S['pair']]
    stp=step_for(base)
    if abs(S['lp']-base)>base*0.05:
        S['lp']=base
    o=S['lp']
    c=round(o+random.uniform(-stp*2,stp*2),4)
    h=round(max(o,c)+random.uniform(0,stp),4)
    l=round(min(o,c)-random.uniform(0,stp),4)
    v=random.randint(800,8500)
    S['lp']=c
    S['price_hist'].append(c)
    if len(S['price_hist'])>60:
        S['price_hist']=S['price_hist'][-60:]
    S['candles'].append({'o':o,'c':c,'h':h,'l':l,'v':v,'time':datetime.now(pkt).strftime('%H:%M:%S'),'dir':'UP' if c>=o else 'DOWN'})
    if len(S['candles'])>24:
        S['candles']=S['candles'][-24:]
    return S['candles'][-1]
def ai_scan_all():
    res=[]
    for pair in PAIRS:
        base=BASE[pair]
        stp=step_for(base)
        prices=[base]
        for i in range(59):
            prices.append(round(prices[-1]+random.uniform(-stp*2,stp*2),4))
        vols=[random.randint(800,8500) for _ in range(60)]
        rsi=calc_rsi(prices)
        macd,sig,hist=calc_macd(prices)
        atr=round(sum([abs(prices[i]-prices[i-1]) for i in range(1,len(prices))])/60,4)
        vwap=round(sum(p*v for p,v in zip(prices,vols))/sum(vols),4)
        vol=random.randint(800,8500)
        bos=calc_bos(prices)
        sweep=calc_sweep(prices)
        pull=calc_pullback(prices)
        hi,lo=calc_liquidity(prices)
        trend=calc_trend(prices)
        score=50
        if rsi<30:
            score+=18
        if rsi>70:
            score+=18
        if macd>0:
            score+=10
        if 'BOS' in bos:
            score+=12
        if 'SWEEP' in sweep:
            score+=15
        if 'PULLBACK' in pull:
            score+=12
        if vol>4000:
            score+=10
        score=min(99,max(55,score))
        direction='UP' if prices[-1]>vwap or macd>0 else 'DOWN'
        if rsi<30:
            direction='UP'
        if rsi>70:
            direction='DOWN'
        if 'BOS UP' in bos:
            direction='UP'
        if 'BOS DOWN' in bos:
            direction='DOWN'
        if 'SWEEP LOW' in sweep:
            direction='UP'
        if 'SWEEP HIGH' in sweep:
            direction='DOWN'
        res.append({'pair':pair,'price':prices[-1],'rsi':rsi,'macd':macd,'atr':atr,'vwap':vwap,'vol':vol,'bos':bos,'sweep':sweep,'pull':pull,'hi':hi,'lo':lo,'trend':trend,'score':score,'dir':direction,'quality':calc_quality(score)})
    return sorted(res,key=lambda x: x['score'],reverse=True)
def hour_count():
    cur=now.replace(minute=0,second=0,microsecond=0)
    if S['hour_start']!=cur:
        S['hour_start']=cur
        S['hour_trades']=[]
    return len(S['hour_trades'])
def rest_left():
    if S['last_win_time']==0:
        return 0
    left=300-(time.time()-S['last_win_time'])
    return int(left) if left>0 else 0
def can_trade_by_conf():
    if time.time()-S['last_trade_time']<S['min_gap_sec']:
        return False
    if rest_left()>0:
        return False
    if S['scan']:
        if S['scan'][0]['score']<S['min_conf']:
            return False
        return True
    return False
def open_trade(pair=None,dir=None,manual=False):
    if S['open'] is not None:
        return False
    if not manual and not can_trade_by_conf():
        return False
    bal=S['rb'] if S['am']=='REAL' else S['db']
    if bal<=0:
        return False
    S['open']={'pair':pair or S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':dir or S['ai'],'am':S['am'],'time':datetime.now(pkt)}
    S['last_trade_time']=time.time()
    if not manual:
        S['hour_trades'].append(now)
    return True
def close_trade():
    if S['open'] is None:
        return
    o=S['open']
    win=random.choice([True,True,False])
    amt=238 if win else -100
    if o['am']=='REAL':
        S['rb']+=amt
        S['rp']+=amt
    else:
        S['db']+=amt
        S['dp']+=amt
    if win:
        S['wc']+=1
        S['streak']+=1
        S['last_win_time']=time.time()
    else:
        S['lc']+=1
        S['streak']=0
    S['total']+=1
    S['today']+=1
    new_id=o['pair']+str(o['entry'])+str(time.time())
    S['ht'].append({'pair':o['pair'],'tf':o['tf'],'entry':o['entry'],'exit':S['lp'],'amt':amt,'win':win,'am':o['am'],'time':datetime.now(pkt).strftime('%H:%M:%S'),'id':new_id})
    S['open']=None
    S['last_sound_id']=new_id if win else ''
if time.time()-S['last']>3:
    S['last']=time.time()
    make_candle()
    if S['auto_scan'] and time.time()-S['last_scan_time']>10:
        S['last_scan_time']=time.time()
        S['scan']=ai_scan_all()
        best=S['scan'][0]
        S['best']=best['pair']
        S['best_score']=best['score']
        S['best_dir']=best['dir']
        S['quality']=best['quality']
        if S['open'] is None:
            set_pair(best['pair'])
            S['ai']=best['dir']
            S['ac']=best['score']
    if S['open'] is not None:
        if (datetime.now(pkt)-S['open']['time']).total_seconds()>=60:
            close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if can_trade_by_conf():
            open_trade()
S['sound_on']=st.toggle('WIN SOUND ON',value=S['sound_on'])
if S['sound_on'] and S['ht'] and S['ht'][-1]['win']:
    if S['last_sound_id']==S['ht'][-1].get('id',''):
        st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>',unsafe_allow_html=True)
        t=G+'WIN SOUND - TRADE WIN +238 - CHECK KARO!'+E
        st.markdown(t,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
    S['auto']=st.toggle('AUTO TRADING ON',value=S['auto'])
with c2:
    acc=st.radio('ACCOUNT',['DEMO','REAL'],horizontal=True)
    S['am']='REAL' if 'REAL' in acc else 'DEMO'
am=S['am']
db=int(S['db'])
rb=int(S['rb'])
dp=int(S['dp'])
rp=int(S['rp'])
cb=rb if am=='REAL' else db
cp=rp if am=='REAL' else dp
t=C+'SONA V149 | DEMO '+str(db)+' | REAL '+str(rb)+E
st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | PROFIT '+str(cp)+E
st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+now.strftime('%H:%M:%S PKT')+E
st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=G+'DEMO MODE - Practice - REAL paisa safe'+E
    st.markdown(t,unsafe_allow_html=True)
if am=='REAL' and rb==0:
    t=R+'REAL 0 - Pehle DEPOSIT karo'+E
    st.markdown(t,unsafe_allow_html=True)
hc=hour_count()
if rest_left()>0:
    t=Y+'WIN REST - '+str(rest_left())+' sec baaki - More trader se bachne ke liye'+E
    st.markdown(t,unsafe_allow_html=True)
else:
    if S['scan'] and S['scan'][0]['score']>=90:
        t=G+'90+ CONFIDENCE - '+str(S['scan'][0]['score'])+'% - TRADE KHULEGA'+E
        st.markdown(t,unsafe_allow_html=True)
    else:
        t=Y+'WAIT - 90+ ka wait - Hour '+str(hc)+' trade'+E
        st.markdown(t,unsafe_allow_html=True)
if S['scan']:
    best=S['scan'][0]
    t=B+'AI BRAIN - BEST = '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | HOUR '+str(hc)+E
    st.markdown(t,unsafe_allow_html=True)
S['auto_scan']=st.toggle('AI BRAIN AUTO SCAN ON',value=S['auto_scan'])
S['min_conf']=st.selectbox('MIN CONFIDENCE',[80,85,90,95],index=2)
S['min_gap_sec']=st.selectbox('MIN GAP SEC',[30,60,120,300],index=1)
t=C+'RULE: WIN ke baad 5 MIN REST - Sirf '+str(S['min_conf'])+'%+ - DATA ON = Trading ON'+E
st.markdown(t,unsafe_allow_html=True)
if st.button('TEST SOUND - Awaz check karo'):
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>',unsafe_allow_html=True)
    st.success('Awaz aayi ka? Volume ON karo - Silent OFF karo!')
menu=st.selectbox('MENU',['AI BRAIN AUTO SCAN','HOME - CANDLE','TERMINAL - CANDLE','DEPOSIT','WITHDRAW','TRADES - HISTORY','SETTINGS'],index=1)
if S['candles']:
    lc=S['candles'][-1]
    move='UP' if lc['dir']=='UP' else 'DOWN'
    t=C+'LAST CANDLE: '+move+' | OPEN '+str(lc['o'])+' | CLOSE '+str(lc['c'])+' | HIGH '+str(lc['h'])+' | LOW '+str(lc['l'])+' | VOL '+str(lc['v'])+' | '+lc['time']+E
    st.markdown(t,unsafe_allow_html=True)
if menu=='AI BRAIN AUTO SCAN':
    t=B+'AI BRAIN - 90+ ONLY - WIN SOUND'+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('SCAN NOW'):
        S['scan']=ai_scan_all()
        st.rerun()
    if S['scan']:
        best=S['scan'][0]
        t=G+'BEST = '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | '+best['quality']+E
        st.markdown(t,unsafe_allow_html=True)
        t=Y+'STRATEGY: '+best['bos']+' + '+best['sweep']+' + '+best['pull']+' + Trend '+best['trend']+E
        st.markdown(t,unsafe_allow_html=True)
        for s in S['scan']:
            col=G if s['score']>=90 else Y if s['score']>=80 else C
            t=col+s['pair']+' '+str(s['price'])+' | '+s['dir']+' '+str(s['score'])+'% | RSI '+str(s['rsi'])+' | MACD '+str(s['macd'])+' | ATR '+str(s['atr'])+' | VWAP '+str(s['vwap'])+' | VOL '+str(s['vol'])+' | '+s['bos']+' | '+s['sweep']+E
            st.markdown(t,unsafe_allow_html=True)
if menu in ['HOME - CANDLE','TERMINAL - CANDLE']:
    if menu=='TERMINAL - CANDLE':
        t=C+'TERMINAL - CANDLE + INDICATORS'+E
        st.markdown(t,unsafe_allow_html=True)
        old=S['pair']
        new_pair=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']))
        S['tf']=st.selectbox('TF - TIME',TFS,index=TFS.index(S['tf']))
        if new_pair!=old:
            set_pair(new_pair)
    else:
        t=C+'HOME - TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+' | HOUR '+str(hc)+E
        st.markdown(t,unsafe_allow_html=True)
    st.line_chart(S['price_hist'])
    pr=S['price_hist']
    rsi=calc_rsi(pr)
    macd,sig,hist=calc_macd(pr)
    atr=calc_atr(S['candles'])
    vwap=calc_vwap(S['candles'])
    bos=calc_bos(pr)
    sweep=calc_sweep(pr)
    pull=calc_pullback(pr)
    hi,lo=calc_liquidity(pr)
    vol=S['candles'][-1]['v'] if S['candles'] else 0
    t=C+'RSI '+str(rsi)+' | Volume '+str(vol)+' | ATR '+str(atr)+' | VWAP '+str(vwap)+' | MACD '+str(macd)+' | Sig '+str(sig)+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'Hi '+str(hi)+' Lo '+str(lo)+' | '+bos+' | '+sweep+' | '+pull+' | Trend '+calc_trend(pr)+E
    st.markdown(t,unsafe_allow_html=True)
    t=Y+'AI DECISION: '+S['pair']+' '+S['ai']+' '+str(S['ac'])+'% - RSI '+str(rsi)+' + MACD '+str(macd)+' + VWAP '+str(vwap)+' + '+bos+' + '+sweep+' = '+S['ai']+E
    st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']
        left=max(0,60-int((datetime.now(pkt)-o['time']).total_seconds()))
        t=G+'OPEN TRADE LIVE: '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | '+o['am']+' | Now '+str(S['lp'])+E
        st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'):
            close_trade()
            st.rerun()
    else:
        if rest_left()>0:
            t=Y+'WIN REST - '+str(rest_left())+' sec baaki - Phir trade'+E
            st.markdown(t,unsafe_allow_html=True)
        elif can_trade_by_conf():
            t=G+'90+ READY - Trade abhi khulega'+E
            st.markdown(t,unsafe_allow_html=True)
        else:
            t=C+'WAIT - 90+ ka wait'+E
            st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE ABHI KHOLO - MANUAL'):
            open_trade(manual=True)
            st.rerun()
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL UP CALL'):
            S['ai']='UP'
            open_trade(manual=True)
            st.rerun()
    with b2:
        if st.button('MANUAL DOWN PUT'):
            S['ai']='DOWN'
            open_trade(manual=True)
            st.rerun()
    t=C+'LAST 5 CANDLES - OPEN - CLOSE - HIGH - LOW'+E
    st.markdown(t,unsafe_allow_html=True)
    for c in reversed(S['candles'][-5:]):
        bar='UP' if c['dir']=='UP' else 'DOWN'
        col='UP' if c['dir']=='UP' else 'DOWN'
        t=C+col+' | OPEN '+str(c['o'])+' -> CLOSE '+str(c['c'])+' | HIGH '+str(c['h'])+' LOW '+str(c['l'])+' | VOL '+str(c['v'])+' | '+bar+' | '+c['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='DEPOSIT':
    t=C+'DEPOSIT - REAL me paisa dalo'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+E
    st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input('Kitna Deposit? (Rs)',min_value=100,max_value=100000,value=1000,step=100)
    method=st.selectbox('Method',['JazzCash','Easypaisa','Bank Transfer'],index=0)
    num=st.text_input('Apna Number',placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM KARO'):
        S['rb']+=int(amt)
        S['dep_hist'].append({'amt':int(amt),'method':method,'num':num,'time':now.strftime('%H:%M:%S')})
        st.success('DEPOSIT HO GAYA!')
        st.rerun()
    for d in reversed(S['dep_hist'][-5:]):
        t=G+'DEPOSIT +'+str(d['amt'])+' | '+d['method']+' | '+d['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='WITHDRAW':
    t=C+'WITHDRAW - REAL se paisa nikalo'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+' | Profit: '+str(rp)+E
    st.markdown(t,unsafe_allow_html=True)
    wamt=st.number_input('Kitna Withdraw?',min_value=100,max_value=int(rb) if rb>0 else 100,value=100,step=100)
    wnum=st.text_input('Jis Number pe bhejna hai',placeholder='0300-1234567')
    if st.button('WITHDRAW CONFIRM KARO'):
        if int(wamt)>rb:
            st.error('BAL se zyada nahi!')
        else:
            S['rb']-=int(wamt)
            S['with_hist'].append({'amt':int(wamt),'num':wnum,'time':now.strftime('%H:%M:%S')})
            st.success('WITHDRAW HO GAYA!')
            st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='TRADES - HISTORY':
    t=C+'TRADES - HISTORY FULL DAY'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+' | HOUR '+str(hc)+E
    st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']
        t=G+'OPEN '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+o['am']+E
        st.markdown(t,unsafe_allow_html=True)
    for h in reversed(S['ht'][-15:]):
        col='WIN' if h['win'] else 'LOSS'
        t=C+col+' '+h['pair']+' '+h['tf']+' ENTRY '+str(h['entry'])+' EXIT '+str(h['exit'])+' '+str(h['amt'])+' | '+h['am']+' | '+h['time']+E
        st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH HISTORY'):
        st.rerun()
if menu=='SETTINGS':
    t=C+'SETTINGS - WIN SOUND + DATA ONLY'+E
    st.markdown(t,unsafe_allow_html=True)
    S['name']=st.text_input('Tumhara Naam',value=S['name'])
    t=C+'DATA ONLY: Chrome khula rakho - DATA ON rakho'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'SOUND: Volume ON rakho - Silent OFF rakho'+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('RESET DEMO 10000'):
        S['db']=10000
        S['dp']=0
        S['today']=0
        S['total']=0
        S['wc']=0
        S['lc']=0
        S['ht']=[]
        S['open']=None
        S['candles']=[]
        S['hour_trades']=[]
        S['last_win_time']=0
        st.rerun()
    if st.button('RESET HOUR'):
        S['hour_trades']=[]
        st.rerun()
    t=C+'AP
