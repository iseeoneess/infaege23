s = open('24_2509.txt').readline().strip()

d = {x:s.count(x) for x in sorted(set(s))}
mx = max(d.values())
mn = min(d.values())

print([x for x in d if d[x] == mx], [x for x in d if d[x] == mn])
print(mx - mn)