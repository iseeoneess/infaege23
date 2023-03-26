x = 3*16**8 - 4**5 + 3
lst = []
while x > 0:
   lst = [x % 4] + lst
   x = x // 4
print(lst.count(3))