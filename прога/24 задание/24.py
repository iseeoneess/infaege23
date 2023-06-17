s = open('24_2499.txt').readline()
s = s.replace("Y", "Z").replace("Z", "*")

while any(z in s for z in ["XXXXX", 'XXXXXX', "XXXXXXX"]):
    s = s.replace("XXXXX", "XXXX XXXX")
    s = s.replace("XXXXXX", "XXXX XXXX XXXX")
    s = s.replace("XXXXXXX", "XXXX XXXX XXXX XXXX")
k = 0

for i in range(len(s) - 3):
    if s[i] + s[i + 1] + s[i + 2] + s[i + 3] == "XXXX":
       k += 1
print(k)
print(s.count("XXXX"))