import os
import sys
import time
import psutil
import pandas as pd
import numpy  as np
import datetime
from email_validator import validate_email, EmailNotValidError
from tqdm import tqdm
import concurrent.futures
import multiprocessing as mp

# read the pickled pandas DataFrame from file
df = pd.read_pickle('nevalid_site_4.pkl')

# filter out any rows where the 'email' column is less than 5 characters long
df = df[df['email'].map(len) > 4].copy()

def check(email):
    try:
        # validate the email address using the email_validator library
        valid = validate_email(email)
        # if validation is successful, return 'Valid'
        return 'Valid'
    except:
        # if validation fails, return 'Not_valid'
        return 'Not_valid'

def get_validate_email(df):
    # apply the 'check' function to the 'email' column of the DataFrame
    df['valid'] = df['email'].map(check)
    return df


df_results = []
# entry point of the program
if __name__ == '__main__':
    logical = False
    start = time.time()
    num_procs = psutil.cpu_count(logical=logical)
    splitted_df = np.array_split(df, num_procs)
    # create a process pool with 4 workers
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=num_procs)
    futures = [executor.submit(get_validate_email, df) for df in splitted_df]

    # iterate over all submitted tasks and get results as they are available
    for future in tqdm(concurrent.futures.as_completed(futures)):
        try:
            df_results.append(future.result())
        except Exception as ex:
            print(str(ex))
            pass
    end = time.time()
    print("-------------------------------------------")
    print("PPID %s Completed in %s" % (os.getpid(), round(end - start, 2)))