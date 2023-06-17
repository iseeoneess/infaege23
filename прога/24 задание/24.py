s = open('24_223.txt').readline()

k = 0

for i in range(len(s) - 2):
    if any(z  == s[i] + s[i + 1] + s[i + 2] for z in ['TIK', 'TOK']):
        k += 1

print(k)