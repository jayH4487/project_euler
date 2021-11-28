
def test():
    assert 40755 in tri_nums(285)
    assert 40755 in pen_nums(165)
    assert 40755 in hex_nums(143)


def tri_nums(n):
    return [int(i * (i + 1) / 2) for i in range(1, n+1)]


def pen_nums(n):
    return [int(i * (3 * i - 1) / 2) for i in range(1, n+1)]


def hex_nums(n):
    return [int(i * (2 * i - 1)) for i in range(1, n+1)]


test()

n = 10**5
tris = tri_nums(n)
pens = pen_nums(n)
hexs = hex_nums(n)


for tri in tris:
    # print(tri)
    if tri in pens and tri in hexs:
        print(tri)

# == 1533776805