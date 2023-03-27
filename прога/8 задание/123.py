for x in "0123456789abcdefg":
    num = int(f"9759{x}", 17) + int(f"3{x}108", 17)
    if num % 11 == 0:
        print(x, num // 11)