a = set()
p = set(range(2,21,2))
q = set(range(3,31,3))
r = set(range(12,61,12))

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    R = x in r
    return (not A) <= ((P and Q) <= R)

for x in range(10000):
    if f(x) == 0:
        a.add(x)

print(a)