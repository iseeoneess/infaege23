from itertools import permutations

k = 0

for x in permutations("ПЕСКАРЬ"):
    slovo = ''.join(x)
    if slovo[0] != "Ь" and all(sub not in slovo for sub in ["ЬЕ", "ЬА", "ЬР"]):
        k += 1
        print(k, slovo)