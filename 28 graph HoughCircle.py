import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
gray_img = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
#中值滤波
img1 = cv.medianBlur(gray_img , 7)
#cv.HoughCircles(滤波后的图像，霍夫梯度法，分辨率dp，圆心之间距离的最小阈值，canny的高阈值，圆心与半径的共同阈值，圆半径最小值，圆半径最小值)
circles = cv.HoughCircles(img1 , cv.HOUGH_GRADIENT , 1 ,200 ,param1 = 100 ,param2 = 30 ,minRadius = 0 ,maxRadius = 100 )

for i in circles[0,:]:
    cv.circle(img , (int(i[0]),int(i[1])) , int(i[2]) ,(0,255,0), 2)
    cv.circle(img , (int(i[0]),int(i[1])) , 2 ,(0,0,255), 3)

plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title("houghcircle")
plt.xticks([])
plt.yticks([])
plt.show()
print(circles)