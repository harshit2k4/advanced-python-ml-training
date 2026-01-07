# Find trace of the matix

import numpy as np

a = np.array([[1,2,4],[3,4,8], [6,7,8]])
print("a = ")
print(a)

print("Trace of the matix is given as: ")
print(np.linalg.trace(a))


# another way is to sum the diagonals directly
# sum(a.diagonal())