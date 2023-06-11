def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e:
        if int(str(c)[0]) < 9 and int(str(c)[1]) < 9: return f(c + 1, e) + f(c + 11, e)
        if int(str(c)[0]) == 9 and int(str(c)[1]) < 9: return f(c + 1, e) + f(c + 1, e)
        if int(str(c)[0]) < 9 and int(str(c)[1]) == 9: return f(c + 1, e) + f(c + 10, e)

print(f(25, 51))