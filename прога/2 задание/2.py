from itertools import *


def f(x, y, z, w):
    return ((w <= y) or (not (y <= z))) and (not x) and (not (x == z))


for a in product([0, 1], repeat=5):
    table = [(0, a[0], 1, a[1]), (1, a[2], a[3], 1), (0, a[4], 1, 1)]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [1,1,1]:
                print(*p, sep = "")