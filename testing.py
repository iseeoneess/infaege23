num = 15
lst = []

while num > 0:
    lst = [num % 3] + lst
    num //= 3

print(lst)