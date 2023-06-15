a = [int(x) for x in open('17_2403.txt')]

ans = []


def f(n):
    lst = []
    while n > 0:
        lst = [n % 8] + lst
        n //= 8
    return ''.join([str(x) for x in lst])

for i in range(len(a) - 1):
    if (a[i] % 9 == 0 and abs(a[i + 1]) % 8 == 3 and a[i + 1] % 9 != 0)\
            or (a[i + 1] % 9 == 0 and abs(a[i]) % 8 == 3 and a[i] % 9 != 0):
        ans.append(max(a[i], a[i + 1]))
print(len(ans), max(ans))