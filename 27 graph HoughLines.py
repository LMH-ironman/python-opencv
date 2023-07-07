import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import random

img = cv.imread("image/sjtu.jpg")

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray , 100, 150)

lines = cv.HoughLines(edges , 0.8 ,np.pi/180 ,200) #cv.HoughLines(img , rho , theta , 阈值（只有超过这个值的才能被称为直线）)

for line in lines:
    rho , theta = line[0]
    a  = np.cos(theta)
    b  = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 - 1000 * b)
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 + 1000 * b)
    y2 = int(y0 - 1000 * a)
    cv.line(img ,(x1,y1) ,(x2,y2),(0 ,255 ,0))

plt.figure( figsize=(10,8) , dpi=100)
plt.imshow(img[:,:,::-1])
plt.title("houghlines")
plt.xticks([])
plt.yticks([])
plt.show()
