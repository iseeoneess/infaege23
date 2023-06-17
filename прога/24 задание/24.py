k = 0
for s in open("24_2503.txt"):
    o_cnt = a_cnt = 0
    for i in range(len(s) - 2):
        if s[i] + s[i + 1] + s[i + 2] == 'AOA' and s[i + 3] != 'O' and s[i - 1] != 'O':
            a_cnt += 1
        if s[i] + s[i + 1] + s[i + 2] == 'OAO' and s[i + 3] != 'A' and s[i - 1] != 'A':
            o_cnt += 1
        if i == len(s) - 3:
            if a_cnt > o_cnt:
                k += 1

print(k)