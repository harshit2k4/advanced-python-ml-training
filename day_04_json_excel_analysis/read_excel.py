# Read excel sheet

data = pd.read_excel('/content/data_set/1998.xlsx')
data.head()

# Read specific excel sheet

data = pd.read_excel('/content/data_set/1998.xlsx', sheet_name='1998')
data.head()

# Reading my data from specific sheet (make some changes in the sheet and reupload it)

data = pd.read_excel('/content/data_set/my_data/1998.xlsx', sheet_name='sheet_data')
data.head()

# skip some data in the dataset in excel

data = pd.read_excel('/content/data_set/my_data/1998.xlsx', sheet_name='sheet_data', skiprows=2)
data.head()