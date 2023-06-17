def f(n):
    k = sorted([x for x in range(2, n) if n % x == 0 and x != n])
    if len(k) == 0: return 0
    return sum(k)


k = 0
for i in range(150_001, 10**10):
    d = f(i)
    if d % 13 == 10:
        k += 1
        print(i, d)
    if k == 7: break
