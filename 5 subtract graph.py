import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("image/sjtu.jpg")
img2 = cv.imread("image/sjtu.jpg")

img3 = cv.subtract(img1,img2)#小于0时，赋值为0
img4 = img1 - img2 + 255

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img3[:,:,::-1])
axes[0].set_title("cv subtract")
axes[1].imshow(img4[:,:,::-1])
axes[1].set_title("straight subtract")
plt.show()

#其它API 乘法：cv.multiply; 除法：cv.divide