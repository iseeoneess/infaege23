from math import *

lst_res = []

for m in range(1, 1001):
    n = 120
    bn = str(n)
    bm = str(m)
    bn_chet = [int(x) for x in bn if (int(x) % 2 == 0 and x != '0')]
    bn_nechet = [int(x) for x in bn if int(x) % 2 != 0]

    bm_chet = [int(x) for x in bm if (int(x) % 2 == 0 and x != '0')]
    bm_neChet = [int(x) for x in bm if int(x) % 2 != 0]

    p_chet = bn_chet + bm_chet
    p_nechet = bn_nechet + bm_neChet

    p_prodChet = prod(p_chet)
    p_prodNeChet = prod(p_nechet)

    res = abs(p_prodNeChet - p_prodChet)
    if res == 29: lst_res.append(m)


print(lst_res)
