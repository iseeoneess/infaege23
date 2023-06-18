def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0
for x in range(300_001, 10 ** 10):
    d = div(x)
    if len(d) > 0:
        p = [z for z in d if z % 3 == 0 and z != x]
        if len(p) == 5:
            k += 1
            print(x, max(p))
    if k == 4: break