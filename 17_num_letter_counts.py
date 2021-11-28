

num_to_word_basic = {0: '',
             1: 'one',
             2: 'two',
             3: 'three',
             4: 'four',
             5: 'five',
             6: 'six',
             7: 'seven',
             8: 'eight',
             9: 'nine',
             10: 'ten',
             11: 'eleven',
             12: 'twelve',
             13: 'thirteen',
             14: 'fourteen',
             15: 'fifteen',
             16: 'sixteen',
             17: 'seventeen',
             18: 'eighteen',
             19: 'nineteen',
             20: 'twenty',
             30: 'thirty',
             40: 'forty',
             50: 'fifty',
             60: 'sixty',
             70: 'seventy',
             80: 'eighty',
             90: 'ninety',
             1000: 'onethousand'}


def hundreds():
    for i in range(1, 10):
        num_to_word_basic[i * 100] = num_to_word_basic[i] + 'hundred' + 'and'


def create_num_to_word(n):
    for i in range(1, n + 1):
        if i not in num_to_word:
            num_to_word[i] = create_num(i)
    

def create_num(n):
    a = list(str(n))
    # print(a)
    b = [int(num)*(10**i) for i, num in enumerate(reversed(a))]
    b.reverse()
    print(b)
    if b[-2] == 10 and b[-1] > 0:
        b = b[:-2] + [b[-2] + b[-1]]
    res = ''
    for num in b:
        res += num_to_word_basic[num]
    print(res)
    return res


def hundreds_w_out_and():
    for i in range(1, 10):
        num_to_word[i * 100] = num_to_word[i] + 'hundred'


def count_num_letters(n):
    res = 0
    for num in range(1, n + 1):
        res += len(num_to_word[num])

    print(res)


hundreds()
num_to_word = num_to_word_basic
create_num_to_word(1000)
hundreds_w_out_and()
# n = 115
# print(num_to_word[n])
# print(len(num_to_word[n]))
count_num_letters(1000) # 21124



        
