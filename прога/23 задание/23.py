from functools import *


@lru_cache(None)
def f(c, e, k):
    if c > e: return 0
    if c == e and k == 1: return 1
    if c == e and k != 1: return 0
    if c < e: return f(c + 1, e, k) + f(c + 2, e, k) + f(c * 2, e, k + 1)


print(f(2, 12, 0))
