# How to subset first n rows based on their position index?

import pandas as pd
data = pd.read_csv('/content/1995.csv')

data.head()

# index of the dataframe
data.index

# create a random list
import random
random_index = [random.randint(1,20) for i in range(10)]
print(random_index)

data.set_index('Years', drop=True, inplace=True)
data.head()

data.index

# setting the index of the dataset as categorical variable
data.set_index('Product', drop=True, inplace=True)
data.head()

# For filtering the data with respect to this label
data.loc['Fast Food']

data.reset_index(inplace=True)
data.head()

data[data['Product'] == 'Sweet']

# Select the data from range 10-15
data[10:15]

# select specific row by index number
data.iloc[[1,2,4,2,3,6,7,0]]

data.iloc[[1,4,5,2],[1]] # row number 1,4,5,2 and col 1

data.iloc[10:15:2] # select rows in the range of 10 to 15 after skipping one row in middle