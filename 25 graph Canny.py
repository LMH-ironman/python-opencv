import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg",0)
#先进行高斯滤波，接着sobel算子计算X、Y方向的梯度，极大值抑制判断边界点，最后设最大最小阈值，canny边缘检测
min =   130
max =   150

img1 = cv.Canny(img ,  min , max)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img , cmap = plt.cm.gray)
axes[0].set_title("Original drawing ")
axes[1].imshow(img1 , cmap = plt.cm.gray)
axes[1].set_title("canny")
plt.show()