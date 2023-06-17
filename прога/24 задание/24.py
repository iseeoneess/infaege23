s = open('24_2500.txt').readline()
k = 0
for i in range(len(s) - 3):
    if s[i] + s[i + 2] + s[i + 3] == 'GME': k += 1
print(k)