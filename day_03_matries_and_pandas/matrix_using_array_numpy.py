# Array operation using numpy

import numpy as np

a = np.array([[1,2,2],[3,4, 7]])
b = np.array([[5,6,7], [8,9,10]])

c = np.matrix([[1,2], [3,4]])
d = np.matrix([[5,6], [8,9]])
print("\nc", type(c))
print(c)
print("\nd", type(d))
print(d)
print("\n* operation on two ndarray objects (Element wise)")
print(a * b)
print("\n* operation on two matrix objects (same as np.dot())")
print(c * d)