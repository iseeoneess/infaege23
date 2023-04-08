def f(x):
    return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)

for a in range(1, 100):
    if all(f(x) for x in range(1, 100000)): print(a)
