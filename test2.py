from itertools import *

for x in product('0123456789abcde', repeat = 5):
    k = ''.join(x)
    if k[0] != '0':
        s = str(int(k, 15))
        k_2 = ['0','2','4','6','8','10','12','14']
        k_3 = ['3','6','9','12']

        if all(z in s[i] for i in range(len(s)) for z in k_2 if i % 2 == 0) and all(z in s[i] for i in range(len(s)) for z in k_3 if i % 2 != 0):
            print(s)
