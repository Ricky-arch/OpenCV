import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi2.jpg', cv2.IMREAD_UNCHANGED)
layer=img.copy()

gp=[layer]

for i in range(5):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
