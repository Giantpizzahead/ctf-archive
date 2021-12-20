from scipy.io import wavfile

samplerate, wavdata = wavfile.read('main.wav')
wavdata = wavdata.tolist()

data = []
for i in range(len(wavdata)):
	data.append(wavdata[i] // 500 - 2)

# print(data)
# print(min(data))
# print(max(data))
# for i in range(16):
# 	count = 0
# 	for x in data:
# 		if x == i: count += 1
# 	print(count)

for i in range(0, len(data), 2):
	x = 16*data[i] + data[i+1]
	print(chr(x), end='')
print()
