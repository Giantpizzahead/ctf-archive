import matplotlib.pyplot as plt
import matplotlib.image as mpimg

frame = mpimg.imread('frame.png')
code = mpimg.imread('code.png')
newimg = mpimg.imread('frame.png')
for i in range(len(frame)):
    for j in range(len(frame[i])):
        a = round(frame[i][j][0])
        b = round(code[i][j][0])
        c = a ^ b
        for k in range(len(newimg[i][j])-1):
            newimg[i][j][k] = c

plt.imshow(newimg)
plt.show()

# A_Code_For_A_Code