KEY_LENGTH = 25

curr_unknown = 24
key = [175, 189, 54, 242, 83, 216, 116, 125, 249, 24, 96, 197, 99, 219, 168, 37, 43, 254, 81, 220, 138, 136, 75, 156, 126]

enc = []
with open("crypto/xor_again/enc", 'rb') as fin:
    enc = [int(x) for x in fin.read()]

print(enc[269:275])

def is_valid(c):
    return c == ord('\n') or (c >= 32 and c < 127)

def try_new(new_key):
    curr_keyi = 0
    new_enc = enc[:]
    for i in range(len(enc)):
        new_enc[i] ^= new_key[curr_keyi]
        if curr_keyi <= curr_unknown and not is_valid(new_enc[i]):
            return False
        curr_keyi = (curr_keyi + 1) % KEY_LENGTH
    return new_enc

def print_enc(key):
    curr_keyi = 0
    for i in range(min(len(enc), 7000)):
        if curr_keyi > curr_unknown:
            print('_', end='')
        else:
            print(chr(enc[i] ^ key[curr_keyi]), end='')
        curr_keyi = (curr_keyi + 1) % KEY_LENGTH
    print()

print_enc(key)
'''
for i in range(0, 256):
    new_key = key[:]
    new_key[curr_unknown] = i
    result = try_new(new_key)
    if result:
        print("Key value", i)
        print_enc(new_key)

curr_keyi = 0
for i in range(len(enc)):
    enc[i] ^= key[curr_keyi]
    print(enc[i], end=' ')
    curr_keyi = (curr_keyi + 1) % KEY_LENGTH
print()
print(len(enc))


'''