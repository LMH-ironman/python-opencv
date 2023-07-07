import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((256,256,3),np.uint8)

plt.imshow(img[:,:,::-1])
plt.show()

sjtu = cv.imread("image/sjtu.jpg")
plt.imshow(sjtu[:,:,::-1])
plt.show()

b,g,r = cv.split(sjtu)
plt.imshow(b,cmap=plt.cm.gray)
plt.show()

img2 = cv.merge((b,g,r))
plt.imshow(img2[:,:,::-1])
plt.show()

hav = cv.cvtColor(sjtu,cv.COLOR_BGR2HSV)
plt.imshow(hav)
plt.show()

