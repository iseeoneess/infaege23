from fnmatch import *
def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)

for x in range(0, 10**7, 217):
    if fnmatch(str(x), '14?4*'):
        d = div(x)
        nechet_d = [z for z in d if z % 2 != 0]
        print(x, sum(nechet_d))