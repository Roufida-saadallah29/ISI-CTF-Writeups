pt = "ISICTF"
ct = [90, 100, 90, 116, 71, 113]

key = []
for i in range(0, len(pt)):
    key.append(ct[i] ^ ord(pt[i]))


c =[90, 100, 90, 116, 71, 113, 104, 111, 35, 101, 76, 6, 96, 104, 39, 64, 32, 68, 35, 90, 32, 104, 32, 65, 32, 89, 76, 64, 34, 67, 123, 7, 102, 67, 76, 3, 76, 92, 32, 78, 110]

flag = ""
for i, value in enumerate(c):
    flag += chr(value ^ key[i % len(key)])

print(flag)
