import streamlit as st
import random, time
from datetime import datetime, timedelta
import pytz

st.set_page_config(page_title='SONA V139 FULL', layout='centered')
C='<div style="background:#111;padding:10px;border-radius:10px;color:#fff;font-weight:bold;text-align:center;margin-bottom:5px;">'
C2='<div style="background:#1e2a1e;padding:8px;border-radius:8px;color:#0f0;font-weight:bold;text-align:center;margin-bottom:5px;">'
C3='<div style="background:#2a1e1e;padding:8px;border-radius:8px;color:#f00;font-weight:bold;text-align:center;margin-bottom:5px;">'
E='</div>'

# --- SESSION ---
if 'S' not in st.session_state:
    st.session_state.S={
        'am':'DEMO','auto':True,'db':10000,'rb':0,
        'dp':0,'rp':0,'ot':[],'ht':[],'wc':0,'lc':0,
        'sm':'SOL/USD','lp':180.02,'ai':'UP','ac':92,
        'last':time.time(),'tf':'1MIN','pair':'SOL/USD',
        'bal_hist':[10000],'price_hist':[180.02],
        'open':None,'open_time':None,'entry':0,
        'today':0,'total':0,'streak':0
    }
S=st.session_state.S
pkt=pytz.timezone('Asia/Karachi')
now=datetime.now(pkt)

PAIRS=['SOL/USD','BTC/USD','BNB/USD','EUR/USD','AUD/CHF OTC','GBP/USD','USD/JPY','XAU/USD']
TFS=['1MIN','2MIN','5MIN','15MIN']

def new_price():
    S['lp']=round(S['lp']+random.uniform(-1.2,1.2),3)
    if S['lp']<1: S['lp']=180.02
    S['ac']=random.randint(85,96)
    S['ai']=random.choice(['UP','UP','DOWN'])
    S['sm']=S['pair']
    S['price_hist'].append(S['lp'])
    if len(S['price_hist'])>60: S['price_hist']=S['price_hist'][-60:]

def open_trade():
    am=S['am']
    bal=S['rb'] if am=='REAL' else S['db']
    if bal<=0:
        return False
    if S['open'] is not None:
        return False
    S['entry']=S['lp']
    S['open_time']=datetime.now(pkt)
    S['open']={'pair':S['pair'],'tf':S['tf'],'entry':S['lp'],'dir':S['ai'],'am':am,'time':S['open_time']}
    return True

def close_trade():
    if S['open'] is None:
        return
    o=S['open']
    win=random.choice([True,True,False])
    amt=238 if win else -100
    am=o['am']
    if am=='REAL':
        S['rb']+=amt; S['rp']+=amt
    else:
        S['db']+=amt; S['dp']+=amt
    if win: S['wc']+=1; S['streak']+=1
    else: S['lc']+=1; S['streak']=0
    S['total']+=1; S['today']+=1
    S['bal_hist'].append(S['db'] if am=='DEMO' else S['rb'])
    S['ht'].append({'pair':o['pair'],'tf':o['tf'],'entry':o['entry'],'exit':S['lp'],'amt':amt,'win':win,'am':am,'time':datetime.now(pkt).strftime('%H:%M:%S'),'date':datetime.now(pkt).strftime('%d-%m')})
    S['open']=None; S['open_time']=None

# --- PRICE UPDATE ---
if time.time()-S['last']>2:
    S['last']=time.time()
    new_price()
    # Auto close after 60 sec
    if S['open'] is not None and S['open_time'] is not None:
        diff=(datetime.now(pkt)-S['open_time']).total_seconds()
        if diff>=60:
            close_trade()
    # Auto open
    if S['auto'] and S['open'] is None and S['today']<96:
        if random.random()<0.06:
            open_trade()

# ======================================================
# V139 FIX : PEHLE ACCOUNT + AUTO — PHIR HEADER
# Isliye BAL kabhi ulta nahi hoga!
# ======================================================
c1,c2=st.columns(2)
with c1:
    t=st.toggle('AUTO TRADING ON',value=S['auto'])
    S['auto']=t
with c2:
    acc=st.radio('ACCOUNT',['DEMO','REAL'],horizontal=True)
    if 'REAL' in acc: S['am']='REAL'
    else: S['am']='DEMO'

am=S['am']
db=int(S['db']); rb=int(S['rb'])
dp=int(S['dp']); rp=int(S['rp'])
if am=='REAL': cb=rb
else: cb=db
if am=='REAL': cp=rp
else: cp=dp

# --- HEADER — AB SAHI HAI ---
pkt_str=now.strftime('%H:%M:%S PKT')
t=C+'SONA V139 FULL | DEMO '+str(db)+' | REAL '+str(rb)+E
st.markdown(t,unsafe_allow_html=True)
t=C+'BAL '+str(cb)+' '+am+' | DEMO '+str(db)+' REAL '+str(rb)+E
st.markdown(t,unsafe_allow_html=True)
t=C+S['pair']+' '+str(S['lp'])+' AI '+S['ai']+' '+str(S['ac'])+'% | '+pkt_str+' | TF '+S['tf']+E
st.markdown(t,unsafe_allow_html=True)

if am=='REAL' and rb==0:
    t=C3+'REAL 0 — Deposit kawa — JazzCash / Easypaisa se paisa bhejo — Phir REAL trade hoga'+E
    st.markdown(t,unsafe_allow_html=True)
if am=='DEMO':
    t=C2+'DEMO MODE — Practice paisa — REAL paisa khatam nahi hoga'+E
    st.markdown(t,unsafe_allow_html=True)

# --- GO TO ---
go=st.selectbox('GO TO',['Terminal','Trades','History'],index=0)

# --- PAIR + TF SELECT ---
cp1,cp2=st.columns(2)
with cp1:
    S['pair']=st.selectbox('PAIR',PAIRS,index=PAIRS.index(S['pair']) if S['pair'] in PAIRS else 0)
with cp2:
    S['tf']=st.selectbox('TF / TIME',TFS,index=TFS.index(S['tf']))

if go=='Terminal':
    t=C+'TERMINAL - CANDLE + INDICATORS'+E
    st.markdown(t,unsafe_allow_html=True)
    # Candle chart - line chart se
    st.line_chart(S['price_hist'])
    t=C+S['pair']+' 85% | '+str(S['lp'])+' | AI '+S['ai']+' '+str(S['ac'])+'% | RSI 62 | MACD UP'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'AUTO MKT / '+S['pair']+' - Auto pick — Signal: '+S['ai']+E
    st.markdown(t,unsafe_allow_html=True)
    # Manual buttons
    b1,b2=st.columns(2)
    with b1:
        if st.button('MANUAL TRADE - UP CALL'):
            S['ai']='UP'; open_trade(); st.rerun()
    with b2:
        if st.button('MANUAL TRADE - DOWN PUT'):
            S['ai']='DOWN'; open_trade(); st.rerun()
    if st.button('REFRESH'):
        st.rerun()

# --- OPEN TRADES - LIVE ---
t=C+'OPEN TRADES - LIVE'+E
st.markdown(t,unsafe_allow_html=True)
if S['open'] is not None:
    o=S['open']
    ot=o['time'].strftime('%H:%M:%S PKT')
    exp=(o['time']+timedelta(minutes=1)).strftime('%H:%M:%S PKT')
    left=60-int((datetime.now(pkt)-o['time']).total_seconds())
    if left<0: left=0
    t=C2+'OPEN '+o['pair']+' '+o['tf']+' '+ot+' -> '+exp+' ENTRY '+str(o['entry'])+' | '+o['dir']+' | '+str(left)+'s LEFT | '+o['am']+E
    st.markdown(t,unsafe_allow_html=True)
    if st.button('CLOSE NOW'):
        close_trade(); st.rerun()
else:
    t=C+'NO OPEN TRADE — AUTO wait kar raha hai...'+E
    st.markdown(t,unsafe_allow_html=True)

# --- TRADES - HISTORY ---
if go in ['Trades','History']:
    t=C+'TRADES - HISTORY FULL DAY'+E
    st.markdown(t,unsafe_allow_html=True)
    t=C+'TODAY '+str(S['today'])+'/96 TOTAL '+str(S['total'])+' | WIN '+str(S['wc'])+' LOSS '+str(S['lc'])+' PROFIT '+str(cp)+E
    st.markdown(t,unsafe_allow_html=True)
    # Last 10 trades
    for h in reversed(S['ht'][-10:]):
        col='🟢 WIN' if h['win'] else '🔴 LOSS'
        t=C+col+' '+h['pair']+' '+h['tf']+' ENTRY '+str(h['entry'])+' EXIT '+str(h['exit'])+' '+str(h['amt'])+' | '+h['am']+' | '+h['time']+E
        st.markdown(t,unsafe_allow_html=True)
    if len(S['ht'])==0:
        t=C+'Abhi koi trade nahi — AUTO ON karo — 1 min wait karo'+E
        st.markdown(t,unsafe_allow_html=True)
    if st.button('RESET DEMO 10000'):
        S['db']=10000; S['dp']=0; S['today']=0; S['total']=0; S['wc']=0; S['lc']=0; S['ht']=[]; S['open']=None; st.rerun()
    if st.button('REFRESH HISTORY'):
        st.rerun()

# --- FOOTER STATS ---
t=C+'STREAK '+str(S['streak'])+' | BAL HIST '+str(S['bal_hist'][-1] if S['bal_hist'] else db)+' | V139 FULL'+E
st.markdown(t,unsafe_allow_html=True)

# Auto refresh
time.sleep(3)
st.rerun()
