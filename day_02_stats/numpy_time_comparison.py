import time

size = 1000000
list1 = list(range(size))
list2 = list(range(size))

array1 = np.arange(size)
array2 = np.arange(size)

start = time.time()
res_list = [x + y for x, y in zip(list1, list2)]
print(f"List addition time: {time.time() - start:.5f} seconds")

start = time.time()
res_np = array1 + array2
print(f"Numpy addition time: {time.time() - start:.5f} seconds")