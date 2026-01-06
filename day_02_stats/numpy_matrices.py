import numpy as np

# Matrices as ndarray objects
a = np.array([[1,2],[3,4]])
b = np.array([[5,6,7], [8,9,10]])
print("a", type(a), a)
print(a)
print("\nb", type(b), b)
print(b)

# Matrices are matrix objects
c = np.matrix([[1,2], [3,4]])
d = np.matrix([[5,6,7], [8,9,10]])
print("\nc", type(c))
print(c)