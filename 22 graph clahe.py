import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg",0)
#直方图自适应均衡化就是在每一个小块，超过阈值的均匀分散到其它bins中，然后再均衡化，使用双线性插值
clahe = cv.createCLAHE(clipLimit = 2.0 , tileGridSize = (8,8)) #clipLimit默认为40，通常为2.0 ,tiles在opencv中指的是一小块小块的内容，默认为8*8

img1 = clahe.apply(img)

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img , cmap = plt.cm.gray)
axes[0].set_title("Original drawing ")
axes[1].imshow(img1 , cmap = plt.cm.gray)
axes[1].set_title("clahe graph")
plt.show()