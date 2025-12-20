1.try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
2.try:
    num = input("Enter an integer: ")
    if not num.isdigit():
        raise ValueError("Not a valid integer")
    num = int(num)
    print("You entered:", num)
except ValueError as e:
    print("Error:", e)
3.try:
    file = open("test.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found.")
4.try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.isdigit() and b.isdigit()):
        raise TypeError("Inputs must be numbers")
    print(int(a) + int(b))
except TypeError as e:
    print("Error:", e)
5.try:
    file = open("protected.txt", "r")
    print(file.read())
    file.close()
except PermissionError:
    print("Error: Permission denied.")
6.try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Error: Index out of range.")
7.try:
    num = input("Enter a number: ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
8.try:
    print(10 / 0)
except ArithmeticError:
    print("Arithmetic error occurred.")
9.try:
    with open("data.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding error while reading file.")
10.try:
    lst = [1, 2, 3]
    lst.push(4)
except AttributeError:
    print("Error: Attribute does not exist.")

PART 2: Python File Input / Output
1.with open("file.txt", "r") as f:
    print(f.read())
2.n = 3
with open("file.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
3.with open("file.txt", "a") as f:
    f.write("\nNew text")

with open("file.txt", "r") as f:
    print(f.read())
4.n = 2
with open("file.txt", "r") as f:
    lines = f.readlines()
    print("".join(lines[-n:]))
5.with open("file.txt", "r") as f:
    lines = f.readlines()
print(lines)
6.with open("file.txt", "r") as f:
    data = f.read()
print(data)
7.arr = []
with open("file.txt", "r") as f:
    for line in f:
        arr.append(line.strip())
print(arr)
8.with open("file.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print(longest)
9.with open("file.txt", "r") as f:
    print(len(f.readlines()))
10.from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().replace(",", " ").split()

print(Counter(words))
11.import os
print(os.path.getsize("file.txt"), "bytes")
12.lst = ["apple", "banana", "cherry"]

with open("file.txt", "w") as f:
    for item in lst:
        f.write(item + "\n")
13.with open("file1.txt", "r") as f1, open("file2.txt", "w") as f2:
    f2.write(f1.read())
14.with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip(), l2.strip())
15.import random

with open("file.txt", "r") as f:
    lines = f.readlines()
print(random.choice(lines))
16.f = open("file.txt", "r")
print(f.closed)
f.close()
print(f.closed)
17.with open("file.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
18.with open("file.txt", "r") as f:
    text = f.read().replace(",", " ")
    print(len(text.split()))
19.chars = []
with open("file.txt", "r") as f:
    for line in f:
        chars.extend(list(line.strip()))
print(chars)
20.import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(letter)
21.import string

n = 5
alphabet = string.ascii_lowercase

with open("alphabet.txt", "w") as f:
    for i in range(0, len(alphabet), n):
        f.write(alphabet[i:i+n] + "\n")
