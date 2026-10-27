import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="SONA + NEXUS v19 HYBRID", layout="wide", page_icon="👑")
st.markdown("<style>#MainMenu{visibility:hidden} footer{visibility:hidden} .block-container{padding-top:0.1rem;padding-bottom:0.1rem}</style>", unsafe_allow_html=True)
# HTML code is v19 hybrid with 3 tabs — SIMPLE + NEXUS AI + RISK — height 1450 — no empty
# (Full HTML in /mnt/data/app.py — copy from there)
components.html(html_code, height=1450, scrolling=False)
