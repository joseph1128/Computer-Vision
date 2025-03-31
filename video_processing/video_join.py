# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:57:06 2025

@author: 123
"""
#웹캠 또는 비디오 캡처 객체 생성
#Windows에서는 DirectShow(cv.CAP_DSHOW) 백엔드를 사용하여 카메라를 엶
#로컬 웹캠 사용(기본 0번 카메라)

import cv2 as cv
import numpy as np
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW) #카메라와 연결 시도

if not cap.isOpened():
    sys.exit('카메라연결실패')
frames=[]
while True:
    ret,frame=cap.read()            #비디오를 구성하는 프레임 획득
    
    if not ret:
        print('프레임획득에 실패하여 루프를 나갑니다')
        break
    cv.imshow('Video display',frame) #윈도우에 영상 표시
    
    key=cv.waitKey(1)              #1밀리초 동안 키보드 입력 기다림
    if key==ord('c'): 
        frames.append(frame)       #'c'키가 들어오면 프레임을 리스트에 추가
    elif key==ord('q'):
        break                      #'q'키가 들어오면 루프를 빠져나감
    
cap.release()                      #카메라와 연결을 끊음
cv.destroyAllWindows()

if len(frame)>0:                   #수집된 영상이 있으면
    imgs=frames[0]
    for i in range(1,min(3,len(frames))): 
        imgs=np.hstack((imgs,frames[i])) #최대 3개까지 배열을 이어 붙임
    cv.imshow('collected images',imgs)
    
    cv.waitKey()                       
    cv.destroyAllWindows() 

    
len(frames)