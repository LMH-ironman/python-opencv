import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

up_img = cv.pyrUp(img)

down_img = cv.pyrDown(img)

fig,axes = plt.subplots(nrows = 1 ,ncols = 3 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(up_img[:,:,::-1])
axes[1].set_title("enlarge")
axes[2].imshow(down_img[:,:,::-1])
axes[2].set_title("shrink")
plt.show()
