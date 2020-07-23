# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 00:44:49 2020

@author: Aanal Sonara
"""


import cv2
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()
    cv2.imshow("live video", frame)
    
    k = cv2.waitKey(1) and 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()