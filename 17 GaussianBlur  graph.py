import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

img1 = cv.GaussianBlur(img , (5,5) ,1) #高斯滤波  GaussianBlur(图像 ， 奇数核大小 ，x方向的标准差 ，y方向标准差 ，边界填充)  主要用于除去高斯噪声

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing ")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("GaussianBlur")
plt.show()

