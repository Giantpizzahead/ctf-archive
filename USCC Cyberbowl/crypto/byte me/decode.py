arr = []

with open('enc', 'rb') as fin:
    arr = fin.readline()

for i in range(255):
    newarr = [x ^ i for x in arr]
    print(''.join([chr(x) for x in newarr]))
