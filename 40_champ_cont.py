

def champ_cont():
    s = ''
    for i in range(1, 10**6):
        s += str(i)

    d = [10**_ for _ in range(0, 7)]
    count = 1
    for i in d:
        count *= int(s[i-1])
    print(count)

champ_cont() # == 210


