s = open('24_1040.txt').readline()

for word in 'qwertyuiopasdfghjklzxcvbnm':
    s = s.replace(word, ' ')

ans = []
for word in s.split():
    mx = 0
    mx = len(word)
    ans.append(mx)
print(max(ans))