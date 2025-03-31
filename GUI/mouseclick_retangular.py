# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:56:59 2025

@author: 123
"""

import cv2 as cv
import sys

img=cv.imread('girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

def draw(event,x,y,flags,param):            #콜백 함수 (이벤트 종류, 이벤트가 일어난 순간 커서의 위치(x,y))
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2) #왼쪽 마우스버튼을 클릭하면 너비와 높이가 200인 빨간 직사각형을 그린다.
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+100,y+100),(255,0,0),2) #오른쪽 마우스 버튼을 클릭하면 너비와 높이가 100인 파란 직사각형을 그린다.
        
    cv.imshow('Drawing',img)               #바뀐 영상을 윈도우에 반영
    
cv.namedWindow('Drawing')                  #'Drawing'이라는 이름의 윈도우 생성
cv.imshow('Drawing',img)                   #'Drawing' 윈도우에 img영상 표시

cv.setMouseCallback('Drawing',draw)        #'Drawing'윈도우에서 mouse event가 발생하면 draw라는 콜백함수를 호출하라고 등록
                                           # mouse event : 버튼클릭하기,버튼에서 손놓기, 커서이동 등
while(True):                               # 무한루프를 돌아 프로그램 실행 지속
    if cv.waitKey(1)==ord('q'):            # 키보드에서 'q'가 입력되면 윈도우를 닫고 루프 탈울
        cv.destroyAllWindows()
        break