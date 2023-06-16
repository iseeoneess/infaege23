a = [int(x) for x in open('17_6270.txt')]

chek_lst = []

ans = []
for z in range(len(a) - 1):
    x = a[z]
    y = a[z + 1]
    if (abs(x) % 10 == 7) != (abs(y) % 10 == 7):
        chek_lst.append(abs(x*x - y*y))


for i in range(len(a) - 1):
    x = a[i]
    y = a[i + 1]
    if any((x - y)**2 < z for z in chek_lst) and (abs(x) % 10 == 7) != (abs(y) % 10 == 7):
        ans.append((x - y)**2)

print(len(ans), min(ans))