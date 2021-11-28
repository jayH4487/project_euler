from typing import Dict

def largest_palin_prod() -> Dict[str, int]:
    max_pal = {'product': 0, 'factor1': 0, 'factor2': 0}
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome1(str(i * j)) and max_pal['product'] < i * j:
                max_pal['product'] = i * j
                max_pal['factor1'] = i
                max_pal['factor2'] = j
    return max_pal


def is_palindrome2(n: str) -> bool:
    if len(n) < 2:
        return True
    else:
        if n[0] == n[-1] and is_palindrome2(n[1:-1]):
            return True
        else:
            return False


def is_palindrome1(n: str) -> bool:
    if n == n[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(largest_palin_prod())
