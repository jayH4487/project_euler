

memo = {1: 1, 2: 1}

def fib(n):
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


n = 0
dig_len = 1
while dig_len < 1000:
    n += 1
    dig_len = len(str(fib(n)))


print(n) # == 4782