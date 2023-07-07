import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
#创建蒙版
mask = np.zeros(img.shape[:2],np.uint8)
mask[400:650 , 200:500] = 255
#掩膜
masked_img = cv.bitwise_and(img,img,mask=mask)
#统计掩膜后的灰度图
masked_dst = cv.calcHist([img],[0],mask,[256],[0,256])

fig,axes = plt.subplots(nrows = 2 ,ncols = 2 ,figsize = (10,8))
axes[0,0].imshow(img , cmap=plt.cm.gray)
axes[0,0].set_title("Original drawing ")
axes[0,1].imshow(mask , cmap=plt.cm.gray)
axes[0,1].set_title("mask")
axes[1,0].imshow(masked_img, cmap=plt.cm.gray)
axes[1,0].set_title("masked_img")
axes[1,1].plot(masked_dst)
axes[1,1].set_title("masked_dst")
axes[1,1].grid()
plt.show()

