def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)
k = 0
for x in range(250_201, 10**10):
    d = div(x)
    if len(d) > 0:
        p = max(d) + min(d)
        if p % 123 == 17:
            k += 1
            print(x, p)
    if k == 5: break
