def f(c, e):
    if c > e: return 0
    if c == e: return 1
    if c < e: return f(c + 1, e) + f(c * 2, e) + f(2*c + 1, e) + f(c * 10, e)

print(f(1, 15))