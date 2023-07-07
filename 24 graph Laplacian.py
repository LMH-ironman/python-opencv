import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg",0)

result = cv.Laplacian(img,cv.CV_16S)
img1 = cv.convertScaleAbs(result)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img , cmap = plt.cm.gray)
axes[0].set_title("Original drawing ")
axes[1].imshow(img1 , cmap = plt.cm.gray)
axes[1].set_title("laplacian")
plt.show()