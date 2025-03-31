# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv
import sys
img=cv.imread('soccer.jpg') # 영상 파일 불러오기
if img is None:
    sys.exit('파일을 찾을 수 없습니다')
cv.imshow('Image Display',img) #'Image Display'라는 윈도우에 img 영상 표시

cv.waitKey()
cv.destroyAllWindows() #키입력을 기다렸다가 윈도우를 닫고, 정상적으로 프로그램 종료