s = open("24_4642.txt").readline()
s = s.replace("B", "A").replace("2", "1").replace("A1", "*").replace("A", " ").replace("1", " ")
print(max(len(c) for c in s.split()))