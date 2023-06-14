from itertools import *
k = 0
for x in product('АВЛОР', repeat = 4):
    s = ''.join(x)
    k += 1
    if s[0] == 'Л':
        print(k, s)