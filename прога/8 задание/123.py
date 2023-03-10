from itertools import product

k = 0

for i in product("ЛОДКА", repeat = 4):
    s = "".join(i)
    if s.count("О") >= 2:
        k += 1
        print(k, s)