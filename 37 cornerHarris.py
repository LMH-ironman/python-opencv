import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("image/sjtu.jpg")
gray_img = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

dst = cv.cornerHarris(gray_img,2,3,0.04)

img[dst>0.001*dst.max()] = [0,0,255]

plt.figure(figsize=(10,8),dpi=100)
plt.imshow(img[:,:,::-1])
plt.title("cornerHarris")
plt.xticks([])
plt.yticks([])
plt.show()