from pwn import *

# Get the encrypted flag
c = remote('mercury.picoctf.net', 58913)
c.recvuntil('flag!\n')
enc_flag = c.recvline().decode().strip()

# Reset key position
loop_around = 50000 - len(enc_flag)//2
c.sendline('A'*loop_around)
c.recvuntil('go!\n')

# Reuse the same pad
plain = '41'*100
c.sendline('A'*100)
c.recvuntil('go!\n')
enc_plain = c.recvline().decode().strip()
print(enc_plain)

# Use XOR to find the key & flag
flag = ''
for i in range(0, len(enc_flag), 2):
	a = int(enc_plain[i:i+2], 16)
	b = int(enc_flag[i:i+2], 16)
	k = a ^ 0x41
	flag += chr(b ^ k)

print('FLAG:', flag)
# picoCTF{35ecb423b3b43472c35cc2f41011c6d2}
