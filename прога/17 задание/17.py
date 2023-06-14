a = [int(x) for x in open('17_2017.txt')]


ans = []



for i in range(len(a)):
    if (a[i] % 16) == 11 and a[i] % 7 == 0 and all(a[i] % z != 0 for z in [6,13,19]):
        ans.append(a[i])

print(sum(x for x in ans), len(ans))