from itertools import *

a = set(range(1000))
b = set(range(3, 13, 3))
c = set(range(1,7))

def f(x):
    A = x in a
    B = x in b
    C = x in c
    return (not ((not A) and B)) or (not C)

for x in range(1, 1000):
    if f(x) == 0:
        a.remove(x)
print(a)