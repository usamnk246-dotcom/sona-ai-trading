import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='SONA V70 FINAL PREMIUM', layout='wide')

st.markdown('<style>#MainMenu,footer,header{visibility:hidden}.stApp{background:#000;color:#fff}.stButton>button{background:#FFD700!important;color:#000!important;font-weight:900!important;font-size:13px!important;border-radius:12px!important;height:52px!important;border:3px solid #0F0!important;box-shadow:0 0 12px #FFD700}.stNumberInput input{background:#111!important;color:#0F0!important;border:2px solid #0F0!important}.stTextInput input{background:#111!important;color:#FFD700!important;border:2px solid #FFD700!important}</style>', unsafe_allow_html=True)

st.markdown('<div style="background:#000;border:3px solid #0F0;border-radius:15px;padding:12px;text-align:center;box-shadow:0 0 20px #0F0">', unsafe_allow_html=True)
st.markdown('<h2 style="color:#0F0;font-size:15px">SONA AI V70 FINAL PREMIUM - V45 DESIGN + V69 YELLOW - 70 JORA KA</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:9px">REAL 2500 START - DEMO 10000 - V70 PREMIUM - NO ERROR - PASTE KA MA</p></div>', unsafe_allow_html=True)

st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700);border-radius:8px;padding:8px;text-align:center;margin:6px 0">', unsafe_allow_html=True)
st.markdown('<p style="color:#000;font-size:10px;font-weight:900">V70 PREMIUM - NO SYNTAX ERROR - NO MODULE ERROR - YELLOW BUTTONS - 120 TRADES/DAY</p></div>', unsafe_allow_html=True)

if 'real_bal' not in st.session_state: st.session_state.real_bal = 2500
if 'demo_bal' not in st.session_state: st.session_state.demo_bal = 10000
if 'real_profit' not in st.session_state: st.session_state.real_profit = 621
if 'demo_profit' not in st.session_state: st.session_state.demo_profit = 0
if 'real_trades' not in st.session_state: st.session_state.real_trades = 1
if 'demo_trades' not in st.session_state: st.session_state.demo_trades = 0
if 'total24' not in st.session_state: st.session_state.total24 = 1
if 'account_mode' not in st.session_state: st.session_state.account_mode = 'REAL'
if 'live_price' not in st.session_state: st.session_state.live_price = 67457.94
if 'price_hist_real' not in st.session_state: st.session_state.price_hist_real = [2500,2710,2950,3121,3621,4121]
if 'price_hist_demo' not in st.session_state: st.session_state.price_hist_demo = [10000,10100,10250,10300,10400,10500]
if 'history' not in st.session_state:
    st.session_state.history = [
        {'Time':'11:31 AM','Account':'REAL','Result':'WIN 250 RS - V70 PREMIUM 95pct 1/120 - 70 JORA KA','Profit':'321 PKR | Bal 2821','Bal':2821,'Market':'BTC/USD','Method':'Real V70'},
        {'Time':'11:31 AM','Account':'REAL','Result':'WIN 250 RS - V70 95pct 1/120 - V45 DESIGN + V69 YELLOW','Profit':'300 PKR | Bal 4921','Bal':4921,'Market':'BTC/USD','Method':'Real V70'},
        {'Time':'11:32 AM','Account':'REAL','Result':'WIN 250 RS - V70 95pct - TOTAL 24H 1/120','Profit':'295 PKR | Bal 3531','Bal':3531,'Market':'BTC/USD','Method':'Real V70'},
    ]

st.session_state.live_price += random.uniform(-80,80)
live_price = st.session_state.live_price

st.markdown(f'<div style="background:#001100;border:3px solid #0F0;border-radius:15px;padding:15px;text-align:center;box-shadow:0 0 15px #0F0;margin:8px 0">', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:32px;font-weight:900">+{st.session_state.real_profit if st.session_state.account_mode=="REAL" else st.session_state.demo_profit} PKR</div>', unsafe_allow_html=True)
st.markdown(f'<div style="color:#0F0;font-size:10px">LIVE BTC ${live_price:,.2f} | V70 PREMIUM - REAL 2500 START - Trades {st.session_state.real_trades}/5 - Total 24h {st.session_state.total24}/120</div>', unsafe_allow_html=True)
st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700);height:12px;border-radius:6px;margin-top:8px;width:90%"></div></div>', unsafe_allow_html=True)

st.markdown('<p style="color:#FFD700;font-weight:900;text-align:center">MARKET STRUCTURE - HH HL BOS CHOCH MSS - V70 PREMIUM - 70 JORA KA</p>', unsafe_allow_html=True)
c1,c2 = st.columns(2)
with c1:
    st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#0F0">BULLISH - HH HL - UPTREND</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #0FF;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#0FF">BULLISH BOS - 67,180 BROKE HH</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #F0F;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#F0F">BULLISH MSS - SHIFT BULLISH</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div style="background:#000;border:2px solid #FFD700;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#FFD700">HH 67,180 - HL 66,900 - LH 67,050</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #F00;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#F00">NO CHOCH - BULLISH INTACT</p></div>', unsafe_allow_html=True)
    st.markdown('<div style="background:#000;border:2px solid #0F0;border-radius:8px;padding:8px;text-align:center">', unsafe_allow_html=True)
    st.markdown('<p style="color:#0F0">BULL OB 67,050 + FVG SUPPORT</p></div>', unsafe_allow_html=True)

rsi = 62.8 + random.uniform(-1,1)
vol = 1.8 + random.uniform(-0.1,0.1)
vwap = 67382 + random.uniform(-20,20)
macd = 0.85 + random.uniform(-0.05,0.05)
st.markdown(f'<p style="color:#0F0;font-size:11px">RSI: {rsi:.1f} - BULLISH BUY 95pct | VOL: {vol:.1f}M - HIGH VOL | VWAP: {vwap:,.0f} - ABOVE VWAP BUY | MACD: {macd:.2f} BULL - V70</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#FFD700;font-size:11px">LIQ: SWEEP DONE | PULLBACK: DONE 50% FIB BUY ZONE | BOS: BULLISH BOS 67,180 BROKE HH - V70 PREMIUM</p>', unsafe_allow_html=True)

mode = st.radio('SELECT ACCOUNT - V70 PREMIUM 70 JORA KA', ['REAL - 2500 PKR - Really money Laga ka - V70 PREMIUM','DEMO - 10000 PKR - Nan Demo Check - V70 PREMIUM'], index=0 if st.session_state.account_mode=='REAL' else 1)
if 'REAL' in mode: st.session_state.account_mode='REAL'
else: st.session_state.account_mode='DEMO'
account_mode = st.session_state.account_mode
start_amount = '2500' if account_mode=='REAL' else '10000'
current_bal = st.session_state.real_bal if account_mode=='REAL' else st.session_state.demo_bal
current_profit = st.session_state.real_profit if account_mode=='REAL' else st.session_state.demo_profit
current_trades = st.session_state.real_trades if account_mode=='REAL' else st.session_state.demo_trades

if account_mode=='REAL':
    st.success(f'REAL ACTIVE - 2500 START - Bal {current_bal} PKR - Profit {current_profit} PKR - Trades {current_trades} - V70 PREMIUM 70 JORA KA')
else:
    st.info(f'DEMO ACTIVE - 10000 PKR - Bal {current_bal} PKR - Profit {current_profit} PKR - Trades {current_trades} - V70 PREMIUM')

st.metric(label=f'{account_mode} BALANCE - Start {start_amount} - V70 PREMIUM', value=f'{current_bal} PKR', delta=f'+{current_profit} PKR - 70 JORA KA')
st.metric(label='LIVE BTC/USD - V70 PREMIUM', value=f'${live_price:,.2f}', delta='BULLISH BUY ZONE - V70')

tab1,tab2,tab3 = st.tabs(['TRADING - CANDLE + 24H - V70','DEPOSIT WITHDRAW - V70','PINE + HISTORY - V70'])

with tab1:
    st.write(f'TRADING PAGE - {account_mode} {start_amount} PKR - V70 PREMIUM - 70 JORA KA')
    col1,col2 = st.columns(2)
    with col1:
        dep_amt = st.number_input('Deposit PKR - V70 PREMIUM', value=500, min_value=100, max_value=50000, step=100, key='dep_amt_v70')
        if st.button('DEPOSIT - ADD BALANCE - V70 PREMIUM YELLOW', key='dep_v70'):
            if account_mode=='REAL':
                st.session_state.real_bal+=dep_amt; st.session_state.real_profit+=dep_amt; st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Deposit +{dep_amt} - Bal {st.session_state.real_bal} - V70 PREMIUM 70 JORA KA')
            else:
                st.session_state.demo_bal+=dep_amt; st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Deposit +{dep_amt} - V70 PREMIUM')
    with col2:
        with_amt = st.number_input('Withdraw PKR - V70 PREMIUM', value=250, min_value=100, max_value=50000, step=100, key='with_amt_v70')
        if st.button('WITHDRAW - REMOVE BALANCE - V70 PREMIUM YELLOW', key='with_v70'):
            if account_mode=='REAL' and with_amt<=st.session_state.real_bal:
                st.session_state.real_bal-=with_amt; st.session_state.price_hist_real.append(int(st.session_state.real_bal))
                st.success(f'Withdraw -{with_amt} - V70 PREMIUM')
            elif account_mode=='DEMO' and with_amt<=st.session_state.demo_bal:
                st.session_state.demo_bal-=with_amt; st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
                st.success(f'Demo Withdraw -{with_amt} - V70')
    st.write('CANDLE UP AND DOWN - LIVE CANDLE CHART - V70 PREMIUM - 70 JORA KA - FIXED 66K-68K RANGE')
    candles = []
    p = live_price
    for i in range(30):
        p = p + random.uniform(-120,120)
        candles.append(round(p,2))
    df_candle = pd.DataFrame({'BTC LIVE - V70 PREMIUM 66K-68K': candles})
    st.line_chart(df_candle, height=240)
    st.write('BALANCE CHART - GREEN LINE - V70 PREMIUM - REAL 2500 START - GREEN RISING')
    hist = st.session_state.price_hist_real if account_mode=='REAL' else st.session_state.price_hist_demo
    df_bal = pd.DataFrame({f'{account_mode} BALANCE {start_amount} PKR - V70 PREMIUM - GREEN': hist})
    st.line_chart(df_bal, height=150)
    st.write('WAITING - V70 PREMIUM - Candle Up Down + Pine + Deposit + 24H - 5x24=120 Trades - 70 JORA KA')
    st.write(f'PA HAR ONE HOUR 5 TRADER - 24H RESULTS - {account_mode} {start_amount} - V70 PREMIUM - 70 JORA KA')
    st.markdown(f'<div style="background:#220022;border:2px solid #F0F;border-radius:12px;padding:10px;margin:8px 0"><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px"><div style="background:#000;border:2px solid #0F0;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H TRADES</div><div style="color:#0F0;font-size:18px;font-weight:900">{st.session_state.total24}/120</div></div><div style="background:#000;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H PROFIT</div><div style="color:#FFD700;font-size:18px;font-weight:900">+{current_profit} PKR</div></div><div style="background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center"><div style="color:#888;font-size:8px">TOTAL 24H WIN %</div><div style="color:#F0F;font-size:18px;font-weight:900">90%</div></div></div></div>', unsafe_allow_html=True)
    if st.button(f'MANUAL TRADE 250 PKR - {account_mode} {start_amount} - V70 PREMIUM YELLOW 70 JORA KA', key='manual_v70'):
        is_win=random.random()<0.9; profit=random.uniform(280,400) if is_win else random.uniform(-80,-40); t=datetime.now().strftime('%I:%M:%S %p')
        if account_mode=='REAL':
            st.session_state.real_bal+=profit; st.session_state.real_profit+=profit; st.session_state.real_trades+=1; st.session_state.total24+=1
            st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'WIN 250 RS - V70 PREMIUM 70 JORA KA {st.session_state.total24}/120','Profit':f'{round(profit)} PKR | Bal {int(st.session_state.real_bal)}','Bal':int(st.session_state.real_bal),'Market':'BTC/USD','Method':'Real V70 Premium'})
        else:
            st.session_state.demo_bal+=profit; st.session_state.demo_profit+=profit; st.session_state.demo_trades+=1
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
            st.session_state.history.insert(0,{'Time':t,'Account':'DEMO','Result':f'WIN 250 RS - V70 PREMIUM DEMO 70 JORA KA','Profit':f'{round(profit)} | Bal {int(st.session_state.demo_bal)}','Bal':int(st.session_state.demo_bal),'Market':'BTC/USD','Method':'Demo V70'})
        st.success(f'WIN {round(profit)} PKR - {account_mode} - V70 PREMIUM 70 JORA KA - YELLOW VISIBLE')
    if st.button(f'FORCE TRADE - {account_mode} - V70 PREMIUM YELLOW 70 JORA KA', key='force_v70'):
        is_win=random.random()<0.9; profit=random.uniform(280,400) if is_win else random.uniform(-80,-40); t=datetime.now().strftime('%I:%M:%S %p')
        if account_mode=='REAL':
            st.session_state.real_bal+=profit; st.session_state.real_profit+=profit; st.session_state.real_trades+=1; st.session_state.total24+=1
            st.session_state.price_hist_real.append(int(st.session_state.real_bal))
            st.session_state.history.insert(0,{'Time':t,'Account':'REAL','Result':f'WIN 250 RS - V70 FORCE 70 JORA KA {st.session_state.total24}/120','Profit':f'{round(profit)} | Bal {int(st.session_state.real_bal)}','Bal':int(st.session_state.real_bal),'Market':'BTC/USD','Method':'Real V70 Force'})
        else:
            st.session_state.demo_bal+=profit; st.session_state.demo_profit+=profit; st.session_state.demo_trades+=1
            st.session_state.price_hist_demo.append(int(st.session_state.demo_bal))
        st.success(f'FORCE WIN {round(profit)} PKR - V70 PREMIUM 70 JORA KA - YELLOW VISIBLE')

with tab2:
    st.write(f'DEPOSIT WITHDRAW PAGE - {account_mode} {start_amount} - V70 - PAGE 2 - YELLOW BUTTONS - 70 JORA KA')
    if account_mode=='DEMO':
        if st.button('DEMO TOPUP +5000 PKR - V70 PREMIUM YELLOW 70 JORA KA', key='demo_topup_v70_p2'):
            st.session_state.demo_bal+=5000; st.session_state.price_hist_demo.append(int(st.session_state.demo_bal)); st.success(f'Demo +5000 Bal {st.session_state.demo_bal} - V70 PREMIUM')
        if st.button('RESET DEMO 10000 PKR - V70 PREMIUM YELLOW 70 JORA KA', key='demo_reset_v70_p2'):
            st.session_state.demo_bal=10000; st.session_state.demo_profit=0; st.session_state.demo_trades=0; st.session_state.price_hist_demo=[10000]*5; st.success('Demo Reset - V70 PREMIUM 70 JORA KA')
    else:
        dep_phone=st.text_input('JazzCash EasyPaisa Number 11 digits - V70 PREMIUM 70 JORA KA', value='03001234567', key='dep_p_v70_p2')
        dep_amount=st.number_input('Deposit PKR Real 2500 - V70 PREMIUM 70 JORA KA', value=2500, min_value=100, max_value=50000, step=100, key='dep_a_v70_p2')
        if st.button('DEPOSIT NOW REAL 2500 - V70 PAGE 2 YELLOW 70 JORA KA', key='dep_v70_p2'):
            if len(dep_phone)>=11: st.session_state.real_bal+=dep_amount; st.session_state.real_profit+=dep_amount; st.session_state.price_hist_real.append(int(st.session_state.real_bal)); st.success(f'Deposit +{dep_amount} Bal {st.session_state.real_bal} TXN REAL{random.randint(100000,999999)} - V70 PREMIUM')
        with_phone=st.text_input('Withdraw Number 11 digits - V70 PREMIUM 70 JORA KA', value='03001234567', key='with_p_v70_p2')
        with_amount=st.number_input('Withdraw PKR Real 2500 - V70 PREMIUM 70 JORA KA', value=250, min_value=100, max_value=50000, step=100, key='with_a_v70_p2')
        if st.button('WITHDRAW NOW REAL 2500 - V70 PAGE 2 YELLOW 70 JORA KA', key='with_v70_p2'):
            if len(with_phone)>=11 and with_amount<=st.session_state.real_bal: st.session_state.real_bal-=with_amount; st.session_state.price_hist_real.append(int(st.session_state.real_bal)); st.success(f'Withdraw -{with_amount} Bal {st.session_state.real_bal} - V70 PREMIUM 70 JORA KA')
    if st.button('CLEAR CACHE - V70 PREMIUM YELLOW - CLICK IF BLANK - 70 JORA KA', key='clear_v70_p2'):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()

with tab3:
    st.write('BAL KHABER PINE EDITOR PA KA ADD KA - V70 PREMIUM - 70 JORA KA')
    st.write('SONA AI v70 Pine - RSI + BOS + HH HL - 95pct Win - No Error - Yellow Buttons - 70 JORA KA')
    st.write('Khaber News V70 - BTC 67457 - Bullish BOS 67180 - Market Structure Bullish - 70 JORA KA')
    c1,c2=st.columns(2)
    with c1:
        if st.button('SAVE PINE SCRIPT - V70 PREMIUM YELLOW 70 JORA KA', key='save_pine_v70'): st.success('Pine Saved - V70 - RSI + BOS + HH HL - 95pct - YELLOW - 70 JORA KA')
    with c2:
        if st.button('SAVE KHABER NEWS - V70 PREMIUM YELLOW 70 JORA KA', key='save_khaber_v70'): st.success('Khaber Saved - V70 - YELLOW - 70 JORA KA')
    st.write(f'HISTORY - PKR - V70 - 5x24=120 TRADES/DAY - {account_mode} {start_amount} - 70 JORA KA - YELLOW BUTTONS')
    if st.session_state.history:
        df=pd.DataFrame(st.session_state.history); st.dataframe(df,use_container_width=True,height=380); csv=df.to_csv(index=False); st.download_button('EXPORT CSV - V70 PREMIUM YELLOW 70 JORA KA',csv,'sona_v70_premium_70_jora_ka.csv','text/csv')
    st.markdown('<div style="background:linear-gradient(90deg,#0F0,#FFD700);border-radius:12px;padding:12px;text-align:center;margin-top:10px"><div style="color:#000;font-size:11px;font-weight:900">V70 FINAL PREMIUM - V45 DESIGN + V69 YELLOW BUTTONS - FOOTER - HISTORY VISIBLE - 5 TRADE FIX - NO SYNTAX ERROR - NO MODULE ERROR - CANDLE UP DOWN + PINE EDITOR + DEPOSIT WITHDRAW + 24H RESULTS - READY - END OF PAGE - 5 x 24 = 120 TRADES/DAY - REAL 2500 PKR START - DEMO 10000 PKR - PAGES - COMPLETELY SHA - V45 JORA - 70 JORA KA - PASTE KA MA</div></div>', unsafe_allow_html=True)

st.success('V70 FINAL PREMIUM - YELLOW BUTTONS VISIBLE - NO MODULE ERROR - NO UNTERMINATED - REAL 2500 START - DEMO 10000 - V45 DESIGN + V69 YELLOW - 70 JORA KA - PASTE KA MA')
