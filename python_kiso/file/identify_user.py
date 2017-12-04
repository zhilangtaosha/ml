"""The script identifies username for crash log."""
import pandas as pd
import numpy as np
import sys
import math
import re
from datetime import datetime

MAX_CHECK_COUNT = 20


def is_username(s):
    """Check whether detail is username or not."""
    usernameReg = re.compile(r'^(.+)\\(.+)')
    return usernameReg.match(s) is not None


def create_allusers_dict(log_df):
    """Create dict with index and computer name."""
    d = dict({})
    for i, s in log_df.iterrows():
        d[i] = s.Computer
    return d


def create_crash_user_df(log_df):
    """Create the updated df and concat."""
    # Prepare dist data
    d = create_allusers_dict(log_df)
    # Prepare entries having crash log
    crash_index = log_df[log_df.iloc[:, 7].str.contains("OUTLOOK.EXE")].index

    username_index = None
    username_index_array = []
    for i in list(crash_index):
        crash_host = d[i]
        for count in range(1, MAX_CHECK_COUNT):

            if crash_host == d[i+(-1)*count]:
                if is_username(log_df.iloc[i+(-1)*count, ].Detail):
                    username_index = i+(-1)*count
                else:
                    continue

            elif crash_host == d[i+count]:
                username_index = i+count

            if username_index is not None:
                username_index_array.append(username_index)
                break

        if username_index is None:
            username_index = np.NaN
            username_index_array.append(username_index)

        username_index = None

    username_array = []
    for index in username_index_array:

        if math.isnan(index) or \
                is_username(log_df.iloc[index, ].Detail) is not True:
            username = "NOT FOUND"
        else:
            username = log_df.iloc[index, ].Detail

        username_array.append(username)

    username_df = pd.DataFrame(username_array, columns=["Username"])

    # Identify record of crash
    crash_log_df = log_df[log_df.iloc[:, 7].str.contains("OUTLOOK.EXE")]
    crash_log_df.reset_index(drop=True, inplace=True)

    update_log_df = pd.concat([crash_log_df, username_df], axis=1)

    return update_log_df

def main():
    """main."""
    args = sys.argv
    basename = datetime.now().strftime("%Y%m%d-%H%M%S")

    log_df = pd.read_csv(args[1])
    log_df.rename(columns={'Unnamed: 7': 'Detail'}, inplace=True)

    create_crash_user_df(log_df).to_csv('./crash_log_'+basename+'.csv')

if __name__ == '__main__': main()
