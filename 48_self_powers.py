

self_power = (x**x for x in range(1,1001))

res = 0
for i in self_power:
    res += i

print(str(res)[-10:]) # == 9110846700