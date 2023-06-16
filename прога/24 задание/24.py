s = open('24_1975.txt').readline()
ans = []
s = s.replace('PP', 'P P')
print(s.split('1'))
for wrd in s.split():
    mx = 0
    mx = len(wrd)
    ans.append(mx)
print(max(ans))