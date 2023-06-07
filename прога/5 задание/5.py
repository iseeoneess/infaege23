for n in range(1, 101):
    bn = bin(n)[2:]
    if bn[-1] == '0':
        bn = bn[:-1][::-1]
    else:
        bn = bn[::-1]
    r = int(bn, 2)
    if r == 13:
        print(n,r)
