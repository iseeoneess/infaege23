s = open('24_2420.txt').readline()
s = s.replace('C', ' ').replace('D', ' ')
m = 0
for sub in s.split():
    m = max(m, len(sub))

print(m)