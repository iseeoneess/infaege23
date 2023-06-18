from fnmatch import *

k = 0
for x in range(700_001, 10**10):
    if (not fnmatch(str(x), '*0??3*')) and (not fnmatch(str(x), '*4??2')) and (not fnmatch(str(x), '*1*')):
        if x % 13 == 0:
            k += 1
            print(x, sum(int(z) for z in str(x)))
    if k == 5: break