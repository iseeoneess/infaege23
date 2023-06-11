from functools import *

@lru_cache(None)
def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c + 2, e) + f(c + 4, e) + f(c + 5, e)


for e in range(1, 100):
    if f(31, e) == 1001: print(e)
