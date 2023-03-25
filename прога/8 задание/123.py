from itertools import permutations, product

k = 0

for x in product("АГИЛМОРТ", repeat = 4):
    slovo = ''.join(x)
    k += 1
    if slovo[-2] == "И" and slovo[-1] == "М":
        print(k, slovo)