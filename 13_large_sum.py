

filename = '113_large_sum.txt'



with open(filename, 'r') as f:

    res = 0
    line = f.readline().replace('\n', '')
    while line != '':
        res += int(line)
        line = f.readline().replace('\n', '')
         
        

    print(str(res)[:10])

