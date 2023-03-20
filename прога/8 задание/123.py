from itertools import product

k = 0
for x in product("ГЕПАРД", repeat = 5):
    slovo = "".join(x)
    if slovo.count("Г") == 1 and slovo[0] != "А" and slovo[-1] != "Е":
        k += 1
        print(k, slovo)