from itertools import permutations, product

k = 0

w = ["ОУ", "УО", "КЛ", 'ЛК', 'ЛН', 'НЛ', 'КН', 'НК']

for x in permutations("КОЛУН"):
    slovo = ''.join(x)
    if all(sub not in slovo for sub in w):
        k += 1
        print(k, slovo)