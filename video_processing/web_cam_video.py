# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:47:54 2025

@author: 123
"""
#웹캠 또는 비디오 캡처 객체 생성
#Windows에서는 DirectShow(cv.CAP_DSHOW) 백엔드를 사용하여 카메라를 엶
#로컬 웹캠 사용(기본 0번 카메라)
import cv2 as cv
import sys

cap=cv.VideoCapture(0,cv.CAP_DSHOW) #카메라와 연결시도
if not cap.isOpened():
    sys.exit('연결실패')
while True:
    ret,frame=cap.read() #비디오를 구성하는 프레임 획득
    
    if not ret:
        print('프레임 획득에실패하여 루프를 나갑니다')
        break
    cv.imshow('Video display',frame)
    
    key=cv.waitKey(1) #1밀리초 동안 키보드 입력 기다림
    if key==ord('q'): #q가 들어오면 루프를 빠져나감
        break
cap.release() #카메라와 연결을 끊음
cv.destroyAllWindows() #윈도우창 닫음