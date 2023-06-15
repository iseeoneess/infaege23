a = [int(x) for x in open('17_1999.txt')]

ans = []

for i in range(len(a) - 2):
    if any(a[i + z] % 12 == 0 for z in [0, 1, 2]) and all(a[i + z] % 3 == 0 for z in [0, 1, 2]):
        ans.append(int((a[i] + a[i + 1] + a[i + 2]) / 3))

print(len(ans), min(ans))