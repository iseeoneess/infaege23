def p(x): return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)
k = 0
for x in range(499_999, 2, - 1):
    d = div(x)
    if len(d) > 0:
        s = sum(z for z in d if p(z))
        if s != 0 and s % 10 == 0:
            k += 1
            print(x, s)
    if k == 7: break
