s = open('24_8166.txt').readline()
s = s.replace("B", "A").replace("C", "A")
while 'AA' in s: s = s.replace("AA","*")

c = m = 0
for i in range(len(s)):
    if s[i] == '*':
        c += 1
        m = max(m, c)
    else: c = 0

print(m)