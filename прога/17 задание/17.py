a = [int(x) for x in open('17_2310.txt')]

numbers_4 = [x for x in a if str(x)[-1] == '4']
min_number_4 = min(numbers_4)
max_number_4 = max(numbers_4)
sum_number_4 = min_number_4 + max_number_4
ans = []

for i in range(len(a) - 1):
    if a[i] + a[i + 1] < sum_number_4:
        ans.append(a[i] + a[i + 1])

print(len(ans), max(ans))