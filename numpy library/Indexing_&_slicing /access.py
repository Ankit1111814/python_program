# array(index) for find the index of an element in a numpy array
# in 2d array(row, column)

import numpy as np
arr = np.array([[2, 4, 3], [3, 2, 1], [1, 2, 3]])  # Creates a 2D array
print(arr[0, 1])  # Accesses the element at row 0, column 1
print(arr[1, 2])  # Accesses the element at row 1, column 2
print(arr[2, 0])  # Accesses the element at row 2, column 0

