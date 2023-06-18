from fnmatch import *
def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)
k = 0
for x in range(65_001, 10**10):
    if fnmatch(str(x), '6*97*5?'):
        d = div(x)
        if len(d) > 0:
            check_chet = [z for z in d if z % 2 == 0]
            if len(check_chet) >= 4:
                k += 1
                print(x, sum(check_chet))

    if k == 7: break