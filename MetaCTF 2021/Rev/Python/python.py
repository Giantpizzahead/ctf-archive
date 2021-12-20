# MetaCTF{yOu_w!N_th1$_0n3}

import random

def do_thing(a, b):
    return ((a << 1) & b) ^ ((a << 1) | b)

flag = ''
x = ''
for z in range(25):
    best_right = 0
    best_y = 0
    for y in range(256):
        x = flag + chr(y) + '?'*(24-z)
        random.seed(997)
        k = [random.randint(0, 256) for _ in range(len(x))]
        a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k) }
        b = list(range(len(x)))
        random.shuffle(b)
        c = [a[i] for i in b[::-1]]
        kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]
        num_right = 0
        for j in range(25):
            if c[j] == kn[j]: num_right += 1
        if num_right > best_right:
            best_right = num_right
            best_y = y
    flag += chr(best_y)
    print(flag)

# [103, 43, 27, 224, 98, 142, 237, 133, 13, 50, 182, 221, 138, 184, 60, 112, 142, 167, 80, 108, 82, 227, 70, 40, 73]
# [103, 43, 27, 224, 98, 142, 237, 133, 13, 50, 182, 221, 138, 184, 60, 112, 142, 167, 80, 106, 82, 227, 70, 40, 73]