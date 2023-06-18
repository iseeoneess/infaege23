from fnmatch import *


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)


k = 0
for x in range(0, 10 ** 10):
    if fnmatch(str(x), '?6*6*?6'):
        if x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
            d = div(x)
            sm_d = sum(d)
            print(x, sm_d)
            k += 1
    if k == 7: break
