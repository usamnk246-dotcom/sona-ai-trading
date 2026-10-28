import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(
    page_title="SONA AI Trading Lab",
    page_icon="🔥",
    layout="wide"
)

# Initialize application state
if "balance" not in st.session_state:
    st.session_state.balance = 3000.0

if "starting_balance" not in st.session_state:
    st.session_state.starting_balance = 3000.0

if "history" not in st.session_state:
    st.session_state.history = []

if "price" not in st.session_state:
    st.session_state.price = 67234.56

if "prices" not in st.session_state:
    st.session_state.prices = [67234.56]

if "paused" not in st.session_state:
    st.session_state.paused = True


# Application styling
st.markdown("""
<style>
.stApp {
    background-color: #070b0a;
    color: #f4fff7;
}

[data-testid="stMetric"] {
    background: #101a15;
    border: 1px solid #1d5a36;
    padding: 14px;
    border-radius: 12px;
}

div.stButton > button {
    border-radius: 9px;
    font-weight: 700;
}

.notice {
    background: #2a2108;
    border: 1px solid #c99b24;
    padding: 12px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# Main dashboard
st.title("🔥 SONA AI — Advanced Trading Lab")

st.caption(
    "Paper Trading | Risk Management | Trade Journal | CSV Export"
)

st.markdown("""
<div class="notice">
<b>SIMULATION MODE:</b>
This application uses simulated prices and trade results.
It does not connect to a live exchange or broker.
Displayed profits are not real money.
</div>
""", unsafe_allow_html=True)


# Sidebar settings
with st.sidebar:
    st.header("⚙️ Trading Settings")

    starting_balance = st.number_input(
        "Starting Balance (PKR)",
        min_value=500.0,
        max_value=1000000.0,
        value=float(st.session_state.starting_balance),
        step=500.0
    )

    stake = st.number_input(
        "Stake per Trade (PKR)",
        min_value=10.0,
        max_value=100000.0,
        value=250.0,
        step=50.0
    )

    payout_pct = st.slider(
        "Winning Return (%)",
        1, 100, 70
    )

    loss_pct = st.slider(
        "Loss on Stake (%)",
        1, 100, 100
    )

    win_probability = st.slider(
        "Assumed Win Probability (%)",
        1, 99, 50
    )

    max_trades = st.number_input(
        "Maximum Trades per Session",
        min_value=1,
        max_value=500,
        value=20
    )

    stop_loss = st.number_input(
        "Session Stop-Loss (PKR)",
        min_value=0.0,
        max_value=1000000.0,
        value=500.0,
        step=100.0
    )

    if st.button("Reset Session", use_container_width=True):
        st.session_state.balance = float(starting_balance)
        st.session_state.starting_balance = float(starting_balance)
        st.session_state.history = []
        st.session_state.price = 67234.56
        st.session_state.prices = [67234.56]
        st.session_state.paused = True
        st.rerun()

    st.divider()

    st.session_state.paused = st.toggle(
        "Pause Trading",
        value=st.session_state.paused
    )

    st.caption("All trades are simulated.")


# Simulated price movement
st.session_state.price *= (
    1 + random.uniform(-0.0018, 0.0018)
)

st.session_state.prices.append(
    st.session_state.price
)

st.session_state.prices = (
    st.session_state.prices[-60:]
)


# Calculate statistics
balance = float(st.session_state.balance)

net_pnl = (
    balance - float(st.session_state.starting_balance)
)

history = st.session_state.history

wins = sum(
    1 for trade in history
    if trade["Result"] == "WIN"
)

losses = sum(
    1 for trade in history
    if trade["Result"] == "LOSS"
)

win_rate = (
    wins / len(history) * 100
    if history else 0
)


# Dashboard metrics
m1, m2, m3, m4 = st.columns(4)

m1.metric(
    "Paper Balance",
    f"₨{balance:,.0f}"
)

m2.metric(
    "Session P/L",
    f"₨{net_pnl:+,.0f}"
)

m3.metric(
    "Total Trades",
    len(history),
    f"{wins} Wins / {losses} Losses"
)

m4.metric(
    "Win Rate",
    f"{win_rate:.1f}%" if history else "—"
)


# Charts
left, right = st.columns([1.15, 1])

with left:
    st.subheader("📈 Simulated Price Monitor")

    st.metric(
        "SIMULATED BTC/USD",
        f"${st.session_state.price:,.2f}"
    )

    st.line_chart(
        pd.DataFrame({
            "Simulated BTC/USD": st.session_state.prices
        }),
        height=230
    )

    st.caption(
        "Synthetic price movement. This is not live market data."
    )


with right:
    st.subheader("🛡️ Risk Management")

    st.write(f"**Stake:** ₨{stake:,.0f}")

    st.write(
        f"**Potential Simulated Win:** "
        f"+₨{stake * payout_pct / 100:,.0f}"
    )

    st.write(
        f"**Potential Simulated Loss:** "
        f"−₨{stake * loss_pct / 100:,.0f}"
    )

    st.write(
        f"**Assumed Win Probability:** "
        f"{win_probability}%"
    )

    expected_value = (
        (win_probability / 100)
        * (stake * payout_pct / 100)
        -
        ((100 - win_probability) / 100)
        * (stake * loss_pct / 100)
    )

    st.write(
        f"**Modelled Expected Value:** "
        f"₨{expected_value:+,.2f}"
    )

    st.caption(
        "This calculation uses your assumptions. "
        "It is not a prediction of actual trading results."
    )


# Paper trading
st.divider()

st.subheader("🎮 Paper Trading")

trades_remaining = (
    int(max_trades) - len(history)
)

session_loss = max(
    0.0,
    float(st.session_state.starting_balance) - balance
)

stop_triggered = (
    stop_loss > 0 and session_loss >= stop_loss
)


if stop_triggered:

    st.error(
        "Session stop-loss reached. "
        "Reset the session to start again."
    )

elif trades_remaining <= 0:

    st.warning(
        "Session trade limit reached."
    )

elif st.session_state.paused:

    st.info(
        "Trading is paused. Turn off Pause Trading "
        "in the sidebar to enable simulated trades."
    )

else:

    st.caption(
        f"{trades_remaining} simulated trades remaining."
    )

    direction = st.radio(
        "Practice Direction",
        ["BUY / LONG", "SELL / SHORT"],
        horizontal=True
    )

    if st.button(
        "Run One Simulated Trade",
        type="primary",
        use_container_width=True
    ):

        if stake > balance:

            st.error(
                "Your stake exceeds the current paper balance."
            )

        else:

            is_win = (
                random.random()
                < (win_probability / 100)
            )

            if is_win:
                pnl = stake * payout_pct / 100
                result = "WIN"
            else:
                pnl = -(stake * loss_pct / 100)
                result = "LOSS"

            st.session_state.balance = (
                balance + pnl
            )

            trade = {
                "Time": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Direction": direction,
                "Stake (PKR)": round(stake, 2),
                "Result": result,
                "P/L (PKR)": round(pnl, 2),
                "Balance (PKR)": round(
                    st.session_state.balance, 2
                ),
                "Mode": "SIMULATION"
            }

            st.session_state.history.insert(
                0, trade
            )

            st.rerun()


# Trade history
st.divider()

st.subheader("📚 Trade Journal")

if history:

    df = pd.DataFrame(history)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv_data = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇️ Export Journal as CSV",
        data=csv_data,
        file_name="sona_paper_trade_history.csv",
        mime="text/csv"
    )

    st.bar_chart(
        df.iloc[::-1].set_index("Time")["P/L (PKR)"],
        height=180
    )

else:

    st.info(
        "No trades yet. Unpause the simulator "
        "and run a practice trade to create history."
    )


# Footer
st.caption(
    "SONA AI Trading Lab | Educational Simulator | "
    "No live prices, broker connection, or validated AI predictions."
)
