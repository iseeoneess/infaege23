a = "123"
lst = []
for i in range(0, len(a)):
    lst.append("0")
    lst[i] = a[i]
print(lst)