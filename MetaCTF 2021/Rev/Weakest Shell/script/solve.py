k1 = "M0FBMUU3M0NFNEREQTkwOTY1REE1QjczNTM2NzQ1RjhEQzQwMTdFRkFBREVCRjRDODhERTQ4NDk3MDdFNDExRA"
c1 = (-7, -39, -16, 18, -12, 0, 7, -34, -5, -62, -38, -11, 1, -3, -17, -53, -18, -19, 46, 58)
k2 = "ODE5MDc5OTJERDQ4MzBDOTYyMDM3MDk4OTlGRDE4NTRFOThGQjYwQUZEMkVGQUE1OERGNzI1ODMyMDdBRTUzRA"
c2 = (-6, 20, -35, -17, -7, -1, -21, -49, 6, 1, -8, -33, -18, -3, -23, -56, -11, 3, 5, 7)
k3 = "Njg0ODg4QzBFQkIxN0YzNzQyOThCNjVFRTI4MDc1MjZDMDY2MDk0QzcwMUJDQzdFQkJFMUMxMDk1RjQ5NEZDMQ"
c3 = (-20, 35, -5, 0, -11, -20, 29, -52, -17, 52, 9, 3, 4, -15, -13, 35, -24, -33, 28, 61)

flag = ""

for i in range(0, len(c1)): flag += chr(ord(k1[i]) - c1[i])
print(flag)
flag = ""
for i in range(0, len(c2)): flag += chr(ord(k2[i]) - c2[i])
print(flag)
flag = ""
for i in range(0, len(c3)): flag += chr(ord(k3[i]) - c3[i])
print(flag)

# MetaCTF{P0w3rSHELL_!$_the_literal_B35T}