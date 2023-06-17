s = open('24_279.txt').readline()

s = s.replace("BOSS", "1")

k = 0

for i in range(len(s)):
    if s[i] == '1' and s[i - 1] != 'J' and s[i + 1] != 'J':
        k += 1
print(k)