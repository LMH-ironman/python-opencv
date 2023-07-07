import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

dist = cv.calcHist([img],[0],None,[256],[0,256]) #直方图显示
#cv.calcHist( 【输入图像】  ，  BGR其中一个通道【0】【1】【2】  ，  掩膜（后面会举例，如果要覆盖全图就是NONE）  ，  bins也就是组距【】 ，  像素值范围【】)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,6), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing ")
axes[1].plot(dist)
axes[1].set_title("medianBlur")
axes[1].grid()
plt.show()










