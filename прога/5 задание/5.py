lst_res = []


for n in range(2, 10000001):
    bn = n
    if bn % 3 == 0: bn = int(bn / 3)
    else: bn -= 1
    if bn % 5 == 0: bn = int(bn / 5)
    else: bn -= 1
    if bn % 11 == 0: bn = int(bn / 11)
    else: bn -= 1
    if bn == 8: lst_res.append(n)

print(len(lst_res))
