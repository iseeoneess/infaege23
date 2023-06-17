s = 'АБВГ БД ВБДЕ ГВЕИ ДКЛ ЕЛЖИ ЖКМН ИЖН КПС ЛКЖ МСР НМР ПС РС'
d = {c[0]:c[1:] for c in s.split()}

def f(s, end):
    if s[-1] == end: return 'М' in s and "Е" in s
    return sum(f(s + c, end) for c in d[s[-1]])
print(f('А','С'))