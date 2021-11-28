

def prop_div(n):
    prop_div_sums = {}
    for num in range(1, n):
        res = []
        squ_root_num = int(num**0.5)
        for j in range(1, squ_root_num + 1):
            if num % j == 0:
                res.append(j)
        # print(res)
        res += [num // i for i in res if i != 1]
        prop_div_sums[num] = sum(set(res))
    
    return prop_div_sums


# a = prop_div(30)
# print(a)


def abundant_nums(n):
    a = prop_div(n)
    res = []
    for i in range(1, n):
        if a[i] > i:
            res.append(i)
    return res

# 28123 - 12 == 28111

a = abundant_nums(28111 + 1)
# print(a)

res = []
for i in range(len(a)):
    for j in range(i, len(a)):
        res.append(a[i] + a[j])

b = set(res)

res_1 = 0
for i in range(1, 28125):
    if i not in b:
        res_1 += i

print(res_1) # == 4179871




