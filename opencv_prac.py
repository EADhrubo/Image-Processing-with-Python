import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("scan0007.jpg")
cv2.line(img,(10,10),(100,100),(255,255,255),10)
cv2.rectangle(img,(30,0),(150,120),(0,255,0),4)
cv2.circle(img,(70,150),20,(0,0,255),-1)
pts = np.array([[65,180],[108,140],[155,165],[152,186],[100,200]],np.int32)
cv2.polylines(img,[pts],True,(0,255,255),5)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Hey",(30,180),font,2,(255,255,0),5,cv2.LINE_AA)
img[150:180,0:30] = [255,255,255]
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()