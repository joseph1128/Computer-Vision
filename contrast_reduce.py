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
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5)

cv.imwrite('soccer_gray.jpg',gray)
cv.imwrite('soccer_gray_small.jpg',gray_small)

cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small',gray_small)

cv.waitKey()
cv.destroyAllWindows()