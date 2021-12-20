import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

HEIGHT = 720
WIDTH = 1280
res = [[[0, 0, 0] for _ in range(WIDTH)] for _ in range(HEIGHT)]
for x in range(1, 67):
	print('On image {}'.format(x))
	img = mpimg.imread('image_{:02d}_01.png'.format(x))
	img *= 255
	img = img.astype(int)
	img &= 1
	res += img
print(res)

enc = ''
for i in range(WIDTH):
	enc += str(res[0][i][2])
flag = ''
for j in range(0, len(enc), 8):
	flag += chr(int(enc[j:j+8], 2))
print(flag)

plt.imshow(res)
plt.show()
