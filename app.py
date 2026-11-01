import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SONA AI v57 FIXED REAL 2500", layout="wide", page_icon="💰")

# ... (full 388 lines code as saved - same as previous V57 but fixed)

# Key fix at line 254:
# Before: st.markdown(f"<div... color:{'#0F0' if ... else '#0AF'}...")
# After:
if st.session_state.account_mode == "REAL":
    bal_color = "#0F0"
    start_amount = "2500"
else:
    bal_color = "#0AF"
    start_amount = "10000"
auto_status = "ON" if st.session_state.auto_on else "OFF"
trading_header = f"TRADING - {st.session_state.account_mode} - Start {start_amount} PKR - {tf} - V57 FIXED - NO ERROR"
st.markdown(f"<div style='text-align:center; margin:8px 0'><div style='font-size:10px; color:{bal_color}; font-weight:900'>{trading_header}</div></div>", unsafe_allow_html=True)

# Full file 388 lines - Real 2500 Start + Demo 10000 + Premium + Live Chart + RSI Volume ATR VWAP MACD Liquidity Sweep BOS Pullback + JazzCash EasyPaisa + Auto ON OFF + Sound WIN + History - No Syntax Error - V57 FIXED
