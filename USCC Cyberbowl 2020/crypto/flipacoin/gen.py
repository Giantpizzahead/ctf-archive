ballot = "af279196fe650cd28f03f62cd9dcd51db58b68e3d73b5f35779b56c3a738bc907c8daf7ea4f55d32d1db65d2945bba62"

orig = ";Chewbarka=1\x04\x04\x04\x04"
target = ";Frank Paws=1\x03\x03\x03"

# ;Chewbarka=1 \x04 \x04 \x04 \x04
# Change to ;Frank Paws=1 \x03 \x03 \x03

# af279196fe650cd28f03f62cd9dcd51d

block = input("Block to switch: ")
block_bytes = []
for i in range(16):
    block_bytes.append(int(block[i*2:(i+1)*2], 16))
    block_bytes[i] ^= ord(orig[i])
    block_bytes[i] ^= ord(target[i])

for i in range(16):
    print(str(hex(block_bytes[i] // 16)[2:]) + str(hex(block_bytes[i] % 16)[2:]), end='')
print()