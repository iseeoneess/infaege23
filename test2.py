def f(c, e, f6):
    if c == 6: f6 = 1
    if c < e: return 0
    if c == e: return f6 == 1
    return f(c - 2, e, f6) + f(c // 3, e,f6)
print(f(200,2, 0))