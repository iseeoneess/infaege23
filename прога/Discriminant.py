from math import *

a, b, c = list(map(int, input().split()))


def df(a, b, c):
    dForm = b ** 2 - 4 * a * c
    x1 = (-b + sqrt(dForm)) / (2 * a)
    x2 = (-b - sqrt(dForm)) / (2 * a)
    return x1,x2


yn = input("Sqrts?\n"
           "y/n ")
if yn == 'y':
    k = sqrt(int(input("sqrt ")))
    secondK = int(input('num wth sqrt '))
    b = k * secondK
    y, d = df(a, b, c)
    print(y,d)

else:
    y, d = df(a, b, c)
    print(y,d)
