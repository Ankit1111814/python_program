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
print(np.std(arr))  # Displays the standard deviation of all elements in the array
print(np.var(arr))  # Displays the variance of all elements in the array
print(np.min(arr))  # Displays the minimum value in the array
print(np.max(arr))  # Displays the maximum value in the array
print(np.argmin(arr))  # Displays the index of the minimum value in the array
print(np.argmax(arr))  # Displays the index of the maximum value in the array
print(np.sort(arr))  # Displays the array sorted in ascending order
print(np.argsort(arr))  # Displays the indices that would sort the array
print(np.unique(arr))  # Displays the unique elements in the array
print(np.concatenate((arr, arr), axis=0))  # Concatenates the array
print(np.concatenate((arr, arr), axis=1))  # Concatenates the array
print(np.split(arr, 3, axis=0))  # Splits the array into 3 equal parts along the first axis
print(np.split(arr, 3, axis=1))  # Splits the array into 3 equal parts along the second axis