from functools import *

lst_res = []
@lru_cache(None)
def f(n):
    if n <= 18: return n + 3
    if n > 18 and n % 3 == 0: return (n // 3) * f(n // 3) + n - 12
    if n > 18 and n % 3 != 0: return f(n - 1) + n ** 2 + 5

for n in range(1, 1001):
    k = str(f(n))
    if all(int(p) % 2 == 0 for p in k): lst_res.append(n)
    else:continue

print(len(lst_res))