from functools import *

d = set()

@lru_cache(None)
def f(c, k):
    if k == 15:
        d.add(c)
    if k != 15:
        f(c * 2, k + 1)
        f(c * 2 + 1, k + 1)

f(1,0)
print(len(d))
