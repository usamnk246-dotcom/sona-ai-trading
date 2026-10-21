import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sona AI Advance - KING V103.5", layout="wide", page_icon="👑")

# === STYLE - PREMIUM GOLD ===
st.markdown("""
<style>
body {background:#060A14;}
.card {background:linear-gradient(180deg, #111A2A 0%, #0A1220 100%); border:1px solid #D4AF37; border-radius:16px; padding:14px; margin-bottom:10px;}
.gold {color:#FFD700; font-weight:900;}
.green {color:#00FF88;}
.red {color:#FF4D4D;}
.stApp {background:#060A14;}
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("""
<div style="background:#0A0E1A; border:1px solid #FFD700; border-radius:12px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
<div style="display:flex; gap:12px; align-items:center;">
<div style="width:56px; height:56px; background:linear-gradient(135deg, #FFD700, #B8860B); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:28px;">⬡</div>
<div><div style="color:#FFD700; font-size:22px; font-weight:900;">SONA AI ADVANCE</div><div style="color:#8AA0B8; font-size:10px;">KING V103.5 x SONA AI LINKED • 5m • XAU/USD GOLD</div></div>
</div>
<div style="text-align:right;"><div style="color:#00FF88; font-weight:800;">LIVE AI MODE ACTIVE</div><div style="color:#8AA0B8; font-size:11px;">PESHAWAR • 03:42 AM PKT • SONA AI v10.3</div><div style="color:#FFD700; font-size:10px;">RISK LOW • LEVERAGE 1:100 • BALANCE SECURED</div></div>
</div>
""", unsafe_allow_html=True)

# === FAKE LIVE DATA - Replace with TradingView API later ===
np.random.seed(42)
dates = pd.date_range("2026-10-20 22:00", "2026-10-21 10:30", freq="5min")
price = 4160 + np.cumsum(np.random.randn(len(dates))*0.8)
df = pd.DataFrame({"time": dates, "close": price, "high": price+np.random.rand(len(dates))*2, "low": price-np.random.rand(len(dates))*2, "open": price-np.random.randn(len(dates))*0.3, "volume": np.random.randint(1000,5000,len(dates))})

# === KING V103.5 LOGIC - PYTHON VERSION OF YOUR PINE ===
def ema(s, n): return s.ewm(span=n, adjust=False).mean()
def rsi_calc(s, n=14):
    delta = s.diff()
    gain = delta.where(delta>0, 0).ewm(alpha=1/n, adjust=False).mean()
    loss = -delta.where(delta<0, 0).ewm(alpha=1/n, adjust=False).mean()
    rs = gain/loss
    return 100 - (100/(1+rs))

df["ema9"] = ema(df["close"], 9)
df["ema21"] = ema(df["close"], 21)
df["ema50"] = ema(df["close"], 50)
df["ema200"] = ema(df["close"], 200)
df["vwap"] = (df["close"]*df["volume"]).cumsum() / df["volume"].cumsum()
df["rsi"] = rsi_calc(df["close"], 14)
df["sh"] = df["high"].rolling(10).max()
df["sl"] = df["low"].rolling(10).min()

df["bosBull"] = df["close"] > df["sh"].shift(1)
df["bosBear"] = df["close"] < df["sl"].shift(1)
df["sweepBull"] = (df["low"] < df["sl"]) & (df["close"] > df["sl"])
df["sweepBear"] = (df["high"] > df["sh"]) & (df["close"] < df["sh"])

df["soniBuy"] = (df["close"] > df["ema50"]) & (df["rsi"] > 35)
df["sonaBuy"] = (df["close"] > df["ema50"]) & (df["rsi"] < 60)
df["soniSell"] = (df["close"] < df["ema50"]) & (df["rsi"] > 68)
df["sonaSell"] = (df["close"] < df["ema50"]) & (df["rsi"] > 70)
df["v103Buy"] = (df["close"] > df["ema21"]) & (df["close"] > df["ema50"]) & (df["rsi"] > 40)
df["v103Sell"] = (df["close"] < df["ema21"]) & (df["close"] < df["ema50"])
df["scalpBuy"] = (df["ema9"] > df["ema21"]) & (df["ema9"].shift(1) <= df["ema21"].shift(1))
df["scalpSell"] = (df["ema9"] < df["ema21"]) & (df["ema9"].shift(1) >= df["ema21"].shift(1))

# Quality Score 0-7 - YOUR LOGIC
df["q"] = 0
df["q"] += (df["ema9"] > df["ema21"]).astype(int)
df["q"] += ((df["rsi"]>40) & (df["rsi"]<70)).astype(int)
df["q"] += (df["close"] > df["ema50"]).astype(int)
df["q"] += (df["close"] > df["ema200"]).astype(int)
df["q"] += (df["close"] > df["vwap"]).astype(int)
df["q"] += (df["ema21"] > df["ema50"]).astype(int)
df["q"] += df["bosBull"].astype(int)
df["q"] = df["q"].clip(upper=7)
df["highQ"] = df["q"] >= 6

last = df.iloc[-1]
price_now = 4182.23 # from your screenshot
# === LAYOUT ===
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown(f"""
    <div class="card">
    <div style="color:#8AA0B8; font-size:12px; font-weight:700;">ACCOUNT GROWTH</div>
    <div style="background:#000; border:1px solid #FFD700; border-radius:12px; padding:12px; margin-top:8px;">
    <div style="color:#8AA0B8; font-size:11px;">REAL ACCOUNT</div>
    <div style="color:#FFD700; font-size:34px; font-weight:900;">$10.00</div>
    <div class="green">+0.00% (24h)</div>
    <div style="color:white; font-size:12px; margin-top:6px;">Real Account <span class="green">+4.32% ↗</span></div>
    </div>
    <div style="margin-top:12px;">
    <div style="color:#8AA0B8; font-size:11px;">Starting Balance $10</div>
    <div style="color:#8AA0B8; font-size:11px;">Initial 5 days ago</div>
    <div style="color:white; font-size:12px; margin-top:8px;">Goal $1000 Target <span style="float:right; color:#FFD700;">1.0%</span></div>
    <div style="height:8px; background:#222; border-radius:6px; margin-top:4px;"><div style="width:10%; height:8px; background:linear-gradient(90deg, #FFD700, #FFF); border-radius:6px;"></div></div>
    <div style="font-size:10px; color:#8AA0B8;">1.0% • $10 / $1000 • Days Active: 5 • Daily Target: +$198.00</div>
    </div>
    <div style="margin-top:10px; border:1px solid #FFD700; border-radius:8px; padding:8px; font-size:11px;"><span style="color:#FFD700;">KING V103 x SONA LINKED •</span> <span class="green">● Selected</span></div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
    <div style="display:flex; justify-content:space-between;">
    <div><div style="color:#FFD700; font-size:11px;">GOLD XAUUSD • XAU/USD GOLD</div><div style="color:#FFD700; font-size:26px; font-weight:900;">GOLD XAUUSD</div><div class="green" style="font-size:14px;">XAUUSD {price_now} +14.21 (+0.34%) • LIVE 5m</div></div>
    <div style="color:#FFD700; font-size:10px;">KING V103 4/HR BOTH<br>KING V103 x SONA AI LINKED</div>
    </div>
    <div style="display:flex; gap:6px; margin-top:10px;">
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">1min</div>
    <div style="background:#FFD700; color:black; padding:5px 10px; border-radius:8px; font-size:11px; font-weight:800;">5min</div>
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">15min</div>
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">30min</div>
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">1H</div>
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">4H</div>
    <div style="background:#222; color:white; padding:5px 10px; border-radius:8px; font-size:11px;">1D</div>
    </div>
    <div style="margin-top:8px; display:flex; gap:6px; font-size:10px; color:#8AA0B8;">
    <div>Market: <span style="background:#FFD700; color:black; padding:2px 8px; border-radius:6px;">XAU/USD • GOLD</span></div>
    </div>
    <div style="margin-top:8px; display:grid; grid-template-columns: repeat(4,1fr); gap:6px; font-size:10px; color:white;">
    <div style="background:#111; border-radius:6px; padding:6px;">BTC/USDT<br><span class="green">67432.18 +2.34%</span></div>
    <div style="background:#111; border-radius:6px; padding:6px;">XAU/USD<br><span class="green">4176.07 +0.82%</span></div>
    <div style="background:#111; border-radius:6px; padding:6px;">EUR/USD<br><span class="green">1.0874 +0.21%</span></div>
    <div style="background:#111; border-radius:6px; padding:6px;">GBP/USD<br><span class="green">1.2987 +0.33%</span></div>
    </div>
    <div style="margin-top:8px; display:flex; gap:12px; font-size:11px; color:white;"><div>Automatic Trading <span style="background:#FFD700; color:black; border-radius:12px; padding:2px 8px;">● ON</span></div><div>Quality Filter Score Minimum <span style="background:#FFD700; color:black; border-radius:6px; padding:2px 6px;">{int(last['q'])}/7</span></div><div>Win Rate 90%</div></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chart
    st.line_chart(df.set_index("time")[["close","ema9","ema21","ema50","ema200"]].tail(100))
    
    signal_text = ""
    if last["sonaBuy"] and last["highQ"]:
        signal_text = f"SONA AI BUY - Quality {int(last['q'])}/7 @ {price_now} - V103 BUY"
    if last["scalpSell"] and last["highQ"]:
        signal_text = f"SCALP SELL - Quality {int(last['q'])}/7 @ {price_now}"
    
    if last["highQ"] and (last["sonaBuy"] or last["soniBuy"] or last["v103Buy"]):
        st.markdown(f"""
        <div style="background:linear-gradient(90deg, #FFD700, #FFB700); color:black; border-radius:10px; padding:12px; font-weight:800; text-align:center;">
        BUY SIGNAL CONFIRMED {int(last['q'])}/7 • GOLD XAUUSD @{price_now} • KING 103 WAR<br>
        TP 4213.25 • SL 4171.62 • 5 min • SONA AI BUY + V103 BUY
        </div>
        """, unsafe_allow_html=True)
    if last["scalpSell"] and last["highQ"]:
        st.markdown(f"""
        <div style="background:#FF4D4D; color:white; border-radius:10px; padding:12px; font-weight:800; text-align:center;">
        SCALP SELL - Quality {int(last['q'])}/7 • GOLD XAUUSD @{price_now} • 4182.23 - 03:23
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <div style="color:#FFD700; font-size:12px; font-weight:700;">PERFORMANCE STATS</div>
    <div style="margin-top:8px; font-size:12px; color:white;">
    <div>Win Rate <div style="font-size:22px; color:#FFD700; font-weight:900;">90%</div>27W / 3L</div>
    <div style="display:flex; justify-content:space-between; margin-top:8px;"><div>Active Trades<br><b>3</b></div><div>Daily Profit<br><b class="green">+$542.17 ↗</b></div></div>
    <div style="margin-top:8px;">Autotrader Status:<br><span class="green">● Running</span></div>
    <div style="margin-top:8px;">Last Alert<br><span class="red">SELL • 4185.50 • Quality 6/7</span></div>
    </div>
    </div>
    <div class="card">
    <div style="color:#FFD700; font-size:12px; font-weight:700;">HOLOGRAPHIC HOLDINGS</div>
    <div style="text-align:center; font-size:40px; margin-top:8px;">🏆</div>
    <div style="text-align:center; font-size:11px; color:#FFD700;">Gold Bar 1oz x2 • 4182.23 oz • Secured<br>Total Holdings Value: $8,359.44</div>
    <div style="margin-top:10px; background:#111; border-radius:8px; padding:8px; font-size:10px; color:#8AA0B8;">LOCATION • PESHAWAR<br>Bala Hisar Fort<br>Session: Overnight • UTC+5 PKT</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"<div style='text-align:center; color:#8AA0B8; font-size:10px; margin-top:10px;'>SONA AI v10.3 • Q Score {int(last['q'])}/7 • EMA9 {last['ema9']:.2f} EMA21 {last['ema21']:.2f} EMA50 {last['ema50']:.2f} EMA200 {last['ema200']:.2f} VWAP {last['vwap']:.2f} RSI {last['rsi']:.1f} • BOS {bool(last['bosBull'])} Sweep {bool(last['sweepBull'])}</div>", unsafe_allow_html=True)
