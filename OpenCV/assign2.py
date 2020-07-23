# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:35:45 2020

@author: Aanal Sonara
"""
import cv2
import numpy as np
img = cv2.imread("C://Users//Aanal Sonara//Downloads//red-blue.jpeg")
(rows, cols) = img.shape[:2]
for i in range(1,5):
    M = np.float32([[1,0,i*20],[0,1,i*20]])
    res_i =  cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow("trans{}".format(i), res_i)
    
for i in range(1,5):
    M = cv2.getRotationMatrix2D((cols/2, rows/2), i*5, 1)
    res_i = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow("rotation{}".format(i), res_i)
    
scale_img = cv2.resize(img, (int(cols/2), int(rows/2)), interpolation = cv2.INTER_CUBIC )
cv2.imshow("scale_img", scale_img)

blur_img = cv2.GaussianBlur(img, (7,7), 1)
cv2.imshow("Blurring image", blur_img)
    
cv2.waitKey(100000) and 0xFF
cv2.destroyAllWindows()