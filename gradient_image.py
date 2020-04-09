import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sudoko.jpg', cv2.IMREAD_GRAYSCALE)

lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3)
absolute_lap=np.uint8(np.absolute(lap))

sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

absolute_sobelX=np.uint8(np.absolute(sobelX))
absolute_sobelY=np.uint8(np.absolute(sobelY))

bitwise_sobel=cv2.bitwise_or(absolute_sobelX,absolute_sobelY)

titles=['Original Image', 'Laplacian Gradient', 'SobelX', 'SobelY', 'Bitwise Sobel']
images=[img, absolute_lap, absolute_sobelX, absolute_sobelY, bitwise_sobel]

for i in range(len(images)):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()