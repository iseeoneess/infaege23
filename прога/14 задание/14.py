for x in range(1, 100):
    num1 = 5 + 15*x + 3*15**2 + 2*15**3 + 15**4
    num2 = 3 + 3*15 + 2*15**2 + x*15**3 + 15**4
    if (num1 + num2) % 14 == 0:
        print(x, (num1 + num2) // 14)

