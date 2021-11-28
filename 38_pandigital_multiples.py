

def test():
    assert bool(pan_mul(9)) == True
    assert bool(pan_mul(192)) == True
    assert bool(pan_mul(8)) == False


def pandigital(string):
    number_of_digits = len(string)
    digits = sorted([int(digit) for digit in string])
    # print(digits, number_of_digits)
    return True if digits == list(range(1, number_of_digits + 1)) else False


def pan_mul(n):
    string = ''
    for i in range(1, 20):
        num = n * i
        string += str(num)
        if pandigital(string):
            return string

    return ''


test()

def search_space():
    largest = 0
    for i in range(9000, 10000):
        if bool(pan_mul(i)) == True:
            # print(i, pan_mul(i))
            if int(pan_mul(i)) > largest:
                largest = int(pan_mul(i))

    return largest


a = search_space()
print(a) # == 932718654




