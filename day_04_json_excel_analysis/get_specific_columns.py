# Get specific columns of the dataset and till 50 rows

import pandas as pd

# by index number
data = pd.read_csv('/content/big_mart_sales_delimiter.csv', delimiter='\t', usecols=[0, 1, 2], nrows=50)
print(data)
print("\n")
print("=================================================")
print("\n")
# by index name
data = pd.read_csv('/content/big_mart_sales_delimiter.csv', delimiter='\t', usecols=['Item_Identifier', 'Item_Type', 'Item_MRP'], nrows=50)
print(data)