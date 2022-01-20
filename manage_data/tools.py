import os, fnmatch
import pandas as pd
import config

def read_CSL_file(input_file):
    filename = config.INPUT_DIR + 'symbol_list_' + input_file + '.csv'
    if not os.path.exists(filename):
        print("no file: ", filename)
    else:
        df = pd.read_csv(filename)
        return df

def save_CRTS_output(df, filename):
    df.to_csv(filename)

def mk_directories():
    if not os.path.exists(config.OUTPUT_DIR):
        os.makedirs(config.OUTPUT_DIR)

    if (config.MULTITHREADING == True):
        if not os.path.exists(config.MULTITHREADING_POOL):
            os.makedirs(config.MULTITHREADING_POOL)
        else:
            for f in os.listdir(config.MULTITHREADING_POOL):
                os.remove(os.path.join(config.MULTITHREADING_POOL, f))

    if (config.COLAB == True):
        if not os.path.exists(config.COLAB_OUTPUT_CRTS):
            os.makedirs(config.COLAB_OUTPUT_CRTS)
        if not os.path.exists(config.COLAB_OUTPUT_DIR):
            os.makedirs(config.COLAB_OUTPUT_DIR)

def split_df(df, size_split):
    return df[:size_split], df[size_split:]

def split_list_into_list(df):
    # split a df into a list of breakdown df
    len_df = len(df)
    len_split_df = int(len_df / config.MULTITHREADING_NB_SPLIT_DF)

    rest_of_the_df = df.copy()
    global_split_list = []

    for i in range(config.MULTITHREADING_NB_SPLIT_DF):
        splited_df, rest_of_the_df = split_df(rest_of_the_df, len_split_df)
        global_split_list.append(splited_df)

    if len(rest_of_the_df) > 1:
        global_split_list.append(rest_of_the_df)

    return global_split_list


