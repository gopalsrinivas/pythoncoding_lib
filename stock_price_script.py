import yfinance as yf

# Input for stock ticker
STK = input("Enter Share name:").upper()

# Get the stock data for a valid period (e.g., '1d' for 1 day)
data = yf.Ticker(STK).history(period="1d")

# Check if the data is not empty
if not data.empty:
    # Get the last market price (the most recent close)
    last_market_price = data["Close"].iloc[-1]
    print(f"Last market price of {STK}: {last_market_price}")
else:
    print(f"No data available for {STK}. Please check the stock symbol.")
