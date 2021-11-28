

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# def find_mill():

#     mill = {10: (0, 0)}
#     for j in range(9, 0, -1):
#         for i in range(1, j + 2):
#             if fact(j) * i < 10**6 - sum([i for k, (i, _) in mill.items() if k > j]):
#                 mill[j] = fact(j) * i, i

#     return mill


# mill = find_mill()

# a = list(range(10))
# b = []
# for i in range(9, 0, -1):
#     b.append(a.pop(mill[i][1]))

# b.append(a.pop(0))

# print(''.join(str(_) for _ in b)) # == 2783915460

def find_n_lex_perm(alist, n):
    x = alist[:]
    len_x = len(x)
    print(x)
    count = 0
    
    a = divmod(n - count, fact(len_x - 1))

    print(a)
    # if a[1] == 0:

    # count += fact(2) * a

    # b = (n - count) // fact(len_x - 2)
    # print(b)

alist = list(range(3))
find_n_lex_perm(alist, 1)
