import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img1=mpimg.imread('scrambled1.png')
img2=mpimg.imread('scrambled2.png')
img3=mpimg.imread('scrambled1.png')
for i in range(len(img3)):
    row = img3[i]
    for j in range(len(row)):
        cell = row[j]
        for k in range(3):
            if img1[i][j][k] + img2[i][j][k] != 1:
                cell[k] = 1
            else:
                cell[k] = 0
imgplot = plt.imshow(img3)

plt.show()
