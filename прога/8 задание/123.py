from itertools import product

k = 0
for i in product("ИГРОК", repeat = 5):
    slovo = "".join(i)
    if slovo.count("И") == 1 and slovo.count("Р") == 1 and slovo.count("Г") == 1 and slovo.count("О") == 1 and slovo.count("К") == 1:
        if slovo[0] != "К" and slovo.count("РОК") == 0:
            k += 1
            print(k, slovo)

