# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 10:04:48 2025

@author: 123
"""

import cv2 as cv
import sys

img=cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')
    

cv.imshow('original_RGB',img) #'original_RGB'라는 윈도우에 영상 img를 디스플레이
cv.imshow('Upper left half',img[0:img.shape[0]//2,0:img.shape[1]//2,:]) #img.shape는 (948,1434,3)이므로 
                                                                         #왼쪽 위 원점에서 x축에서는 왼쪽부터 전체의 1/2만큼, y축에서는 위에서 1/2만큼 
                                                                         #z축에서는 Blue, Green, Red화소를 모두 포함하여 ndarray클래스의 슬라이싱 기능 활용하여 
                                                                         #영상 왼쪽 위의 1/4만큼 자름  
cv.imshow('Center half',img[img.shape[0]//4:3*img.shape[0]//4,img.shape[1]//4:3*img.shape[1]//4,:]) #img.shape는 (948,1434,3)이므로 
                                                                         #왼쪽 위 원점에서 x축에서는 948을 4로 나눈 몫인 237부터 711까지, y축에서는  1434를 4로 나눈 358.5부터 1075.5까지
                                                                         #z축에서는 Blue, Green, Red화소를 모두 포함하여 ndarray클래스의 슬라이싱 기능 활용하여 
                                                                         #영상 가운데 부분을 잘라 표현
 
cv.imshow('Rchannel',img[:,:,2]) #'Rchannel'이라는 윈도우에 Red채널 저장
cv.imshow('Gchannel',img[:,:,1]) # 'Gchannel' 이라는 윈도우에 Green채널 저장
cv.imshow('Bchannel',img[:,:,0]) # 'Bchannel' 이라는 윈도우에 Blue채널 저장 

cv.waitKey()
cv.destroyAllWindows()