import pandas as pd
from datetime import date
DATE = str(date.today())

INPUT_DIR = "./DATA/INPUT/"
OUTPUT_DIR = "./DATA/OUTPUT/" + DATE

OUTPUT_FILENAME = ""

YAHOO_RECOM = True

MULTITHREADING = True
MULTITHREADING_POOL = OUTPUT_DIR + "/POOL/"
MULTITHREADING_NB_SPLIT_DF = 30
MULTITHREADING_NUM_THREADS = 5
MULTITHREADING_MIXED_COMPUTATION = False

COLAB = False
COLAB_OUTPUT_CRTS = "../drive/MyDrive/colab_results/CRTS/"
COLAB_OUTPUT_DIR = COLAB_OUTPUT_CRTS + DATE
COLAB_OUTPUT_FILENAME = ""


data = ["Strong Buy", "Buy", "Hold", "Under-perform", "Sell"]
DF_YAHOO_RECOMENDATTION = pd.DataFrame(data, columns=['recom_key'])
