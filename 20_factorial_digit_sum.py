



def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


a = sum([int(num) for num in str(fact(100))])

print(a)
