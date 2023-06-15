a = [int(x) for x in open('17_2309.txt')]

ans11 = []
ans17 = []

for i in range(len(a)):
    if a[i] % 11 == 0: ans11.append(a[i])
    if a[i] % 17 == 0: ans17.append(a[i])

print(len(ans11), min(ans11))