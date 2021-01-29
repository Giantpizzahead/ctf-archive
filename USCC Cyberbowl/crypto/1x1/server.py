#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


flag = "USCC{HELLO}"

key = b"abcdefghijklmnop"

def encrypt(data):
    print(len(data))
    for i in range(len(data) // 16):
        print(data[i*16:(i+1)*16])
    return cipher.encrypt(pad(data, 16))


cipher = AES.new(key, AES.MODE_ECB)
banner = (
    "Welcome to the super secure voting booth.\n"
    "I can connect to the internet because I use super secure encryption.\n"
    )
print(banner)

print('Who would you like to vote for?')
vote = input(">>> ")

msg = b"A vote has been submitted for %s" % vote.encode()
msg += flag.encode()
enc = encrypt(msg)

print('Your vote has been submitted.')
print('This is the encrypted ballot.')
print(enc.hex())
