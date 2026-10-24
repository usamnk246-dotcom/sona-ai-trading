import streamlit as st
import requests

# --- SECRETS ---
TOKEN = st.secrets["TELEGRAM_TOKEN"].strip()
CHAT_ID = str(st.secrets["TELEGRAM_CHAT_ID"]).strip()

st.write(f"Token OK: {TOKEN[:10]}... Chat ID: {CHAT_ID}")

def send_telegram_signal(message):
    try:
        # chat_id ko int me convert karna zaroori hai
        chat_id_int = int(CHAT_ID)
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {
            "chat_id": chat_id_int,
            "text": message,
            "parse_mode": "HTML"
        }
        r = requests.post(url, json=payload, timeout=15)
        return r.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}

# --- TEST BUTTON ---
if st.button("📱 TEST TELEGRAM - SEND NOW"):
    result = send_telegram_signal("✅ FINAL TEST OK - Sona King V103")
    st.json(result)
    if result.get("ok"):
        st.success("Telegram Success!")
    else:
        st.error(f"Telegram Failed: {result}")

# --- Tumhara baqi King V103 ka code yahan neeche rahega ---
