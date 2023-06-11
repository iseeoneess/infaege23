from functools import *

d = set()


@lru_cache(None)
def f(c,k):
    if k == 8:
        if 1000 <= c <= 1024:
            d.add(c)
    else:
        f(c + 1, k + 1)
        f(c + 5, k + 1)
        f(c * 3, k + 1)

f(1,0)

print(len(d))