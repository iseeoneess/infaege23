from itertools import permutations, product

k = 0

for x in set(permutations("МИМИКРИЯ")):

    slovo = "".join(x)
    k += 1
    print(k, slovo)
