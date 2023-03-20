from itertools import permutations

k = 0

for x in permutations("ДЕЙКСТРА", r = 6):
    slovo = "".join(x)
    if any(sub in slovo for sub in ['ЙД','ЙК','ЙС','ЙТ','ЙР']):
        k += 1
        print(k, slovo)