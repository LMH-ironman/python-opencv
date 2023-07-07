import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 创建图像
img = np.zeros((512,512,3),np.uint8)

# 2 绘制图像
cv.line(img,(0,0),(512,512),(255,0,0),5)
cv.circle(img,(300,300),100,(0,0,255),-1)
cv.rectangle(img,(200,200),(400,400),(0,255,0),5)
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img,"lmh",(100,100),font,3,(255,255,255),3)

# 3 显示图像
plt.imshow(img[:,:,::-1])
plt.show()