for x in range(2, 1000):
    num = 81 ** 20 - 9 ** x + 50
    lst = []
    d = ""
    while num > 0:
        lst = [num % 9] + lst
        num = num // 9

    # for i in range(len(lst)):
    #     lst[i] = str(lst[i])
    #
    # for g in range(len(lst)):
    #     d = d + "".join(lst[g])

    if sum(lst) == 138:
        print(x, sum(lst))
        break
