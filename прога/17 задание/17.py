a = [int(x) for x in open('17_2003.txt')]

ans = []

for i in range(len(a)):
    if a[i] % 3 == 0 and all(a[i] % z != 0 for z in [7,17,19,27]):
        ans.append(a[i])

print(len(ans), max(ans))