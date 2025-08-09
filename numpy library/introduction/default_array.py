# np.zeroes(shape) creates an array filled with zeros
# np.ones(shape) creates an array filled with ones
# shape (3) 1d, (3, 3) 2d, (3, 3, 3) 3d


import numpy as np
arr =np.zeros((3, 3))  # Creates a 2D array of shape (3, 3) filled with zeros
print(arr)

arr = np.ones((3))  # Creates a 1D array of shape (3,) filled with ones
print(arr)