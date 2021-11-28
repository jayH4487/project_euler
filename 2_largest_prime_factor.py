from typing import List

def is_prime(n: int) -> List[int]:
    square_root_n: int = int(n**0.5) + 1
    for i in range(2, square_root_n):
        if n % i == 0:
            return False
    return True


def factor(n: int) -> int:
    res: List[int] = []
    square_root_n: int = int(n**0.5)
    for i in range(2, square_root_n):
        if n % i == 0:
            res.append(i)
    return res


def largest_prime_factor(n: int) -> int:
    res: int = 0
    factor_list: List[int] = factor(n)
    for num in factor_list:
        if is_prime(num):
            res = num
    return res


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
