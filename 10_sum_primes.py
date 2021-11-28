

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root_n = n**0.5
    if int(square_root_n) == square_root_n:
        return False
    for i in range(3, int(square_root_n) + 1):
        if n % i == 0:
            return False
    return True


def yield_prime():
    i = 1
    while True:
        i += 1
        if is_prime(i):
            yield i


def prime_list(limit):
    x = yield_prime()
    res = 0
    while True:
        prime = next(x)
        if prime < limit:
            res += prime
        else:
            break
    return res




print(prime_list(2000000))


# x = yield_prime()
# print(x)
# print(next(x))
# print(next(x))
