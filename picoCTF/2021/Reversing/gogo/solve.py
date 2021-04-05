# Password: reverseengineericanbarelyforward

a = '6534313239383338626462353733616664373236643365333166363338313638'
b = '4a53475d414503545d025a0a5357450d05005d555410010e4155574b45504601'
N = len(a)

for i in range(N-2, -2, -2):
	x = int(a[i:i+2], 16)
	y = int(b[N-i-2:N-i], 16)
	c = chr(x ^ y)
	print(c, end='')
print()

# MD5 hash: 861836f13e3d627dfa375bdb8389214e
# Plain: goldfish