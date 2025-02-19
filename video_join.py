# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:57:06 2025

@author: 123
"""

import cv2 as cv
import numpy as np
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit('카메라연결실패')
frames=[]
while True:
    ret,frame=cap.read()
    
    if not ret:
        print('프레임획득에 실패하여 루프를 나갑니다')
        break
    cv.imshow('Video display',frame)
    
    key=cv.waitKey(1)
    if key==ord('c'):
        frames.append(frame)
    elif key==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()

if len(frame)>0:
    imgs=frames[0]
    for i in range(1,min(3,len(frames))):
        imgs=np.hstack((imgs,frames[i]))
    cv.imshow('collected images',imgs)
    
    cv.waitKey()
    cv.destroyAllWindows()
    
len(frames)