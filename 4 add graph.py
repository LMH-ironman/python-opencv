import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("image/sjtu.jpg")
img2 = cv.imread("image/sjtu.jpg")

img3 = cv.add(img1,img2)   #饱和值取255 例如当 250 + 10 = 260时， 260 》 255
img4 = img1 + img2   # 饱和值取余数， 250 + 10 =260 ， 260 % 256 = 4

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title("cv add")
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title("straight add")
plt.show()
