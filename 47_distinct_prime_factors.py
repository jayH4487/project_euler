from EulerTools import primes

prime_list = primes()


def comp_nums():
    for i in range(2, 10**10):
        if i not in prime_list:
            yield i


def consecutive_nums(n):
    res = []
    sub_res = []
    for num in comp_nums():
        sub_res.append(num)
        # print(sub_res)
        if len(sub_res) > 1:
            if sub_res[-1] == sub_res[-2] + 1:
                if len(sub_res) == n:
                    yield sub_res #res.append(sub_res[:])
                    del sub_res[0:n-1]
            else:
                del sub_res[0:n-1]
    #return res

# for nums in consecutive_nums(4):
#     print(nums)


def factor(n):
    factors = []
    i = 0
    # print(i)
    while n > 1:
        # print(prime_list[i])
        if n % prime_list[i] == 0:
            n //= prime_list[i]
            factors.append(prime_list[i])
        else:
            i += 1
    return len(set(factors))

# a = factor(646)
# print(a)


def search(n=2):
    
    for nums in consecutive_nums(n):
        # print(consecutive_num)
        check = [1 for num in nums if len(factor(num)) == n]
        if len(check) == n:
            print(nums, check)
            break


def search2(n=2):
    target_pf = n
    target_consec = n
    consec = 1
    num = 1

    while consec < target_consec:
        num += 1
        if factor(num) >= target_pf:
            consec += 1
        else:
            consec = 0
    print(num - n+1)

search2(4)# == 134043
