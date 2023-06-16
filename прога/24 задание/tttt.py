s = open('24_1145 (1).txt').readline()
s = s.replace('D', ' ')
print(min(len(c) for c in s.split()) + 2)


