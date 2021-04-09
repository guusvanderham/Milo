# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:52:57 2021

@author: guusv
"""

import cv2

cap = cv2.VideoCapture(0)
i=0

while(True):
    ret, frame = cap.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.imwrite(str(i)+'.jpg', frame)
        print('saved: '+str(i))
        i+=1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()