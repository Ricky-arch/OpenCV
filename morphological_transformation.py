import cv2
import numpy as np
from matplotlib import pyplot as plt

# cv2.namedWindow('TrackBar')
# img = cv2.imread('smarties.png', 0)



# def glider(x):
#     print(x)


# cv2.createTrackbar('maskValue', 'TrackBar', 0, 255, glider)


# while(1):

#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     maskValue=cv2.getTrackbarPos('maskValue','TrackBar')
#     ret, mask = cv2.threshold(img, maskValue, 255, cv2.THRESH_BINARY_INV)
#     cv2.imshow('mask',mask)
# cv2.destroyAllWindows()

img = cv2.imread('smarties.png', 0)
ret, mask = cv2.threshold(img, 149, 255, cv2.THRESH_BINARY_INV)

kernel=np.ones((2,2), np.uint8)
dilation=cv2.dilate(mask,kernel, iterations=13)
erosion=cv2.erode(mask,kernel,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT, kernel)



titles = ['Original Image', 'Mask', 'Dialation', 'Erosion', 'Opening','Closing', 'Morphlogy Gradient', 'Top Hat']
images = [img, mask, dilation, erosion, opening, closing, mg, th]
for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


