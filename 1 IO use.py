import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 读取图像
img = cv.imread("image/sjtu.jpg",0)

# 2 显示图像
# 2.1 Opencv
#cv.imshow("sjtu",img)
#cv.waitKey(0)
#cv.destroyAllWindows()

# 2.2 matplotlib
plt.imshow(img,cmap=plt.cm.gray)
plt.show()

# 3 图像保存
cv.imwrite("image/sjtu.png",img)