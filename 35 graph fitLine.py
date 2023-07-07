import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/flash.png")
imgray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)

res , thresh = cv.threshold(imgray,127,255,0)#函数的返回值 res 是选择的阈值，thresh 是应用阈值后的图像。

contours,hierarchy = cv.findContours(thresh, 1 , 2 )

cnt = contours[1]
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt,cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
im = cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)


plt.figure(figsize=(10,8),dpi=100)
plt.imshow(im[:,:,::-1])
plt.title("fitline")
plt.xticks([])
plt.yticks([])
plt.show() 