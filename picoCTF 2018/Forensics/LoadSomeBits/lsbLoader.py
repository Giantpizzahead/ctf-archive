# Prints out the first few least significant bits of a file.

NUM_TO_PRINT = 500
OFFSET = 6

# The right offset is 6
# Flag: picoCTF{st0r3d_iN_tH3_l345t_s1gn1f1c4nT_b1t5_770554193}

with open("pico2018-special-logo.bmp", 'rb') as fin:
    fin.read(OFFSET)
    for i in range(NUM_TO_PRINT):
        print(ord(fin.read(1)) % 2, end='')
