def f(x): return (x & 107 == 0) <= ((x & 55 != 0) <= (x & a != 0))

for a in range(1, 1000000):
    if all(f(x) for x in range(1,1000000)):
        print(a)
        break