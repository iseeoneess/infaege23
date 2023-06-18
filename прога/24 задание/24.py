s = open('24_2506.txt').readline().strip()
d = {x:s.count(x) for x in sorted(set(s))}
m = max(d.values())
print([x for x in d if d[x] == m], m)
