def f(c,e, f11):
    if c == 11: f11 = 1
    if c > e or c == 15: return 0
    if c == e: return f11 == 1
    return f(c + 1, e, f11) + f(c * 2, e, f11) + f(c * 3, e, f11)
print(f(1,25,0))