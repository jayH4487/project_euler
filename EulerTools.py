

def is_prime(n):
    n = abs(n)
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    square_root_n = n**0.5
    if int(square_root_n) == square_root_n:
        return False
    for i in range(3, int(square_root_n) + 1, 2):
        if n % i == 0:
            return False
    return True


def write_primes(n):
    fname = 'primes.txt'
    with open(fname, 'w') as fhand:
        for i in range(2, n + 1):
            if is_prime(i):
                fhand.write(f'{i}\n')


def primes():
    res = []
    fname = 'primes.txt'
    with open(fname, 'r') as fhand:
        for prime in fhand:
            prime = int(prime.rstrip())
            res.append(prime)
    return res
                

def multiply_series(a_series):
    res = 1
    for i in a_series:
        res *= i
    return res


def triangle_num_dict(n):
    tri_num_dict = {}
    for i in range(1, n + 1):
        tri_num_dict[i] = i * (i + 1) / 2
    return tri_num_dict


def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def is_palindrome(n: str) -> bool:
    if n == n[::-1]:
        return True
    else:
        return False

    
def is_pandigital(string):
    number_of_digits = len(string)
    digits = sorted([int(digit) for digit in string])
    # print(digits, number_of_digits)
    return True if digits == list(range(1, number_of_digits + 1)) else False
