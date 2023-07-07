import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

#创建一个核
kernel = np.ones((5,5),np.uint8)

#腐蚀与膨胀

img1 = cv.erode(img,kernel,1)  #erode(腐蚀的对象，核子，腐蚀的次数)  注：腐蚀核子对应原图全1为1

img2 = cv.dilate(img,kernel,1) #dilate(膨胀的对象 ， 核子 ， 腐蚀的次数)  注：膨胀核子对应原图有1就为1

fig,axes = plt.subplots(nrows = 1 ,ncols = 3 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(img1[:,:,::-1])
axes[1].set_title("erode")
axes[2].imshow(img2[:,:,::-1])
axes[2].set_title("dilate")
plt.show()