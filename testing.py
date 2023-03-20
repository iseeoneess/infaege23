d = [1, 2 ,3]
def F(n):
    if n in d:
        return 1
    if n > 3 and n % 1 == 0:
        return F(n-3) + F(n - 2)
print(F(10))