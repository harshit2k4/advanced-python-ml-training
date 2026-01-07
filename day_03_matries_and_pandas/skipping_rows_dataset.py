# Skipping some of the rows of the csv file
data = pd.read_csv('/content/read_data_with_skipping_row.csv', skiprows=4)
print(data)

data.info()