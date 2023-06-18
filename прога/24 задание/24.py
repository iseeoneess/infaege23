s = open('24_1143.txt').readline()

k = 0

for i in range(len(s) - 6):
    if s[i] +s[i + 6] == 'AF':
        k += 1

for i in range(len(s) - 7):
    if s[i] +s[i + 7] == 'AF':
        k += 1

for i in range(len(s) - 8):
    if s[i] +s[i + 8] == 'AF':
        k += 1

for i in range(len(s) - 9):
    if s[i] +s[i + 9] == 'AF':
        k += 1

print(k)