# Install first: pip install numpy
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:", numbers)
print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data type:", numbers.dtype)
print("Matrix:\n", matrix)

# Create common arrays
print("Zeros:", np.zeros((2, 3)))
print("Ones:", np.ones(4))
print("Range:", np.arange(0, 11, 2))
print("Evenly spaced:", np.linspace(0, 1, 5))

# Indexing, slicing and filtering
print("First value:", numbers[0])
print("Slice:", numbers[1:4])
print("Values above 25:", numbers[numbers > 25])

# Vectorized calculations and statistics
print("Doubled:", numbers * 2)
print("Square roots:", np.sqrt(numbers))
print("Sum:", numbers.sum())
print("Mean:", numbers.mean())
print("Minimum and maximum:", numbers.min(), numbers.max())
print("Standard deviation:", numbers.std())

# Reshape, flatten and combine arrays
reshaped = np.arange(1, 13).reshape(3, 4)
print("Reshaped:\n", reshaped)
print("Flattened:", reshaped.flatten())
print("Vertical stack:\n", np.vstack((matrix, [[7, 8, 9]])))
print("Column totals:", matrix.sum(axis=0))
