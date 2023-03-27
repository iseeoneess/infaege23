for x in "123456789abcdefghijkl":
    for y in "0123456789abc":
        num = int(f"{x}23{x}5", 22) - int(f"67{y}9{y}", 13)
        if num % 57 == 0:
            print(x, y, int(x, 22) + int(y, 13) // 57, num // 57)
