from functools import *
@lru_cache(None)
def f(n):
    k = [x for x in range(1, n + 1, 2) if z(x)]
    if len(set(k)) == 5: return k
    return 0
@lru_cache(None)
def z(k):
    for x in range(1, k + 1):
        return k % x == 0



for i in range(55_000_000, 60_000_001):
    d = f(i)
    if d != 0:
        print(i, max(d))

