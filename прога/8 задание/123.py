from itertools import product
k = 0
for x in product("АНИМЕ", repeat = 4):
    slovo = "".join(x)
    k += 1

for x in product("АНИМЕ", repeat = 5):
    slovo = "".join(x)
    k += 1

for x in product("АНИМЕ", repeat = 6):
    slovo = "".join(x)
    k += 1
print(k)