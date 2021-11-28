

def read_file(fname):
    with open(fname, 'r') as fhand:
        for line in fhand:
            line = line.rstrip()
            yield line


def create_list(fname):
    alist = []
    for line in read_file(fname):
        alist.append([int(_) for _ in line.split()])
    return alist


def max_path_sum_1(alist):
    while len(alist) != 1:
        last_row = alist.pop()
        n = len(alist) - 1
        # print(n)
        # print(last_row)
        for i, num in enumerate(alist[n]):
            left = num + last_row[i]
            right = num + last_row[i+1]
            # print(max(left, right))
            alist[n][i] = max(left, right)
            # print(alist)
    return alist[0][0]


def max_path_sum_2(alist):
    while len(alist) != 1:
        last_row = len(alist) - 1
        # print(last_row)
        for i, num in enumerate(alist[last_row - 1]):
            alist[last_row - 1][i] += max(alist[last_row][i], alist[last_row][i+1]
            
            # print(alist)
        del alist[last_row]
    return alist[0][0]


alist = create_list('118_max_path_sum_1b.txt')
max_path = max_path_sum_1(alist)
print(max_path)
