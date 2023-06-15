a = [int(x) for x in open('17_2400.txt')]

ans = []

for i in range(len(a) - 1):
    if any(a[i + g] < 0 for g in [0, 1]) and sum(x for x in [a[i], a[i + 1]]) >= 100:
        ans.append(a[i] * a[i + 1])

print(len(ans), max(ans))
