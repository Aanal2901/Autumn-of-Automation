# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:07:48 2020

@author: Aanal Sonara
"""

import cv2
import numpy as np
filepath = input("Please Enter video file path: ")
img = cv2.VideoCapture(filepath)
while img.isOpened():

    _, frame = img.read()
    frame = cv2.resize(img, (600, 600))
    #green range
    lower_green = np.array([40,40, 40])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    #Do masking
    ground = cv2.bitwise_and(frame, frame, mask=mask)
    #convert to gray
    bgr = cv2.cvtColor(ground, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    #apply threshold
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    #cv2.imshow("thresh", thresh)
    
    #apply morphological transformations
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        if ((h>=1 and w>=1) and (h<=40 and w<=40)):
            ball_img = thresh[ y:y+h, x:x+w]

        lp = np.array([0,0,0])
        up = np.array([0,0,255])
    
        hsv = cv2.cvtColor(ball_img, cv2.COLOR_BGR2HSV)
    
        mask = cv2.inRange(hsv, lp, up)
        masked_img = cv2.bitwise_and(frame, frame, mask = mask)
        
        masked_bgr = cv2.cvtColor(masked_img, cv2.COLOR_HSV2BGR)
        masked_gray = cv2.cvtColor(masked_bgr, cv2.COLOR_HSV2BGR)

        count = cv2.countNonZero(masked_gray)
        if count>=5:
            cv2.putText(image, 'football', (x-2, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2, cv2.LINE_AA)
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
#there is one more method
#after morphological transformation, uncomment this 
    """blurred = cv2.GuassianBlur(thresh, (5,5), 0)
    Canny = cv2.Canny(blurred, 100, 200) #you might have to tweak parameters
    detected_circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 80, param2 = 50, minRadius = 10, maxRadius = 40) 
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        
        for pt in detected_circles[0,:]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(img, (a,b), r, (0, 255, 0), 3)
            cv2.circle(img, (a,b), 1, (255, 0, 0), 3)
            cv2.imshow("ball", img)
    """
    cv2.imshow("ball", image)
    k = cv2.waitKey(1) and 0xFF
    if k==27:
        break
    
img.release()
cv2.destroyAllWindows()