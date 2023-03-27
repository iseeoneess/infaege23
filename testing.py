for n in range(1, 10000):
    def ssWhile(x, c):
        lst = []
        while x > 0:
            lst = [x % c] + lst
            x //= c
        return lst
    frNum = ssWhile(n, 7)
    scNum = ssWhile(n, 6)
    thrNum = ssWhile(n, 13)
    if len(frNum) == 2 and len(scNum) == 3 and thrNum[-1] == 3: print(n)