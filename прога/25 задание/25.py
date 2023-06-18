def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0

for x in range(190_201, 190260 + 1):
    d = div(x)
    if len(d) > 0:
        p = [x for x in d if x % 2 == 0]
        if len(p) == 4:
            k += 1
            print(p[-1], p[-2])
    if k == 5: break
