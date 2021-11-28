

# def _permutate(n):
#     if len(n) == 1:
#         yield n
#     for i in range(len(n)):
#         for perm in _permutate(n[:i] + n[i+1:]):
#             yield (n[i] + perm)
    

# def permutate(n):

#     return list(_permutate(n))






# for n in range(2, 3):
#     options = 'R' * (n) + 'D' * n


#     p = permutate(options)
#     # a = (n + 1)
#     # b = (n * (n + 1) / 2)

#     print(n, len(p), p)


# from EulerTools import triangle_num_dict

# tri_dict = triangle_num_dict(6)

# # print(tri_dict)


# def num_lattice(n):

#     #1st order
#     res1 = n + 1

#     #2nd order
#     res2 = tri_dict[n]

#     #3rd order
#     res3 = 0
#     for i in range(n, 0, -1):
#         res3 += tri_dict[i]
    
#     #4th order
#     res4 = 0
#     for j in range(n, 0, -1):
#         for i in range(j, 0, -1):

#             res4 += tri_dict[i]

#     #5th order
#     res5 = 0
#     for k in range(n, 0, -1):
#         for j in range(k, 0, -1):
#             for i in range(j, 0, -1):

#                 res5 += tri_dict[i]


    

#     return res1, res2, res3, res4, res5, res1 + res2 + res3 + res4 + res5


# print(num_lattice(6))

# def tri_num_dict(old_dict):
#     new_dict = {}
#     for i in range(1, len(old_dict)+1):
#         new_dict[i] = sum([old_dict[_] for _ in range(1, i + 1)])
#     return new_dict



# tri_dict_0 = {_: _ for _ in range(1, 11)}
# print(tri_dict_0)

# tri_dict_1 = tri_num_dict(tri_dict_0)
# print(tri_dict_1)

# tri_dict_2 = tri_num_dict(tri_dict_1)
# print(tri_dict_2)

# def lattice_paths(n):
#     tri_dict_dict = {0: {_: _ for _ in range(1, n+1)}}
#     for i in range(1, n):
#         tri_dict_dict[i] = tri_num_dict(tri_dict_dict[i-1])

#     # for i in range(n):
#     #     print(i, tri_dict_dict[i])

#     return tri_dict_dict

# n = 20
# tri_dict_dict = lattice_paths(n)
# print(tri_dict_dict[n-1][n]*2)

''' Actual solutions '''

# iterative
def print_grid(grid):
    for _ in range(len(grid)):
        print(grid[_])
    print()


def count_routes(m, n):
    grid = [[0 for _ in range(0, m + 1)] for _ in range(0, n + 1)]
    print_grid(grid)
    for _ in range(m + 1):
        grid[_][0] = 1
    print_grid(grid)
    for _ in range(n + 1):
        grid[0][_] = 1
    print_grid(grid)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    print_grid(grid)





count_routes(20, 20)

