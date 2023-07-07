import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("image/sjtu.jpg")

rows,cols = img1.shape[:2]

M = cv.getRotationMatrix2D((cols/2,rows/2),45,0.5)   #cv.getRotationMatrix2D(旋转中心，角度，大小比例)

dst = cv.warpAffine(img1,M,(cols,rows))

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img1[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("change place photo")
plt.show()
print(rows,cols)
