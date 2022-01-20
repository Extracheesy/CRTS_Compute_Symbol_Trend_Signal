from yahoo_fin import stock_info as si
import yfinance as yf
import datetime
import concurrent.futures
import uuid

import config

from tools import split_list_into_list
from merge import merge_csv_to_df

def use_yfinance_api(df):
    list_stocks = df.symbol.tolist()
    df = df.set_index('symbol')

    for stock in list_stocks:
        try:
            yf_stock = yf.Ticker(stock)
            df["T_r_Key"][stock] = yf_stock.info['recommendationKey']
            df["T_r_Mean"][stock] = yf_stock.info['recommendationMean']
            print("symbol: ", stock)
        except:
            print("no YahooF data symbol: ", stock)

    df.reset_index(inplace=True)

    # df["symbol"] = df.index
    # first_column = df.pop('symbol')
    # df.insert(0, 'symbol', first_column)
    # df.reset_index(drop=True, inplace=True)

    return df

def use_yfinance_multi_api(df):
    df = use_yfinance_api(df)
    filename = config.MULTITHREADING_POOL + str(uuid.uuid4()) + '_result.csv'
    df.to_csv(filename)

def use_yahoo_fin_api(df):
    return df

def use_yahoo_finance_scraping(df):
    return df

def get_yahoo_recommendation(df):
    df["T_r_Key"] = ""
    df["T_r_Mean"] = ""
    START_TIME = datetime.datetime.now().now()
    print("get YahooF recom")
    if config.MULTITHREADING == True:
        global_split_list = split_list_into_list(df)

        with concurrent.futures.ThreadPoolExecutor(max_workers=config.MULTITHREADING_NUM_THREADS) as executor:
            executor.map(use_yfinance_multi_api, global_split_list)

        df = merge_csv_to_df(config.MULTITHREADING_POOL, "*_result.csv")

    else:
        df = use_yfinance_api(df)

    print("runtime: ", datetime.datetime.now().now() - START_TIME)

    # df = use_yahoo_fin_api(df)

    return df




