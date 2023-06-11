from functools import *


@lru_cache(None)
def f(c, e, k):
    if c > e: return 0
    if c == e and k <= 3: return 1
    if c == e and k > 3: return 0
    return f(c + 2, e, k) + f(c * 3, e, k + 1) + f(c * 5, e, k + 1)
print(f(2,200,0))
