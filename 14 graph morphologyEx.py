import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
#创建一个10 * 10 的核
kernel = np.ones((10,10),np.uint8)

cvopen = cv.morphologyEx(img , cv.MORPH_OPEN , kernel)  #开运算先腐蚀后膨胀  消除噪音
cvclose = cv.morphologyEx(img , cv.MORPH_CLOSE , kernel) #闭运算先膨胀后腐蚀 填充孔洞

fig,axes = plt.subplots(nrows = 1 ,ncols = 3 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(cvopen[:,:,::-1])
axes[1].set_title("open")
axes[2].imshow(cvclose[:,:,::-1])
axes[2].set_title("close")
plt.show()

