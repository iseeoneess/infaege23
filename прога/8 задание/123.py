from itertools import permutations, product

k = 0

for x in permutations("ВАЙФУ", r = 4):
    slovo = "".join(x)
    if slovo [0] != "Й" and "ВФ" not in slovo and "ФВ" not in slovo:
        k += 1
        print(k, slovo)
