
# _directions = ['right', 'down', 'left', 'up']
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# def build_array(n):
    
#     _array = [[7, 8, 9],
#               [6, 1, 2],
#               [5, 4, 3]]

#     return [[0 for _ in range(n)] for _ in range(n)]


# def next_direction():
#     new_direction = directions.pop(0)

#     directions.append(new_direction)

#     return new_direction


# def pp(item):
#     for i in range(len(item)):
#         print(item[i])
#     print()


# def in_bounds(row, col, n):
#     # if 0 > row or row > n-1:
#     #     return False
#     # return True
#     check = [row >= 0,
#              row <= n - 1,
#              col >= 0,
#              col <= n - 1]
#     # print(check)
#     return all(check)

# # print(in_bounds(0, 3, 3))


# def build_spiral(n=3):
    
    
#     array = build_array(n)
#     start = n // 2
#     # print(start)

#     array[start][start] = 1
#     # print(array)

#     col, row = start, start
#     # print(col, row)

#     direction = next_direction()
#     # print(direction)


#     size = 3

#     count = 2

#     while count < 10:
#         row += direction[0]
#         col += direction[1]
#         if int(count**0.5) == size:
#             size += 2
#         print(count, size)
#         if in_bounds(row, col, size):
            
#             # print(row, col)

#             array[row][col] = count
#             count += 1
#         else:
#             row -= direction[0]
#             col -= direction[1]

#             direction = next_direction()
#             # print(direction)
        
#         pp(array)

        
# build_spiral(5)


'''
1 x 1 == [1] -> range(1, 2) -> 1

3 x 3 == [1] + [2, 3*, 4, 5*, 6, 7*, 8, 9*] -> range(2, 10) -> 25

5 x 5 == [1] + [2, 3, 4, 5, 6, 7, 8, 9] + [10, 11, 12, 13*, 14, 15, 16, 17*, 18, 19, 20, 21*, 22, 23, 24, 25*] -> range(10, 26) -> 101

7 x 7 == []

1) 3^2 + 5^2 + 7^2 ... (n+2)^2

2) (3^2 - 2) + (5^2 - 4) + (7^2 - 6) ... [(n+2)^2 - (n-1)]

3) (3^2 - 4) + (5^2 - 8) + (7^2 - 12)... [(n+2)^2 - (n-1)*2]

4) (3^2 - 6) + (5^2 - 12) + (7^2 - 18)... [(n+2)^2 - (n-1)*3]
'''

def num_spiral_diagonals(n):
    if n == 1:
        return 1
    else:
        return 4 * (n**2) - 6 * (n - 1) + num_spiral_diagonals(n - 2)


print(num_spiral_diagonals(1001)) # == 669171001


