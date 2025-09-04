import numpy as np

arr = np.arange(1,6)
print(arr)

# indexing
print(arr[2])
print(arr[4],arr[-1], arr[len(arr)-1])

# slicing
print(arr[1:3])
print(arr[::3])