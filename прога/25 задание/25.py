def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d = d | {i, x//i}
    return sorted(d)

for x in range(81_234, 134_689):
    d = div(x)
    if len(d) == 3:
        print(*d)
