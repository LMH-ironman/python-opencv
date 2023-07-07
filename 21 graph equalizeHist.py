import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg",0)
#要以灰度图的形式读入
img1 = cv.equalizeHist(img)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img , cmap = plt.cm.gray)
axes[0].set_title("Original drawing ")
axes[1].imshow(img1 , cmap = plt.cm.gray)
axes[1].set_title("equal graph")
plt.show()