for x in range(2, 1000):
    num = 64**12 - 8**14 + x
    lst = []
    d = ""
    while num > 0:
        lst = [num % 8] + lst
        num = num // 8

    if lst.count(7) == 12 and lst.count(1) == 1:
        print(x)
