k = 0
for s in open('24_2502.txt'):
    cnt = 0
    for i in range(len(s) - 3):
        if s[i] + s[i + 2] + s[i + 3] == 'KGE':
            cnt += 1
        if cnt >= 1:
            k += 1
            break
print(k)