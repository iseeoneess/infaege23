lst = []

for n in range(1, 10001):
    bn = bin(n)[2:]
    chetnK = 0
    ne_chentK = 0
    for i in range(len(bn)):
        if i % 2 != 0 and bn[i] == '1':
            chetnK += 1
        if i % 2 == 0 and bn[i] == '0':
            ne_chentK += 1

    r = abs(chetnK - ne_chentK)

    if r == 5: lst.append(n)
print(min(lst))