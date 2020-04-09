import cv2
cap= cv2.VideoCapture(0)
fourcc= cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3,1280)
cap.set(4,720)

print(cap.get(3))
print(cap.get(4))



while(cap.isOpened()):
    ret, frame= cap.read()
    if ret== True:
        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text="Width: "+str(cap.get(3))+" Height: "+str(cap.get(4))
        frame= cv2.putText(frame,text, (10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0.0),4, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cap.destroyAllWindows()
