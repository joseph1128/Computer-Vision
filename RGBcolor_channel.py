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
    

cv.imshow('original_RGB',img)
cv.imshow('Upper left half',img[0:img.shape[0]//2,0:img.shape[1]//2,:])
cv.imshow('Center half',img[img.shape[0]//4:3*img.shape[0]//4,img.shape[1]//4:3*img.shape[1]//4,:])
 
cv.imshow('Rchannel',img[:,:,2])
cv.imshow('Gchannel',img[:,:,1]) 
cv.imshow('Bchannel',img[:,:,0])  

cv.waitKey()
cv.destroyAllWindows()