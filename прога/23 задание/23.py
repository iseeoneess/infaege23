def f(c,e):
    if c > e: return 0
    if c == e: return 1
    if c % 2 == 0 and c < e: return f(c + 1, e) + f(c * 1.5, e)
    if c % 2 != 0 and c < e: return f(c + 1, e)

print(f(1,20))