enc = b'\x9dn\x93\xc8\xb2\xb9A\x8b\xc5\xc6\xdda\x93\xc3\xc2\xda?\xc7\x93\xc1\x8b1\x95\x93\x93\x8eb\xc8\x94\xc9\xd5d\xc0\x96\xc4\xd97\x93\x93\xc2\x90'
key = b'\xf1\xa7\xf0\x07\xed'
flag = ''

for i in range(len(enc)):
    j = 4 - (i % 5)
    a = enc[i]
    b = key[j]
    # Change both to signed
    if a >= 128:
        a -= 256
    if b >= 128:
        b -= 256
    # print(a, b)
    # XOR
    flag += chr(a ^ b)

print(flag)
