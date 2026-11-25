
import yfinance as yf

stock = yf.Ticker("AAPL")

info = stock.info

print("Company:", info.get("longName"))
print("Ticker:", info.get("symbol"))
print("Industry:", info.get("industry"))
print("P/E Ratio:", info.get("trailingPE"))

print("\nAnnual Net Income:")
print(stock.income_stmt.loc["Net Income"])
