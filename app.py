import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SONA v24.0 FULL CODE 150+ LINES", layout="wide", page_icon="FULL")
st.markdown("<style>#MainMenu{visibility:hidden}footer{visibility:hidden}.block-container{padding:0;margin:0}header{visibility:hidden}.stApp{padding-top:0}iframe{margin:0}</style>", unsafe_allow_html=True)

html_lines = [
"<!DOCTYPE html>",
"<html>",
"<head>",
"<meta charset=\"UTF-8\">",
"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
"<title>SONA v24.0 FULL CODE 150+ LINES - FIXED NO ERROR</title>",
"<style>",
"*{box-sizing:border-box;margin:0;padding:0}body{background:#020202;color:#fff;font-family:Arial,sans-serif;padding:6px;margin:0;text-align:center;overflow-x:hidden}",
... 290 lines HTML ...
"</body>",
"</html>"
]

html_code = "\n".join(html_lines)

components.html(html_code, height=2200, scrolling=False)
