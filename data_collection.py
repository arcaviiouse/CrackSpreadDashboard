import yfinance as yf

def fetch_price_data(ticker, start_date, end_date):
    """
    Fetches historical price data from Yahoo Finance.
    :param ticker: str, ticker symbol
    :param start_date: str, start date in 'YYYY-MM-DD' format
    :param end_date: str, end date in 'YYYY-MM-DD' format
    :return: pandas Series of closing prices
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Close']

