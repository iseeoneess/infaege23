s = open('24_1146.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('E', 'A').replace('F', 'A').replace('A', ' ').split()
i = 1
while s.count('D'*i) == 0: i += 1
print(i)
