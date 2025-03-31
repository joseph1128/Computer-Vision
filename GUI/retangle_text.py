# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:51:07 2025

@author: 123
"""

import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.rectangle(img,(830,30),(1000,200),(0,0,255),2) #직사각형 그리기 
                                      #왼쪽위 구석점 좌표, 오른쪽아래 구석점 좌표,빨간색,선두께:2)
cv.putText(img,'laugh',(830,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) #영상에 문자열 쓰는 putText함수 가져와 글씨 쓰기
cv.imshow('Draw',img)                 #윈도우에 영상표시

cv.waitKey()
cv.destroyAllWindows() #키입력을 기다렸다가 윈도우를 닫고, 정상적으로 프로그램 종료