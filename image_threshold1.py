import cv2
import numpy as np


img=cv2.imread('gradient.jpg')
ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)




cv2.imshow('image', img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()