s = open('24_865.txt').readline()
ans = []
s = s.replace('C', ' ').replace('F', ' ')

for word in s.split():
    mx = 0
    mx = len(word)
    ans.append(mx)
print(max(ans))