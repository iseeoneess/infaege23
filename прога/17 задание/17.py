a = [int(x) for x in open('1_17.txt')]
ans = []
avgDuo = max([z for z in a if len(str(z)) == 2])

for i in range(len(a) - 1):
    w, y = a[i], a[i + 1]
    if (len(str(y)) == 2) + (len(str(w)) == 2) == 1 and (w + y) % avgDuo == 0:
        ans.append(w + y)
print(len(ans), max(ans))
