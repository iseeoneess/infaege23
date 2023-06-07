lst_res = []

for n in range(1, 100001):
    bn = str(n)
    chetnSum = sum(int(x) for x in bn if int(x) % 2 == 0)
    if len(bn) == 1: chet_indexNum = 0
    else: chet_indexNum = sum(int(bn[z]) for z in range(len(bn)) if z % 2 != 0)
    res = abs(chetnSum - chet_indexNum)
    if res == 9: lst_res.append(n)

print(min(lst_res))