from itertools import *


def f(x, y, z, w):
    return (not w) and ((y or z) <= ((not x) and y))


for a in product([0, 1], repeat=3):
    table = [(a[0], a[1], a[2], 1), (a[0], a[1], 1, a[2]), (a[0], 1, 1, a[1])]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [1,1,1]:
                print(p)