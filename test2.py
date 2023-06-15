n = 5
lst = []
while n > 0:
    lst = [n % 8] + lst
    n //= 8
print(lst)