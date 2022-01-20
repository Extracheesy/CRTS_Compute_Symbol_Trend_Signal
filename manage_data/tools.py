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

