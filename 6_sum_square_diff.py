

def sum_squares(n):
    return sum([i**2 for i in range(1, n + 1)])


def square_sums(n):
    return sum(list(range(1, n + 1)))**2

n = 100

print(sum_squares(n))
print(square_sums(n))
print(square_sums(n) - sum_squares(n))
    