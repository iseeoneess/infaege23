x = 64**30 + 2**300 - 4
lst = []
while x > 0:
   lst = [x % 8] + lst
   x = x // 8
print(lst.count(7))