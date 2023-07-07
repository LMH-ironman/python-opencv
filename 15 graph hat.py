import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

kernel = np.ones((10 , 10),np.uint8)

cvtophat = cv.morphologyEx(img , cv.MORPH_TOPHAT , kernel)   #礼帽（白帽、顶帽）运算  原图像-开运算   分离亮一点的点
cvblackhat = cv.morphologyEx(img , cv.MORPH_BLACKHAT , kernel) #黑帽运算 闭运算 - 原图像 分离暗一点的点

fig,axes = plt.subplots(nrows = 1 ,ncols = 3 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing ")
axes[1].imshow(cvtophat[:,:,::-1])
axes[1].set_title("cvtophat")
axes[2].imshow(cvblackhat[:,:,::-1])
axes[2].set_title("cvblackhat")
plt.show()