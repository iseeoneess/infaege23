s = open('24_2250.txt').readline()
c = m = k = 0

for i in range(len(s) - 1):
    x, y = s[i], s[i + 1]
    if x == 'A' and k != 1:
        c += 1
        m = max(m, c)
        k += 1
        if y == 'A' and k == 1:
            c = k = 0
    if y == 'A' and k != 1:
        c += 1
        m = max(m, c)
        k += 1
        if x == 'A' and k == 1:
            c = k = 0
    if x == y == 'A': c = k = 0
print(m)