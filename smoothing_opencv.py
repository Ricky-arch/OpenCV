import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Noise_salt_and_pepper.png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel= np.ones((5,5),np.float32)/25

homogenous=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))
gaussian_blur=cv2.GaussianBlur(img, (5,5), 0)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(median, 10,75,75)



titles=['Original Image', 'Homogenous Filter', 'Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images=[img, homogenous, blur, gaussian_blur, median, bilateral]

for i in range(len(images)):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
