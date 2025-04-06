# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 12:18:52 2025

@author: 123
"""

import numpy as np
import tensorflow as tf
import tensorflow.keras.datasets as ds

from tensorflow.keras.models import Sequential 
#model 모듈, 다층퍼셉트론처럼 계산이 한줄기로 흐르는 경우 Sequential 사용
from tensorflow.keras.layers import Dense
#layers 모듈, 다층 퍼셉트론을 구성하는 완전 연결층은 Dense 클래스로 쌓음
from tensorflow.keras.optimizers import Adam
#optimizers 모듈, 최적화 방법으로 Adam optimizer 선택


(x_train,y_train),(x_test,y_test)=ds.mnist.load_data()#훈련집합, 테스트 집합 
x_train=x_train.reshape(60000,784) #28x28의 2차원 구조 맵을 1차원으로 펼치기
x_test=x_test.reshape(10000,784) 
# x_train의 원래 데이터형인 uint8을 실수 연산 가능하도록 float32로 변환
#255로 나누어 [0,255]범위를 [0,1]범위로 변환
x_train=x_train.astype(np.float32)/255.0 
x_test=x_test.astype(np.float32)/255.0
#0~9사이의 정수로 표현된 y_train과 y_test를 원핫코드로 변환
y_train=tf.keras.utils.to_categorical(y_train,10)
y_test=tf.keras.utils.to_categorical(y_test,10)

dmlp=Sequential() 
#Sequential함수로 dmlp객체 생성, 4개의 층 쌓아 깊은 다층 퍼셉트론 형성
dmlp.add(Dense(units=1024,activation='relu',input_shape=(784,))) #입력층에 784개 노드
dmlp.add(Dense(units=512,activation='relu')) #은닉층의 노드 개수 512개 노드
dmlp.add(Dense(units=512,activation='relu')) #activation 매개변수로 ReLU함수 활성
dmlp.add(Dense(units=10,activation='softmax')) #출력층에 노드 10개, 활성함수:softmax

dmlp.compile(loss='categorical_crossentropy',
             optimizer=Adam(learning_rate=0.0001),metrics=['accuracy'])
#손실함수로 교차엔트로피 사용, 학습률 0.0001,정확률 기준으로 성능 측정
hist=dmlp.fit(x_train,y_train,batch_size=128,epochs=50,
              validation_data=(x_test,y_test),verbose=2)
#실제로 학습 실행, 미니 배치크기=128로 설정, 세대를 50번 반복
print('정확률=',dmlp.evaluate(x_test,y_test,verbose=0)[1]*100)
#evaluate함수로, 테스트 집합으로 성능 측정, 정확률을 퍼센트로 출력

dmlp.save('dmlp_trained.h5') 
#학습을 마친 신경망 모델의 구조 정보와 가중치 값을 지정한 파일에 저장

import matplotlib.pyplot as plt

plt.plot(hist.history['accuracy']) #훈련집합에 대한 정확률
plt.plot(hist.history['val_accuracy']) #검증집합에 대한 정확률
plt.title('Accuracy graph')            #그래프 제목
plt.xlabel('epochs')                   #x축 제목
plt.ylabel('accuracy')                 #y축 제목
plt.legend(['train','test'])           #범례
plt.grid()                             #격자 넣기
plt.show()

plt.plot(hist.history['loss']) #훈련집합에 대한 손실함수값
plt.plot(hist.history['val_loss']) #검증집합에 대한 손실함수값
plt.title('Loss graph') #그래프 제목
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(['train','test'])
plt.grid()
plt.show()