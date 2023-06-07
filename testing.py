from itertools import *

for x in product('0123456789ab'):
    s = ''.join(x)
    s = int(s, 12)
    s = str(s)
    c = 0
    k = ['0', '1', '4', '5', '7', '8', 'a', 'b']
    nk = ['3', '6', '9']
    if len(s) == 7:
        if ((s[0] in k) and (s[2] in k) and (s[4] in k) and (s[6] in k)) and (
                (s[1] in nk) and (s[3] in nk) and (s[5] in nk)):
            if s[0] != '0':
                c += 1
                print(f'{s} k')
        if ((s[0] in nk) and (s[2] in nk) and (s[4] in nk) and (s[6] in nk)) and (
                (s[1] in k) and (s[3] in k) and (s[5] in k)):
           if s[0] != '0':
               c += 1
               print(f'{s} nk')
        print(c)