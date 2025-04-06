# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 08:55:42 2025

@author: 123
"""

import tensorflow as tf
import tensorflow.keras.datasets as ds #데이터셋을 읽어오는데 필요한 모듈
import matplotlib.pyplot as plt

#mnist.load_data함수로 MNIST 데이터셋(70,000개의 필기숫자샘플:traindata-60,000,testdata-10,000) 읽어오기
(x_train,y_train),(x_test,y_test)=ds.mnist.load_data() #훈련집합, 테스트 집합 읽어오기
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape) #구조 출력
plt.figure(figsize=(24,3)) #그림의 크기 지정
plt.suptitle('MNIST',fontsize=30) #그림의 제목달기
for i in range(10): #숫자부류:0~9,x_train의  10개 샘플 보여주기 
    plt.subplot(1,10,i+1) # 1줄에 10개영상 배치,i+1번째를 채우라고 지시
    plt.imshow(x_train[i],cmap='gray') #i번째 샘플을 명암으로 출력
    plt.xticks([]);plt.yticks([]) #x,y축에 눈금 달지 말라고 지시
    plt.title(str(y_train[i]),fontsize=30) #샘플의 부류 정보를 제목으로 달아주기
    
#cifar10.load_data함수로 CIFAR-10 데이터셋(60,000개의 자연영상(traindata-50,000,test-10,000 읽어오기    
(x_train,y_train),(x_test,y_test)=ds.cifar10.load_data() #훈련집합, 테스트 집합 읽어오기
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
class_names=['airplane','car','bird','cat','deer','dog','frog','horse','ship','truck'] #0~9사이의 숫자로 표현된 부류 정보를 물체이름으로 변환
plt.figure(figsize=(24,3))#그림의 크기 지정
plt.suptitle('CIFAR-10',fontsize=30)#그림의 제목달기
for i in range(10): #부류:10개,x_train의 10개 샘플 보여주기
    plt.subplot(1,10,i+1) #1줄에 10개영상 배치, ㅑ+1번째를 채우라고 지시
    plt.imshow(x_train[i]) #i번째 샘플을 출력
    plt.xticks([]);plt.yticks([])#x,y축에 눈금 달지 말라고 지시
    plt.title(class_names[y_train[i,0]],fontsize=30)#샘플 위에 물체 부류 정보 표시