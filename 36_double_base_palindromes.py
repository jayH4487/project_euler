from EulerTools import is_palindrome


def binary(n):
    s = bin(n)
    return s[2:]


# a = binary(585)
# print(a)
# b = is_palindrome(a)
# print(b)


def double_base_pals():
    count = 0
    for i in range(1, 10**6):
        if is_palindrome(str(i)) and is_palindrome(binary(i)):
            count += i
    return count


a = double_base_pals()
print(a) # == 872187