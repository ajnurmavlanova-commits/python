1.def is_leap(year):
    """
    Determines whether a given year is a leap year.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
2.n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
3.1. a = int(input())
b = int(input())

if a % 2 != 0:
    a += 1

evens = list(range(a, b + 1, 2))
print(evens)
2.a = int(input())
b = int(input())

start = a + (a % 2)
evens = list(range(start, b + 1, 2))
print(evens)



