correct = '783ea06eb8ce405e381ea08ef8aec07ef87ea02e380e401eb85ea04e78eec03e78bea0eeb84e40de389ea00ef82ec0fef8fea0ae388e409eb8dea0ce786ec0ff'
mine = '741a954ebadb4764092dd1bf8a9dde5ad75c9316093b306f9740d07c57dbde0c09a0849b8a762fb157a2e14fb96f81bfb9bfe1ef79cf01dff99fe18f392f81ff'

flag = ''

for i in range(64):
	c = int(correct[i*2:(i+1)*2], 16)
	m = int(mine[i*2:(i+1)*2], 16) ^ 0x41
	t = c ^ m
	flag += chr(t)

print(flag)

# MetaCTF{pr0p3r_encrypt10n_1snt_s0_e4sy...}
