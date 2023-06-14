def f(n, cc):
    lst = []
    while n > 0:
        lst = [n % cc] + lst
        n //= cc
    return ''.join([str(x) for x in lst])

print(f(1035,16))