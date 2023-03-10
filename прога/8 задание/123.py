from itertools import product

k = 0

for i in product("ABCWXYZ", repeat = 6):
    s = "".join(i)

    if s[0] in "XYZW" and s[-1] in "XYZW":
        if s[1] in "ABC" and s[2] in "ABC" and s[3] in "ABC" and s[4] in "ABC":
            k += 1
            print(k, s)