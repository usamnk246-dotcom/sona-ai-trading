import streamlit as st
import random, time
from datetime import datetime, timedelta
import pytz

st.set_page_config(page_title='SONA V140 PORA APP', layout='centered')
C='<div style="background:#111;padding:12px;border-radius:12px;color:#fff;font-weight:bold;text-align:center;margin-bottom:6px;">'
G='<div style="background:#0f3d1e;padding:10px;border-radius:10px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:6px;">'
R='<div style="background:#3d0f0f;padding:10px;border-radius:10px;color:#f55;font-weight:bold;text-align:center;margin-bottom:6px;">'
E='</div>'

if 'S' not in st.session_state:
    st.session_state.S={'am':'DEMO','auto':True,'db':10000,'rb':0,'dp':0,'rp':0,'open':None,'open_time':None,'ht':[],'wc':0,'lc':0,'today':0,'total':0,'streak':0,'pair':'SOL/USD','tf':'1MIN','lp':180.02,'ai':'UP','ac':92,'price_hist':[180.02],'dep_hist':[],'with_hist':[],'last':time.time(),'name':'Usam'}
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)
PAIRS=['SOL/USD','BTC/USD','BNB/USD','EUR/USD','AUD/CHF OTC','GBP/USD','USD/JPY','XAU/USD']
TFS=['1MIN','2MIN','5MIN','15MIN']

def new_price():
    S['lp']=round(S['lp']+random.uniform(-1.2,1.2),3)
    if S['lp']<10: S['lp']=180.02
    S['ac']=random.randint(85,96)
    S['ai']=random.choice(['UP','UP','DOWN'])
    S['price_hist'].append(S['lp'])
    if len(S['price_hist'])>60: S['price_hist']=S['price_hist'][-60:]

def open_trade():
    if S['open'] is not None: return False
    bal=S['rb'] if S['am']=='REAL' else S['db']
    if bal<=0: return False
    S['open']={'pair':S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':S['ai'],'am':S['am'],'time':datetime.now(pkt)}
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
    S['open']=None; S['open_time']=None

if time.time()-S['last']>2:
    S['last']=time.time(); new_price()
    if S['open'] is not None and S['open']['time'] is not None:
        if (datetime.now(pkt)-S['open']['time']).total_seconds()>=60: close_trade()
    if S['auto'] and S['open'] is None and S['today']<96:
        if random.random()<0.06: open_trade()

# --- TOP — ACCOUNT PEHLE — BAL BAAD ME — FIX ---
c1,c2=st.columns(2)
with c1:
    S['auto']=st.toggle('AUTO TRADING ON',value=S['auto'])
with c2:
    acc=st.radio('ACCOUNT',['DEMO','REAL'],horizontal=True)
    S['am']='REAL' if 'REAL' in acc else 'DEMO'
am=S['am']; db=int(S['db']); rb=int(S['rb']); dp=int(S['dp']); rp=int(S['rp'])
cb=rb if am=='REAL' else db; cp=rp if am=='REAL' else dp

t=C+'SONA V140 PORA APP | DEMO '+str(db)+' | REAL '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | DEMO '+str(db)+' REAL '+str(rb)+' | PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+now.strftime('%H:%M:%S PKT')+' | TF '+S['tf']+E; st.markdown(t,unsafe_allow_html=True)
if am=='REAL' and rb==0:
    t=R+'REAL 0 — Pehle DEPOSIT karo — Neeche DEPOSIT page me jao'+E; st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=G+'DEMO MODE — Practice — REAL paisa safe hai'+E; st.markdown(t,unsafe_allow_html=True)

# --- MENU — PORA APP ---
menu=st.selectbox('MENU — PORA APP',['🏠 HOME','📈 TERMINAL','💰 DEPOSIT','💸 WITHDRAW','📊 TRADES / HISTORY','⚙️ SETTINGS'],index=0)

if menu=='🏠 HOME':
    t=C+'HOME — TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    st.line_chart(S['price_hist'])
    if S['open'] is not None:
        o=S['open']; left=60-int((datetime.now(pkt)-o['time']).total_seconds()); left=max(0,left)
        t=G+'OPEN '+o['pair']+' '+o['tf']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | '+o['am']+E; st.markdown(t,unsafe_allow_html=True)
        if st.button('CLOSE NOW'): close_trade(); st.rerun()
    else:
        t=C+'NO OPEN TRADE — AUTO wait kar raha hai...'+E; st.markdown(t,unsafe_allow_html=True)
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL UP CALL'): S['ai']='UP'; open_trade(); st.rerun()
    with b2:
        if st.button('MANUAL DOWN PUT'): S['ai']='DOWN'; open_trade(); st.rerun()

if menu=='📈 TERMINAL':
    t=C+'TERMINAL - CANDLE + INDICATORS'+E; st.markdown(t,unsafe_allow_html=True)
    S['pair']=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']))
    S['tf']=st.selectbox('TF / TIME',TFS,index=TFS.index(S['tf']))
    st.line_chart(S['price_hist'])
    t=C+S['pair']+' 85% | '+str(S['lp'])+' | AI '+S['ai']+' '+str(S['ac'])+'% | RSI 62 | MACD UP'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'AUTO MKT / '+S['pair']+' - Signal: '+S['ai']+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH TERMINAL'): st.rerun()

if menu=='💰 DEPOSIT':
    t=C+'DEPOSIT — REAL me paisa dalo'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'Tumhara REAL BAL: '+str(rb)+E; st.markdown(t,unsafe_allow_html=True)
    amt=st.number_input('Kitna Deposit karna hai? (Rs)',min_value=100,max_value=100000,value=1000,step=100)
    method=st.selectbox('Method',['JazzCash','Easypaisa','Bank Transfer'],index=0)
    num=st.text_input('Apna JazzCash / Easypaisa Number',placeholder='0300-1234567')
    if st.button('DEPOSIT CONFIRM KARO'):
        S['rb']+=int(amt); S['dep_hist'].append({'amt':int(amt),'method':method,'num':num,'time':now.strftime('%H:%M:%S')})
        st.success(f'DEPOSIT HO GAYA! REAL BAL ab {int(S["rb"])} hai — Ab REAL pe jao!')
        st.rerun()
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
        if int(wamt)>rb: st.error('REAL BAL se zyada nahi nikal sakte!')
        else:
            S['rb']-=int(wamt); S['with_hist'].append({'amt':int(wamt),'num':wnum,'time':now.strftime('%H:%M:%S')})
            st.success(f'WITHDRAW HO GAYA! {int(wamt)} bheja gaya — REAL BAL ab {int(S["rb"])}')
            st.rerun()
    for w in reversed(S['with_hist'][-5:]):
        t=R+'WITHDRAW -'+str(w['amt'])+' | '+w['num']+' | '+w['time']+E; st.markdown(t,unsafe_allow_html=True)

if menu=='📊 TRADES / HISTORY':
    t=C+'TRADES - HISTORY FULL DAY'+E; st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E; st.markdown(t,unsafe_allow_html=True)
    if S['open'] is not None:
        o=S['open']; t=G+'OPEN '+o['pair']+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+o['am']+E; st.markdown(t,unsafe_allow_html=True)
    for h in reversed(S['ht'][-10:]):
        col='🟢 WIN' if h['win'] else '🔴 LOSS'
        t=C+col+' '+h['pair']+' '+h['tf']+' ENTRY '+str(h['entry'])+' EXIT '+str(h['exit'])+' '+str(h['amt'])+' | '+h['am']+' | '+h['time']+E; st.markdown(t,unsafe_allow_html=True)
    if len(S['ht'])==0:
        t=C+'Abhi koi trade nahi — AUTO ON karo — 1 min wait'+E; st.markdown(t,unsafe_allow_html=True)
    if st.button('REFRESH HISTORY'): st.rerun()

if menu=='⚙️ SETTINGS':
    t=C+'SETTINGS'+E; st.markdown(t,unsafe_allow_html=True)
    S['name']=st.text_input('Tumhara Naam',value=S['name'])
    if st.button('RESET DEMO 10000'):
        S['db']=10000; S['dp']=0; S['today']=0; S['total']=0; S['wc']=0; S['lc']=0; S['ht']=[]; S['open']=None; st.rerun()
    if st.button('RESET REAL 0 — Sab saaf karo'):
        S['rb']=0; S['rp']=0; S['dep_hist']=[]; S['with_hist']=[]; st.rerun()
    if st.button('AUTO OFF KARO'): S['auto']=False; st.rerun()
    if st.button('AUTO ON KARO'): S['auto']=True; st.rerun()
    t=C+'APP: SONA V140 PORA APP | USER: '+S['name']+' | STREAK '+str(S['streak'])+E; st.markdown(t,unsafe_allow_html=True)

t=C+'STREAK '+str(S['streak'])+' | BAL HIST '+str(db)+' | V140 PORA APP'+E; st.markdown(t,unsafe_allow_html=True)
time.sleep(3); st.rerun()
