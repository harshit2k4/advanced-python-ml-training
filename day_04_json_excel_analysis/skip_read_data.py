# skip 10 rows and then take 20 rows from it

import pandas as pd

original_data = pd.read_csv('/content/big_mart_sales_delimiter.csv', delimiter='\t', nrows=20)
print(original_data)

print("\n---------------------------------------------------\n")

data = pd.read_csv('/content/big_mart_sales_delimiter.csv', delimiter='\t', skiprows=10, nrows=20)
print(data)