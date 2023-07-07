import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 = cv.imread("image/sjtu.jpg")
img2 = cv.imread("image/sjtu.jpg")

img3 = cv.addWeighted(img1,0.7,img2,0.3,100)  #g = (1-a)f  +  af  + b

plt.figure(figsize=(8,8))
plt.imshow(img3[:,:,::-1])
plt.show()