import pandas as pd
from datetime import date
DATE = str(date.today())

INPUT_DIR = "./DATA/INPUT/"
OUTPUT_DIR = "./DATA/OUTPUT/" + DATE

OUTPUT_FILENAME = ""

YAHOO_RECOM = True
INVESTING_RECOM = True

MULTITHREADING = True
MULTITHREADING_POOL = OUTPUT_DIR + "/POOL/"
MULTITHREADING_NB_SPLIT_DF = 30
MULTITHREADING_NUM_THREADS = 10
MULTITHREADING_MIXED_COMPUTATION = True

COLAB = False
COLAB_OUTPUT_CRTS = "../drive/MyDrive/colab_results/CRTS/"
COLAB_OUTPUT_DIR = COLAB_OUTPUT_CRTS + DATE
COLAB_OUTPUT_FILENAME = ""


data = ["Strong Buy", "Buy", "Hold", "Under-perform", "Sell"]
DF_YAHOO_RECOMENDATTION = pd.DataFrame(data, columns=['recom_key'])

INTERVAL_FILTERS = {
    "1min": 60,
    "5mins": 60 * 5,
    "15mins": 60 * 15,
    "30mins": 60 * 30,
    "1hour": 60 * 60,
    "5hours": 60 * 60 * 5,
    "daily": 60 * 60 * 24,
    "weekly": "week",
    "monthly": "month",
}
