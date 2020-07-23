# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:41:24 2020

@author: Aanal Sonara
"""


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame_canny = cv2.Canny(frame, 125, 200)
# I prefer canny detection here because Laplacian was very noisy.     
    cv2.imshow("Canny detection", frame_canny)
    
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()