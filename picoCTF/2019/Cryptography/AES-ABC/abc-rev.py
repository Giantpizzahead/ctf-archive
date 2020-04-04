#!/usr/bin/env python

import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def reverse_abc(ct):
    blocks = [ct[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(ct) / BLOCK_SIZE)]

    # Reverse abc algorithm
    for i in range(len(blocks) - 2, -1, -1):
        prev_blk = int(get_hex(blocks[i]), 16)
        curr_blk = int(get_hex(blocks[i+1]), 16)

        n_curr_blk = (curr_blk - prev_blk) % UMAX
        blocks[i+1] = to_bytes(n_curr_blk)

    # Remove IV
    blocks = blocks[1:]

    return "".join(blocks)

def get_hex(text):
    # Remove padding
    i = 0
    while text[i] == '\0': i += 1
    text = text[i:]

    text_hex = text.encode('hex')
    
    # Added 0 won't affect results
    return text_hex


def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0: 
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded
    
def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index('\n') + 1], s[s.index('\n')+1:]

def parse_header_ppm(f):
    data = f.read()

    header = ""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data

def main():
    with open('body.enc.ppm', 'rb') as f:
        header, data = parse_header_ppm(f)

    # print(header)
    rev_data = reverse_abc(data)

    with open('decoded.enc.ppm', 'wb') as fw:
        fw.write(header)
        fw.write(rev_data)

main()
