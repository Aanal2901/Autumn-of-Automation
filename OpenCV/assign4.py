# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:51:37 2020

@author: Aanal Sonara
"""

import cv2
import numpy as np
img = cv2.imread("C://Users//Aanal Sonara//Downloads//shape.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img_thresh = cv2.threshold(img_gray, 230, 255, cv2.THRESH_BINARY) #threshold value based on my image
cv2.imshow("threshold", img_thresh)
contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt)>4000:
    
        #print(cv2.contourArea(cnt))
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), closed = True)
        #print(len(approx))
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        org = (cx, cy) 
        font = cv2.FONT_HERSHEY_SIMPLEX 

# fontScale 
        fontScale = 1
   
# Blue color in BGR 
        color = (255, 0, 0) 
  
# Line thickness of 2 px 
        thickness = 2

        if len(approx) == 3:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.putText(img, 'triangle', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        elif len(approx) >= 16:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.putText(img, 'circle', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        elif len(approx)>=10:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.putText(img, 'ellipse', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        elif len(approx)==5:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
            cv2.putText(img, 'pentagon', org, font, fontScale, color, thickness, cv2.LINE_AA) 
        elif len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            
            if w/float(h)>=1.05:
                cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
                cv2.putText(img, 'square', org, font, fontScale, color, thickness, cv2.LINE_AA) 
            else:
                cv2.drawContours(img, cnt, -1, (0, 255, 0), 5)
                cv2.putText(img, 'rectangle', org, font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.imshow("contour", img)
cv2.waitKey(1000000)
cv2.destroyAllWindows()