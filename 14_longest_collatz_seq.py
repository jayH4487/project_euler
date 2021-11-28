


def _collatz(n):
    res = [n]
    while n !=1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res.append(n)
    return res


memo = {1: [1]}

#memo = {1: [1], 2: [2, 1], 3: [3, 10, 5, 16, 8, 4, 2, 1]}

def collatz(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = [n]
        memo[n].append(collatz(n)
        return memo[n]
    # print(res)




    


n = 2
res = collatz(n)
# assert len(collatz(13)) == 10
# assert collatz(13) == [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
print(len(res), res)
# print(memo)


# def longest_collatz_seq(n):
#     max_seq_count = 0
#     max_seq = []
#     for i in range(500000, n + 1):
#         seq = collatz(i)
#         # print(seq)
#         if len(seq) > max_seq_count:
#             max_seq_count = len(seq)
#             max_seq = seq

#     return max_seq_count, max_seq


# max_seq_count, max_seq = longest_collatz_seq(1000000)
# print(max_seq_count, max_seq[0])
# print(memo)

