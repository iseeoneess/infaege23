s = open("24_5171.txt").readline()

s = s.replace("B", "D").replace("E", "D").replace("F", "D").replace("D", "*")

m = 0
sub = ""
for i in range(2, len(s) - 1):
    if s[i] + s[i + 1] == "CA":
        sub += "CA"
        m = max(m, len(sub))
    if s[i] == "C" and s[i - 2] + s[i - 1] == "CA":
        sub += "C"
        m = max(m, len(sub))
        sub = s[i]
print(m)
