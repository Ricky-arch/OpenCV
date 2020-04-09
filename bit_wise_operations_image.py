import cv2
import numpy as np
img=cv2.imread('bw.png')
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]
img2=np.zeros((height,width,channels),np.uint8)


img2=cv2.rectangle(img2,(130,0),(230,100),(255,255,255),-1)

bitAnd=cv2.bitwise_xor(img,img2)


print(height)
print(width)


cv2.imshow('image',img)
cv2.imshow('image2', img2)
cv2.imshow('image3',bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()