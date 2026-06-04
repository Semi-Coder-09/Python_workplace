import numpy as np

# array
arr = np.array([1,2,3,4])

print(arr)

print(arr + 10)
print(arr * 2)


# Multidimensional array
arr = np.array([
    [1,2],
    [3,4]
])

print(arr.shape)
print(arr)  # Accessing element at row 0, column 1

# indexing and slicing

print(arr[0])
print(arr[:,1])