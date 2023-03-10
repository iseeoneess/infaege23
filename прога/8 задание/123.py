from itertools import product

k = 0

for i in product("ПУЛЯ", repeat = 6):
    s = "".join(i)
    if s.count("У") == 2:
        k += 1
        print(k, s)