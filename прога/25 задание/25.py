from fnmatch import fnmatch

for x in range(0, 10**9 + 1, 169):
    if fnmatch(str(x), "123*567?"):
        print(x, x // 169)