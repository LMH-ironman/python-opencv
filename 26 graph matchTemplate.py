import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
template = cv.imread("image/cat.jpg")
h,w,l= template.shape

res = cv.matchTemplate(img  , template , cv.TM_SQDIFF)
min_v ,max_v ,min_l ,max_l = cv.minMaxLoc(res)

top_left = min_l
bottom_right = (min_l[0] + w , min_l[1] + h )
cv.rectangle(img,top_left,bottom_right,(0,255,0),5)

plt.imshow(img[:,:,::-1])
plt.title("match graph")
#不显示x，y坐标
plt.xticks([])
plt.yticks([])
plt.show()