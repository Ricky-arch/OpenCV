import cv2
import numpy as np
from matplotlib import pyplot as plt
cv2.namedWindow('canny')
def nothing(x):
    print(x)


img = cv2.imread('messi2.jpg')
cv2.createTrackbar('ThreshHold-1', 'canny', 0, 255, nothing)
cv2.createTrackbar('ThreshHold-2', 'canny', 0, 255, nothing)

while(1):

    threshold1 = cv2.getTrackbarPos('ThresHold-1', 'canny')
    threshold2 = cv2.getTrackbarPos('ThresHold-2', 'canny')
    edge = cv2.Canny(img, 100, 200)
    cv2.imshow('image', img)
    cv2.imshow('canny', edge)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
