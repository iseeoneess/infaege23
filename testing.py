def f(x):
    return 120 % a == 0 and ((x % 36 == 0) <= ((x % a != 0) <= (x % 45 != 0)))

for a in range(1, 100000):
    if all(f(x) for x in range(1,1000)): print(a)