

def tri_num(n):
    if n == 1:
        return 1
    else:
        return int(n * (n + 1) / 2)


def factor_set(n):
    res = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            res.add(i)
            res.add(int(n/i))
    return res


def highly_div_tri_num(n):
    i = 1
    while True:
        num = tri_num(i)
        factor = factor_set(num)
        if len(factor) > n:
            return num
        i += 1

a = highly_div_tri_num(500)
assert a == 76576500
print(a)
