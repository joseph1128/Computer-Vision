# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:26:53 2025

@author: 123
"""

import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')
    
def draw(event,x,y,flags,param):
    global ix,iy                 # 버튼을 클릭한 순간의 좌표를 저장할 ix와 iy를 전역변수 global variable로 선언 
    
    if event==cv.EVENT_LBUTTONDOWN:
        ix,iy=x,y                # 이벤트가 lBUTTONDOWN이면 좌표 x와 y를 전역변수 ix와 iy에 저장
        
    elif event==cv.EVENT_LBUTTONUP: 
        cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2) #이벤트가 LBUTTONUP이 된 순간 클릭했을 때 저장해둔 좌표 (ix,iy)와 놓았을 때 좌표 (x,y)를 이용해 직사각형을 그린다.
        
    cv.imshow('Drawing',img) #바뀐 영상 윈도우에 반영
        
cv.namedWindow('Drawing') #'Drawing'이라고 하는 윈도우 생성
cv.imshow('Drawing',img)  #'Drawing'윈도우에 img영상 표시

cv.setMouseCallback('Drawing',draw) #'Drawing'이라는 윈도우에서 마우스 이벤트가 발생할 때 draw라는 콜백함수를 호출하라고 등록

while(True):                 # 무한루프를 돌아 프로그램 실행 지속
    if cv.waitKey(1)==ord('q'): # 키보드에서 'q'가 입력되면 윈도우 닫고 루프 탈출
        cv.destroyAllWindows()
        break
    