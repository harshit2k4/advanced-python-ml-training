import pandas as pd

# Data Files
data = pd.read_csv('/content/1995.csv')
# this will give information about the data
data.info()

print("\nShape of the data is: ")
# to check the dimen of the data set we can use the shape function
print(data.shape)
print("\n")

# to check some value of data set we can use the following code
data.head(10) # 10 represents the number of rows to be printed