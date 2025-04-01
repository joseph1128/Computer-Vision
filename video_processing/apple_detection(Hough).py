# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 14:18:03 2025

@author: 123
"""

import cv2 as cv

img=cv.imread('apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #컬러이미지를 흑백(grayscale)으로 변환

apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,200,param1=150,param2=20, #HoghCircles함수는 명암 영상에서 원을 검출해 중심과 반지름을 저장한 리스트 반환, cv.HOUGH_GRADIENT:에지 방향 정보 추가로 사용,1:입력 영상과 같은 크기를 사용,200:원 사이의 최소 거리 지정,param1:상한 임계값,param2:비최대 억제를 적용할 때 쓰는 임계값,
                       minRadius=50,maxRadius=120) #원의 최소 반지름, 원의 최대 반지름
for i in apples[0]:
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2) #apples 리스트가 가진 원의 중심과 반지름 정보를 이용하여 원래 영상에 원 그리기
cv.imshow('Apple detection',img)

cv.waitKey()
cv.destroyAllWindows()