from typing import List
from math import factorial
from functools import reduce
import matplotlib.pyplot as plt


def smallest_multiple(a) -> int:
    n = prime_factorial(a)
    x = n
    while True:
        # print(x)
        if check_mod1(x, a):
            return x
        x += n


def check_mod1(n: int, a) -> bool:
    for i in range(1, a + 1):
        if n % i != 0:
            return False
    return True


def check_mod(n: int) -> bool:
    for i in not_factor(20):
        if n % i != 0:
            return False
    return True


def not_factor(n: int) -> List[int]:
    res: List[int] = []
    for i in range(1, n + 1):
        if n % i != 0:
            res.append(i)
    return res


def test():
    fact = 1
    for i in range(8, 11):
        fact *= i
    return fact


def is_prime(n: int) -> bool:
    square_root_n: int = int(n**0.5) + 1
    for i in range(2, square_root_n):
        if n % i == 0:
            return False
    return True


def prime_factorial(n):
    p = [i for i in range(1, n + 1) if is_prime(i)]
    return reduce(lambda x, y: x * y, p)


if __name__ == '__main__':
    # print(prime_factorial(10))
    



    for i in range(1, 101):
        w = 5
        a = smallest_multiple(i)
        b = prime_factorial(i)
        c = a // b
        d = c /i
        # print(f'{i:<3} {a:<{w}} {b:<{w}} {c:<{w}} {d:<30}')
        print(f'{i:<3} {c:<{w}} {d:<{w}}')


    # for i in range(1, 11):
    #     print(2520/i)
    # print(not_factor(20))
    # a = [x for x in range(11,21)]
    # print(a)
    # print(test())