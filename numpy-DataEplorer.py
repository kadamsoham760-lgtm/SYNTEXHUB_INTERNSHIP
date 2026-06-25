import numpy as np
import time

print("===== NumPy Data Explorer =====\n")

print("1. Array Creation")
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)


print("\n2. Indexing and Slicing")

print("First Element:", arr1[0])
print("Last Element:", arr1[-1])
print("Slice [1:4]:", arr1[1:4])

print("Element at row 2, column 3:", arr2[1, 2])


print("\n3. Mathematical Operations")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)


print("\n4. Statistical Operations")

data = np.array([12, 15, 18, 22, 25, 30])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))
print("Standard Deviation:", np.std(data))


print("\n5. Axis-wise Operations")

matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print("Matrix:\n", matrix)

print("Column-wise Sum (axis=0):", np.sum(matrix, axis=0))
print("Row-wise Sum (axis=1):", np.sum(matrix, axis=1))


print("\n6. Reshaping")

original = np.arange(12)

print("Original Array:")
print(original)

reshaped = original.reshape(3, 4)

print("Reshaped Array (3x4):")
print(reshaped)


print("\n7. Broadcasting")

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

value = 10

result = arr + value

print("Original Array:\n", arr)
print("After Broadcasting (+10):\n", result)


print("\n8. Save and Load Arrays")

sample = np.array([100, 200, 300, 400])

np.save("sample_array.npy", sample)

loaded = np.load("sample_array.npy")

print("Saved Array:", sample)
print("Loaded Array:", loaded)


print("\n9. Performance Comparison")

size = 1000000


list1 = list(range(size))
list2 = list(range(size))

start = time.time()
list_result = [x + y for x, y in zip(list1, list2)]
list_time = time.time() - start


np1 = np.arange(size)
np2 = np.arange(size)

start = time.time()
np_result = np1 + np2
numpy_time = time.time() - start

print(f"Python List Time: {list_time:.6f} seconds")
print(f"NumPy Array Time: {numpy_time:.6f} seconds")

if numpy_time < list_time:
    print("NumPy is faster than Python Lists!")
else:
    print("Python Lists are faster!")


print("\n===== Project Completed Successfully =====")