def p(x): return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def div(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0: d |= {i, x // i}
    return sorted(d)

for x in range(125_697, 125_721 + 1):
    d = div(x)
    if len(d) > 0:
        df_d = [z for z in d if p(z)]
        if len(df_d) == 2:
            prd = df_d[0]*df_d[1]
            if x == prd: print(df_d[0], df_d[1])

