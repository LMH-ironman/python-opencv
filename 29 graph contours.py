import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

img_gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
#先canny边缘检测
canny = cv.Canny(img_gray,177,255,0)
#轮廓提取
contours ,hierarchy = cv.findContours(canny , cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#将轮廓绘制在图像上(-1代表所有轮廓)
img = cv.drawContours(img,contours,-1 , (0,0,255),2)

plt.imshow(img[:,:,::-1])
plt.xticks([])
plt.yticks([])
plt.show()

