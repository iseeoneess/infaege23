k = 0
for s in open('24_859.txt'):
    if s.count("S") == s.count("X"):k += 1
print(k)