a = [int(x) for x in open('17_2402.txt')]

ans = []
def f(n, cc):
    lst = []
    while n > 0:
        lst += [n % cc]
        n //= cc
    return ''.join([str(x) for x in lst[::-1]])

for i in range(len(a) - 2):
    if any(f(a[i + g], 3)[-1] == '2' for g in [0,1,2]):
        ans.append(min(a[i], a[i + 1], a[i + 2]))

print(len(ans), sum(ans))