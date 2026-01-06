import sys

# large dataset
size = 10000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Memory comparison
# sys-getsizeof for list only counts the size of the pointer array itself
# but even so, the overhead is much higher do lists

print(f"List overhead (base): {sys.getsizeof(python_list)} bytes")
print(f"Numpy array overhead (base): {sys.getsizeof(numpy_array)} bytes")