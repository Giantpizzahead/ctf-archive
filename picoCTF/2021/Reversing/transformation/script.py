flag = 'picoCTF{hello}'

print([hex((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# picoCTF{16_bits_inst34d_of_8_e141a0f7}