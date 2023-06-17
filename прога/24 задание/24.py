s = open('24_314.txt').readline()

s = s.replace('STOCK', "*")

k = 0

for i in range(len(s) - 2):
    if s[i] + s[i + 1] + s[i + 2] == 'OCK':
        k += 1
print(k)