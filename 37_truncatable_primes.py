from EulerTools import primes


def truncatables(n):
    res = set()
    res.add(n)
    digits = list(str(n))
    for i in range(1, len(digits)):
        # print(type(int(''.join(digits[i:]))))
        res.add(int(''.join(digits[i:])))
        # print(''.join(digits[:-i]))
        res.add(int(''.join(digits[:-i])))
    return res

# a = truncatables(3797)
# print(a)


prime_set = primes()
# print(a <= prime_set)

def run():
    count = 0
    for prime in prime_set:
        if truncatables(prime) <= prime_set:
            if prime not in (2, 3, 5, 7):
                count += prime

    return count


a = run()
print(a) # == 748317
