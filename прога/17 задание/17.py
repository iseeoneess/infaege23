a = [int(x) for x in open('17_2016.txt')]

ans = []

for i in range(len(a)):
    if a[i] % 13 == 7 and all(a[i] % z != 0 for z in [7,11]):
        ans.append(a[i])

print(max(ans) - min(ans), len(ans))