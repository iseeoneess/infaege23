for x in range(1, 10000):
    k = 0
    def ssWhile(x, c):
        lst = []
        while x > 0:
            lst = [x % c] + lst
            x //= c
        return lst
    frNum = ssWhile(x, 5)
    scNum = ssWhile(x, 2)
    thrNum = str(ssWhile(x, 16))
    if len(frNum) <= 4 and len(scNum) >= 5 and thrNum[-1:-3] == "12":
        k += 1
        print(k, x)
