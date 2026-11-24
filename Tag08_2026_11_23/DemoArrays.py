# https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
import numpy as np

# Convert a regular Python list into a NumPy array
numbers = np.array([10, 20, 30])

# Math applies to every item at once (outputs: [20, 40, 60])
print(numbers * 2)