# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:36:40 2020

@author: Aanal Sonara
"""


import cv2
import numpy as np

img = cv2.imread("C://Users//Aanal Sonara//Downloads//red-blue.jpeg", 0)
img_lap = cv2.Laplacian(img, cv2.CV_64F)
#img_canny = cv2.Canny(img_lap, 100, 250)

cv2.imshow("Canny", img_lap)
cv2.waitKey(100000)
cv2.destroyAllWindows()