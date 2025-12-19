1.fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[2])
2.list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)
3.numbers = [10, 20, 30, 40, 50]

new_list = [numbers[0], numbers[len(numbers)//2], numbers[-1]]
print(new_list)
4.movies = ["Inception", "Titanic", "Avatar", "Gladiator", "Interstellar"]
movies_tuple = tuple(movies)

print(movies_tuple)
5.cities = ["London", "Paris", "Rome", "Berlin"]

print("Paris" in cities)
6.numbers = [1, 2, 3]
duplicate = numbers * 2

print(duplicate)
7.numbers = [10, 20, 30, 40, 50]

numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)
8.nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums[3:7])
9.colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))
10.animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))
11.t1 = (1, 2, 3)
t2 = (4, 5, 6)

merged = t1 + t2
print(merged)
12.my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)

print(len(my_list))
print(len(my_tuple))
13.numbers = (1, 2, 3, 4, 5)
numbers_list = list(numbers)

print(numbers_list)
14.nums = (5, 10, 2, 8, 1)

print("Max:", max(nums))
print("Min:", min(nums))
15.words = ("hello", "world", "python")
print(words[::-1])
