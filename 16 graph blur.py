import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

img1 = cv.blur(img , (5,5))  #均值滤波 blur(图像，卷积和大小)  容易失去细节信息

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing ")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("Mean filtering ")
plt.show()