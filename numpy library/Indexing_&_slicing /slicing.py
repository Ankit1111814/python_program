# array([start : end :step]) for slicing a numpy array
# array -1 for reverse slicing

import numpy as np
arr = np.array([3,4,2,42,2,2,4,2,2,1]) # Creates a 1D array
print(arr[1:5])  # Displays elements from index 1 to 4
print(arr[2:])  # Displays elements from index 2 to the end
print(arr[:5])  # Displays elements from the start to index 4
print(arr[::2])  # Displays every second element
print(arr[::-1])  # Displays the array in reverse order
print(arr[1:5:2])  # Displays elements from index 1 to 4 with a step of 2
print(arr[-1])  # Displays the last element
print(arr[-2])  # Displays the second last element
print(arr[-3:])  # Displays the last three elements
print(arr[-4:-1])  # Displays elements from the fourth last to the second last
print(arr[-5:-1:2])  # Displays elements from the fifth last to the second last with a step of 2