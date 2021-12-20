#!/usr/bin/python3 -u

import zlib
from random import randint
import os
from Crypto.Cipher import Salsa20

flag = open("./flag").read()


def compress(text):
    return zlib.compress(bytes(text.encode("utf-8")))

def encrypt(plaintext):
    secret = os.urandom(32)
    # Stream cipher
    # Encrypts by doing ciphertext = plaintext XOR rand_stream()
    # Does not shift order of bytes!
    cipher = Salsa20.new(key=secret)
    return cipher.nonce + cipher.encrypt(plaintext)

def main():
    while True:
        usr_input = input("Enter your text to be encrypted: ")
        compressed_text = compress(flag + usr_input)
        encrypted = encrypt(compressed_text)
        
        nonce = encrypted[:8]
        encrypted_text =  encrypted[8:]
        print("C:", compressed_text)
        for i in range(len(compressed_text)):
            decomp = zlib.decompressobj()
            try: print("D {}:".format(i), decomp.decompress(compressed_text[:i]))
            except Exception as e: print(e)
        print("N:", nonce)
        print("E:", encrypted_text)
        print("L:", len(encrypted_text), len(compressed_text))

if __name__ == '__main__':
    main() 



