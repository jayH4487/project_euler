

def reciprocal_cycle(divisor):
    res_list = []
    res = set()
    mod = 1
    if 10**6 % divisor == 0:
        return res
    while mod < divisor:
        mod *= 10
    for _ in range(10000):
        div, mod = divmod(mod, divisor)
        
        if mod == 0:
            return res
        res.add(mod)
        if div == 0:
            mod *= 10
        else:
            res_list.append((div, mod))
    return res



max_cycle = (0, 0)
for i in range(1, 1001):
    a = reciprocal_cycle(i)
    # print(f'{i:<3} {0 if a == None else len(a)} {a}')
    if len(a) > max_cycle[1]:
        max_cycle = i, len(a)

print(max_cycle) # == 983


# a, b = _reciprocal_cycle(7)
# print(a)
# print(len(b), b)
