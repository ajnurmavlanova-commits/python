1.def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = ""
    count = 0
    i = 0

    while i < len(txt):
        result += txt[i]
        count += 1

        # check every 3rd character
        if count == 3:
            # do not add underscore at the end
            if i + 1 < len(txt) and txt[i] not in vowels and txt[i + 1] != "_":
                result += "_"
                count = 0
        i += 1

    # remove underscore if it ends the string
    if result.endswith("_"):
        result = result[:-1]

    return result
2.n = int(input())

for i in range(n):
    print(i * i)
3.i = 1
while i <= 10:
    print(i)
    i += 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
4.n = int(input())

for i in range(1, 11):
    print(n * i)
5.numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
6.num = int(input())
count = 0

while num != 0:
    num //= 10
    count += 1

print(count)
7.for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
8.list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
9.for i in range(-10, 0):
    print(i)
10.for i in range(5):
    print(i)
else:
    print("Done!")
11.start = 25
end = 50

print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
12.a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
13.n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"{n}! =", fact)
4.def uncommon_elements(list1, list2):
    result = []

    for item in list1:
        if item not in list2:
            result.append(item)

    for item in list2:
        if item not in list1:
            result.append(item)

    return result
