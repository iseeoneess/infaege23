from itertools import *


def f(x, y, z, w):
    return (not (z and (not w))) or ((z <= w) == (x <= y))


for a in product([0, 1], repeat=6):
    table = [(1, a[0], a[1], a[2]), (1,1,a[3],1), (1, a[4], a[5], 1)]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in table] == [0,0,0]:
                print(*p, sep = "")