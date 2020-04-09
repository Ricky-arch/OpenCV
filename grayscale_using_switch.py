import cv2
import numpy as np

cv2.namedWindow('image')
switch='color/gray'

def glider(x):
    print(x)
cv2.createTrackbar('Bar Value', 'image', 10, 400, glider)
cv2.createTrackbar(switch,'image', 0,1, glider)


while(1):
    img = cv2.imread('messi2.jpg')
    cp=cv2.getTrackbarPos('Bar Value','image')


    cv2.putText(img,str(cp),(50,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0))

    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    g = cv2.getTrackbarPos(switch, 'image')
    if g==0:
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)
cv2.destroyAllWindows()
