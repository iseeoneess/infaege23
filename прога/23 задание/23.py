from functools import *


@lru_cache(None)
def f(c, e, k):
    if c > e: return 0
    if c % 2 == 0: k += 1
    if c == e and k == 6: return 1
    return f(c + 1, e, k) + f(c + 3, e, k) + f(c + 5, e, k)

print(f(3,25,0))