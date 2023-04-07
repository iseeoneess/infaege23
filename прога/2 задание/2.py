from itertools import *


def f(x, y, z):
    return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))


table = [(0, 0, 0), (1, 0, 0), (1, 0, 1)]

for p in permutations("xyz", r = 3):
    if [f(**dict(zip(p, row))) for row in table] == [1,1,1]:
        print(*p)
