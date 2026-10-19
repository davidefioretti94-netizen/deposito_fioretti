import numpy as np

arr = np.array([1 ,2 ,3 ,4 ,5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

arr = np.array([1, 2, 3], dtype='int32')
print(arr.dtype)  # Output: int32

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3) stampa 2 righe e 3 colonne


arr = np.arange(10)
print(arr)  # Output: [0 1 2 3 4 5 6 7 8 9]


arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# Output:  [[0 1 2] [3 4 5]]