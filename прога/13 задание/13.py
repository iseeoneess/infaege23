s = 'АЖБ БЗВ ВГ ГДЖЗ ДЖАЕК ЕАИ ЖЗ ЗВА ИА КЕ'
d = {c[0]:c[1:] for c in s.split()}


def f(s, end):
    if s[-1] == end : return 1
    return sum(f(s + c, end) for c in d[s[-1]] if c not in s)


print(f('А','З') + f('В','З'))
