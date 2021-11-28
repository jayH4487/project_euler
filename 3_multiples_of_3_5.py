

def multiples_of_3_5(n: int) -> int:
    res: int = 0
    for number in range(n):
        if number % 3 == 0 or number % 5 == 0:
            res += number

    return res


if __name__ == '__main__':
    assert multiples_of_3_5(10) == 23
    print(multiples_of_3_5(1000))

