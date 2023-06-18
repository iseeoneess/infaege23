k = 0
for s in open('9_8497.csv'):
    a = [int(x) for x in s.split(";")]
    if len(a) == len(set(a)):
        d = sorted(a)
        if (d[0] + d[-1])*3 >= (d[1] + d[2] + d[3])*2:
            k += 1
print(k)