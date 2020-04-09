import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi2.jpg',0)
image=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

ret, t1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, t2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, t3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, t4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, t5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


windows=['Original Image', 'Binary', 'Binary Inverse', 'Trunc', 'Zero', 'Zero Inverse']
images=[image, t1, t2, t3, t4, t5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i],'gray')
    plt.title(windows[i])
    plt.xticks([]),plt.yticks([])


plt.show()
