

prop_div_sums = {}

def prop_div(n):
    res = []
    squ_root = int(n**0.5)
    for i in range(1, squ_root + 1):
        if n % i == 0:
            res.append(i)

    res += [n // num for num in res if num != 1]

    prop_div_sums[n] = sum(res)


def amicable_nums(a):
   
    b = prop_div_sums[a]
    try:
        if prop_div_sums[b] == a:
            if a != b:
                return a + b
    except:
        pass
    return 0


# a = prop_div(220)
# b = prop_div(a)
# print(a, b)

for i in range(1, 10**4):
    prop_div(i)


# print(prop_div_sums[220])
# print(prop_div_sums[prop_div_sums[220]])


# if 220 == prop_div_sums[prop_div_sums[220]]:
#     print('True')
# else:
#     print('not looking good')

print(amicable_nums(220))
print(284 + 220)

a = sum([amicable_nums(i) for i in range(1, 10**4)])

print(a // 2) # == 31626
