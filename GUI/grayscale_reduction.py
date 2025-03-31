# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:37:36 2025

@author: 123
"""

import cv2 as cv
import sys
img=cv.imread('soccer.jpg')
if img is None:
    sys.exit('파일 못찾음')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #cvtColor함수로 컬러영상을 명암 영상으로 변환
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5) #resize함수(입력영상, 변환할 크기 지정,가로 세로 반으로 축소)

cv.imwrite('soccer_gray.jpg',gray) #gray객체에 있는 영상을 'soccer_gray.jpg'파일에 저장
cv.imwrite('soccer_gray_small.jpg',gray_small) #gray_small객체에 있는 영상을 'soccer_gray_small.jpg' 파일에 저장

cv.imshow('Color image',img) #'Color image'윈도우에 img영상표시
cv.imshow('Gray image',gray) #'Gray image'윈도우에 gray영상표시
cv.imshow('Gray image small',gray_small) #'Gray image small'윈도우에 gray_small영상표시

cv.waitKey()
cv.destroyAllWindows()