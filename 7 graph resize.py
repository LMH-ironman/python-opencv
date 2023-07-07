import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img1 =  cv.imread("image/sjtu.jpg")
plt.imshow(img1[:,:,::-1])
plt.show()
rows,cols = img1.shape[:2]#行和列
res = cv.resize(img1,(2*cols,2*rows))#绝对
plt.imshow(res[:,:,::-1])
plt.show()

res1 = cv.resize(img1,None,fx = 0.5  ,fy = 0.5)#相对
plt.imshow(res1[:,:,::-1])
plt.show()

print(img1.shape,res.shape,res1.shape)