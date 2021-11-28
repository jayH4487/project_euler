

def read_file(fname):
    with open(fname, 'r') as fhand:
        return fhand.read()
            # print(name)
            # print()


def process_file(fname):
    names = read_file(fname).replace('"', '').split(',')
    names.sort()
    return names


def alpha_value(name):
        return sum([ord(char.upper()) - 64 for char in name])



fname = '22_names_scores.txt'

names = process_file(fname)


res = 0
for i, name in enumerate(names):
    # if i == 10: break
    # print(i + 1, name, alpha_value(name))
    res += (i + 1) * alpha_value(name)

print(res) # == 871198282
