#!/usr/bin/env python3

from random import randint, seed
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

seed(298324)
flag = "TEST-FLAG"

def chargen(n = 16):
    return bytes([randint(0, 255) for _ in range(n)])

def encrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, 16))

def decrypt(data):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data), 16)

def parseballot(ballot):
    for candidate in ballot.split(b';'):
        if candidate.endswith(b'=1'):
            name, _ = candidate.split(b'=')
            return name.decode()
    raise ValueError

key = chargen()
iv = chargen()

print('IV:', iv.hex())
print('Key:', key.hex())
print('This ballot was intercepted on its way from the voting booth.')
print('Can you change the ballot to vote for Frank Paws?')
msg = 'Droolius Caesar=0;Hairy Pawter=0;Chewbarka=1'
print(f"Current ballot: {msg}")
print(f"Ballot length: {len(msg)}\n")
print(f"Encrypted ballot: {encrypt(msg.encode()).hex()}\n")

print('Send the modified ballot in hex: ')
msg = input('>>> ')
try:
    ballot = decrypt(bytes.fromhex(msg))
    candidate = parseballot(ballot)
    print(f'A vote has been submitted for {candidate}')
    if candidate == 'Frank Paws':
        print("Congratulations! Here's your flag")
        print(flag)
except Exception as e:
    print('Error occurred while parsing ballot. Try again.')
    print(e)
