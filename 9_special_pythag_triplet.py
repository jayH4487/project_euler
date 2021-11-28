
target_sum = 1000


def natural_num(n):
    return True if int(n) == n else False


def abc_less(a, b, c):
    return True if a<b<c else False


def abc_target_sum(a, b, c):
    return True if a + b + c == target_sum else False


def abc_pytag(a, b, c):
    return True if c == (a**2 + b**2)**0.5 else False


for a in range(1, target_sum):
    for b in range(a + 1, target_sum):
        c = target_sum - b - a
        if abc_less(a, b, c) and abc_target_sum(a, b, c) and abc_pytag(a, b, c):
            print(a, b, c, a+b+c, a*b*c)



