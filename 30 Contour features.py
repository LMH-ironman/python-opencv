import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#轮廓近似
img = cv.imread("image/sjtu.jpg")
img_gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
#转换为二值图
ret , thresh = cv.threshold(img_gray,127,255,0)
#轮廓提取
contours , hierarchy = cv.findContours(thresh ,cv.RETR_LIST ,cv.CHAIN_APPROX_NONE)
#轮廓近似
epsilon = 100*cv.arcLength(contours[0],True)#轮廓周长
approx = cv.approxPolyDP(contours[0],epsilon,True)
#原始轮廓
img1 = cv.drawContours(img,contours,-1,(0,0,255),2)
#近似轮廓
img2 = cv.polylines(img,[approx],True,(0,255,0),2)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(img[:,:,::-1])
axes[1].set_title("approx graph")
plt.show()