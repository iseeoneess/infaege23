def f(x): return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)

for a in range(1, 10000):
    if all(f(x) for x in range(10000)): print(a)