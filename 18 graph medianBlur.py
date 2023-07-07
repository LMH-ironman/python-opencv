import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

img1 = cv.medianBlur(img , 5)     #主要作用在椒盐噪声

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing ")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("medianBlur")
plt.show()