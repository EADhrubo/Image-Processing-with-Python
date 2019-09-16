import cv2
import numpy as np

img1 = cv2.imread("classroom_image_easy.jpg")
img2 = cv2.imread("scan0007.jpg")

row,col,c = img2.shape
roi = img1[0:row,0:col]
bgr_to_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("bgr_to_gray",bgr_to_gray)
ret,mask = cv2.threshold(bgr_to_gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow("mask",mask)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv",mask_inv)
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
cv2.imshow("img1_bg",img1_bg)
img1_fg = cv2.bitwise_and(img2,img2,mask=mask)
cv2.imshow("img1_fg",img1_fg)
dst = cv2.add(img1_bg,img1_fg)
cv2.imshow("dst",dst)
img1[0:row,0:col] = dst
cv2.imshow("img1_modified",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

