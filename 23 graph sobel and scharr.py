import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg",0)
#sobel算子x，y方向都要转换成16进制cv.CV_16S，因为出现负值会归零，ksize不填入时默认为3
x = cv.Sobel(img , cv.CV_16S , 1 , 0)
y = cv.Sobel(img , cv.CV_16S , 0 , 1)
#数据转换,将16进制转换成8进制
X = cv.convertScaleAbs(x)
Y = cv.convertScaleAbs(y)
#混合之后得到边缘检测的图像
img1 = cv.addWeighted(X , 0.5 , Y , 0.5 ,0)

#scharr算子，只要把ksize改为-1就可以
scharr_x = cv.Sobel(img , cv.CV_16S , 1 , 0 , ksize =  -1)
scharr_y = cv.Sobel(img , cv.CV_16S , 0 , 1 , ksize =  -1)
#数据转换,将16进制转换成8进制
scharr_X = cv.convertScaleAbs(scharr_x)
scharr_Y = cv.convertScaleAbs(scharr_y)
#混合之后得到边缘检测的图像
img2 = cv.addWeighted(scharr_X , 0.5 , scharr_Y , 0.5 ,0)

fig,axes = plt.subplots(nrows = 1 ,ncols = 3 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img , cmap = plt.cm.gray)
axes[0].set_title("Original drawing ")
axes[1].imshow(img1 , cmap = plt.cm.gray)
axes[1].set_title("Sober skill")
axes[2].imshow(img2 , cmap = plt.cm.gray)
axes[2].set_title("Scharr skill")
plt.show()
