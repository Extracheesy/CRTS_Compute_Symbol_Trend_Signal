import sys
from df_manager import get_df
from df_manager import add_market_recom
from tools import mk_directories
import config

"""
    CRTS module: Compute Recommendation Trend Signals
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mk_directories()

    input_file = str(sys.argv[1])
    input_file = input_file[2:]

    df = get_df(input_file)
    df = add_market_recom(df)


    print_hi('PyCharm')

