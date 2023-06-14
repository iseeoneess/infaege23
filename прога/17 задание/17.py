a = [int(x) for x in open('17_2015.txt')]

ans = []

for i in range(len(a)):
    if any(str(a[i])[-1] == z for z in ['5','7']) and all(a[i] % z != 0 for z in [9,11]):
        ans.append(a[i])

print(len(ans), min(ans) + max(ans))