lst = []

for n in range(100, 1000):
    bn = str(n)
    firstEq = int(bn[0])**2 + int(bn[1])**2
    secondEq = int(bn[1])**2 + int(bn[2])**2
    res = str(max(firstEq,secondEq)) + str(min(firstEq,secondEq))
    if res == '9010':
        lst.append(n)
print(lst)