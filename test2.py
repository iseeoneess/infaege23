s = 'АБГ БД ВДБАГ ГЕЖ ДИЛЕ ЕВЛ ЖЕ ИЛ КЖ ЛКЖ'
d = {c[0]:c[1:] for c in s.split()}

def f(s, end):
    if s[-1] == end and len(s) > 1: return 1
    return sum(f(s + c,end) for c in d[s[-1]] if c not in s)

print(f('Б','В') + f('Д','В') + f('А','В') + f('Г','В'))