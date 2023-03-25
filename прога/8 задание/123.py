from itertools import permutations, product

k = 0

for x in product("АИМРЯ", repeat = 4):
    slovo = ''.join(x)
    k += 1
    if k == 211:
        print(k, slovo)