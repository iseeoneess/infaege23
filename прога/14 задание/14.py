for x in range(2, 37):
    try:
        if int("21", x) * int("13", x) == int("313", x):
            print(x)
    except:
        pass