

def distinct_powers(n):
    res = set()
    for a in range(2, n+1):
        for b in range(2, n+1):
            res.add(a**b)

    return res


a = distinct_powers(100)

print(len(a)) # == 9183

