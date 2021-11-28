
import sys

def test():
    a = pentagon_nums(100)
    assert a[4] + a[7] in a
    assert a[7] - a[4] not in a

    assert is_pentagon_num(4187) == True
    assert is_pentagon_num(4031) == False


def pentagon_nums(n):
    res = [0]
    for i in range(1, n+1):
        pen_num = i * (3 * i - 1) / 2
        res.append(int(pen_num))
    return res


def pentagon_nums2(n):
    res = [0]
    for i in range(1, n+1):
        pen_num = i * (3 * i - 1) / 2
        if ((pen_num + 2) / 3) == int((pen_num + 2) / 3):
            res.append(int(pen_num))
    return res




def pentagon_num_diffs(n):
    res = [0]
    a = pentagon_nums(n)
    for i in range(1, len(a)):
        res.append(a[i] - a[i-1])
    return res
        

def pentagon_num(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagon_num(x):
    n = ((((24 * x) + 1)**0.5) + 1) / 6
    if n == int(n):
        return True
    else:
        return False



def search(n):
    pen_nums = pentagon_nums(n)
    for i in range(4, n):
       for j in range(i + 1, n + 1):
            if pen_nums[i] < (3 * j - 2):
                break
            else:
                add_pen = pen_nums[i] + pen_nums[j]
                dif_pen = pen_nums[j] - pen_nums[i]
                # print(i, j)
                if add_pen in pen_nums and dif_pen in pen_nums:
                    print(pen_nums[i], pen_nums[j])
                    # sys.exit()


def search2(n):
    pen_nums = pentagon_nums(n)
    pen_nums2 = pentagon_nums2(n)
    x = len(pen_nums)
    print(x)
    for i in range(4, x-1):
       for j in range(i + 1, x):
            add_pen = pen_nums[i] + pen_nums[j]
            dif_pen = pen_nums[j] - pen_nums[i]
            # print(i, j)
            if add_pen in pen_nums and dif_pen in pen_nums:
                print(pen_nums[i], pen_nums[j])
                # sys.exit()


def search3():
    # pen_nums = pentagon_nums(n)
    found = False
    i = 4
    while not found:
        # print(i)
        j = i - 1
        # print(pentagon_num(i), (3 * j - 2))
        while pentagon_num(j) > (3 * i - 2):
            add_pen = pentagon_num(i) + pentagon_num(j)
            dif_pen = pentagon_num(i) - pentagon_num(j)
            # print(i, j)
            if is_pentagon_num(add_pen) and is_pentagon_num(dif_pen):# 
                print(i, j, pentagon_num(i), pentagon_num(j), dif_pen)
                found = True
            j -= 1        
        i += 1
        # if i == 100:
            # found = True
    


def search4():
    found = False
    i = 4
    while not found:
        # print(i)
        add_pen = pentagon_num(i) * 2
        dif_pen = pentagon_num(i) // 2
        # print(dif_pen)
        if is_pentagon_num(add_pen) and is_pentagon_num(dif_pen):
            print(pentagon_num(i))
            found = True
        
        i += 1

test()

# search(10**3)
# n = 99
# a = pentagon_nums(n)
# b = pentagon_num_diffs(n)

# for i in range(1, n+1):
#     print(f'{i:<2} {a[i]:<4} {a[i] / 3}')

# a = pentagon_nums2(10**1)
# print(a)

# search2(10**4)

search3() # == 5482660
# search4()
