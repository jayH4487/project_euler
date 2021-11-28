

def fifth_powers():
    res = []
    for i in range(10, 10**6):
        if _fifth_powers(i):
            res.append(i)
    return sum(res)





def _fifth_powers(n):

    digits = [int(_) for _ in str(n)]

    res = sum([_**5 for _ in digits])

    return True if res == n else False




print(fifth_powers()) # == 443839


