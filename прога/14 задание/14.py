x = 2*27**7 + 3**10 - 9
lst = []
while x > 0:
   lst = [x % 3] + lst
   x = x // 3
print(lst.count(0))