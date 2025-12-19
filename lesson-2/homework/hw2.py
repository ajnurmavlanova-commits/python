1.name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

current_year = 2025
age = current_year - birth_year

print(f"Hello {name}, you are {age} years old.")
2.txt = 'LMaasleitbtui'
car_name = txt[::2]
print(car_name)
3.txt = 'MsaatmiazD'
car_name = txt[::2]
print(car_name)
4.txt = "I'am John. I am from London"
area = txt.split("from ")[1]
print(area)
5.text = input("Enter a string: ")
print(text[::-1])
6.text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
7.numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", max(numbers))
8.word = input("Enter a word: ")

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
9.email = input("Enter your email: ")
domain = email.split("@")[1]
print("Domain:", domain)
10.import random
import string

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for i in range(8))

print("Generated password:", password)
