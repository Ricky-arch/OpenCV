import cv2
import numpy as np
from matplotlib import pyplot as plt

img =cv2.imread('messi2.jpg')
imgPlt=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(imgPlt)
plt.show()
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()