

def fact(n):
    facts = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    return facts[n]

def is_digit_factorial(n):
    digits = list(str(n))
    # print(digits)
    digit_factorial = [fact(int(_)) for _ in digits]
    # print(len(str(n)), digit_factorial, len(str(sum(digit_factorial))))
    if n == sum(digit_factorial):
        return True
    return False



# print(is_digit_factorial(9990000))


def sum_digit_factorials():
    res = [i for i in range(10, 2540160) if is_digit_factorial(i)]
    return sum(res)


print(sum_digit_factorials()) # == 40730


