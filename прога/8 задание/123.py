from itertools import permutations, product

k = 0

for x in product("ЕЛМРУ", repeat = 4):
    slovo = ''.join(x)
    k += 1
    print(k, slovo)