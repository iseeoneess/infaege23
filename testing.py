for n in range(2, 1001):
    num = 68
    lst = []
    while num > 0:
        lst = [num % n] + lst
        num //= n
    if len(lst) == 4 and lst[-1] == 2:
        print(lst)
# proverka:
print(int("2112", 3))