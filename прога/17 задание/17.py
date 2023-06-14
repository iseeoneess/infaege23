from math import *

a = [int(x) for x in open('17_1994.txt')]

ans1 = []
ans2 =[]
for i in range(len(a) - 1):
   if (a[i] * a[i + 1]) > 0 and (a[i] + a[i + 1]) % 7 == 0:
       ans2.append(a[i]*a[i + 1])

print(len(ans1))
print(min(ans2))