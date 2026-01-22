1.lst = [12.23, 13.32, 100, 36.32]

array_1d = np.array(lst)

print("Original List:", lst)
print("One-dimensional NumPy array:", array_1d)
2.matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)
3.null_vector = np.zeros(10)
print(null_vector)

# Update sixth value (index 6)
null_vector[6] = 11
print("After update:")
print(null_vector)
4.arr = np.arange(12, 38)
print(arr)
5.arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)

print("Original array:")
print(arr)

print("Float array:")
print(float_arr)
6.celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9 / 5) + 32

print("Values in Centigrade degrees:")
print(celsius)

print("Values in Fahrenheit degrees:")
print(fahrenheit)
7.arr = np.array([10, 20, 30])
values = [40, 50, 60, 70, 80, 90]

new_arr = np.append(arr, values)

print("Original array:")
print(arr)

print("After append values to the end of the array:")
print(new_arr)
8.random_arr = np.random.rand(10)

print("Array:", random_arr)
print("Mean:", np.mean(random_arr))
print("Median:", np.median(random_arr))
print("Standard Deviation:", np.std(random_arr))
9.arr = np.random.rand(10, 10)

print("Array:")
print(arr)

print("Minimum value:", arr.min())
print("Maximum value:", arr.max())
10.arr = np.random.rand(3, 3, 3)
print(arr)

