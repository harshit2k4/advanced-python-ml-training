import numpy as np

# 1. Normal python list
data_list = [1,2,3]
try:
  # this will fail as you canot add an integer to a list
  data_list = data_list + 10
except TypeError:
  print("List require loops: ", [x+10 for x in data_list])

# 2. Numpy array
data_np = np.array([1,2,3])
# this works on all elements (vectoriztion)
print("Numpy vectorized array addition: ", data_np + 10)