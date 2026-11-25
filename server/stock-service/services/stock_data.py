
import yfinance as yf


def get_company_info(ticker):
    ticker = ticker.strip().upper()

    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "ticker": ticker,
        "companyName": info.get("longName"),
        "industry": info.get("industry"),
        "peRatio": info.get("trailingPE")
    }
