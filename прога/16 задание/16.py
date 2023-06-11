from functools import *

d = set()

@lru_cache(None)
def f(curr):
    if curr % 2 == 0 and curr < 100: d.add(curr)
    if curr >= 100: return 0
    f(curr + 3)
    f(curr * 3)

f(3)
print(len(d))