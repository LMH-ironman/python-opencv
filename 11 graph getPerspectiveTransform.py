import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
rows,cols = img.shape[:2]
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,145],[300,100],[80,290],[310,300]])

T = cv.getPerspectiveTransform(pts1,pts2) #透射变换

dst =cv.warpPerspective(img,T,(cols,rows))

fig,axes = plt.subplots(nrows = 1 ,ncols = 2 ,figsize = (10,8), dpi = 100)
axes[0].imshow(img[:,:,::-1])
axes[0].set_title("Original drawing")
axes[1].imshow(dst[:,:,::-1])
axes[1].set_title("change place photo")
plt.show()

print(T)