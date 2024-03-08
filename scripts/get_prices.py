import pandas as pd 
import yfinance as yf
import os
import sys


sys.path.append(os.path.abspath('../classes'))

from tickers import Tickers

def get_prices(tikers_list, start_date, end_date):

    prices = pd.DataFrame(yf.download(tikers_list, start= start_date, end= end_date))

    return prices

if __name__ == '__main__':

    tickers_list = Tickers.IBOV
    start_date = '2015-01-01'
    end_date = '2024-01-01'
    get_prices(tickers_list, start_date, end_date)