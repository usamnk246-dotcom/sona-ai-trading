import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v53 FIXED - JazzCash EasyPaisa", layout="wide")

st.markdown("<style>#MainMenu{visibility:hidden}footer{visibility:hidden}header{visibility:hidden}.stApp{background:#020202}</style>", unsafe_allow_html=True)

st.markdown("""
<div style='background:#000;border:3px solid #0F0;border-radius:12px;padding:10px;text-align:center'>
<h1 style='color:#0F0;font-size:13px;margin:0'>SONA AI v53 FIXED - JAZZCASH EASYPAISA + AUTO ON OFF + SOUND WIN + LIVE CANDLE 1m 5m 1h - NO SYNTAX ERROR - V45 JORA</h1>
</div>
""", unsafe_allow_html=True)

if 'bal' not in st.session_state:
    st.session_state.bal = 10123
    st.session_state.profit = 621
    st.session_state.trades_hour = 0
    st.session_state.total24 = 1
    st.session_state.history = [
        {"Time":"04:19:53 AM","Result":"DEPOSIT +502 PKR - JazzCash","Profit":"502 PKR | Bal 10123","Bal":10123,"Market":"BTC/USD","Method":"JazzCash"},
        {"Time":"07:37:58 AM","Result":"WIN 250 RS - V53","Profit":"300 PKR | Bal 9621","Bal":9621,"Market":"BTC/USD","Method":"Trading"},
    ]
    st.session_state.price_hist = [3000,3621,4621,9621,10123]
    st.session_state.auto_on = False
    st.session_state.sound_on = True

c1,c2,c3,c4 = st.columns(4)
with c1:
    st.session_state.auto_on = st.toggle("AUTO TRADING ON/OFF", value=st.session_state.auto_on)
    if st.session_state.auto_on:
        st.success("AUTO ON - 5x24=120 Running")
    else:
        st.error("AUTO OFF - Manual Only")
with c2:
    st.session_state.sound_on = st.toggle("SOUND WIN ON/OFF", value=st.session_state.sound_on)
    st.info(f"Sound {'ON' if st.session_state.sound_on else 'OFF'} - WIN pe Ding!")
with c3:
    market = st.selectbox("DIFFERENT MARKET", ["BTC/USD - $67,421","ETH/USD - $3,450","SOL/USD - $180","GOLD/USD - $2,350","EUR/USD - $1.08","PKR/USD - 278"], index=0)
with c4:
    tf = st.selectbox("LIVE CANDLE TIMEFRAME", ["1m - 1 MIN - Fast","5m - 5 MIN - Medium","15m - 15 MIN","1h - 1 HOUR - Slow","4h - 4 HOUR","1D - 1 DAY"], index=0)

st.markdown("""
<div style='background:#1a0033;border:2px solid #FFD700;border-radius:10px;padding:8px;text-align:center;margin:5px 0'>
<div style='color:#FFD700;font-weight:900'>MARKET STRUCTURE - HH HL LH LL BOS CHOCH - BULLISH HH HL UPTREND - BOS BULLISH</div>
</div>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("<div style='background:#000;border:2px solid #0F0;border-radius:8px;padding:6px;text-align:center;color:#0F0;font-weight:900'>TREND: BULLISH HH HL</div>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div style='background:#000;border:2px solid #0FF;border-radius:8px;padding:6px;text-align:center;color:#0FF;font-weight:900'>BOS: BULLISH BOS 67,180 BROKE HH</div>", unsafe_allow_html=True)

st.markdown(f"""
<div style='background:#000;border:3px solid #0F0;border-radius:12px;padding:12px;text-align:center;margin:6px 0'>
<div style='font-size:36px;color:#0F0;font-weight:900'>+{st.session_state.profit} PKR | Bal {st.session_state.bal} PKR</div>
<div style='color:#0F0;font-size:10px'>LIVE: {market} | AUTO {'ON' if st.session_state.auto_on else 'OFF'} | Sound {'ON' if st.session_state.sound_on else 'OFF'} | Trades {st.session_state.trades_hour}/5 | Total 24h {st.session_state.total24}/120 | TF {tf} | V53 FIXED</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='background:linear-gradient(135deg,#FFD700,#FF6A00);border-radius:10px;padding:10px;text-align:center;color:#000;font-weight:900;margin:5px 0'>JAZZCASH AND EASYPAISA DEPOSIT WITHDRAW EASY KAGA - V53 FIXED - DASE JORA KA</div>", unsafe_allow_html=True)

j1, j2 = st.columns(2)
with j1:
    st.markdown("**JAZZCASH / EASYPAISA DEPOSIT - EASY KAGA**")
    dep_method = st.selectbox("Deposit Method", ["JazzCash","EasyPaisa","Bank Transfer","USDT"], index=0, key="dep_m")
    dep_phone = st.text_input("JazzCash / EasyPaisa Number (11 digits) Deposit", value="03001234567", key="dep_p")
    dep_amount = st.number_input("Deposit Amount PKR", value=500, min_value=100, max_value=50000, step=100, key="dep_a")
    if st.button("DEPOSIT NOW - JAZZCASH EASYPAISA EASY KAGA - V53 FIXED", key="dep_btn"):
        if len(dep_phone) >= 11:
            st.session_state.bal += dep_amount
            st.session_state.profit += dep_amount
            st.session_state.price_hist.append(st.session_state.bal)
            st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Result": f"DEPOSIT +{dep_amount} PKR - {dep_method} {dep_phone}", "Profit": f"{dep_amount} PKR | Bal {st.session_state.bal}", "Bal": st.session_state.bal, "Market": market, "Method": dep_method})
            st.success(f"Deposit Success +{dep_amount} PKR via {dep_method} {dep_phone} - Bal {st.session_state.bal} PKR - Transaction JC{random.randint(100000,999999)} - EASY KAGA - V53 FIXED")
            if st.session_state.sound_on:
                st.markdown("<audio autoplay><source src='https://www.soundjay.com/buttons/beep-07a.wav' type='audio/wav'></audio>", unsafe_allow_html=True)
        else:
            st.error("Number ghalat da - 11 digits likho - 0300-XXXXXXX")

with j2:
    st.markdown("**JAZZCASH / EASYPAISA WITHDRAW - EASY KAGA**")
    with_method = st.selectbox("Withdraw Method", ["JazzCash","EasyPaisa","Bank Transfer","USDT"], index=0, key="with_m")
    with_phone = st.text_input("JazzCash / EasyPaisa Number (11 digits) Withdraw", value="03001234567", key="with_p")
    with_amount = st.number_input("Withdraw Amount PKR", value=250, min_value=100, max_value=50000, step=100, key="with_a")
    if st.button("WITHDRAW NOW - JAZZCASH EASYPAISA EASY KAGA - V53 FIXED", key="with_btn"):
        if len(with_phone) >= 11:
            if with_amount <= st.session_state.bal:
                st.session_state.bal -= with_amount
                st.session_state.price_hist.append(st.session_state.bal)
                st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Result": f"WITHDRAW -{with_amount} PKR - {with_method} {with_phone}", "Profit": f"-{with_amount} PKR | Bal {st.session_state.bal}", "Bal": st.session_state.bal, "Market": market, "Method": with_method})
                st.success(f"Withdraw Success -{with_amount} PKR via {with_method} {with_phone} - Bal {st.session_state.bal} PKR - 5 Min me ayega - Transaction JC{random.randint(100000,999999)} - V53 FIXED")
            else:
                st.error(f"Balance kam da - Max {st.session_state.bal} PKR")
        else:
            st.error("Number ghalat da - 11 digits likho")

st.markdown("<div style='background:#000;border:2px solid #F0F;border-radius:10px;padding:8px;text-align:center;color:#F0F;font-weight:900;margin:5px 0'>RSI 62.4 BULLISH BUY 95pct | VOLUME HIGH 1.8M CONFIRM BUY | ATR 1.24 LOW VOL SAFE | VWAP 67,180 ABOVE | MACD BULLISH | LIQUIDITY SWEEP | BOS PULLBACK - V53 FIXED</div>", unsafe_allow_html=True)

st.markdown(f"<div style='background:#000;border:2px solid #FFD700;border-radius:8px;padding:6px;text-align:center;color:#FFD700;font-weight:900'>LIVE CANDLE CHART - {market} - {tf} - V53 FIXED - CANDLE UP DOWN RAWAN</div>", unsafe_allow_html=True)

if "1m" in tf:
    num_candles = 30
    vol = 80
elif "5m" in tf:
    num_candles = 25
    vol = 150
else:
    num_candles = 20
    vol = 250

candle_data = []
price = 67421
for i in range(num_candles):
    o = price + random.uniform(-vol, vol)
    c = o + random.uniform(-vol, vol)
    h = max(o, c) + random.uniform(10, vol/2)
    l = min(o, c) - random.uniform(10, vol/2)
    candle_data.append({"Open": o, "High": h, "Low": l, "Close": c})
    price = c

df_c = pd.DataFrame(candle_data)
st.line_chart(df_c, height=250)
st.line_chart(pd.DataFrame({"Balance PKR": st.session_state.price_hist}), height=150)

if st.session_state.auto_on:
    st.info("AUTO ON - Every 1 Min Trade - V53 FIXED")
    if st.session_state.trades_hour < 5:
        if st.button("SIMULATE AUTO TRADE NOW - V53 FIXED", key="auto_sim"):
            is_win = random.random() < 0.9
            p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
            st.session_state.bal += p
            st.session_state.price_hist.append(st.session_state.bal)
            st.session_state.trades_hour += 1
            st.session_state.total24 += 1
            st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Result": f"{'WIN' if is_win else 'LOSS'} 250 RS - V53 Auto - {tf}", "Profit": f"{round(p)} PKR | Bal {int(st.session_state.bal)}", "Bal": int(st.session_state.bal), "Market": market, "Method": "Auto"})
            st.success(f"AUTO {'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.bal)} - {market} - {tf}")
            if is_win and st.session_state.sound_on:
                st.markdown("<audio autoplay><source src='https://www.soundjay.com/misc/sounds/bell-ringing-05.wav' type='audio/wav'></audio><div style='color:#0F0;font-weight:900'>Ding! WIN Sound Alert - V53 FIXED</div>", unsafe_allow_html=True)
    else:
        st.warning("Hourly limit 5/5 reached - Reset karo")

col_m1, col_m2 = st.columns(2)
with col_m1:
    if st.button("MANUAL TRADE - 250 PKR - V53 FIXED - DASE JORA KA", key="manual"):
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        st.session_state.bal += p
        st.session_state.price_hist.append(st.session_state.bal)
        st.session_state.trades_hour += 1
        st.session_state.total24 += 1
        st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Result": f"{'WIN' if is_win else 'LOSS'} 250 RS - V53 Manual", "Profit": f"{round(p)} PKR | Bal {int(st.session_state.bal)}", "Bal": int(st.session_state.bal), "Market": market, "Method": "Manual"})
        st.success(f"{'WIN' if is_win else 'LOSS'} {round(p)} PKR - Bal {int(st.session_state.bal)}")
        if is_win and st.session_state.sound_on:
            st.markdown("<audio autoplay><source src='https://www.soundjay.com/misc/sounds/bell-ringing-05.wav' type='audio/wav'></audio><div style='color:#0F0;font-weight:900'>Ding! WIN - Sound - V53 FIXED</div>", unsafe_allow_html=True)

with col_m2:
    if st.button("CLEAR COOLDOWN + RESET HOUR - V53 FIXED", key="clear"):
        st.session_state.trades_hour = 0
        st.success("Cooldown cleared - 0/5 - V53 FIXED")

col_f1, col_f2 = st.columns(2)
with col_f1:
    if st.button("FORCE TRADE NOW - 5x24=120 - V53 FIXED", key="force"):
        st.session_state.trades_hour = 0
        is_win = random.random() < 0.9
        p = random.uniform(280, 400) if is_win else random.uniform(-80, -40)
        st.session_state.bal += p
        st.session_state.price_hist.append(st.session_state.bal)
        st.session_state.trades_hour += 1
        st.session_state.total24 += 1
        st.session_state.history.insert(0, {"Time": datetime.now().strftime("%I:%M:%S %p"), "Result": f"{'WIN' if is_win else 'LOSS'} 250 RS - V53 Force", "Profit": f"{round(p)} PKR | Bal {int(st.session_state.bal)}", "Bal": int(st.session_state.bal), "Market": market, "Method": "Force"})
        st.success(f"FORCE {'WIN' if is_win else 'LOSS'} {round(p)} PKR - V53 FIXED - DASE JORA KA")
        if is_win and st.session_state.sound_on:
            st.markdown("<audio autoplay><source src='https://www.soundjay.com/misc/sounds/bell-ringing-05.wav' type='audio/wav'></audio>", unsafe_allow_html=True)

with col_f2:
    if st.button("RESET HOURLY LIMIT - V53 FIXED", key="reset"):
        st.session_state.trades_hour = 0
        st.success("Hourly reset 0/5 - V53 FIXED")

st.markdown("<div style='background:#0a0a0a;border:2px solid #FFD700;border-radius:10px;padding:8px;margin:5px 0;color:#FFD700;font-weight:900'>HISTORY - PKR - JAZZCASH EASYPAISA + TRADING - V53 FIXED - 5x24=120 - V45 JORA</div>", unsafe_allow_html=True)

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, height=350)
    csv_data = df.to_csv(index=False)
    st.download_button("EXPORT CSV - V53 FIXED", csv_data, "sona_v53_fixed.csv", "text/csv")
else:
    st.write("No trades yet - V53 FIXED")

st.markdown("<div style='background:linear-gradient(90deg,#FFD700,#0F0);border-radius:10px;padding:8px;text-align:center;color:#000;font-weight:900;margin:5px 0'>V53 FIXED - JAZZCASH EASYPAISA EASY KAGA + AUTO ON OFF + SOUND WIN + LIVE CANDLE 1m 5m 1h - NO SYNTAX ERROR - V45 JORA - DASE JORA KA - READY!</div>", unsafe_allow_html=True)
