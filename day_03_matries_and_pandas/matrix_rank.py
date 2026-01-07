# Find the rank of the matrix
import numpy as np

a = np.arange(1,10)
a.reshape(3,3)
print("a = ")
print(a)

print("Rank of the matrix is given as: ")
print(np.linalg.matrix_rank(a))