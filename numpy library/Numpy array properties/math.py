# math operations on numpy array
import numpy as np
arr = np.array([[2, 4, 3], [3, 2, 1], [1, 2, 3]])  # Creates a 2D array
print(arr+5 )   # Displays the array
print(arr-2)   # Displays the array after subtracting 2 from each element
print(arr*3)   # Displays the array after multiplying each element by 3
print(arr/2)   # Displays the array after dividing each element by 2
print(arr**2)  # Displays the array after squaring each element
print(np.sqrt(arr))  # Displays the square root of each element in the array
print(np.sin(arr))  # Displays the sine of each element in the array
print(np.cos(arr))  # Displays the cosine of each element in the array
print(np.tan(arr))  # Displays the tangent of each element in the array
print(np.log(arr))  # Displays the natural logarithm of each element in the array
print(np.exp(arr))  # Displays the exponential of each element in the array
print(np.sum(arr))  # Displays the sum of all elements in the array
print(np.mean(arr))  # Displays the mean of all elements in the array
print(np.median(arr))  # Displays the median of all elements in the array   