

def is_triangle_num(n):
    _ = (((1 + (8 * n))**0.5) - 1) / 2
    if _.is_integer():
        return True
    return False


def read_words(fname='42_coded_triangle_numbers.txt'):
    with open(fname, 'r') as fhand:
        words = fhand.readline().replace('"', '').split(',')
        for word in words:
            yield word


def word_value(string):
    return sum([ord(c) - 64 for c in list(string)])
    


def check():
    count = 0
    for word in read_words():
        if is_triangle_num(word_value(word)):
            count += 1

    print(count)


check() # == 162


