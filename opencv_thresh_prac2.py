import cv2
import numpy as np

img = cv2.imread("book1.jpg")
ret,thresholding = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
cv2.imshow("orginal",img)
#cv2.imshow("thresholding",thresholding)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret2,thresholding2 = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
#cv2.imshow("thresholding2",thresholding2)
gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,15)
cv2.imshow("gaus",gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
