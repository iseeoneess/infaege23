def ccFind(num, cc):
    num = str(num)[::-1]
    lst = []
    for i in range(len(num)):
        lst = [int(num[i]) * cc ** i] + lst
    return sum(lst)


for x in range(1001):
    num1 = f"21011{x}"
    if x == 0:
        num2 = "814"
    else:
        num2 = f"{x}814"
    res1 = ccFind(num1, 12)
    res2 = ccFind(num2, 17)
    resultation = res1 + res2
    if resultation % 27 == 0:
        print(x, resultation // 27)
        break
