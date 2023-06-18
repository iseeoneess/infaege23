def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0
for x in range(500_001, 10 ** 10):
    d = div(x)
    if len(d) > 0:
        p = [z for z in d if str(z)[-1] == '8' and z != 8]
        if len(p) > 0:
            k += 1
            print(x, min(p))
    if k == 5: break