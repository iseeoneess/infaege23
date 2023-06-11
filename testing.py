from itertools import *
d = []
for p in set(permutations('123321')):
    s = ''.join(p)
    d.append(s)
print(len(d))