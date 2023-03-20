from itertools import product

k = 0
for x in product("ВИШНЯ", repeat = 6):
    slovo = "".join(x)
    if slovo.count("В") <= 1 and slovo[0] != "Ш" and slovo[-1] not in "ИЯ":
        k += 1
        print(k, slovo)