lst = []

for n in range(1000, 10000):
    bn = str(n)
    p_1 = str(int(bn[0]) * int(bn[1]))
    p_2 = str(int(bn[2]) * int(bn[3]))
    res = int(str(min(int(p_1), int(p_2))) + str(max(int(p_1), int(p_2))))
    if res == 1214: lst.append(n)

print(lst)
