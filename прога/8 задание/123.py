from itertools import product
k = 0

for x in product("ЖИРАФ", repeat = 5):
    slovo = ''.join(x)
    if slovo.count("Ж") == 1 and (slovo[0] != 'Ф' and slovo[-1] != "Р"):
        k += 1
        print(k, slovo)