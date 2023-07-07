import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#轮廓近似
img = cv.imread("image/sjtu.jpg")
img1 = img.copy()
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#边缘检测
canny = cv.Canny(imgray,127,255,0)
#轮廓提取
contours,hierarchy = cv.findContours(canny,cv.RETR_LIST ,cv.CHAIN_APPROX_NONE)
#轮廓绘制在图像上
img = cv.drawContours(img,contours,-1,(255,0,0),2)

#凸包检测
hulls=[]
for cnt in contours:
    hull = cv.convexHull(cnt)
    hulls.append(hull)
draw_hulls = cv.drawContours(img1,hulls,-1,(0,255,0),2)

plt.figure(figsize=(10,8),dpi=100)
plt.subplot(121),plt.imshow(img[:,:,::-1]),plt.title("Original drawing")
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(draw_hulls[:,:,::-1]),plt.title("hull")
plt.xticks([]),plt.yticks([])
plt.show()