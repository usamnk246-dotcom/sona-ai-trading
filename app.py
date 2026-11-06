import streamlit as st
import random,time,json,os
from datetime import datetime
import pytz
st.set_page_config(page_title='SONA V153',layout='centered')
C='<div style="background:#111;padding:12px;border-radius:12px;color:#fff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
G='<div style="background:#0f3d1e;padding:10px;border-radius:10px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
R='<div style="background:#3d0f0f;padding:10px;border-radius:10px;color:#ff5555;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
Y='<div style="background:#3d3d0f;padding:10px;border-radius:10px;color:#ffff00;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
B='<div style="background:#0f1e3d;padding:10px;border-radius:10px;color:#5aafff;font-weight:bold;text-align:center;margin-bottom:6px;font-size:15px;">'
E='</div>'
FILE='sona_data.json'
BASE={'SOL/USD':179.50,'BTC/USD':67200,'BNB/USD':710,'EUR/USD':1.085,'AUD/CHF OTC':0.585,'GBP/USD':1.275,'USD/JPY':152.30,'XAU/USD':2650,'EUR/GBP OTC':0.850,'USD/CHF OTC':0.885,'GBP/JPY':194.20,'AUD/USD':0.655}
def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE,'r') as f:
                return json.load(f)
        except:
            return None
    return None
def save_data():
    try:
        d=dict(S)
        d['open']=None
        if S['open'] is not None:
            o=S['open']
            d['open']={'pair':o['pair'],'tf':o['tf'],'entry':o['entry'],'dir':o['dir'],'am':o['am'],'dur':o.get('dur',60),'time':o['time'].strftime('%Y-%m-%d %H:%M:%S')}
        d['hour_start']=S['hour_start'].strftime('%Y-%m-%d %H:%M:%S')
        d['save_time']=time.time()
        with open(FILE,'w') as f:
            json.dump(d,f)
    except:
        pass
if 'S' not in st.session_state:
    sv=load_data()
    if sv is not None:
        try:
            sv['hour_start']=datetime.strptime(sv['hour_start'],'%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.timezone('Asia/Karachi'))
            if sv.get('open') is not None:
                sv['open']['time']=datetime.strptime(sv['open']['time'],'%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.timezone('Asia/Karachi'))
            sv['last']=time.time()
            sv['last_scan_time']=0
            st.session_state.S=sv
        except:
            sv=None
    if sv is None:
        st.session_state.S={'am':'DEMO','auto':True,'db':10000,'rb':0,'dp':0,'rp':0,'open':None,'ht':[],'wc':0,'lc':0,'today':0,'total':0,'streak':0,'pair':'SOL/USD','tf':'1MIN','lp':179.50,'ai':'UP','ac':89,'price_hist':[179.50]*30,'dep_hist':[],'with_hist':[],'last':time.time(),'last_trade_time':0,'last_scan_time':0,'name':'Usam','scan':[],'best':'SOL/USD','best_score':0,'best_dir':'UP','candles':[],'quality':'GOOD','auto_scan':True,'hour_trades':[],'hour_start':datetime.now(pytz.timezone('Asia/Karachi')).replace(minute=0,second=0,microsecond=0),'min_conf':90,'min_gap_sec':60,'last_win_time':0,'sound_on':True,'last_sound_id':''}
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
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
    m=round(calc_ema(pr,12)-calc_ema(pr,26),4)
    s=round(m*0.9,4)
    return m,s
def calc_atr(cd):
    if len(cd)<2:
        return round(step_for(S['lp'])*2,4)
    tr=[]
    for i,c in enumerate(cd):
        if i>0:
            tr.append(max(c['h']-c['l'],abs(c['h']-cd[i-1]['c']),abs(c['l']-cd[i-1]['c'])))
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
    return 'UP' if pr[-1]>calc_ema(pr,20) else 'DOWN'
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
        S['candles']=[{'o':b,'c':b,'h':b,'l':b,'v':1000,'time':now.strftime('%H:%M:%S'),'dir':'UP'}]
def make_tick():
    b=BASE[S['pair']]
    stp=step_for(b)/3
    c=round(S['lp']+random.uniform(-stp,stp),4)
    S['lp']=c
    S['price_hist'].append(c)
    if len(S['price_hist'])>60:
        S['price_hist']=S['price_hist'][-60:]
    if not S['candles']:
        S['candles'].append({'o':c,'c':c,'h':c,'l':c,'v':1000,'time':now.strftime('%H:%M:%S'),'dir':'UP'})
    else:
        lc=S['candles'][-1]
        lc['c']=c
        if c>lc['h']:
            lc['h']=c
        if c<lc['l']:
            lc['l']=c
        lc['dir']='UP' if c>=lc['o'] else 'DOWN'
        lc['v']=lc['v']+random.randint(10,200)
    tfm=int(S['tf'].replace('MIN',''))
    ticks_per_candle=tfm*20
    if len(S['price_hist'])%ticks_per_candle==0:
        S['candles'].append({'o':c,'c':c,'h':c,'l':c,'v':1000,'time':now.strftime('%H:%M:%S'),'dir':'UP'})
    if len(S['candles'])>24:
        S['candles']=S['candles'][-24:]
def ai_scan_all():
    res=[]
    for pair in PAIRS:
        b=BASE[pair]
        stp=step_for(b)
        pr=[b]
        for i in range(59):
            pr.append(round(pr[-1]+random.uniform(-stp*2,stp*2),4))
        vs=[random.randint(800,8500) for _ in range(60)]
        rsi=calc_rsi(pr)
        macd,sig=calc_macd(pr)
        atr=round(sum([abs(pr[i]-pr[i-1]) for i in range(1,len(pr))])/60,4)
        vwap=round(sum(p*v for p,v in zip(pr,vs))/sum(vs),4)
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
        dr='UP' if pr[-1]>vwap or macd>0 else 'DOWN'
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
        res.append({'pair':pair,'price':pr[-1],'rsi':rsi,'macd':macd,'atr':atr,'vwap':vwap,'vol':vol,'bos':bos,'sweep':sweep,'trend':trend,'score':sc,'dir':dr,'quality':calc_q(sc)})
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
    lf=300-(time.time()-S['last_win_time'])
    return int(lf) if lf>0 else 0
def can_trade():
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
    dur=int(S['tf'].replace('MIN',''))*60
    S['open']={'pair':S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':S['ai'],'am':S['am'],'time':datetime.now(pkt),'dur':dur}
    S['last_trade_time']=time.time()
    if not manual:
        S['hour_trades'].append(now)
    save_data()
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
    nid=o['pair']+str(o['entry'])+str(time.time())
    S['ht'].append({'pair':o['pair'],'tf':o['tf'],'entry':o['entry'],'exit':S['lp'],'amt':amt,'win':win,'am':o['am'],'time':datetime.now(pkt).strftime('%H:%M:%S'),'id':nid})
    S['open']=None
    S['last_sound_id']=nid if win else ''
    save_data()
if S.get('save_time',0)>0:
    missed=int(time.time()-S['save_time'])
    if missed>90 and S['auto']:
        n=min(5,missed//360)
        if n>0:
            for i in range(n):
                win=random.choice([True,True,False])
                amt=238 if win else -100
                S['db']+=amt
                S['dp']+=amt
                if win:
                    S['wc']+=1
                    S['streak']+=1
                else:
                    S['lc']+=1
                    S['streak']=0
                S['total']+=1
                S['today']+=1
                S['ht'].append({'pair':S['pair'],'tf':S['tf'],'entry':S['lp'],'exit':S['lp'],'amt':amt,'win':win,'am':S['am'],'time':datetime.now(pkt).strftime('%H:%M:%S'),'id':'catch'+str(time.time())+str(i)})
            S['open']=None
            S['save_time']=time.time()
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
            set_pair(best['pair'])
            S['ai']=best['dir']
            S['ac']=best['score']
    if S['open'] is not None:
        dur=S['open'].get('dur',60)
        el=(datetime.now(pkt)-S['open']['time']).total_seconds()
        if el>=dur:
            close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if can_trade():
            open_trade()
    save_data()
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
t=C+'SONA V153 | DEMO '+str(db)+' | REAL '+str(rb)+' | SAVED!'+E
st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | PROFIT '+str(cp)+E
st.markdown(t,unsafe_allow_html=True)
lock='LOCKED' if S['open'] is not None else 'FREE'
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+lock+' | '+now.strftime('%H:%M:%S PKT')+E
st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=G+'DEMO MODE - Practice - REAL paisa safe'+E
    st.markdown(t,unsafe_allow_html=True)
if am=='REAL' and rb==0:
    t=R+'REAL 0 - Pehle DEPOSIT karo'+E
    st.markdown(t,unsafe_allow_html=True)
hc=hour_count()
if rest_left()>0:
    t=Y+'WIN REST - '+str(rest_left())+' sec baaki'+E
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
    t=B+'AI BRAIN - BEST = '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | HOUR '+str(hc)+' | '+lock+E
    st.markdown(t,unsafe_allow_html=True)
t=G+'V153 - TF = TRADE TIME - 1MIN=60s 2MIN=120s 5MIN=300s'+E
st.markdown(t,unsafe_allow_html=True)
S['auto_scan']=st.toggle('AI BRAIN AUTO SCAN ON',value=S['auto_scan'])
S['min_conf']=st.selectbox('MIN CONFIDENCE',[80,85,90,95],index=2)
S['min_gap_sec']=st.selectbox('MIN GAP SEC',[30,60,120,300],index=1)
t=C+'RULE: WIN ke baad 5 MIN REST - Sirf '+str(S['min_conf'])+'%+ - DATA ON = Trading ON'+E
st.markdown(t,unsafe_allow_html=True)
if st.button('TEST SOUND'):
    st.markdown('<audio autoplay><source src="https://www.soundjay.com/buttons/sounds/beep-07a.mp3" type="audio/mpeg"></audio>',unsafe_allow_html=True)
    st.success('Awaz aayi ka? Volume ON karo!')
menu=st.selectbox('MENU',['AI BRAIN','HOME','TERMINAL','DEPOSIT','WITHDRAW','HISTORY','SETTINGS'],index=1)
if S['candles']:
    lc=S['candles'][-1]
    mv='UP' if lc['dir']=='UP' else 'DOWN'
    t=C+'LAST CANDLE: '+mv+' | OPEN '+str(lc['o'])+' | CLOSE '+str(lc['c'])+' | HIGH '+str(lc['h'])+' | LOW '+str(lc['l'])+' | VOL '+str(lc['v'])+' | '+lc['time']+E
    st.markdown(t,unsafe_allow_html=True)
if menu=='AI BRAIN':
    t=B+'AI BRAIN - 90+ ONLY - WIN SOUND'+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('SCAN NOW'):
        S['scan']=ai_scan_all()
        st.rerun()
    if S['scan']:
        best=S['scan'][0]
        t=G+'BEST = '+best['pair']+' | '+best['dir']+' | SCORE '+str(best['score'])+' | '+best['quality']+E
        st.markdown(t,unsafe_allow_html=True)
        t=Y+'STRATEGY: '+best['bos']+' + '+best['sweep']+' + Trend '+best['trend']+E
        st.markdown(t,unsafe_allow_html=True)
        for s in S['scan']:
            col=G if s['score']>=90 else Y if s['score']>=80 else C
            t=col+s['pair']+' '+str(s['price'])+' | '+s['dir']+' '+str(s['score'])+'% | RSI '+str(s['rsi'])+' | MACD '+str(s['macd'])+' | ATR '+str(s['atr'])+' | VWAP '+str(s['vwap'])+' | VOL '+str(s['vol'])+' | '+s['bos']+' | '+s['sweep']+E
            st.markdown(t,unsafe_allow_html=True)
if menu in ['HOME','TERMINAL']:
    if menu=='TERMINAL':
        t=C+'TERMINAL - CANDLE + INDICATORS'+E
        st.markdown(t,unsafe_allow_html=True)
        old=S['pair']
        np=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']))
        S['tf']=st.selectbox('TF - TIME',TFS,index=TFS.index(S['tf']))
        if np!=old:
            if S['open'] is not None:
                t=R+'PAIR LOCKED - Trade OPEN hai!'+E
                st.markdown(t,unsafe_allow_html=True)
            else:
                set_pair(np)
    else:
        t=C+'HOME - TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+' | HOUR '+str(hc)+E
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
    t=C+'RSI '+str(rsi)+' | Volume '+str(vol)+' | ATR '+str(atr)+' | VWAP '+str(vwap)+' | MACD '+str(macd)+' | Sig '+str(sig)+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'Hi '+str(hi)+' Lo '+str(lo)+' | '+bos+' | '+sweep+' | Trend '+calc_trend(pr)+E
    st.markdown(t,unsafe_allow_html=True)
    t=Y+'AI DECISION: '+S['pair']+' '+S['ai']+' '+str(S['ac'])+'% - RSI '+str(rsi)+' + MACD '+str(macd)+' + Sig '+str(sig)+' + VWAP '+str(vwap)+' + '+bos+' + '+sweep+' = '+S['ai']+E
    st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']
        dur=o.get('dur',60)
        el=(datetime.now(pkt)-o['time']).total_seconds()
        left=max(0,int(dur-el))
        t=G+'OPEN TRADE LIVE: '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | TF '+o['tf']+' | '+o['am']+' | Now '+str(S['lp'])+' | LOCKED'+E
        st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'):
            close_trade()
            st.rerun()
    else:
        if rest_left()>0:
            t=Y+'WIN REST - '+str(rest_left())+' sec baaki - Phir trade'+E
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
        t=C+col+' | OPEN '+str(c['o'])+' -> CLOSE '+str(c['c'])+' | HIGH '+str(c['h'])+' LOW '+str(c['l'])+' | VOL '+str(c['v'])+' | '+c['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='DEPOSIT':
    t=C+'DEPOSIT - REAL me paisa dalo'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+E
    st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input('Kitna Deposit? (Rs)',min_value=100,max_value=100000,value=1000,step=100)
    method=st.selectbox('Method',['JazzCash','Easypaisa','Bank Transfer'],index=0)
    num=st.text_input('Apna Number',placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM'):
        S['rb']+=int(amt)
        S['dep_hist'].append({'amt':int(amt),'method':method,'num':num,'time':now.strftime('%H:%M:%S')})
        save_data()
        st.success('DEPOSIT HO GAYA!')
        st.rerun()
    for d in reversed(S['dep_hist'][-5:]):
        t=G+'DEPOSIT +'+str(d['amt'])+' | '+d['method']+' | '+d['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='WITHDRAW':
    t=C+'WITHDRAW'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'REAL BAL: '+str(rb)+' | Profit: '+str(rp)+E
    st.markdown(t,unsafe_allow_html=True)
    wamt=st.number_input('Amt',100,10000,100)
    wnum=st.text_input('Number','0300-1234567')
    if st.button('WITHDRAW CONFIRM'):
        if int(wamt)>rb:
            st.error('BAL se zyada nahi!')
        else:
            S['rb']-=int(wamt)
            S['with_hist'].append({'amt':int(wamt),'num':wnum,'time':now.strftime('%H:%M:%S')})
            save_data()
            st.success('WITHDRAW HO GAYA!')
            st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['time']+E
        st.markdown(t,unsafe_allow_html=True)
if menu=='HISTORY':
    t=C+'TRADES - HISTORY SAVED!'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'PROFIT '+str(cp)+' HOUR '+str(hc)+E
    st.markdown(t,unsafe_allow_html=True)
