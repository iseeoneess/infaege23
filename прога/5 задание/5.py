for n in range(1,10001):
    bn = bin(2*n)[2:]
    for i in range(2):
        if bn.count('1') % 2 == 0: bn += '0'
        else: bn += '1'
    r = int(bn,2)
    if r >1017:
        print(n, r)
        break