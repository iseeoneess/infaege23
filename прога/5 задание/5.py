for n in range(110, 1000):
    lst = []
    n = str(n)
    p_1 = int(n[0]) * int(n[1])
    p_2 = int(n[1]) * int(n[2])
    lst.append(p_1)
    lst.append(p_2)
    lst = sorted(lst)[::-1]
    s = ''
    for k in lst:
        s = s + str(k)
    if s == '240':
        print(n)