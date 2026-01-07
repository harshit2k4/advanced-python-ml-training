# Calculate the pseudoinverse for singluar matrix
import numpy as np

a = np.array([[2, 8],
              [1, 4]])

pseudo_inv_matrix = np.linalg.pinv(a)

print("Original Matrix:\n", a)
print("\nPseudoinverse:\n", pseudo_inv_matrix)