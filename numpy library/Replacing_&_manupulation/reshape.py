# reshape(rows,column)
# reshape the array to the specified number of rows and columns
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Creates a 2D array
reshaped_arr = arr.reshape(1, 9)  # Reshapes the array
print(reshaped_arr)  # Displays the reshaped array