from EulerTools import is_prime


def primes():
    prime_set = set()
    fname = 'primes.txt'
    with open(fname, 'r') as fhand:
        for prime in fhand:
            prime = int(prime.rstrip())
            prime_set.add(prime)
    return prime_set


prime_set = primes()


def rotations(n):
    n = list(str(n))
    res = set()
    res.add(int(''.join(n)))
    for _ in range(len(n) - 1):
        n.append(n.pop(0))
        res.add(int(''.join(n)))
    # print(res)
    return res


# res = rotations(197)
# print(res)


def is_circular_prime(prime):
    # print(prime)
    if rotations(prime) <= prime_set:
        # print(prime)
        return True
    return False
    

# prime_set = set([num for num in range(2, 100) if is_prime(num)])
# print(prime_set)

def primes_count():
    memo = {}
    for prime in prime_set:
        # print(prime)
        if prime not in memo:
            # print(prime)
            if is_circular_prime(prime):
                # print(prime)
                memo[prime] = True
    return memo

a = primes_count()
# print(a)
print(len(a)) # == 55





    



