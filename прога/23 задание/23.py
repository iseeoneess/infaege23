from functools import *

d = set()
@lru_cache(None)
def f(c, e, cnt):
    if c > e: return 0
    if c % 2 != 0: cnt += 1
    if c == e and cnt == 1: return 1
    return f(c + 1, e, cnt) + f(c + 2, e, cnt) + f(c*2, e, cnt)

print(f(2,40,0))