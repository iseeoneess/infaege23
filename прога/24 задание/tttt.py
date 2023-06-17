s = open('24_4643.txt').readline()
s = s.replace("B", "A").replace("11", "0").replace("21", "0").replace("22", "0").replace("12","0")
s = s.replace("0A", "*").replace("0", " ").replace("A", " ").replace("1", " ").replace("2", " ").split()
print(max(len(c) for c in s))
