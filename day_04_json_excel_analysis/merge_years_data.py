# Merge all the data in the years database

import pandas as pd
import glob

file_list = glob.glob('/content/data_set/Years/*.xlsx')

for file in file_list:
    print(file)

all_data = pd.DataFrame()

for file in file_list:
    df = pd.read_excel(file)
    all_data = pd.concat([all_data, df])

all_data.head(20)