from PIL import Image

im = Image.open("forensics/fooled/rotatedlsb.png")

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

interval = 0
bin_num = ""
bin_arr = []
for i in range(height):
    for j in range(width):
        bin_num += str(pixels[i][j][0] // 128)
        interval += 1
        if interval == 8:
            bin_num = bin_num[::-1]
            # print(bin_num, end=' ')
            bin_arr.append(int(bin_num, 2))
            interval = 0
            bin_num = ""

print(''.join([chr(x) for x in bin_arr][::-1]))