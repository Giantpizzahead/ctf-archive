

def read_files():
    START_LOC = 2019
    READ_LEN = 50 * 32

    for FILE_NUM in range(5, 0, -1):
        with open("Item0{}_cp.bmp".format(FILE_NUM), 'rb') as f:
            f.read(START_LOC)
            raw_data = list(f.read(READ_LEN))

        data = []
        for i in range(10):
            for j in range(8):
                data.append(raw_data[i*12+j] & 1)

        for i in range(len(data) // 8):
            bits = ""
            for j in data[i*8:(i+1)*8]:
                bits += str(j)
            print(chr(int(bits[::-1], 2)), end='')


def calc_working_vals():
    for i in range(50):
        edx = 0x66666667 * i >> 1 >> 32

        # Do the shift left and add
        edx = edx + (edx << 2)

        # Do the subtract
        edx = edx - i

        # Figure out which values of i work
        if edx == 0:
            print(str(i) + " works")

calc_working_vals()
read_files()
"""
edx = overflow(edx * loop_j)
edx >> 1



"""
