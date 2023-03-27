num = 3364

cc = 12

num = str(num)[::-1]
lst = []

for i in range(len(num)):
    lst = [int(num[i]) * cc**i] + lst

print(sum(lst))