s = open('24_2251 (1).txt').readline()

s = s.split("D")

m = 0

for i in range(len(s) - 2):
    sub = s[i] + "D" + s[i + 1] + 'D' + s[i + 2] + 'D'
    m = max(m, len(sub))
print(m)