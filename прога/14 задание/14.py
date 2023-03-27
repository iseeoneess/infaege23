for n in range(2, 1000):
    num = 2 + 3*n + n**2
    num2 = 11
    equal = 4 + 2*(n+1) + pow((n + 1), 2)
    if num + num2 == equal:
        print(n)
        break
# proverka:
print(int("132", 6), int("13", 8), int("123", 7))

# for n in range(2, 100001):
#     try:
#         num1 = 132
#         num2 = 13
#         num3 = 124
#
#
#         def lstStr(num, n):
#             d = ""
#             lst = []
#             while num > 0:
#                 lst = [num % n] + lst
#                 num //= n
#             for i in range(len(lst)):
#                 lst[i] = str(lst[i])
#             for g in range(len(lst)):
#                 d = d + "".join(lst[g])
#             return d
#
#
#         res1 = int(lstStr(num1, n), n)
#         res2 = int(lstStr(num2, 8), 8)
#         res3 = int(lstStr(num3, n + 1), n + 1)
#         if res1 + res2 == res3:
#             print(n)
#             break
#     except:
#         pass