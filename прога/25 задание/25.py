def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)

for x in range(1_204_300, 1_204_380 + 1):
    d = div(x)
    if len(d) > 0:
        s = sum(z for z in d if z % 2 == 0)
        if s % 10 == 0 and s != 0:
            print(x, s)