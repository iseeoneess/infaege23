from math import prod


def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0
for x in range(400_000_001, 10 ** 20):
    d = div(x)
    if len(d) >= 5:
        PN = d[0] * d[1] * d[2] * d[3] * d[4]
        if PN <= x and str(PN)[-2:] == '17':
            k += 1
            print(PN, d[4])
    if k == 5: break