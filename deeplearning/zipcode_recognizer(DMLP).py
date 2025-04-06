# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 06:11:42 2025

@author: 123
"""

import numpy as np
import tensorflow as tf
import cv2 as cv
import matplotlib.pyplot as plt
import winsound

model=tf.keras.models.load_model('dmlp_trained.h5') 
#load_model함수로 신경망 파일 'dmlp_trained.h5'읽어와 model객체에 저장
def reset(): #reset함수로 img라는 영상 만들기
    global img #img를 전역 변수로 선언하여 img를 다른 함수와 공유
    
    img=np.ones((200,520,3),dtype=np.uint8)*255
    #np.ones함수로 200x520크기의 3채널 컬러 영상을 저장할 배열 만들기,255곱해 흰색화소 생성
    for i in range(5): #지정하나 위치에 5개의 빨간색 박스 만들기
        cv.rectangle(img,(10+i*100,50),(10+(i+1)*100,150),(0,0,255))
    cv.putText(img,'e:erase s:show r:recognition q:quit',
               (10,40),cv.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0),1)
    #명령어를 나타내는 글씨를 써넣기
    
def grab_numerals():          #grab_numerals()함수 생성
    numerals=[]              #numerals에 빈리스트 생성
    
    for i in range(5):
        #5번 반복, img에서 숫자를 떼내 28x28크기로 변환하여 리스트에 추가
        roi=img[51:149,11+i*100:9+(i+1)*100,0]
        #세로행은 51~149픽셀까지 자르기, 열은 각 숫자 영역을 100픽셀간격으로 자르기
        roi=255-cv.resize(roi,(28,28),interpolation=cv.INTER_CUBIC)
        #28x28사이즈로 변환, 삼차보간법으로 이미지를 부드럽게 변환, 배경을 검은색으로
        numerals.append(roi) #5개 이비지 numerals리스트에 추가
        
    numerals=np.array(numerals) #리스트를 numpy배열로 변환
    return numerals             #반환
    
def show():                    #show함수 생성
    numerals=grab_numerals()   # grab_numerals() 함수의 반환값을 numerals에 저장
    plt.figure(figsize=(25,5)) #전체 그림 크기를 가로 25, 세로 5인치로 설정
    for i in range(5):         #숫자 5개를 표시하기 위해 0~4까지 반복
        plt.subplot(1,5,i+1)    # 1행 5열 중 i+1번째 칸에 subplot 배치
        plt.imshow(numerals[i],cmap='gray')  # i번째 숫자 이미지를 흑백으로 출력
        plt.xticks([]);plt.yticks([])  # x,y축 격자 제거
    plt.show()
    
def recognition():
    numerals=grab_numerals() #grab_numerals()함수로부터 5개 숫자 받아 numerals에 저장
    numerals=numerals.reshape(5,784) #2차원 구조를 1차원으로 펼치기 (5,28,28)에서 변경
    numerals=numerals.astype(np.float32)/255.0 #데이터 타입 실수형,[0,255]범위를 [0,1]범위로 변환
    res=model.predict(numerals) #model.predict함수로 예측 수행하고 결과를 res객체에 저장
    class_id=np.argmax(res,axis=1)#res에서 최대값가지는 인덱스를 찾아 class_id에 저장
    for i in range(5):
        cv.putText(img,str(class_id[i]),(50+i*100,180),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
        #class_id에 있는 예측 숫자를 문자열로 변환해서 표시, x좌표와 y좌표
    winsound.Beep(1000,500)           # 숫자인식완료후 1000Hz를 0.5초동안 삑소리 생성
    
    
BrushSiz=4                              #붓 크기
LColor=(0,0,0)                          #검은색
 
def writing(event,x,y,flags,param):     # writing함수 
    if event==cv.EVENT_LBUTTONDOWN:     #마우스 왼쪽 버튼 클릭하면  
        cv.circle(img,(x,y),BrushSiz,LColor,-1) #circle함수로 BrushSiz크기의 원 검은색으로
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON: #마우스를 누른채 이동
        cv.circle(img,(x,y),BrushSiz,LColor,-1)#circle함수로 BrushSiz크기의 원 검은색으로
        
reset()                                #reset함수 호출
cv.namedWindow('Writing')              #윈도우 생성
cv.setMouseCallback('Writing',writing) #윈도우의 콜백함수로 writing함수 등록

while(True): 
    cv.imshow('Writing',img)           #img영상을 표시, 변경된 내용 윈도우에 반영
    key=cv.waitKey(1)                 #키보드 입력이 있으면 읽어서 key에 저장
    if key==ord('e'):                 #키가 'e'이면 reset함수 호출
        reset()
    elif key==ord('s'):               #키가 's'이면 show함수 호출   
        show()
    elif key==ord('r'):               #키가 'r'이면 recognition함수 호출 
        recognition()
    elif key==ord('q'):               #키가 'q'이면 루프 빠져나가 프로그램 종료 
        break

cv.destroyAllWindows()