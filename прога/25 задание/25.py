def p(x): return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)

for x in range(25_317, 51_237 + 1):
    d = div(x)
    chk_D = [z for z in d if p(z)]
    if len(chk_D) >= 6: print(x, max(chk_D))