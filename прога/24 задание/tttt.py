s = open('24_21.txt').readline()

c = m = 0
k = 0
for j in 0,1:
    c = 0 
    for i in range(j, len(s) - 1, 2):
        if s[i] != s[i + 1]:
            c += 1
            m = max(m,c)
        else: c = 0
print(m)
