from itertools import product

k = 0
for x in product("AB123", repeat = 8):
    slovo = "".join(x)
    if slovo.count("A") + slovo.count("B") == 2:
        k += 1
        print(k, slovo)