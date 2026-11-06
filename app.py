import streamlit as st
import random,time,json,os
from datetime import datetime
import pytz
st.set_page_config(
page_title='SONA V157',
layout='centered')
C='<div style="background:#111;'
C+='padding:12px;border-radius:12px;'
C+='color:#fff;font-weight:bold;'
C+='text-align:center;margin-bottom:6px;'
C+='font-size:15px;">'
G='<div style="background:#0f3d1e;'
G+='padding:10px;border-radius:10px;'
G+='color:#0f0;font-weight:bold;'
G+='text-align:center;margin-bottom:6px;'
G+='font-size:15px;">'
R='<div style="background:#3d0f0f;'
R+='padding:10px;border-radius:10px;'
R+='color:#ff5555;font-weight:bold;'
R+='text-align:center;margin-bottom:6px;'
R+='font-size:15px;">'
Y='<div style="background:#3d3d0f;'
Y+='padding:10px;border-radius:10px;'
Y+='color:#ffff00;font-weight:bold;'
Y+='text-align:center;margin-bottom:6px;'
Y+='font-size:15px;">'
B='<div style="background:#0f1e3d;'
B+='padding:10px;border-radius:10px;'
B+='color:#5aafff;font-weight:bold;'
B+='text-align:center;margin-bottom:6px;'
B+='font-size:15px;">'
E='</div>'
FILE='sona_data.json'
HF='sona_hist.json'
BASE={'SOL/USD':179.50,
'BTC/USD':67200,'BNB/USD':710,
'EUR/USD':1.085,
'AUD/CHF OTC':0.585,
'GBP/USD':1.275,
'USD/JPY':152.30,
'XAU/USD':2650,
'EUR/GBP OTC':0.850,
'USD/CHF OTC':0.885,
'GBP/JPY':194.20,
'AUD/USD':0.655}
def load_json(f):
    if os.path.exists(f):
        try:
            with open(f,'r') as x:
                return json.load(x)
        except:
            return None
    return None
def save_hist():
    try:
        with open(HF,'w') as x:
            json.dump(S['ht'],x)
    except:
        pass
def save_data():
    try:
        d={}
        d['db']=S['db']
        d['rb']=S['rb']
        d['dp']=S['dp']
        d['rp']=S['rp']
        d['wc']=S['wc']
        d['lc']=S['lc']
        d['today']=S['today']
        d['total']=S['total']
        d['streak']=S['streak']
        d['pair']=S['pair']
        d['tf']=S['tf']
        d['lp']=S['lp']
        d['ai']=S['ai']
        d['ac']=S['ac']
        d['open']=S['open']
        d['last_win_time']=S['last_win_time']
        d['last_trade_time']=S['last_trade_time']
        d['hour_start']=S['hour_start']
        d['hour_trades']=S['hour_trades']
        d['save_time']=time.time()
        d['name']=S['name']
        d['trade_amt']=S['trade_amt']
        d['target']=S['target']
        with open(FILE,'w') as x:
            json.dump(d,x)
    except:
        pass
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
if 'S' not in st.session_state:
    sv=load_json(FILE)
    ht=load_json(HF)
    if ht is None:
        ht=[]
    if sv is not None:
        st.session_state.S={
        'am':'DEMO','auto':True,
        'db':sv.get('db',10000),
        'rb':sv.get('rb',0),
        'dp':sv.get('dp',0),
        'rp':sv.get('rp',0),
        'open':sv.get('open',None),
        'ht':ht,
        'wc':sv.get('wc',0),
        'lc':sv.get('lc',0),
        'today':sv.get('today',0),
        'total':sv.get('total',0),
        'streak':sv.get('streak',0),
        'pair':sv.get('pair','SOL/USD'),
        'tf':sv.get('tf','1MIN'),
        'lp':sv.get('lp',179.50),
        'ai':sv.get('ai','UP'),
        'ac':sv.get('ac',89),
        'price_hist':[sv.get('lp',179.50)]*30,
        'dep_hist':[],'with_hist':[],
        'last':time.time(),
        'last_trade_time':sv.get(
        'last_trade_time',0),
        'last_scan_time':0,
        'name':sv.get('name','Usam'),
        'scan':[],'best':'SOL/USD',
        'best_score':0,'best_dir':'UP',
        'candles':[],'quality':'GOOD',
        'auto_scan':True,
        'hour_trades':sv.get(
        'hour_trades',[]),
        'hour_start':sv.get(
        'hour_start',time.time()),
        'min_conf':90,'min_gap_sec':60,
        'last_win_time':sv.get(
        'last_win_time',0),
        'sound_on':True,
        'last_sound_id':'',
        'trade_amt':sv.get(
        'trade_amt',250),
        'target':sv.get('target',15000),
        'bal_hist':[sv.get('db',10000)],
        'loss_streak':0}
    else:
        st.session_state.S={
        'am':'DEMO','auto':True,
        'db':10000,'rb':0,
        'dp':0,'rp':0,'open':None,
        'ht':ht,'wc':0,'lc':0,
        'today':0,'total':0,
        'streak':0,'pair':'SOL/USD',
        'tf':'1MIN','lp':179.50,
        'ai':'UP','ac':89,
        'price_hist':[179.50]*30,
        'dep_hist':[],'with_hist':[],
        'last':time.time(),
        'last_trade_time':0,
        'last_scan_time':0,
        'name':'Usam','scan':[],
        'best':'SOL/USD',
        'best_score':0,'best_dir':'UP',
        'candles':[],'quality':'GOOD',
        'auto_scan':True,
        'hour_trades':[],
        'hour_start':time.time(),
        'min_conf':90,'min_gap_sec':60,
        'last_win_time':0,
        'sound_on':True,
        'last_sound_id':'',
        'trade_amt':250,
        'target':15000,
        'bal_hist':[10000],
        'loss_streak':0}
S=st.session_state.S
if 'dep_hist' not in S:
    S['dep_hist']=[]
if 'with_hist' not in S:
    S['with_hist']=[]
if 'bal_hist' not in S:
    S['bal_hist']=[S['db']]
if 'loss_streak' not in S:
    S['loss_streak']=0
if S['trade_amt'] not in [250,500,1000,2000,4000,8000]:
    S['trade_amt']=250
if S['target'] not in [1000,5000,10000,15000]:
    S['target']=15000
if S['pair'] not in list(BASE.keys()):
    S['pair']='SOL/USD'
if S['tf'] not in ['1MIN','2MIN','5MIN','15MIN']:
    S['tf']='1MIN'
PAIRS=list(BASE.keys())
TFS=['1MIN','2MIN','5MIN','15MIN']
def step_for(b):
    return max(b*0.001,0.0005)
def calc_rsi(pr):
    if len(pr)<15:
        return 50.0
    g=[]
    l=[]
    for i in range(1,15):
        d=pr[-i]-pr[-i-1]
        if d>0:
            g.append(d)
        else:
            l.append(abs(d))
    ag=sum(g)/14 if g else 0.0001
    al=sum(l)/14 if l else 0.0001
    if al==0:
        return 95.0
    return round(100-(100/(1+ag/al)),1)
def calc_ema(pr,p):
    if len(pr)<p:
        return pr[-1] if pr else 0
    k=2/(p+1)
    e=pr[-p]
    for x in pr[-p:]:
        e=x*k+e*(1-k)
    return round(e,4)
def calc_macd(pr):
    m=calc_ema(pr,12)-calc_ema(pr,26)
    m=round(m,4)
    return m,round(m*0.9,4)
def calc_atr(cd):
    if len(cd)<2:
        return round(step_for(S['lp'])*2,4)
    tr=[]
    for i,c in enumerate(cd):
        if i>0:
            a=c['h']-c['l']
            b=abs(c['h']-cd[i-1]['c'])
            cc=abs(c['l']-cd[i-1]['c'])
            tr.append(max(a,b,cc))
    return round(sum(tr[-14:])/min(14,len(tr)),4)
def calc_vwap(cd):
    if not cd:
        return S['lp']
    tp=sum(c['c']*c['v'] for c in cd)
    tv=sum(c['v'] for c in cd)
    return round(tp/tv,4) if tv else S['lp']
def calc_bos(pr):
    if len(pr)<10:
        return 'NO BOS'
    if pr[-1]>max(pr[-10:-1]):
        return 'BOS UP'
    if pr[-1]<min(pr[-10:-1]):
        return 'BOS DOWN'
    return 'NO BOS'
def calc_sweep(pr):
    if len(pr)<10:
        return 'NO SWEEP'
    lo=min(pr[-10:])
    hi=max(pr[-10:])
    if pr[-2]<lo and pr[-1]>lo:
        return 'SWEEP LOW + UP'
    if pr[-2]>hi and pr[-1]<hi:
        return 'SWEEP HIGH + DOWN'
    return 'NO SWEEP'
def calc_trend(pr):
    if pr[-1]>calc_ema(pr,20):
        return 'UP'
    return 'DOWN'
def calc_q(sc):
    if sc>=90:
        return 'EXCELLENT 90+'
    if sc>=80:
        return 'HIGH 80+'
    return 'GOOD'
def set_pair(np):
    if S['pair']!=np:
        S['pair']=np
        b=BASE[np]
        S['lp']=b
        S['price_hist']=[b]*30
        S['candles']=[{'o':b,'c':b,
        'h':b,'l':b,'v':1000,
        'time':now.strftime('%H:%M:%S'),
        'dir':'UP'}]
def make_tick():
    b=BASE[S['pair']]
    stp=step_for(b)/3
    c=round(S['lp']+random.uniform(
    -stp,stp),4)
    S['lp']=c
    S['price_hist'].append(c)
    if len(S['price_hist'])>60:
        S['price_hist']=S['price_hist'][-60:]
    if not S['candles']:
        S['candles'].append({'o':c,
        'c':c,'h':c,'l':c,'v':1000,
        'time':now.strftime('%H:%M:%S'),
        'dir':'UP'})
    else:
        lc=S['candles'][-1]
        lc['c']=c
        if c>lc['h']:
            lc['h']=c
        if c<lc['l']:
            lc['l']=c
        if c>=lc['o']:
            lc['dir']='UP'
        else:
            lc['dir']='DOWN'
        lc['v']=lc['v']+random.randint(10,200)
    if len(S['price_hist'])%20==0:
        S['candles'].append({'o':c,
        'c':c,'h':c,'l':c,'v':1000,
        'time':now.strftime('%H:%M:%S'),
        'dir':'UP'})
    if len(S['candles'])>24:
        S['candles']=S['candles'][-24:]
def ai_scan_all():
    res=[]
    for pair in PAIRS:
        b=BASE[pair]
        stp=step_for(b)
        pr=[b]
        for i in range(59):
            pr.append(round(pr[-1]+
            random.uniform(-stp*2,stp*2),4))
        vs=[random.randint(800,8500)
        for _ in range(60)]
        rsi=calc_rsi(pr)
        macd,sig=calc_macd(pr)
        atr=round(sum([abs(pr[i]-
        pr[i-1]) for i in range(
        1,len(pr))])/60,4)
        vwap=round(sum(p*v for p,v
        in zip(pr,vs))/sum(vs),4)
        vol=random.randint(800,8500)
        bos=calc_bos(pr)
        sweep=calc_sweep(pr)
        trend=calc_trend(pr)
        sc=50
        if rsi<30:
            sc+=18
        if rsi>70:
            sc+=18
        if macd>0:
            sc+=10
        if 'BOS' in bos:
            sc+=12
        if 'SWEEP' in sweep:
            sc+=15
        if vol>4000:
            sc+=10
        sc=min(99,max(55,sc))
        dr='UP'
        if pr[-1]<vwap or macd<0:
            dr='DOWN'
        if rsi<30:
            dr='UP'
        if rsi>70:
            dr='DOWN'
        if 'BOS UP' in bos:
            dr='UP'
        if 'BOS DOWN' in bos:
            dr='DOWN'
        if 'SWEEP LOW' in sweep:
            dr='UP'
        if 'SWEEP HIGH' in sweep:
            dr='DOWN'
        res.append({'pair':pair,
        'price':pr[-1],'rsi':rsi,
        'macd':macd,'atr':atr,
        'vwap':vwap,'vol':vol,
        'bos':bos,'sweep':sweep,
        'trend':trend,'score':sc,
        'dir':dr,
        'quality':calc_q(sc)})
    res=sorted(res,
    key=lambda x: x['score'],
    reverse=True)
    return res
def hour_count():
    if time.time()-S['hour_start']>3600:
        S['hour_start']=time.time()
        S['hour_trades']=[]
    return len(S['hour_trades'])
def rest_left():
    if S['last_win_time']==0:
        return 0
    lf=300-(time.time()-
    S['last_win_time'])
    return int(lf) if lf>0 else 0
def win_rate():
    if S['total']==0:
        return 0
    return round(S['wc']/S['total']*100,1)
def can_trade():
    if S['dp']>=S['target']:
        return False
    if S['loss_streak']>=3:
        return False
    if time.time()-S['last_trade_time']<S['min_gap_sec']:
        return False
    if rest_left()>0:
        return False
    if S['scan']:
        if S['scan'][0]['score']<S['min_conf']:
            return False
        return True
    return False
def open_trade(manual=False):
    if S['open'] is not None:
        return False
    if not manual and not can_trade():
        return False
    bal=S['rb'] if S['am']=='REAL' else S['db']
    if bal<=0:
        return False
    dur=int(S['tf'].replace(
    'MIN',''))*60
    S['open']={'pair':S['pair'],
    'tf':S['tf'],'entry':S['lp'],
    'dir':S['ai'],'am':S['am'],
    't0':time.time(),'dur':dur,
    'amt':S['trade_amt']}
    S['last_trade_time']=time.time()
    if not manual:
        S['hour_trades'].append(time.time())
    save_data()
    return True
def do_close(o,exit_p):
    win=random.choice(
    [True,True,False])
    amt=o.get('amt',250) if win else -100
    if o['am']=='REAL':
        S['rb']+=amt
        S['rp']+=amt
    else:
        S['db']+=amt
        S['dp']+=amt
    if win:
        S['wc']+=1
        S['streak']+=1
        S['loss_streak']=0
        S['last_win_time']=time.time()
        if S['trade_amt']<8000:
            S['trade_amt']=S['trade_amt']*2
    else:
        S['lc']+=1
        S['streak']=0
        S['loss_streak']+=1
        S['trade_amt']=250
    S['total']+=1
    S['today']+=1
    S['bal_hist'].append(S['db'])
    if len(S['bal_hist'])>50:
        S['bal_hist']=S['bal_hist'][-50:]
    nid=o['pair']+str(o['entry'])+str(time.time())
    S['ht'].append({'pair':o['pair'],
    'tf':o['tf'],'entry':o['entry'],
    'exit':exit_p,'amt':amt,
    'win':win,'am':o['am'],
    'time':datetime.now(pkt).strftime(
    '%H:%M:%S'),'id':nid})
    S['open']=None
    S['last_sound_id']=nid if win else ''
    save_hist()
    save_data()
def close_trade():
    if S['open'] is None:
        return
    o=S['open']
    do_close(o,S['lp'])
sv2=load_json(FILE)
if sv2 is not None and 'save_time' in sv2:
    missed=time.time()-sv2['save_time']
    if missed>10 and S['auto']:
        if S['open'] is not None:
            o=S['open']
            el=time.time()-o.get(
            't0',time.time())
            if el>=o.get('dur',60):
                do_close(o,S['lp'])
        if missed>360:
            n=min(10,int(missed//360))
            for i in range(n):
                win=random.choice(
                [True,True,False])
                amt=S['trade_amt'] if win else -100
                S['db']+=amt
                S['dp']+=amt
                if win:
                    S['wc']+=1
                    S['streak']+=1
                    S['loss_streak']=0
                    if S['trade_amt']<8000:
                        S['trade_amt']=S['trade_amt']*2
                else:
                    S['lc']+=1
                    S['streak']=0
                    S['loss_streak']+=1
                    S['trade_amt']=250
                S['total']+=1
                S['today']+=1
                S['bal_hist'].append(S['db'])
                S['ht'].append({'pair':S['pair'],
                'tf':S['tf'],
                'entry':S['lp'],
                'exit':S['lp'],'amt':amt,
                'win':win,'am':'DEMO',
                'time':datetime.now(pkt).strftime(
                '%H:%M:%S'),
                'id':'bg'+str(time.time())+str(i)})
            save_hist()
            save_data()
if time.time()-S['last']>3:
    S['last']=time.time()
    make_tick()
    if S['auto_scan'] and time.time()-S['last_scan_time']>10:
        S['last_scan_time']=time.time()
        S['scan']=ai_scan_all()
        best=S['scan'][0]
        S['best']=best['pair']
        S['best_score']=best['score']
        S['best_dir']=best['dir']
        S['quality']=best['quality']
        if S['open'] is None:
            S['ai']=best['dir']
            S['ac']=best['score']
    if S['open'] is not None:
        dur=S['open'].get('dur',60)
        el=time.time()-S['open'].get(
        't0',time.time())
        if el>=dur:
            close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if can_trade():
            open_trade()
    save_data()
S['sound_on']=st.toggle(
'WIN SOUND ON',value=S['sound_on'])
if S['sound_on'] and S['ht']:
    if S['ht'][-1]['win']:
        if S['last_sound_id']==S['ht'][-1].get('id',''):
            au='<audio autoplay><source src='
            au+='"https://www.soundjay.com/'
            au+='buttons/sounds/beep-07a.mp3"'
            au+=' type="audio/mpeg"></audio>'
            st.markdown(au,unsafe_allow_html=True)
            t=G+'WIN SOUND - TRADE WIN!'+E
            st.markdown(t,unsafe_allow_html=True)
c1,c2=st.columns(2)
with c1:
    S['auto']=st.toggle(
    'AUTO TRADING ON',value=S['auto'])
with c2:
    acc=st.radio('ACCOUNT',
    ['DEMO','REAL'],horizontal=True)
    S['am']='REAL' if 'REAL' in acc else 'DEMO'
am=S['am']
db=int(S['db'])
rb=int(S['rb'])
dp=int(S['dp'])
rp=int(S['rp'])
cb=rb if am=='REAL' else db
cp=rp if am=='REAL' else dp
hc=hour_count()
lock='LOCKED' if S['open'] is not None else 'FREE'
t=C+'SONA V157 | DEMO '+str(db)+' | REAL '+str(rb)+' | SAVED!'+E
st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | PROFIT '+str(cp)+' | WIN RATE '+str(win_rate())+'%'+E
st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+lock+' | '+now.strftime('%H:%M:%S PKT')+E
st.markdown(t,unsafe_allow_html=True)
t=C+'LADDER NOW: '+str(S['trade_amt'])+' | TARGET: '+str(cp)+' / '+str(S['target'])+E
st.markdown(t,unsafe_allow_html=True)
if S['dp']>=S['target']:
    t=G+'DAILY TARGET POORA! '+str(S['dp'])+' / '+str(S['target'])+' - AUTO BAND!'+E
    st.markdown(t,unsafe_allow_html=True)
if S['loss_streak']>=3:
    t=R+'3 LOSS LAGATAR - AUTO RUK GAYA!'+E
    st.markdown(t,unsafe_allow_html=True)
if rest_left()>0:
    t=Y+'WIN REST - '+str(rest_left())+' sec baaki'+E
    st.markdown(t,unsafe_allow_html=True)
if S['scan']:
    best=S['scan'][0]
    t=B+'AI BRAIN - BEST = '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | HOUR '+str(hc)+' | '+lock+E
    st.markdown(t,unsafe_allow_html=True)
t=G+'V157 - PAIR / TF UPAR - AI PAIR NAHI BADLEGA'+E
st.markdown(t,unsafe_allow_html=True)
S['auto_scan']=st.toggle(
'AI BRAIN AUTO SCAN ON',value=S['auto_scan'])
S['min_conf']=st.selectbox(
'MIN CONFIDENCE',[80,85,90,95],index=2)
S['min_gap_sec']=st.selectbox(
'MIN GAP SEC',[30,60,120,300],index=1)
S['trade_amt']=st.selectbox(
'TRADE AMOUNT',
[250,500,1000,2000,4000,8000],
index=[250,500,1000,2000,4000,8000].index(S['trade_amt']) if S['trade_amt'] in [250,500,1000,2000,4000,8000] else 0)
S['target']=st.selectbox(
'DAILY TARGET',
[1000,5000,10000,15000],
index=[1000,5000,10000,15000].index(S['target']) if S['target'] in [1000,5000,10000,15000] else 3)
t=C+'PAIR / TIMEFRAME - YAHAN SE BADLO - UPAR HI HAI!'+E
st.markdown(t,unsafe_allow_html=True)
np=st.selectbox('PAIR - MARKET',
PAIRS,index=PAIRS.index(S['pair']))
ntf=st.selectbox('TF - TIMEFRAME',
TFS,index=TFS.index(S['tf']))
if np!=S['pair'] or ntf!=S['tf']:
    if S['open'] is not None:
        t=R+'PAIR / TF LOCKED - Trade OPEN hai! Pehle CLOSE hone do!'+E
        st.markdown(t,unsafe_allow_html=True)
    else:
        if np!=S['pair']:
            set_pair(np)
        S['tf']=ntf
        save_data()
        st.rerun()
if st.button('TEST SOUND'):
    au='<audio autoplay><source src='
    au+='"https://www.soundjay.com/'
    au+='buttons/sounds/beep-07a.mp3"'
    au+=' type="audio/mpeg"></audio>'
    st.markdown(au,unsafe_allow_html=True)
    st.success('Awaz aayi ka?')
menu=st.selectbox('MENU',
['HOME','AI BRAIN','TERMINAL',
'DEPOSIT','WITHDRAW','HISTORY',
'SETTINGS'],index=0)
if menu=='WITHDRAW':
    t=C+'WITHDRAW - Paisa Nikalo'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+' | Profit: '+str(rp)+E
    st.markdown(t,unsafe_allow_html=True)
    wamt=st.number_input(
    'Kitna Nikalna Hai?',100,10000,100)
    wnum=st.text_input(
    'JazzCash / Easypaisa Number',
    '0300-1234567')
    if st.button('WITHDRAW CONFIRM'):
        if int(wamt)>rb:
            st.error('BAL se zyada nahi!')
        else:
            S['rb']-=int(wamt)
            S['with_hist'].append(
            {'amt':int(wamt),
            'num':wnum,
            'time':now.strftime('%H:%M:%S')})
            save_data()
            st.success('WITHDRAW HO GAYA!')
            st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['time']+E
        st.markdown(t,unsafe_allow_html=True)
elif menu=='DEPOSIT':
    t=C+'DEPOSIT - REAL me paisa dalo'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+E
    st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input(
    'Kitna Deposit? (Rs)',
    min_value=100,max_value=100000,
    value=1000,step=100)
    method=st.selectbox('Method',
    ['JazzCash','Easypaisa',
    'Bank Transfer'],index=0)
    num=st.text_input('Apna Number',
    placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM'):
        S['rb']+=int(amt)
        S['dep_hist'].append(
        {'amt':int(amt),
        'method':method,'num':num,
        'time':now.strftime('%H:%M:%S')})
        save_data()
        st.success('DEPOSIT HO GAYA!')
        st.rerun()
    for d in reversed(S['dep_hist'][-5:]):
         t=G+'DEPOSIT +'+str(d['amt'])
    t+=' | '+d['method']
    t+=' | '+d['time']+E
    st.markdown(t,unsafe_allow_html=True)
elif menu=='HISTORY':
    t=C+'TRADES - HISTORY SAVED!'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'WIN '+str(S['wc'])
    t+=' LOSS '+str(S['lc'])
    t+=' | WIN RATE '+str(win_rate())+'%'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'PROFIT '+str(cp)+' HOUR '+str(hc)+E
    st.markdown(t,unsafe_allow_html=True)
    st.line_chart(S['bal_hist'])
    if S['open'] is not None:
        o=S['open']
        t=G+'OPEN '+o['pair']
        t+=' ENTRY '+str(o['entry'])
        t+=' | '+o['dir']
        t+=' | TF '+o['tf']
        t+=' | '+o['am']+E
        st.markdown(t,unsafe_allow_html=True)
    for h in reversed(S['ht'][-20:]):
        col='WIN' if h['win'] else 'LOSS'
        t=C+col+' '+h['pair']
        t+=' '+h['tf']
        t+=' ENTRY '+str(h['entry'])
        t+=' EXIT '+str(h['exit'])
        t+=' '+str(h['amt'])
        t+=' | '+h['am']
        t+=' | '+h['time']+E
        st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH HISTORY'):
        st.rerun()
elif menu=='SETTINGS':
    t=C+'SETTINGS - V157'+E
    st.markdown(t,unsafe_allow_html=True)
    S['name']=st.text_input(
    'Tumhara Naam',value=S['name'])
    t=C+'V157 BACKGROUND MODE ON hai'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'HISTORY alag file me hai'+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('RESET DEMO 10000'):
        S['db']=10000
        S['dp']=0
        S['today']=0
        S['total']=0
        S['wc']=0
        S['lc']=0
        S['open']=None
        S['candles']=[]
        S['hour_trades']=[]
        S['last_win_time']=0
        S['loss_streak']=0
        S['trade_amt']=250
        S['bal_hist']=[10000]
        save_data()
        st.rerun()
    if st.button('RESET HOUR'):
        S['hour_trades']=[]
        save_data()
        st.rerun()
    if st.button('CLEAR HISTORY'):
        S['ht']=[]
        S['wc']=0
        S['lc']=0
        S['total']=0
        save_hist()
        save_data()
        st.rerun()
    t=C+'APP: SONA V157 | USER: '+S['name']+' | SAVED!'+E
    st.markdown(t,unsafe_allow_html=True)
elif menu=='AI BRAIN':
    t=B+'AI BRAIN - 90+ ONLY - WIN SOUND'+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('SCAN NOW'):
        S['scan']=ai_scan_all()
        st.rerun()
    if S['scan']:
        best=S['scan'][0]
        t=G+'BEST = '+best['pair']
        t+=' | '+best['dir']
        t+=' | SCORE '+str(best['score'])
        t+=' | '+best['quality']+E
        st.markdown(t,unsafe_allow_html=True)
        t=Y+'STRATEGY: '+best['bos']
        t+=' + '+best['sweep']
        t+=' + Trend '+best['trend']+E
        st.markdown(t,unsafe_allow_html=True)
        for s in S['scan']:
            col=G if s['score']>=90 else Y if s['score']>=80 else C
            t=col+s['pair']
            t+=' '+str(s['price'])
            t+=' | '+s['dir']
            t+=' '+str(s['score'])+'%'
            t+=' | RSI '+str(s['rsi'])
            t+=' | MACD '+str(s['macd'])
            t+=' | ATR '+str(s['atr'])
            t+=' | VWAP '+str(s['vwap'])
            t+=' | VOL '+str(s['vol'])
            t+=' | '+s['bos']
            t+=' | '+s['sweep']+E
            st.markdown(t,unsafe_allow_html=True)
elif menu in ['HOME','TERMINAL']:
    if menu=='TERMINAL':
        t=C+'TERMINAL - CANDLE + INDICATORS'+E
        st.markdown(t,unsafe_allow_html=True)
        t=C+'PAIR / TF upar se badlo!'+E
        st.markdown(t,unsafe_allow_html=True)
    else:
        t=C+'HOME - TODAY '+str(S['today'])
        t+='/96 TOTAL '+str(S['total'])
        t+=' | WIN '+str(S['wc'])
        t+=' LOSS '+str(S['lc'])
        t+=' PROFIT '+str(cp)
        t+=' | HOUR '+str(hc)+E
        st.markdown(t,unsafe_allow_html=True)
    st.line_chart(S['price_hist'])
    pr=S['price_hist']
    rsi=calc_rsi(pr)
    macd,sig=calc_macd(pr)
    atr=calc_atr(S['candles'])
    vwap=calc_vwap(S['candles'])
    bos=calc_bos(pr)
    sweep=calc_sweep(pr)
    hi=max(pr[-20:]) if len(pr)>=20 else max(pr)
    lo=min(pr[-20:]) if len(pr)>=20 else min(pr)
    vol=S['candles'][-1]['v'] if S['candles'] else 1000
    t=C+'RSI '+str(rsi)
    t+=' | Volume '+str(vol)
    t+=' | ATR '+str(atr)
    t+=' | VWAP '+str(vwap)
    t+=' | MACD '+str(macd)
    t+=' | Sig '+str(sig)+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'Hi '+str(hi)
    t+=' Lo '+str(lo)
    t+=' | '+bos
    t+=' | '+sweep
    t+=' | Trend '+calc_trend(pr)+E
    st.markdown(t,unsafe_allow_html=True)
    t=Y+'AI DECISION: '+S['pair']
    t+=' '+S['ai']
    t+=' '+str(S['ac'])+'%'
    t+=' - RSI '+str(rsi)
    t+=' + MACD '+str(macd)
    t+=' + VWAP '+str(vwap)
    t+=' + '+bos+' + '+sweep
    t+=' = '+S['ai']+E
    st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']
        dur=o.get('dur',60)
        el=time.time()-o.get('t0',time.time())
        left=max(0,int(dur-el))
        t=G+'OPEN TRADE LIVE: '+o['pair']
        t+=' ENTRY '+str(o['entry'])
        t+=' | '+o['dir']
        t+=' | '+str(left)+'s LEFT'
        t+=' | TF '+o['tf']
        t+=' | '+o['am']
        t+=' | Now '+str(S['lp'])
        t+=' | LOCKED'+E
        st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'):
            close_trade()
            st.rerun()
    else:
        if rest_left()>0:
            t=Y+'WIN REST - '+str(rest_left())
            t+=' sec baaki - Phir trade'+E
            st.markdown(t,unsafe_allow_html=True)
        elif can_trade():
            t=G+'90+ READY - Trade abhi khulega'+E
            st.markdown(t,unsafe_allow_html=True)
        else:
            t=C+'WAIT - 90+ ka wait'+E
            st.markdown(t,unsafe_allow_html=True)
        if st.button('TRADE ABHI KHOLO'):
            open_trade(manual=True)
            st.rerun()
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL UP'):
            S['ai']='UP'
            open_trade(manual=True)
            st.rerun()
    with b2:
        if st.button('MANUAL DOWN'):
            S['ai']='DOWN'
            open_trade(manual=True)
            st.rerun()
    t=C+'LAST 5 CANDLES'+E
    st.markdown(t,unsafe_allow_html=True)
    for c in reversed(S['candles'][-5:]):
        col='UP' if c['dir']=='UP' else 'DOWN'
        t=C+col+' | OPEN '+str(c['o'])
        t+=' -> CLOSE '+str(c['c'])
        t+=' | HIGH '+str(c['h'])
        t+=' LOW '+str(c['l'])
        t+=' | VOL '+str(c['v'])
        t+=' | '+c['time']+E
        st.markdown(t,unsafe_allow_html=True)
if S['candles']:
    lc=S['candles'][-1]
    mv='UP' if lc['dir']=='UP' else 'DOWN'
    t=C+'LAST CANDLE: '+mv
    t+=' | OPEN '+str(lc['o'])
    t+=' | CLOSE '+str(lc['c'])
    t+=' | HIGH '+str(lc['h'])
    t+=' | LOW '+str(lc['l'])
    t+=' | VOL '+str(lc['v'])
    t+=' | '+lc['time']+E
    st.markdown(t,unsafe_allow_html=True)
t=C+'STREAK '+str(S['streak'])
t+=' | BEST '+S['best']
t+=' '+str(S['best_score'])+'%'
t+=' | HOUR '+str(hc)
t+=' | V157 | '+lock+E
st.markdown(t,unsafe_allow_html=True)
save_data()
time.sleep(3)
st.rerun()   
