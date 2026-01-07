# How to merge multiple data into one file
import pandas as pd
import glob

# Get a list of csv files names in a directory
file_list = glob.glob('/content/data_set/*.csv')

# iterate through each of the files
for files in file_list:
  print(files)

# Create an empty dataframe to store the data
all_data = pd.DataFrame()

# Loop through the list of csv files and concatenate them
for file in file_list:
  df = pd.read_csv(file)
  all_data = pd.concat([all_data, df], ignore_index=False)

# display the combined dataframe
print(all_data)
type(all_data)
all_data.head(20)
print(all_data.shape)

# How to save csv file from python
all_data.to_csv('/content/data_set/combined_data.csv', index=False)