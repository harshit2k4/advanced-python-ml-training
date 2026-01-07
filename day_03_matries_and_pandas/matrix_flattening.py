# flattening a matrix

import numpy as np

a = np.arange(1,10)
a.shape = (3,3)
print("a = ")
print(a)
print("\nAfter flattening:")
print(a.flatten())