from EulerTools import primes

prime_list = primes()

def is_odd_comp_num(n):
    if n % 2 == 0 or n in prime_list:
        return False
    return True

def odd_comp_nums():
    for i in range(2, 10**4):
        if is_odd_comp_num(i):
            yield i


def search():
    seen = set()
    for num in odd_comp_nums():
        # print(num)
        for prime in prime_list:
            # print(num, prime)
            # print()
            if prime > num:
                break
            else:
                for i in range(1, 100):
                    res = prime + 2 * i**2
                    if res == num:
                        if num not in seen:
                            seen.add(num)    
                            # print(prime, i)
                            # print()
                        break
        if num not in seen:
            print(num)
            # print('something')
            break




search() # == 5777
