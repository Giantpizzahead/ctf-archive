from pwn import *

c = remote('cfta-nm01.allyourbases.co', 8017)

b = c.recvline().decode().strip()
t = ''
for i in range(0, len(b), 4):
	t += chr(int(b[i+2:i+4], 16))
print(t)
c.sendline(t)

c.interactive()