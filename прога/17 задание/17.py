a = [int(x) for x in open('17_2401.txt')]

ans = []

for i in range(len(a) - 1):
    if 50 <= sum(abs(x) for x in [a[i], a[i + 1]]) <= 200:
        ans.append([a[i], a[i + 1]])

print(len(ans), ans)