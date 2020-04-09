import numpy as np
import cv2

img= cv2.imread('messi.jpg')
img2=cv2.imread('woman.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)

img= cv2.resize(img,(100,100))
img2=cv2.resize(img2,(100,100))

addedImage=cv2.add(img2,img)

#addedImageWeighted=cv2.add(img,0.9,img2,0.1,0)


# img=cv2.merge((b,g,r))
# ball=img[80:100,140:160]
# img[120:140,60:80]=ball
cv2.imshow('image', addedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
