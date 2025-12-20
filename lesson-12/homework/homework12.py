1.import threading

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Thread function
def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)


# Main program
def main():
    start_range = 1
    end_range = 100
    num_threads = 4

    threads = []
    primes = []

    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start + step if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, primes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Prime numbers:", sorted(primes))


if __name__ == "__main__":
    main()
2.import threading
from collections import defaultdict

# Thread function
def count_words(lines, word_count):
    local_count = defaultdict(int)

    for line in lines:
        words = line.lower().split()
        for word in words:
            local_count[word] += 1

    # Merge local counts into global dictionary
    for word, count in local_count.items():
        word_count[word] += count


def main():
    file_path = "sample.txt"
    num_threads = 4

    with open(file_path, "r") as file:
        lines = file.readlines()

    threads = []
    word_count = defaultdict(int)
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = threading.Thread(
            target=count_words,
            args=(lines[start:end], word_count)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word occurrences:")
    for word, count in word_count.items():
        print(word, ":", count)


if __name__ == "__main__":
    main()
