

def sum_even_fib_nums(n) -> int:
    a = 1
    b = 2
    res = 0
    while a < n:
        if a % 2 == 0:
            res += a
        b, a = a + b, b
    return res


if __name__ == '__main__':
    print(sum_even_fib_nums(4000000))



        
    

