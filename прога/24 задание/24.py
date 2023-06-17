s = open('24_2501.txt').readline()
k = 0
for i in range(len(s) - 5):
    if s[i] + s[i + 2] + s[i + 4]  == 'AAA': k += 1
print(k)