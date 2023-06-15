from itertools import *

def f(x):
    d = 17 <= x <= 58
    c = 29 <= x <= 80
    a = a1 <= x <= a2
    return d <= (((not c) and (not a)) <= (not d))

ox = [i / 6 for i in range(17*6,80*6 + 1)]
m = []

for a1,a2 in combinations(ox, 2):
    if all(f(x) for x in ox): m.append(a2-a1)
print(round(min(m)))