import cv2
import numpy as np

img=cv2.imread('sudoko.jpg',0)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,2)


cv2.imshow('image', img)
cv2.imshow('threshold', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
