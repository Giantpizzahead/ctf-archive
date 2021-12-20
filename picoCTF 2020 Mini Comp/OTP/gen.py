target = 'adpjkoadapekldmpbjhjhbaghlfldbhjdalgnbeedheenfoeddabpmdnliokcahomdphbcleipfgibjdcgmjcmadaomiakpdjcni'
vals = [0, 2, 4, 6, 8, 10, 12, 14, 17, 19, 21, 23, 25, 27, 29, 31]

last_val = 0
key = []
for i in range(100):
    target_val = ord(target[i]) - 0x61
    print("{} target {} =>".format(i, target_val), end=' ')
    for j in range(16):
        new_val = (last_val + vals[j]) % 16
        if new_val == target_val:
            key.append(hex(j)[2:])
            print(hex(j)[2:])
            last_val = target_val
            break

print(''.join(key))

flag = '790ce176acf7c2b277040687b23e185b2bb0d0fcc1939bf782db10c1210218dc4b2b3c931a5c2f04ad5aa711d04175920aa0'

flag_hex = hex(int(flag, 16) ^ int(''.join(key), 16))[2:]
for i in range(50):
    print(chr(int(flag_hex[i*2:(i+1)*2], 16)), end='')
print()

# picoCTF{cust0m_jumbl3s_4r3nt_4_g0Od_1d3A_db877006}
