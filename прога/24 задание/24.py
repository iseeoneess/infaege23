s = open('24_2497.txt').readline()

k = 0

for i in range(len(s) - 4):
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] + s[i + 4] == 'XVIII':
        k += 1

print(k)