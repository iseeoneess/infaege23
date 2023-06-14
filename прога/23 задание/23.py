from functools import *




@lru_cache(None)
def f(c, p, k):
    if k == 24: {c}
    if p == '+1': return f(c + 7, '+7', k + 1) | f(c * 4, '*4', k + 1)
    if p == '+7': return f(c + 1, '+1', k + 1) | f(c * 4, '*4', k + 1)
    if p == '*4': return f(c + 1, '+1', k + 1) | f(c + 7, '+7', k + 1)
    if p == '': return f(c + 7, '+7', k + 1) | f(c * 4, '*4', k + 1) | f(c + 1, '+1', k + 1)

print(len(f(1,'',0)))