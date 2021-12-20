#!/usr/bin/env python3

# Uses ECB... so just hack that

import re
from random import randint
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


flag = "hello-FLAGL"

from random import seed
seed(21342412)
key = bytes([randint(0, 255) for _ in range(16)])
cipher = AES.new(key, AES.MODE_ECB)

def encrypt_ballot(username):
    ballot = bytes(map(ord, username))
    print(ballot)
    print(len(ballot))
    print(pad(ballot, 16))
    return cipher.encrypt(pad(ballot, 16))

def decrypt_ballot(ballot):
    ballot = unpad(cipher.decrypt(ballot), 16)
    ballot = ''.join(map(chr, ballot))
    return ballot

def parse_ballot(s):
    profile = dict(kv.split('=') for kv in s.split('&'))
    assert set(['Name', 'Candidate']) == set(profile.keys())
    return profile

def create_ballot(name=''):
    badchars = re.escape('!"#$%&\'()*+,-=./:;<>?@[\\\\]^_`{|}~')
    name = re.sub(f'[{badchars}]', '', name)
    return 'Name='+name+'&Candidate=Kittens Corleone'

def check_ballot(ballot):
    ballot = decrypt_ballot(ballot)
    ballot = parse_ballot(ballot)
    if ballot['Candidate'] == 'Frank Paws':
        print("You did it! Here's your flag:")
        print(flag)
    print('Your ballot is:')
    print(ballot,'\n')
        

welcome = "Welcome to the super awesome voting booth.\n"
menu = ('Pick an option:\n'
        '1) Generate ballot\n'
        '2) Check ballot\n'
        '3) Exit'
        )

print(welcome)
while True:
    print(menu)
    option = input('>>> ')
    if option == '1':
        print('What is your name?')
        voter_name = input('>>> ')
        print('Who would you like to vote for?')
        input('>>> ')
        ballot = create_ballot(voter_name)
        ballot = encrypt_ballot(ballot)
        print(ballot.hex()+'\n')
    elif option == '2':
        print('Enter your encrypted ballot in hex:')
        ballot = input('>>> ')
        try:
            ballot = bytes.fromhex(ballot)
            check_ballot(ballot)
        except:
            print('Decryption error. Ballot is corrupt.'+'\n')
    elif option == '3':
        break
    else:
        print('Invalid option.\n')
