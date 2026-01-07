# Reading csv files with ',' delimiter

import numpy as np

data = pd.read_csv('/content/big_mart_sales.csv', delimiter=',')
print(data)

# This line will give information about data

data.info()