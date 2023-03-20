from itertools import product

k = 0
for x in product("ABCD", repeat = 4):
    slovo = "".join(x)
    if slovo[0] <= slovo [1] <= slovo[2] <= slovo[3]:
        k += 1
        print(k, slovo)