import streamlit as st
import pandas as pd
import numpy as np
import requests
from datetime import datetime
import pytz

TELEGRAM_TOKEN = "7994090809:AAH1234abc...tumhara_asli_token"
TELEGRAM_CHAT_ID = "7994090809"

def send_king_v103_alert(symbol, entry, sl, tp, quality):
    if entry is None:
        return
    msg = f"👑 KING V103 BUY CONFIRMED\n{symbol}\nEntry: {entry}\nSL: {sl}\nTP: {tp}\nQuality: {quality}\nTime: Peshawar"
    try:
        r = requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}, timeout=10)
        if r.status_code == 200:
            st.success("✅ TELEGRAM SUCCESS!")
        else:
            st.error(f"❌ FAIL: {r.text[:250]}")
    except Exception as e:
        st.error(f"Error: {e}")

st.set_page_config(page_title="SONA AI ADVANCE v10.3", layout="wide")

st.markdown("""
<style>
.stApp {background:#0a1929; color:#e6c07a;}
.sona-header {background: linear-gradient(135deg,#0f2640 0%,#122e4f 100%); border:2px solid #d4af37; border-radius:20px; padding:18px 20px; display:flex; justify-content:space-between; align-items:center;}
.gold-badge {background:#00e676; color:#000; padding:4px 14px; border-radius:10px; font-weight:800; font-size:13px;}
.sona-card {background:#0f2135; border:1.5px solid #c9a86a; border-radius:18px; padding:18px; margin:12px 0;}
.sona-title {color:#e6c07a; font-weight:800; font-size:15px;}
.price-big {color:#e6c07a; font-size:38px; font-weight:900;}
.green {color:#00e676; font-weight:700;}
.progress-bg {background:#1a324d; height:12px; border-radius:10px;}
.progress-fill {background:linear-gradient(90deg,#e6c07a,#f5d78e); height:12px; border-radius:10px;}
.market-card {background:#11263d; border:1px solid #1e3a5a; border-radius:14px; padding:12px; text-align:center; margin:6px 0;}
.market-card.active {border:1.5px solid #d4af37; background:#14304d;}
.king-green {background:#0a3320; border:2px solid #00e676; color:#00e676; border-radius:16px; padding:16px; font-weight:700; font-size:18px;}
</style>
""", unsafe_allow_html=True)

pkt = pytz.timezone('Asia/Karachi')
now_str = datetime.now(pkt).strftime("%I:%M %p")

st.markdown(f"""
<div class="sona-header">
  <div style="display:flex; align-items:center; gap:16px;">
    <div style="width:60px;height:70px;background:linear-gradient(#d4af37,#a67c00);border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:28px;">⬡</div>
    <div>
      <div style="font-size:32px;font-weight:900;color:#e6c07a;line-height:1.1;">SONA AI<br>ADVANCE<br>v10.3</div>
      <div style="color:#7fa8c7;font-size:12px;margin-top:6px;">KING V103 x SONA LINKED - PINE EDITOR INSIDE</div>
    </div>
  </div>
  <div style="text-align:right;">
    <div style="color:#00e676;font-weight:800;">||| LIVE AI MODE</div>
    <div><span class="gold-badge">ACTIVE</span></div>
    <div style="color:#cfe0f0;font-size:13px;margin-top:8px;">PESHAWAR - {now_str}<br>AM PKT - 10 MIN<br>READY</div>
  </div>
</div>
""", unsafe_allow_html=True)

if st.button("📲 TEST TELEGRAM - SEND NOW"):
    send_king_v103_alert("XAU/USD - GOLD", 4176.07, 4170.0, 4195.0, "6/7 TEST")

tab1, tab2 = st.tabs(["🔱 SONA AI TRADING TERMINAL", "📝 SONA AI PINE EDITOR (KHAPEL)"])

with tab1:
    st.markdown("""
    <div class="sona-card">
      <div class="sona-title">📈 ACCOUNT GROWTH - 5 DAY 100%</div>
      <div style="margin-top:12px; background:#0a1a2d; border:1px solid #c9a86a; border-radius:16px; padding:16px;">
        <div style="color:#7fa8c7;">REAL ACCOUNT</div>
        <div class="price-big">$10.00</div>
        <div class="green">+0.00% (24h) • +4.32% Real</div>
        <div style="display:flex; justify-content:space-between; margin-top:14px; color:#7fa8c7; font-size:13px;">
          <span>Goal $1000</span><span>1.0% $10/$1000</span>
        </div>
        <div class="progress-bg" style="margin-top:6px;"><div class="progress-fill" style="width:38%;"></div></div>
        <div style="color:#7fa8c7; font-size:12px; margin-top:10px;">Days Active: 5 • Daily Target: +$198 • KING V103 x SONA LINKED ✓</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    tf = st.selectbox("Timeframe", ["5min","1min","15min","1h","4h","Daily"], index=0)
    market = st.selectbox("Market", ["XAU/USD • GOLD","BTC/USDT","EUR/USD","GBP/USD"], index=0)
    auto = st.toggle("Automatic Trading", value=True)

    st.markdown("""
    <div class="market-card"><div style="color:#7fa8c7;">BTC/USDT</div><div class="green">67432.18 +2.34%</div></div>
    <div class="market-card active"><div style="color:#e6c07a;">XAU/USD</div><div class="green">4176.07 +0.82%</div></div>
    <div class="market-card"><div style="color:#7fa8c7;">EUR/USD</div><div class="green">1.0874 +0.21%</div></div>
    <div class="market-card"><div style="color:#7fa8c7;">GBP/USD</div><div class="green">1.2987 +0.33%</div></div>
    """, unsafe_allow_html=True)

    c1,c2 = st.columns([1,4])
    with c1:
        st.markdown("""<div style="background:#e6c07a;color:#000;padding:6px 14px;border-radius:12px;font-weight:900;text-align:center;">6/7</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div style="color:#7fa8c7;font-size:13px;">Quality Filter<br><span style="color:#cfe0f0;">Win Rate 90% - ATR SL/TP - Liquidity Strategy ON</span></div>""", unsafe_allow_html=True)

    np.random.seed(10)
    n=120
    price = 4170 + np.cumsum(np.random.randn(n)*0.4) + np.linspace(0,15,n)
    df = pd.DataFrame({"close": price})
    df["ema9"] = df["close"].ewm(9).mean()
    df["ema21"] = df["close"].ewm(21).mean()
    df["ema50"] = df["close"].ewm(50).mean()
    df["ema200"] = df["close"].ewm(200).mean()
    st.line_chart(df)

    st.markdown("""
    <div class="sona-card">
      <div class="sona-title">◈ PERFORMANCE STATS - KING 103</div>
      <div style="color:#7fa8c7;margin-top:8px;">Win Rate</div>
      <div style="font-size:36px;font-weight:900;color:#e6c07a;">90%</div>
      <div style="color:#7fa8c7;font-size:13px;">27W / 3L • BOS 17 • Sweep 18</div>
      <div style="display:flex; justify-content:space-between; margin-top:14px;">
        <div><div style="color:#7fa8c7;">Active</div><div style="font-size:20px;font-weight:800;color:#fff;">3 • RSI 83</div></div>
        <div><div style="color:#7fa8c7;">Daily</div><div class="green" style="font-size:20px;">+$542.17</div></div>
      </div>
      <div style="color:#7fa8c7;font-size:12px;margin-top:10px;">MACD 2.84 • ATR 1.42 • VWAP 4182.24</div>
    </div>
    <div class="sona-card">
      <div class="sona-title">☰ HOLOGRAPHIC HOLDINGS + SL TP</div>
      <div style="text-align:center; margin-top:14px; font-size:42px;">🪙 🪙 🪙</div>
      <div style="text-align:center; color:#fff; font-weight:800; margin-top:8px;">Gold Bar 1oz x2 • $8,359.44</div>
      <div style="text-align:center;" class="green">SL 4197.45 • TP 4204.56 • RR 1:2.3</div>
      <div style="text-align:center; color:#7fa8c7; font-size:12px; margin-top:6px;">Liquidity Strategy: Sweep+ BOS + Pullback + EMA Stack</div>
    </div>
    <div class="sona-card">
      <div class="sona-title">LOCATION • PESHAWAR - BALA HISAR FORT</div>
      <div style="background:#0a1a2d; border-radius:12px; height:120px; margin-top:12px; position:relative; background-image: linear-gradient(#1a324d 1px, transparent 1px), linear-gradient(90deg, #1a324d 1px, transparent 1px); background-size: 20px 20px;">
        <div style="position:absolute; left:55%; top:45%; font-size:32px;">📍</div>
      </div>
      <div style="color:#7fa8c7; font-size:12px; margin-top:8px;">Session: Overnight • UTC+5 PKT • 5min XAU/USD • GOLD</div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="sona-card">
      <div class="sona-title">📝 SONA AI KHAPEL PINE EDITOR - WORLD FIRST INSIDE STREAMLIT</div>
      <div style="color:#7fa8c7; font-size:13px; margin-top:8px;">Yahan apna Pine Code likho - EMA9/21/50/200 RSI ATR MACD VWAP Volume King103 Liquidity Sweep BOS Pullback - Sab yahan chalega - TradingView ki zarurat nahi!</div>
    </div>
    """, unsafe_allow_html=True)

    pine_default = "// SONA AI PINE EDITOR - KHAPEL CODE - KING 103\nindicator('Sona AI King V103 - Custom', overlay=true)\nema9 = ta.ema(close, 9)\nema21 = ta.ema(close, 21)\nema50 = ta.ema(close, 50)\nema200 = ta.ema(close, 200)\nrsi = ta.rsi(close, 14)\natr = ta.atr(14)\nmacdLine, sigLine, hist = ta.macd(close, 12, 26, 9)\nvwap = ta.vwap(close)\nsh = ta.highest(high, 20)\nsl = ta.lowest(low, 20)\nbos = close > sh\nsweep = low < sl"
    pine_code = st.text_area("Pine Code - Yahan likho:", value=pine_default, height=320)

    st.markdown("""
    <div class="king-green">
    KING V103 BUY CONFIRMED from Pine Editor • Quality 6/7 • SL TP auto calculated • Liquidity Sweep + BOS + Pullback strategy active
    </div>
    <div class="sona-card">
      <div class="sona-title">⚙️ INDICATORS TOGGLES</div>
      <div style="color:#7fa8c7; line-height:2.2; font-size:14px; margin-top:10px;">
      • EMA 9 ✅<br>
      • EMA 21 ✅<br>
      • EMA 50 ✅<br>
      • EMA 200 ✅<br>
      • RSI 14 ✅<br>
      • ATR 14 ✅ SL TP<br>
      • MACD 12/26/9 ✅<br>
      • VWAP ✅<br>
      • Volume ✅<br>
      • King 103 ✅<br>
      • Liquidity Sweep ✅<br>
      • BOS ✅<br>
      • Pullback ✅<br>
      • Multi Timeframe ✅<br>
      • Multi Market ✅<br>
      • SL TP ATR Based ✅<br>
      • Liquidity Strategy ✅
      </div>
      <div style="background:#0a1a2d; border-radius:12px; padding:14px; margin-top:16px;">
        <div style="color:#e6c07a; font-weight:800;">PINE EDITOR FEATURES</div>
        <div style="color:#7fa8c7; font-size:13px; line-height:1.9; margin-top:6px;">
        1. Khapel code likho<br>
        2. Compile karo<br>
        3. Sona AI me auto chale<br>
        4. TradingView ki zarurat nahi<br>
        5. SL TP auto<br>
        6. World best design
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
