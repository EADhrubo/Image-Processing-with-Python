import numpy as np
import cv2
 
img = cv2.imread('shape.png')
img = cv2.resize(img,(640,480))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
ret,thresh = cv2.threshold(gray,127,255,1)
 
img2,contours,h = cv2.findContours(thresh,1,2)
count = 0
i = 0
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    #print(len(approx))
    if len(approx)==4:
        print("square")
        x,y,w,h = cv2.boundingRect(cnt)
        print("x=" + str(x) + "y=" + str(y))
        i += 1
    count += 1
    if count >= 20:
        break
    

print(i)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()