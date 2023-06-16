s = open('24_2426.txt').readline()
ans = []
s = s.replace('C', ' ').replace('B', ' ').replace('A', ' ')
for word in s.split():
    mx = 0
    mx = len(word)
    ans.append(mx)
print(max(ans))