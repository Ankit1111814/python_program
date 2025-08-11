# ravel = view of the array
# flatten = copy of the array


import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Creates a 2D array
flattened_arr = arr.flatten()  # Flattens the array
print(flattened_arr)  # Displays the flattened array
raveled_arr = arr.ravel()  # Ravel the array
print(raveled_arr)  # Displays the raveled array