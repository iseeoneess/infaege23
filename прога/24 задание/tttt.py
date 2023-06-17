s = open('24_4546.txt').readline()
m = 0
for j in range(4):
    c = 0
    for i in range(j, len(s) - 3, 3):
        if any(s[i] + s[i + 1] + s[i + 2] == z for z in ["AAA", "ABA","ACA","CAC","CBC","CCC"]):
            c += 1
            m = max(m, c)
        else: c = 0
print(m)

