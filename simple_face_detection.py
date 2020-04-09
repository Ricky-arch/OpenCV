import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('avengers.jpg')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(imgray,1.1,4)

for(x,y,w,h)in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow('Me', img)
cv2.waitKey(0)
cv2.destroyAllWindows()