from functools import *

lst_res = []
@lru_cache(None)
def f(n):
    if n > 30: return n ** 2 + 5 * n + 4
    if n <= 30 and n % 2 == 0: return f(n + 1) + 3 * f(n + 4)
    if n <= 30 and n % 2 != 0: return 2 * f(n + 2) + f(n + 5)

for n in range(1, 1001):
    if sum(int(x) for x in str(f(n))) == 27: lst_res.append(n)

print(len(lst_res))