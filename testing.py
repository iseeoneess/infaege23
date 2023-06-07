from itertools import *

for x in permutations('0351', r = 2):
    s = ''.join(x)
    if s[0] != '0':
        print(s)