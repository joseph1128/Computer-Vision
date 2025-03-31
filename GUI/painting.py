# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:37:08 2025

@author: 123
"""

import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일 찾을 수 없습니다')
    
BrushSiz=5
LColor,RColor=(255,0,0),(0,0,255) #붓크기는 5로 고정, 왼쪽은 파란색, 오른쪽은 빨간색

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,LColor,-1) # 왼쪽 버튼을 클릭했을 때 img영상에 원을 그린다 (원의 중심:커서의 위치,원의 반지름: BrushSiz인 속이 찬 파란색 원)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,RColor,-1) # 오른쪽 버튼 클릭했을 때 img 영상에 원을 그린다.(원의 중심 : 커서의 위치, 원의 반지름:BrushSiz인 속이 찬 빨간색 원)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,LColor,-1) #왼쪽 버튼 클릭하고 이동하면 파란색 으로 그려짐
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,RColor,-1) #오른쪽 버튼 클릭하고 이동하면 빨간색으로 그려짐
        
    cv.imshow('Painting',img) #붓칠이 된 영상을 윈도우에 다시 디스플레이
    
cv.namedWindow('Painting')          #'Painting'이라는 윈도우 생성
cv.imshow('Painting',img)           #'Painting'윈도우에 img 영상 표시

cv.setMouseCallback('Painting',painting)  #'Painting'이라는 윈도우에서 마우스 이벤트가 발생할 때 painting이라는 콜백함수를 호출하라고 등록

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break