# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 10:32:31 2025

@author: 123
"""

import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
canny=cv.Canny(gray,100,200) #Canny 함수로 에지 맵 구하기
#findContours함수로 경계선을 찾아 contour객체에 저장(findContours함수는 시작점부터 끝점까니 추적한 다음 역추적하여 시작점으로 돌아오도록 경계선을 표현)
contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) #canny:경계선을 찾을 에지 영상,cv.RETR_LIST:맨 바깥쪽 경계선만 찾도록 지시,cv.CHAIN_APPROX_NONE:경계선 표현하는 방식 지정,모든 점 기록

lcontour=[]

for i in range(len(contour)):
    if contour[i].shape[0]>100: #길이가 100보다 크면 실제로는 50 이상인 경계선만 남김
        lcontour.append(contour[i])
        
cv.drawContours(img,lcontour,-1,(0,255,0),3) #영상에 경계선 그린다. (img:경계선 그려넣을 영상,lcontour:경계선 ,-1:모든 경계선을 그려줌,초록색, 팬두께 )

cv.imshow('Original with contours',img) #'Original with contours'라는 윈도우에 img영상표시
cv.imshow('Canny',canny) #'Canny'라는 윈도우에 canny영상 표시

cv.waitKey()
cv.destroyAllWindows() #키입력을 기다렸다가 윈도우를 닫고 정상적으로 프로그램 종료