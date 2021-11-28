

def test():
    assert pandigital('15234') == True
    assert pandigital('15233') == False
    a = '39'
    b = '186'
    c = str(7254)
    assert pandigital(a+b+c) == True


def pandigital(string):
    number_of_digits = len(string)
    digits = sorted([int(digit) for digit in string])
    # print(digits, number_of_digits)
    return True if digits == list(range(1, number_of_digits + 1)) else False

test()



def pandigital_products():
    res = set()
    for i in range(1, 99):
        for j in range(9876, 101, -1):
            k = i * j
            num_str = str(i) + str(j) + str(k)
            if len(num_str) == 9:
                if pandigital(num_str):
                    print(i, j, k)
                    res.add(k)
    return res

a = pandigital_products()
print(a)
print(sum(a)) # == 45228
