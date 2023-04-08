from itertools import *
bit = ["".join(z) for z in product("01", repeat = 8)]

a = set()
p = {i for i in bit if i[0] + i[1] == '11'}
q = {g for g in bit if g[-1] == "0"}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (not (A)) <= ((not(P)) and (not(Q)))

for x in bit:
    if f(x) == 0:
        a.add(x)
print(len(a))