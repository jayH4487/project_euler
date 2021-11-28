from itertools import permutations


def perms():
    string = '0123456789'
    return permutations(string, len(string))





def sub_string_div(string='1406357289'):
    perm_list = []
    primes = (2, 3, 5, 7, 11, 13, 17)
    for perm in perms():
        perm = ''.join(perm)
        sub_count = 0
        for i, prime in enumerate(primes):
            if int(perm[i+1:i+4]) % prime == 0:
                sub_count += 1
        if sub_count == 7:
            perm_list.append(perm)
    print(sum([int(_) for _ in perm_list]))
        

sub_string_div() # == 16695334890

# a = perms()

# for i in range(10):
#     b = next(a)
#     print(''.join(b))