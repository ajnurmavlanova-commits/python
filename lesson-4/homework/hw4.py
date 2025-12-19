1.my_dict = {1: 50, 2: 20, 3: 40, 4: 10}

# Ascending order
asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc)

# Descending order
desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc)
2.my_dict = {0: 10, 1: 20}
my_dict[2] = 30

print(my_dict)
3.dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)
4.n = 5
squares = {}

for x in range(1, n + 1):
    squares[x] = x * x

print(squares)
5.squares = {}

for i in range(1, 16):
    squares[i] = i ** 2

print(squares)
Set Exercises
1.my_set = {1, 2, 3, 4, 5}
print(my_set)
2.my_set = {1, 2, 3}

my_set.add(4)          # add one element
my_set.update([5, 6])  # add multiple elements

print(my_set)
3.my_set = {1, 2, 3}

my_set.add(4)          # add one element
my_set.update([5, 6])  # add multiple elements

print(my_set)
4.my_set = {1, 2, 3, 4}

my_set.remove(3)
print(my_set)
5.my_set = {10, 20, 30}

my_set.discard(20)   # no error if element does not exist
print(my_set)
