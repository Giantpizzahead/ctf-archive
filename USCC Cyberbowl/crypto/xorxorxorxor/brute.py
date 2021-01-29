arr = []
with open('crypto/xorxorxorxor/flagonly', 'rb') as fin:
    arr = fin.readline()

key = [109, 35, 121, 35]

print([int(x) for x in arr])