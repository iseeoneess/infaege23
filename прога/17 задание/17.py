a = [int(x) for x in open('17_2399.txt')]

ans = []
sm_ALL = sum(int(i) for z in a if z % 35 == 0 for i in str(z))

def hexx(n):
    lst = []
    while n > 0:
        lst = [n % 16] + lst
        n //= 16
    return ''.join([str(x) for x in lst])


for i in range(len(a) - 1):
    if (a[i] > sm_ALL and hexx(a[i + 1])[-2:] == str(int('ef',16)) and a[i + 1] < sm_ALL) \
            or (a[i + 1] > sm_ALL and hexx(a[i])[-2:] == str(int('ef',16)) and a[i] < sm_ALL):
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))
