What does asm4("picoCTF_d7243") return? (Treat the array argument as a pointer)

asm4:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	push   ebx
	<+4>:	sub    esp,0x10
	<+7>:	mov    local_var_a,0x244
	<+14>:	mov    variable_i,0x0
	<+21>:	jmp    0x518 <asm4+27>
	<+23>:	add    variable_i,0x1
	<+27>:	mov    edx,variable_i
	<+30>:	mov    eax,DWORD PTR INPUT_ARG
	<+33>:	add    eax,edx
	<+35>:	movzx  eax,BYTE PTR [eax]
# Gets the ith character of the input string, and stores it in eax.
	<+38>:	test   al,al
	<+40>:	jne    0x514 <asm4+23>
# Jumps if al != 0, otherwise continues...?
# This would theoretically only continue when i = 13 (past entire string).
	<+42>:	mov    variable_j,0x1
	<+49>:	jmp    0x587 <asm4+138>
# Above initializes j to 1
# BEGINNING OF MAIN PART
	<+51>:	mov    edx,variable_j
	<+54>:	mov    eax,DWORD PTR INPUT_ARG
	<+57>:	add    eax,edx
	<+59>:	movzx  eax,BYTE PTR [eax]
	<+62>:	movsx  edx,al
# The entire above section moves the jth character of the input into edx.
	<+65>:	mov    eax,variable_j
	<+68>:	lea    ecx,[eax-0x1]
# Sets ecx = j - 1.
	<+71>:	mov    eax,DWORD PTR INPUT_ARG
	<+74>:	add    eax,ecx
	<+76>:	movzx  eax,BYTE PTR [eax]
	<+79>:	movsx  eax,al
# Moves the j-1th character of the input into eax.

# At this point:
# edx = input[j]
# eax = input[j-1]
# ecx = j-1
# local_var_a was initialized to 0x244
	<+82>:	sub    edx,eax
	<+84>:	mov    eax,edx
	<+86>:	mov    edx,eax
# edx = edx - eax
# eax = edx - eax
# Same thing as eax & edx = input[j] - input[j-1]
	<+88>:	mov    eax,local_var_a
	<+91>:	lea    ebx,[edx+eax*1]
# ebx = input[j] - input[j-1] + local_var_a
	<+94>:	mov    eax,variable_j
	<+97>:	lea    edx,[eax+0x1]
# edx = j + 1
	<+100>:	mov    eax,DWORD PTR INPUT_ARG
	<+103>:	add    eax,edx
	<+105>:	movzx  eax,BYTE PTR [eax]
	<+108>:	movsx  edx,al
# Moves the j+1th character of the input into edx.
	<+111>:	mov    ecx,variable_j
	<+114>:	mov    eax,DWORD PTR INPUT_ARG
	<+117>:	add    eax,ecx
	<+119>:	movzx  eax,BYTE PTR [eax]
	<+122>:	movsx  eax,al
# Moves the jth character of the input into eax.
	<+125>:	sub    edx,eax
	<+127>:	mov    eax,edx
	<+129>:	add    eax,ebx
# edx = edx - eax
# eax = edx - eax + ebx
# eax = input[j+1] - input[j] + input[j] - input[j-1] + local_var_a
# = input[j+1] - input[j-1] + local_var_a
	<+131>:	mov    local_var_a,eax
	<+134>:	add    variable_j,0x1
# Increments j by one to continue the for loop.
	<+138>:	mov    eax,variable_i
	<+141>:	sub    eax,0x1
	<+144>:	cmp    variable_j,eax
# Checks if j < 12, if so, continues the for loop.
	<+147>:	jl     0x530 <asm4+51>
	<+149>:	mov    eax,local_var_a
# Returns local_var_a.
	<+152>:	add    esp,0x10
	<+155>:	pop    ebx
	<+156>:	pop    ebp
	<+157>:	ret    

So here's what the code does.
result = 0x244
for j in range(1, 12):
	result += ord(input[j+1]) - ord(input[j-1])

Which ends up simplifying to:
result = 0x244 + ord(input[12]) + ord(input[11]) - ord(input[1]) - ord(input[0])
result = 466 = 0x1d2