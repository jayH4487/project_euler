

def search_space():
    numerator = 1
    denominator = 1
    for i in range(11, 99):
        for j in range(i+1, 100):
            if digit_cancel(i, j):
               print(f'{i}/{j}')
               numerator *= i
               denominator *= j
    print(denominator / numerator)


def digit_cancel(a, b):
    # print(a, b)
    if a % 10 == 0 and b % 10 == 0:
        return False
    new_a = [int(_) for _ in str(a) if _ not in str(b)]
    new_b = [int(_) for _ in str(b) if _ not in str(a)]
    # print(new_a, new_b)

    if len(new_a) == 0 or len(new_b) == 0 or len(new_a) == 2 or len(new_b) == 2 or b == 0 or new_b[0] == 0:
        return False
    else:
        if a/b == new_a[0] / new_b[0]:
            return True
    return False



search_space() # == 100

# digit_cancel(12, 36)