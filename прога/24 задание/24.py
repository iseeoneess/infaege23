s = open('24_2498.txt').readline()
while "XIXIX" in s:
    s = s.replace('XIXIX', "XIX XIX")

s = s.replace("XIX", "*")
print(s.count('*'))