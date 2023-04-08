def f(x): return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))

for a in range(1, 100000):
    if all(f(x) for x in range(1, 1000000)):
        print(a)
        break