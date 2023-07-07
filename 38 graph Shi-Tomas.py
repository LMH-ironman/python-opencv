import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/flash.png")
gray_img = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray_img,1000,0.01,10)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(int(x),int(y)),2,(0,0,255),-1)

plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title("Shi-Tomas corners")
plt.xticks([])
plt.yticks([])
plt.show()