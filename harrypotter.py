import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
time.sleep(5)
count = 0
background = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

for i in range(60):
    _,background = cap.read()

background = np.flip(background,axis=1)

while(cap.isOpened()):
    ret, image = cap.read()
    count+=1
    if not ret:
        print("error")
        break
    image = np.flip(image,axis=1)
    lower = np.array([4,  33,  33])
    upper = np.array([255, 100, 80])
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    mask = cv2.inRange(image, lower, upper)
    mask = cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
    inv = cv2.bitwise_not(mask)
    a = cv2.bitwise_and(background, background, mask=mask)
    b = cv2.bitwise_and(image, image, mask=inv)
    d = cv2.bitwise_or(a,b)
    cv2.imshow("output",d)
    out.write(d)
    if cv2.waitKey(40)==27:
        break

out.release()
cv2.destroyAllWindows()
cap.release()


