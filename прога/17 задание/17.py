a = [int(x) for x in open('17_2238.txt')]

sr_ALL = sum(a) / len(a)

ans = []

for i in range(len(a) - 2):
    d = [a[i], a[i + 1], a[i + 2]]
    if all(z > sr_ALL for z in d) \
            or all(z > sr_ALL for z in [a[i], a[i + 1]]) \
            or all(z > sr_ALL for z in [a[i], a[i + 2]]) \
            or all(z > sr_ALL for z in [a[i + 1], a[i + 2]]):
        ans.append(sum(d))

print(len(ans), max(ans))
