from itertools import product

k = 0

for i in product("САЛО", repeat = 6):
    s = "".join(i)
    if 1 <= s.count("О") <= 3:
        k += 1
        print(k, s)

## Допустил ошибку минимум 1 раз, но не больше трех!