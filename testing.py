from itertools import *

k = 0

for x in permutations('РУСЛАН'):
    s = ''.join(x)
    if all(z not in s for z in ['УА', 'АУ', 'УУ', 'АА']):
        k += 1
        print(k, s)