

def is_prime(n):
    if int(n**0.5) == n**0.5:
        return False
    square_root_n = int(n**0.5) + 1
    for i in range(2, square_root_n):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    return [i for i in range(1, n + 1) if is_prime(i)]


def nth_prime(n):
    i = 1
    counter = 0
    while counter < n:
        i += 1
        if is_prime(i):
            counter += 1
    return counter, i


print(nth_prime(100001))


# print(len(prime_list(500000)))