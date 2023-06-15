s = 'ABM BCM CND DGE EF GEF HNG MCNH NDG TAMHF'
d = {c[0]:c[1:] for c in s.split()}

def f(s, end):
    if s[-1] == end: return (s.count('G') == 1 and s.count('C') == 1) or (s.count('C') == 1) or (s.count('G') == 1)
    return sum(f(s + c, end) for c in d[s[-1]])
print(f('T','F'))
