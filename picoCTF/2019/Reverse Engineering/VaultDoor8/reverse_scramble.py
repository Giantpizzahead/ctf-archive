def unscramble(b):
    b = str(bin(b))[2:]
    b = '0' * (8 - len(b)) + b
    b = switch(b, 7, 6)
    b = switch(b, 5, 2)
    b = switch(b, 4, 3)
    b = switch(b, 1, 0);
    b = switch(b, 7, 4);
    b = switch(b, 6, 5);
    b = switch(b, 3, 0);
    b = switch(b, 2, 1);
    return int(b, 2)

def switch(b, a1, a2):
    return b[:a2] + b[a1] + b[a2+1:a1] + b[a2] + b[a1+1:]

expected = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xF1, 0xC1, 0xF0, 0x94, 0xC1, 0xA5, 0xC1, 0xC2, 0xA4]
unscrambled = []

for b in expected:
    unscrambled.append(unscramble(b))

print("".join([chr(x) for x in unscrambled]))

# s0m3_m0r3_b1t_sh1fTiNg_743a4f48b
