# Read only first 50 rows
import pandas as pd

data = pd.read_csv('/content/big_mart_sales_delimiter.csv', delimiter='\t', nrows=50)
print(data)
# print(data.head(50))