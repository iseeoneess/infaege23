s = open('24_1302.txt').readline()
s = s.replace('ZZ', '1').replace('X1Y', ' ').replace('Y1X', ' ')
ans = []
print(s.split()[:10])
for wrd in s.split():
    mx = 0
    mx = len(wrd)
    ans.append(mx)
print(max(ans))
