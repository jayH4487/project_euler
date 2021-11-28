from EulerTools import is_prime, is_pandigital
from itertools import permutations


def test():
    assert pan_prime(2143) == True


def pan_prime(n):
    if is_pandigital(str(n)) and is_prime(n):
        return True
    else:
        return False


test()

def perms(string):
    for perm in permutations(string, len(string)):
        if perm[-1] in ('1', '3', '7', '9'):
            yield int(''.join(perm))


def search():
    strings = []
    for i in range(3,11):
        strings.append(''.join([str(j) for j in range(1, i)]))

    max_prime = 0
    for string in strings:
        for perm in perms(string):
            if pan_prime(perm) == True:
                if perm > max_prime:
                    max_prime = perm
    print(max_prime)


search() # == 7652413