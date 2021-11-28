



def triplet(n):
    max_count = 0
    max_i = 0
    for i in range(3, n):
        count = 0
        for a in range(3, (i-3)//3):
            for b in range(a + 1, (i-1-a)//2):
                c = i - a - b
                if c*c == a*a + b*b:
                    # print(a, b, c)
                    count += 1
        if count > max_count:
            max_count = count
            max_i = i
    return max_i


a = triplet(1000)

print(a) # == 840


        
    