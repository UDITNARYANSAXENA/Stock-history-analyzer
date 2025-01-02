import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date, timedelta
import streamlit as st

today = date.today()
end_date = today.strftime("%Y-%m-%d")
start_date = (today - timedelta(days=360)).strftime("%Y-%m-%d")

st.title("NSE Stock Price Viewer")
st.markdown("Enter a company's name or ticker (without `.NS` or `.BO`).")

a = st.text_input("Enter Company Name or Ticker Symbol (e.g., RELIANCE):")

if a:
    ticker = f"{a.strip().upper()}.NS"

    try:
        st.write(f"Fetching data for {ticker} from {start_date} to {end_date}...")
        data = yf.download(ticker, start=start_date, end=end_date)

        if not data.empty:
            fig, ax = plt.subplots(figsize=(12, 8))
            ax.plot(data.index, data["Close"], label="Close Price", color="blue")
            ax.set_title(f"{a.upper()} Stock Prices", fontsize=20)
            ax.set_xlabel("Date", fontsize=14)
            ax.set_ylabel("Price (INR)", fontsize=14)
            ax.legend()
            ax.grid()

            st.pyplot(fig)
        else:
            st.error("No data found for the provided company. Please check the name or symbol and try again.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a company name or ticker symbol to view stock prices.")
