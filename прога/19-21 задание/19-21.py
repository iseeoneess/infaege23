from functools import *


@lru_cache(None)
def f(a, b, m):
    if a >= 40 or b >= 40: return m % 2 == 0
    if m == 0: return 0
    if a > b: h = [f(a + 1, b, m - 1), f(a + 2, b, m - 1), f(a + 3, b, m - 1), f(a, b * 2, m - 1)]
    if a < b: h = [f(a, b + 1, m - 1), f(a, b + 2, m - 1), f(a, b + 3, m - 1), f(a * 2, b, m - 1)]
    if a == b: h = [f(a, b + 1, m - 1), f(a, b + 2, m - 1), f(a, b + 3, m - 1),
                    f(a + 1, b, m - 1), f(a + 2, b, m - 1), f(a + 3, b, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', sum(min([(s, k) for s in range(1, 40) for k in range(1, 40) if f(s,k,1)])))
print('20)', [s for s in range(1, 40) if not f(11,s,1) and f(11,s,3)])
print('21)', [s for s in range(1, 40) if not f(31,s,2) and f(31,s,4)])

