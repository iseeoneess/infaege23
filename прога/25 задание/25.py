def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0

for x in range(550_001, 10 ** 10):
    d = div(x)
    print(d)
    input()
    if len(d) > 0:
        f = sum(x for x in d) // len(d)
        if f % 31 == 13:
            k += 1
            print(x, f)
    if k == 5: break