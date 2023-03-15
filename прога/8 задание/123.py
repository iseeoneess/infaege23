from itertools import *

k = 0

for x in product("01234", repeat = 6):
    slovo = "".join(x)
    if (slovo[0] in "234") and (slovo[-1] in "012"):
        k += 1
        print(k, slovo)