#!/usr/bin/env python3

import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


flag = "FKLDFJD"

print('Welcome to the super secure voting machine!')
print('Submit as many votes as you want\n')

while True:
    iv = random.getrandbits(128).to_bytes(16, 'big')
    key = random.getrandbits(128).to_bytes(16, 'big')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    print('Who would you like to vote for?')
    candidate = bytes(map(ord, input('>> ')))
    msg = b'Vote has been submitted for: %s' % candidate
    enc = cipher.encrypt(pad(msg, 16)).hex()
    print(f'encrypted message: {enc}')
    print('Can you find the key used to encrypt? (Enter in hex)')
    try:
        guess = bytes.fromhex(input('>> '))
        assert len(guess) == 16
        if guess == key:
            print("Nice! Here's your flag")
            print(flag)
            break
        else:
            print('WRONG!\n')
    except:
        print('Please enter a valid 16 byte key.')
        print('Example: 555343437b46616b655f466c6167217d\n')

    print(f'The key was {key.hex()}')
    print(f'Oh, and heres the iv if you were curious {iv.hex()}\n')
