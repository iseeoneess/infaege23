k = 0
for s in open('24_587 (1).txt'):
    if s.count("B") / s.count("A") >= 1.05:
        k += 1
print(k)