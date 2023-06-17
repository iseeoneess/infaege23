from functools import *
@lru_cache(None)
def f(n): return [x for x in range(7, n, 10) if str(x)[-1] == '7' and x != n if n % x == 0]
k = 0

for n in range(550_001, 10**9):
    z = f(n)
    if len(z) == 3:
        k += 1
        print(n, max(z))
    if k == 5: break