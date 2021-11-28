from EulerTools import is_prime
from itertools import permutations
import matplotlib.pyplot as plt



def chart():
    plt.style.use('ggplot')

    x = some_primes()
    y = diff()

    plt.plot(x, y)

    plt.xlabel('Primes')
    plt.ylabel('diff')
    plt.show()


def some_primes():
    return [x for x in range(10**3, 10**4) if is_prime(x)]


def is_perm(n):
    res = sorted(list(str(n)))
    return res


def diff(n):
    res = [0]
    for i in range(1, len(n)):
        res.append(n[i] - n[i-1])
    return res


def some_perms(n):
    string = str(n)
    return set([int(''.join(x)) for x in permutations(string, 4) if x[0] != '0'])
 

def prime_perms():
    res = []
    primes = some_primes()
    for prime in primes:
        perms = some_perms(prime)
        sub_res = []
        for perm in perms:
            if perm in primes:
                sub_res.append(perm)
        if len(sub_res) >= 3:
            sub_res.sort()
            if sub_res not in res:
                res.append(sub_res)
    return res


def search():
    for nums in prime_perms():
        nums.reverse()
        # print(nums)
        for i in range(0, len(nums)-2):
            for j in range(i + 1, len(nums)-1):
                for k in range(j + 1, len(nums)-0):
                    if nums[i] - nums[j] == nums[j] - nums[k]:
                        print(nums[k], nums[j], nums[i])


search() # == 2969 6299 9629

