# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 16:24:56 2025

@author: 123
"""
#Caany 에지 검출 이론 알고리즘
#Canny 에지 실험
import cv2 as cv

img=cv.imread('soccer.jpg') #영상 읽기

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) #컬러이미지를 흑백(grayscale)으로 변환

canny1=cv.Canny(gray,50,150) #OpenCV에서 제공하는 Canny함수 #이력 임계값 사용하여 경계 감지- 하한 임계값 T(low)=50, 상한 임계값 T(high)=100
canny2=cv.Canny(gray,100,200) #하한 임계값 T(low)=50, 상한 임계값 T(high)=100 상한 임계값보다 크면 엣지로 간주

cv.imshow('Original',gray) #'Original'이라는 윈도우에 gray 영상 표시
cv.imshow('Canny1',canny1) #'Canny1'이라는 윈도우에 canny1 영상 표시
cv.imshow('Canny2',canny2) #'Canny2'라는 윈도우에 canny2 영상 표시

cv.waitKey()
cv.destroyAllWindows() #키입력을 기다렸다가 윈도우를 닫고 정상적으로 프로그램 종료