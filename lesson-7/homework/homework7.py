1.def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  # False
print(is_prime(7))  # True


2.def digit_sum(k):
    return sum(int(digit) for digit in str(abs(k)))
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

3.def powers_of_two(N):
    result = []
    power = 1
    while 2 ** power <= N:
        result.append(2 ** power)
        power += 1
    return result
print(*powers_of_two(10))  # 2 4 8
