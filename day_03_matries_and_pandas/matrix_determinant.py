# Find determinant of the matrix using numpy

import numpy as np

a = np.array([[1,2,4],[3,4,8], [6,7,8]])
print("a = ")
print(a)

print("\nDeterminant of a = ")
print(np.linalg.det(a))