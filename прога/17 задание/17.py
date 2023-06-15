a = [int(x) for x in open('17_2239.txt')]

max19 = max([x for x in a if x % 19 == 0])
ans = []

for i in range(len(a) - 1):
    if (a[i] > max19) + (a[i + 1] > max19) >= 1:
        ans.append(sum([a[i], a[i + 1]]))
print(len(ans), min(ans))