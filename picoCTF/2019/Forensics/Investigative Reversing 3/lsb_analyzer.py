START_LOC = 723
READ_LEN = 50 * 16

with open("encoded.bmp", 'rb') as f:
    f.read(START_LOC)
    raw_data = list(f.read(READ_LEN))

data = []
for i in range(50):
    for j in range(8):
        data.append(raw_data[i*9+j] & 1)

for i in range(len(data) // 8):
    bits = ""
    for j in data[i*8:(i+1)*8]:
        bits += str(j)
    print(chr(int(bits[::-1], 2)), end='')
