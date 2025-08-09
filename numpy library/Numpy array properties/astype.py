
# astype() converts the data type of the array elements


import numpy as np
arr = np.array([[2, 4, 3], [3, 2, 1], [1, 2, 3]])  # Creates a 2D array
converted_arr = arr.astype(float)  # Converts the data type of the array elements to float
print(converted_arr)  # Displays the array with converted data type
print(converted_arr.dtype)  # Prints the data type of the elements in the converted array
