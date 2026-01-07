# find the inverse of the matrix

import numpy as np

a = np.array([[1,2,4],[3,4,8], [6,7,8]])
print("a = ")
print(a)
det_a = np.linalg.det(a)
print(f"\nDeterminant of a: {det_a:.2f}")

if det_a != 0:
    inverse_a = np.linalg.inv(a)
    print("\nInverse (using np.linalg.inv):")
    print(inverse_a)

    # For a non-singular matrix: adj(A) = inv(A) * det(A)
    adj_matrix = inverse_a * det_a
    print("\nAdjoint of a:")
    print(adj_matrix)

else:
    print("\nInverse does not exist (determinant is zero)")