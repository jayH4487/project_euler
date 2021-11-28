from EulerTools import is_prime

def test():
    assert quad_primes(1, 41) == 40
    assert quad_primes(-79, 1601) == 80


def quad_primes(a, b):
    # print(f'{(n**2 + n + 41):<5} {is_prime(a)}')

    res = 0
    for i in range(100):
        quad = i**2 + a*i + b
        # print(quad)
        if is_prime(quad):
            res += 1
            # print(res)
        else:
            return res
    return res
    
test()

# a = quad_primes(-79, 1601)
# print(a)


def find_coefficients():
    # -1000 < a < 1000
    # -1001 < b < 1001
    
    max_no_of_primes = 0, 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            x = quad_primes(a, b)
            if x > max_no_of_primes[2]:
                max_no_of_primes = a, b, x
    
    return max_no_of_primes


a = find_coefficients()
print(a)
print(a[0]*a[1]) # == -59231






