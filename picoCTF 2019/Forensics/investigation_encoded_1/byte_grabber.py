def get_lookup():
    START_LOC = 0xdc4
    READ_LEN = 0x20

    with open("mystery", 'rb') as f:
        f.read(START_LOC)
        raw_data = list(f.read((READ_LEN + 1) * 8))

    print('[', end='')
    for i in range(READ_LEN):
        print(raw_data[i*8], end=', ')
    print(']')

def get_matrix():
    START_LOC = 0xdc0
    READ_LEN = 0x20

    with open("mystery", 'rb') as f:
        f.read(START_LOC)
        raw_data = list(f.read((READ_LEN + 1) * 8))

    print('[', end='')
    for i in range(READ_LEN):
        print(raw_data[i*8], end=', ')
    print(']')

get_lookup()

print()

get_matrix()
