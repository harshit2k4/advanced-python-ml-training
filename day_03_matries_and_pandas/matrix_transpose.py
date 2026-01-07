# transpose a matrix in numpy
import numpy as np

my_matrix = np.matrix([[1,2,3], [4,5,6],[7,8,9]])
transpose_matrix = np.transpose(my_matrix)
print(transpose_matrix)

# Another way to do the same
"""
import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print("a = ")
print(a)

print("\nWith np.transpose(a) function")
print(np.transpose(a))

print("\nWith ndarray.transpose() method")
print(a.transpose())

print("\nWith ndarray.T short form")
print(a.T)
"""