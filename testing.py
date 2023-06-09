a = 'КАРА'
k = 1
b = 'Т'
i = len(a)
while i > 1:
    c = a[i - 1]
    b = b + c
    i -= k

print(b)