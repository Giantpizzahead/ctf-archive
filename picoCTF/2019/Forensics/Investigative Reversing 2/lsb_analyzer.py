START_LOC = 2000
READ_LEN = 50 * 8

with open("encoded.bmp", 'rb') as f:
    f.read(START_LOC)
    data = list(f.read(READ_LEN))

for i in range(len(data)):
    data[i] = data[i] & 1

for i in range(len(data) // 8):
    bits = ""
    for j in data[i*8:(i+1)*8]:
        bits += str(j)
    print(chr(int(bits[::-1], 2) + 5), end='')
