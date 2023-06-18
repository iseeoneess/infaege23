from fnmatch import *
def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)

for x in range(0, 10**7):
    if fnmatch(str(x), '9?*55*7'):
        d = div(x)
        if len(d) > 0:
            sm_d = sum(d)
            print(x, sm_d % 21)