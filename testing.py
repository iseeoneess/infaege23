for x in range(2, 1001):
    num = 3 + 3*(x+4) - 15
    if num == 33:
        print(x)
        break
    # proverka
print(int('33', 15) - int('33', 4))