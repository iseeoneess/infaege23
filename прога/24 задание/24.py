ans = []
s = open('24_2421.txt').readline()
s = s.replace('D', ' ')
for word in s.split():
    mx = 0
    mx = len(word)
    ans.append(mx)
print(max(ans))
