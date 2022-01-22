from tools import read_CSL_file
from tools import save_CRTS_output
from scrap_yahoo import get_yahoo_recommendation
from scrap_investing import get_investing_recommendation

import config

def get_df(input_file):
    config.OUTPUT_FILENAME = config.OUTPUT_DIR + "/recom_df_" + input_file + ".csv"
    if (config.COLAB == True):
        config.COLAB_OUTPUT_FILENAME = config.COLAB_OUTPUT_DIR + "/recom_df_" + input_file + ".csv"

    df = read_CSL_file(input_file)
    return df

def save_df(df):
    save_CRTS_output(df, config.OUTPUT_FILENAME)
    if (config.COLAB == True):
        save_CRTS_output(df, config.COLAB_OUTPUT_FILENAME)

def add_market_recom(df):
    if (config.INVESTING_RECOM == True):
        df = get_investing_recommendation(df)
    if(config.YAHOO_RECOM == True):
        df = get_yahoo_recommendation(df)

    save_df(df)

    return df