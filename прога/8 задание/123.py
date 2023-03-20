from itertools import product

k = 0
for x in product("0123456789", repeat = 3):
    slovo = "".join(x)
    if slovo[0] != "0" and slovo[0] <= slovo[1] <= slovo[-1]:
        k = k + 1
        print(k, slovo)