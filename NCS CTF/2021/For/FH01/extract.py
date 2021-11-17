with open('maybe.hex', 'r') as fin:
	data = fin.read().split()

fout = open('maybe.hex2', 'w')

file_num = 5
num_short = 0
part_cnt = 1
for i in range(len(data)):
	l = data[i]
	if len(l) < 4000:
		# End of image
		num_short += 1
		continue
	# Remove header
	l = l[32:]
	if num_short == file_num:
		header = data[i][:32]
		cnt = 0
		for j in range(12, -2, -2):
			cnt *= 0x100
			cnt += int(header[j:j+2], 16)
		assert cnt == part_cnt, 'Missing part {} (jumped to {}'.format(part_cnt, cnt)
		part_cnt += 1
		print(cnt)
		fout.write(l)
fout.close()

with open('maybe.hex2', 'r') as fin:
	data = fin.read()

fout = open('raw.out', 'wb')

for i in range(0, len(data), 2):
	fout.write(bytes([int(data[i:i+2], 16)]))
fout.close()
