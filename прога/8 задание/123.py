def solution(s):
    lst = []
    filterArr = [x for x in s]
    if len(filterArr) % 2 == 0:
        k = len(filterArr) - 1
        for z in range(int(len(filterArr) / 2)):
            lst.append(s[k - 1:k])
            k = k - 2
        return lst

    else:
        if len(filterArr) > 1:
            k = len(filterArr) - 1
            z = int((len(filterArr) - 1) / 2)
            for l in range(z):
                lst.append(s[k - 1:k])
                k = k - 2
            lst.append(filterArr[-1] + '_')
            return lst
        if len(filterArr) == 1:
            return [f'{s}_']
    pass