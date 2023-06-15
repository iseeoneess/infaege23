a = [int(x) for x in open('17_2002.txt')]

ans = []
for i in range(len(a) - 3):
    d = [a[i], a[i + 1], a[i + 2], a[i + 3]]
    if len(d) == len(set(d)) and max(d) - min(d) > 1000 and a[i] > a[i + 1] > a[i + 2] > a[i + 3]:
        ans.append(a[i] + a[i + 1] + a[i + 2] + a[i + 3])

print(len(ans), min(ans))
