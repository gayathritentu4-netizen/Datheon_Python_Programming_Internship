
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(
    page_title="Stock Portfolio Tracker",
    page_icon="📈",
    layout="wide"
)

# Load S&P 500 dataset
@st.cache_data
def load_data():
    data = pd.read_csv("constituents.csv")
    data["Symbol"] = data["Symbol"].astype(str).str.strip()
    return data

df = load_data()

st.title("📈 Stock Portfolio Performance Tracker")
st.write("Track your stock investments, market value and profit or loss.")

st.sidebar.header("About")
st.sidebar.write("S&P 500 Portfolio Tracker")
st.sidebar.write("Built using Python and Streamlit")

# Initialize portfolio
if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

# Select stock
st.header("Add Stock to Portfolio")

with st.form("stock_form"):
    ticker = st.selectbox(
        "Select Stock",
        sorted(df["Symbol"].unique())
    )

    company = df.loc[
        df["Symbol"] == ticker, "Security"
    ].iloc[0]

    st.write("Company:", company)

    buy_price = st.number_input(
        "Buy Price ($)",
        min_value=0.01,
        value=100.0,
        step=1.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1,
        step=1
    )

    submitted = st.form_submit_button("Add Stock")

    if submitted:
        yahoo_symbol = ticker.replace(".", "-")

        try:
            stock = yf.Ticker(yahoo_symbol)
            history = stock.history(period="5d")

            if history.empty or history["Close"].dropna().empty:
                st.error("Price unavailable. Please try again later.")
            else:
                current_price = float(
                    history["Close"].dropna().iloc[-1]
                )

                st.session_state.portfolio.append({
                    "Ticker": ticker,
                    "Company": company,
                    "Buy Price": float(buy_price),
                    "Quantity": int(quantity),
                    "Current Price": current_price
                })

                st.success(f"{ticker} added successfully!")

        except Exception as e:
            st.error(f"Could not retrieve stock price: {e}")

# Display portfolio
st.header("My Portfolio")

if st.session_state.portfolio:

    portfolio_df = pd.DataFrame(
        st.session_state.portfolio
    )

    portfolio_df["Investment"] = (
        portfolio_df["Buy Price"] *
        portfolio_df["Quantity"]
    )

    portfolio_df["Market Value"] = (
        portfolio_df["Current Price"] *
        portfolio_df["Quantity"]
    )

    portfolio_df["Profit/Loss"] = (
        portfolio_df["Market Value"] -
        portfolio_df["Investment"]
    )

    portfolio_df["Profit/Loss %"] = (
        portfolio_df["Profit/Loss"] /
        portfolio_df["Investment"] * 100
    )

    total_investment = portfolio_df["Investment"].sum()
    total_market_value = portfolio_df["Market Value"].sum()
    total_profit_loss = total_market_value - total_investment

    total_percentage = (
        total_profit_loss / total_investment * 100
        if total_investment else 0
    )

    # Portfolio metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Investment",
        f"${total_investment:,.2f}"
    )

    col2.metric(
        "Current Market Value",
        f"${total_market_value:,.2f}"
    )

    col3.metric(
        "Total Profit / Loss",
        f"${total_profit_loss:,.2f}",
        f"{total_percentage:.2f}%"
    )

    st.subheader("Individual Stock Performance")

    display_df = portfolio_df.copy().round(2)
    st.dataframe(display_df, use_container_width=True)

    st.subheader("Portfolio Investment Chart")

    st.bar_chart(
        portfolio_df.set_index("Ticker")[
            ["Investment", "Market Value"]
        ]
    )

    # Download CSV
    if st.button("Download Portfolio Report"):
        export_df = portfolio_df.copy()
        export_df["Date"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        csv_data = export_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Click to Download CSV",
            data=csv_data,
            file_name="portfolio_summary.csv",
            mime="text/csv"
        )

    if st.button("Clear Portfolio"):
        st.session_state.portfolio = []
        st.rerun()

else:
    st.info("Your portfolio is empty. Add a stock to get started.")

st.caption("Stock prices are based on the latest available daily closing data.")
st.caption("This application is for educational purposes, not financial advice.")
