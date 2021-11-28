

# variables = [1, 2, 5, 10, 20, 50, 100, 200]
# variables = [1, 2, 5, 10]

# domain = {v: [d for d in range(0, 11)] for v in variables}

# # print(domain)

# constraint = 10


# def _coin_sums():
#     u = 20
#     count = 0
#     for i in range(0, u // 1 + 1):
#         # if (1 * i) == 200:
#         #     count += 1
#         for j in range(0, u // 2 + 1):
#             # if (1 * i) + (2 * j) == 200:
#             #     count += 1
#             for k in range(0, u // 5 + 1):
#                 # if (1 * i) + (2 * j) + (5 * k) == 200:
#                 #     count += 1
#                 for l in range(0, u // 10 + 1):
#                     # if (1 * i) + (2 * j) + (5 * k) + (10 * l) == 200:
#                     #     count += 1
#                     for m in range(0, u // 20 + 1):
#                         if (1 * i) + (2 * j) + (5 * k) + (10 * l) + (20 * m) == 20:
#                             count += 1
#         #                 for n in range(0, u // 50 + 1):
#         #                     for o in range(0, u // 100 + 1):
#         #                         for p in range(0, u // 200 + 1):
#         #                             if (1 * i) + (2 * j) + (5 * k) + (10 * l) + (20 * m) + (50 * n) + (100 * o) + (200 * p) == 200:
#         #                                 count += 1
#     return count


# def pp(items):
#     for item in items:
#         print(item)
#     print()


count = 0

def coin_sums(coins, target_amt, current_amt):

    global count

    for coin in coins:
        if current_amt == target_amt:
            count += 1
            return
        elif current_amt > target_amt:
            return
        else:
            remaining_coins = [_ for _ in coins if _ <= coin]
            coin_sums(remaining_coins, target_amt, current_amt + coin)
    return
    
    




coin_sums(coins=[200, 100, 50, 20, 10, 5, 2, 1], target_amt=200, current_amt=0)
print(count) # == 73682

