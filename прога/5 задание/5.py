from itertools import *

lst = []
for n in range(100, 1000):
    lst_nums = [] # буферные списки только внутри цикла, иначе переполниться стэк!
    for x in permutations(f'{n}', r = 2):
        s = ''.join(x)
        if s[0] != '0':
            lst_nums.append(int(s))
    res = max(lst_nums) - min(lst_nums)

    if res == 5:
        lst.append(n)
print(lst)