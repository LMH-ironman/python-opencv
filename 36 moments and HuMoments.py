import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/flash.png")
imgray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
#计算图像的Hu矩
imgmn = cv.moments(imgray)
imghu = cv.HuMoments(imgmn)
print("HuMoments:\n",imghu)
#计算轮廓的Hu矩
ret , thresh = cv.threshold(imgray,127,255,0)

contours,hierarchy = cv.findContours(thresh, 1 , 2 )

cnt = contours[1]
mn = cv.moments(cnt)
hu = cv.HuMoments(mn)
print("contours HuMoments:\n",hu)

#Hu矩常常作为描述图像的特征，训练分类器，来进行目标识别