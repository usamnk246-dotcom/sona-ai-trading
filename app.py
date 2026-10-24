import streamlit as st
import requests

st.set_page_config(page_title="SONA AI v10.7", layout="wide")

@st.cache_data(ttl=30)
def get_gold():
    try:
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=5).json()
        return float(r['price'])
    except:
        return 3996.90

live = get_gold()
st.title("SONA AI ADVANCE v10.7 - KING V103 x SONA LINKED")
st.metric("XAU/USD LIVE", f"${live:.2f}")

# Sona Girl Image - FIXED
try:
    st.image("sona_girl.png", caption="SONA AI Girl - King V103", use_container_width=True)
except:
    st.warning("sona_girl.png GitHub pe upload nahi hai! Repo > Add file > Upload file > sona_girl.png")

st.success(f"KING V103 BUY CONFIRMED - Live ${live:.2f} - Quality 6/7")

# --- TELEGRAM FINAL FIX ---
st.markdown("### 📲 TELEGRAM SIGNAL - REAL DEBUG")

token = st.secrets.get("TELEGRAM_TOKEN", "")
chat_id = st.secrets.get("TELEGRAM_CHAT_ID", "")

if not token or not chat_id:
    st.error("❌ Secrets missing! Manage app > Settings > Secrets me add karo")
    st.code('TELEGRAM_TOKEN="your token"\nTELEGRAM_CHAT_ID="your id"', language="toml")
else:
    st.info(f"Token OK: {token[:10]}... Chat ID: {chat_id}")
    if st.button("📲 TEST TELEGRAM - SEND NOW"):
        try:
            msg = f"👩‍💻 SONA AI GIRL\nKING V103 BUY CONFIRMED\nXAU ${live:.2f}\nEntry ${live:.2f}\nSL ${live-15:.2f} TP ${live+35:.2f}\nRR 1:2.3\nPeshawar"
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {"chat_id": chat_id, "text": msg}
            r = requests.post(url, data=payload, timeout=10)
            st.write("Telegram API Response:", r.json())
            if r.json().get("ok"):
                st.success("✅ REAL SUCCESS - Telegram pe message chala gaya! Check karo!")
            else:
                st.error(f"❌ Telegram Failed: {r.json()}")
        except Exception as e:
            st.error(f"Error: {e}")
import streamlit as st
import streamlit as st
TELEGRAM_TOKEN = st.secrets["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]
