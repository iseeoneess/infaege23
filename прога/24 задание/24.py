s = open('24_1428.txt').readline()

s = s.replace('XY', "X Y").replace("XZ", "X Z").split()
print(max(len(c) for c in s))