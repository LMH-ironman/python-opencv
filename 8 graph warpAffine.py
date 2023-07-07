import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")

rows,cols  = img.shape[:2]
M  = np.float32([[1,0,100], [0,1,50]])  #warpAffine只是图像变换接口，这个才是平移变换
dst = cv.warpAffine(img,M,(cols,rows))  #cv.warpAffine(img,平移，desize) desize（宽度，高度） 先列后行
a = dst.shape[:2]
fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("change place photo")
plt.show()
print(rows,cols,a)