import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/flash.png")
imgray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)

res , thresh = cv.threshold(imgray,127,255,0)#函数的返回值 res 是选择的阈值，thresh 是应用阈值后的图像。

contours,hierarchy = cv.findContours(thresh, 1 , 2 )

cnt = contours[1]

(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv.circle(img,center,radius,(0,255,0),2)

plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title("circle")
plt.xticks([])
plt.yticks([])
plt.show()