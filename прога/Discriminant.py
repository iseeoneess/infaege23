from math import *

a, b, c = list(map(int, input().split()))

dForm = b ** 2 - 4 * a * c
x1 = (-b + sqrt(dForm)) / (2 * a)
x2 = (-b - sqrt(dForm)) / (2 * a)

print(f'first: {x1} '
      f'second: {x2}')
