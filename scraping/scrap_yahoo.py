from yahoo_fin import stock_info as si
import yfinance as yf
import datetime
import concurrent.futures
import uuid

from bs4 import BeautifulSoup
import requests
import re

import config

from tools import split_list_into_list
from merge import merge_csv_to_df

def use_yfinance_mixed(df):
    list_stocks = df.symbol.tolist()
    df = df.set_index('symbol')

    for stock in list_stocks:
        try:
            yf_stock = yf.Ticker(stock)
            df["T_r_Key"][stock] = yf_stock.info['recommendationKey']
            df["T_r_Mean"][stock] = yf_stock.info['recommendationMean']
            print("symbol Yfinance: ", stock)
        except:
            try:
                url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'
                print(url)
                page = requests.get(url)

                soup = BeautifulSoup(page.text, 'lxml')
                html_text = soup.text

                match = re.findall(r'Rating...1StrongBuy', html_text)
                string = match[0]
                string = string[6:10]

                Y_recom = float(string)
                df["T_r_Mean"][stock] = Y_recom
                df["T_r_Key"][stock] = config.DF_YAHOO_RECOMENDATTION['recom_key'][int(Y_recom)-1]

                print("symbol requests: ", stock)
            except:
                try:
                    quote_data = si.get_quote_data(stock)
                    yahoo_recommendation = quote_data['averageAnalystRating']
                    yahoo_recommendation_split = yahoo_recommendation.split(" - ")
                    df["T_r_Mean"][stock] = yahoo_recommendation_split[0]
                    df["T_r_Key"][stock] = yahoo_recommendation_split[1]

                    print("symbol Y_fin: ", stock)
                except:
                    print("symbol failure: ", stock)

    df.reset_index(inplace=True)

    return df

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

    return df

def use_yahoo_fin_api(df):
    list_stocks = df.symbol.tolist()
    df = df.set_index('symbol')

    for stock in list_stocks:
        try:
            quote_data = si.get_quote_data(stock)
            yahoo_recommendation = quote_data['averageAnalystRating']
            yahoo_recommendation_split = yahoo_recommendation.split(" - ")
            df["T_r_Mean"][stock] = yahoo_recommendation_split[0]
            df["T_r_Key"][stock] = yahoo_recommendation_split[1]

            print("symbol Y_fin: ", stock)
        except:
            print("no Y_finF data symbol: ", stock)

    df.reset_index(inplace=True)

    return df

def use_yfinance_scraping(df):
    url = 'https://google.com'
    page = requests.get(url)

    list_stocks = df.symbol.tolist()
    df = df.set_index('symbol')

    for stock in list_stocks:
        #stock = "AAPL"
        try:
            url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock + '&.tsrc=fin-srch'
            print(url)
            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'lxml')
            html_text = soup.text

            match = re.findall(r'Rating...1StrongBuy', html_text)
            string = match[0]
            string = string[6:10]

            Y_recom = float(string)
            df["T_r_Mean"][stock] = Y_recom
            df["T_r_Key"][stock] = config.DF_YAHOO_RECOMENDATTION['recom_key'][int(Y_recom)-1]

            print("symbol requests: ", stock)
        except:
            print("no requests data symbol: ", stock)

    df.reset_index(inplace=True)

    # df["symbol"] = df.index
    # first_column = df.pop('symbol')
    # df.insert(0, 'symbol', first_column)
    # df.reset_index(drop=True, inplace=True)

    return df

def use_yfinance_multi_api(df):
    # df = use_yfinance_api(df)
    df = use_yfinance_mixed(df)
    filename = config.MULTITHREADING_POOL + str(uuid.uuid4()) + '_result.csv'
    df.to_csv(filename)


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
        df = use_yfinance_mixed(df)
        df = use_yahoo_fin_api(df)
        df = use_yfinance_api(df)
        df = use_yfinance_scraping(df)


    print("runtime: ", datetime.datetime.now().now() - START_TIME)

    # df = use_yahoo_fin_api(df)

    return df




