for x in range(2, 21):
    for y in range(2, 21):
        num1 = 9 + x*21 + y*21**2 + 2*21**3 + 21**4
        num2 = 9 + 9*21 + y*21**2 + 6*21**3 + 3*21**4
        res = num1 + num2
        if res % 18 == 0:
            if y == 5:
                print(x, y, res // 18)