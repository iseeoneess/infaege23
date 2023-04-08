def f(x): return ((x % 15 == 0) and (x % 21 != 0)) <= ((x % a != 0) or (x % 15 != 0))

for a in range(1, 100):
    if all(f(x) for x in range(10000)): print(a)