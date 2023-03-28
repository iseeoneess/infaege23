def ccFind(num, cc):
    lst = []
    num = str(num)[::-1]
    for i in range(len(num)):
        lst = [int(num[i]) * cc ** i] + lst
    return sum(lst)
print(ccFind(3364, 11))