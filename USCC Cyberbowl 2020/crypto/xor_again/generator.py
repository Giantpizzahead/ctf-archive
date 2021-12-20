#!/usr/bin/env python3

from random import randint


def xor(s):
    key = [randint(0, 255) for _ in range(randint(16, 32))]
    return bytes([ord(c) ^ key[i%len(key)] for i, c in enumerate(s)])

def main():
    with open('text.txt', 'r') as f:
        text = f.read()
    ct = xor(text)
    with open('enc', 'wb') as f:
        f.write(ct)

if __name__ == '__main__':
    main()